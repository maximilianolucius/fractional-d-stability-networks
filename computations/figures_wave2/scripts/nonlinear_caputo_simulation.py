"""Full nonlinear W2-A time-domain comparison used in the manuscript.

The computation compares the same row-scaled Double-Allee IGP model and the
same initial perturbation at alpha=0.9 and alpha=1.  Fractional trajectories
are computed by the Caputo PECE method with a step-halving study; the
integer-order trajectory is computed independently with DOP853.

Run the numerical stage on Aureus (or another compute host) and then render
the figure locally with ``fig09_nonlinear_caputo_dynamics.py``.
"""
from __future__ import annotations

import argparse
import csv
import json
import math
import os
import platform
import sys
import time

import numpy as np
from scipy.integrate import solve_ivp

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "src"))
sys.path.insert(0, HERE)

from design_tools import params_from_design  # noqa: E402
from fdsn.caputo import caputo_pece  # noqa: E402
from fdsn.double_allee import full_jacobian, g_da, reduced_matrix, residuals  # noqa: E402


def relative_distance(states: np.ndarray, equilibrium: np.ndarray) -> np.ndarray:
    return np.linalg.norm(states / equilibrium - 1.0, axis=1)


def max_shared_grid_difference(
    coarse: tuple[np.ndarray, np.ndarray],
    fine: tuple[np.ndarray, np.ndarray],
    equilibrium: np.ndarray,
) -> float:
    tc, yc = coarse
    tf, yf = fine
    ratio = int(round((tc[1] - tc[0]) / (tf[1] - tf[0])))
    if ratio < 1 or len(yf[::ratio]) != len(yc) or not np.allclose(tf[::ratio], tc):
        raise ValueError("refinement grids are not nested")
    return float(np.max(np.abs((yc - yf[::ratio]) / equilibrium)))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", default=os.path.join(HERE, "..", "data"))
    parser.add_argument("--t-end", type=float, default=180.0)
    parser.add_argument("--steps", type=float, nargs="+", default=[0.04, 0.02, 0.01])
    parser.add_argument("--output-stride", type=int, default=5)
    parser.add_argument("--exit-radius", type=float, default=0.20)
    args = parser.parse_args()

    started = time.time()
    os.makedirs(args.output_dir, exist_ok=True)
    selection_path = os.path.join(HERE, "..", "data", "design_selected.json")
    with open(selection_path, encoding="utf-8") as stream:
        selected = json.load(stream)

    params, equilibrium_raw = params_from_design(selected["design"])
    equilibrium = np.asarray(equilibrium_raw, dtype=float)
    per_capita = np.asarray(reduced_matrix(*equilibrium, params), dtype=float)
    state_jacobian = np.asarray(full_jacobian(*equilibrium, params), dtype=float)
    d_star = np.asarray(selected["direct"]["worst_d_geomean1"], dtype=float)

    # R_* diag(u_*) B = D_* B exactly.  Multiplying the nonlinear equations
    # by R_* therefore realizes the same positive-diagonal orbit point.
    equation_rates = d_star / equilibrium
    scaled_jacobian = np.diag(equation_rates) @ state_jacobian
    target_jacobian = np.diag(d_star) @ per_capita
    if not np.allclose(scaled_jacobian, target_jacobian, rtol=1e-13, atol=1e-13):
        raise AssertionError("row-scaling identity R_* J = D_* B failed")

    equilibrium_residual = np.asarray(residuals(*equilibrium, params), dtype=float)
    if np.max(np.abs(equilibrium_residual)) > 1e-12:
        raise AssertionError("anchor is not an equilibrium to working precision")

    def rhs(_time: float, state: np.ndarray) -> np.ndarray:
        x, y, z = state
        per_capita_rhs = np.array(
            [
                g_da(x, params) - params.q1 * y - params.q2 * z,
                params.e1 * params.q1 * x - params.mu1 - params.c1 * y - params.h * z,
                params.e2 * params.q2 * x + params.e3 * params.h * y - params.mu2 - params.c2 * z,
            ]
        )
        return equation_rates * state * per_capita_rhs

    relative_initial = np.array([1.0e-3, -1.0e-3, 1.0e-3])
    initial = equilibrium * (1.0 + relative_initial)

    steps = sorted(set(float(step) for step in args.steps), reverse=True)
    if any(step <= 0.0 for step in steps):
        raise ValueError("all refinement steps must be positive")
    fractional: dict[float, tuple[np.ndarray, np.ndarray]] = {}
    for step in steps:
        fractional[step] = caputo_pece(rhs, initial, 0.9, args.t_end, step)

    finest_step = min(steps)
    times, fractional_states = fractional[finest_step]
    refinement = []
    for coarse_step, fine_step in zip(steps[:-1], steps[1:]):
        error = max_shared_grid_difference(
            fractional[coarse_step], fractional[fine_step], equilibrium
        )
        refinement.append(
            {"coarse_step": coarse_step, "fine_step": fine_step, "max_relative_difference": error}
        )
    if len(refinement) >= 2 and refinement[-1]["max_relative_difference"] > 0.0:
        refinement_ratio = refinement[-2]["max_relative_difference"] / refinement[-1]["max_relative_difference"]
        observed_order = math.log(refinement_ratio, 2.0)
    else:
        refinement_ratio = None
        observed_order = None

    def exit_event(_time: float, state: np.ndarray) -> float:
        return args.exit_radius - float(np.linalg.norm(state / equilibrium - 1.0))

    exit_event.terminal = True
    exit_event.direction = -1
    classical = solve_ivp(
        rhs,
        (0.0, args.t_end),
        initial,
        method="DOP853",
        rtol=1e-11,
        atol=1e-13,
        max_step=min(0.02, finest_step),
        events=exit_event,
        dense_output=True,
    )
    if not classical.success:
        raise RuntimeError(classical.message)
    classical_exit_time = float(classical.t_events[0][0]) if classical.t_events[0].size else None
    classical_end = classical_exit_time if classical_exit_time is not None else args.t_end

    stride = max(1, args.output_stride)
    output_times = times[::stride]
    if output_times[-1] != times[-1]:
        output_times = np.append(output_times, times[-1])
    fractional_output = np.vstack(
        [np.interp(output_times, times, fractional_states[:, j]) for j in range(3)]
    ).T
    classical_output = np.full_like(fractional_output, np.nan)
    valid = output_times <= classical_end + 1e-13
    classical_output[valid] = classical.sol(output_times[valid]).T

    csv_path = os.path.join(args.output_dir, "nonlinear_caputo_timeseries.csv")
    with open(csv_path, "w", newline="", encoding="utf-8") as stream:
        writer = csv.writer(stream)
        writer.writerow(
            [
                "t",
                "x_alpha_0.9",
                "y_alpha_0.9",
                "z_alpha_0.9",
                "x_alpha_1",
                "y_alpha_1",
                "z_alpha_1",
            ]
        )
        writer.writerows(np.column_stack([output_times, fractional_output, classical_output]))

    eigenvalues = np.linalg.eigvals(scaled_jacobian)
    fractional_distance = relative_distance(fractional_states, equilibrium)
    classical_terminal = classical.y[:, -1]
    summary = {
        "model": "full nonlinear three-species Caputo Double-Allee IGP system W2-A",
        "interpretation": "numerical corroboration of local dynamics, not proof or empirical calibration",
        "alpha_fractional": 0.9,
        "alpha_classical": 1.0,
        "t_end": args.t_end,
        "production_step": finest_step,
        "refinement_steps": steps,
        "output_stride": stride,
        "equilibrium": equilibrium.tolist(),
        "initial_state": initial.tolist(),
        "initial_relative_perturbation": relative_initial.tolist(),
        "d_star_for_per_capita_matrix": d_star.tolist(),
        "equation_row_rates": equation_rates.tolist(),
        "row_scaling_identity_max_abs_error": float(np.max(np.abs(scaled_jacobian - target_jacobian))),
        "equilibrium_residual_max_abs": float(np.max(np.abs(equilibrium_residual))),
        "scaled_jacobian_eigenvalues": [[float(v.real), float(v.imag)] for v in eigenvalues],
        "minimum_eigenvalue_angle": float(np.min(np.abs(np.angle(eigenvalues)))),
        "matignon_boundary_alpha_0.9": 0.9 * math.pi / 2.0,
        "fractional": {
            "initial_relative_distance": float(fractional_distance[0]),
            "final_relative_distance": float(fractional_distance[-1]),
            "maximum_relative_distance": float(np.max(fractional_distance)),
            "minimum_state": float(np.min(fractional_states)),
            "final_state": fractional_states[-1].tolist(),
        },
        "classical": {
            "exit_radius": args.exit_radius,
            "exit_time": classical_exit_time,
            "terminal_time": float(classical.t[-1]),
            "terminal_relative_distance": float(np.linalg.norm(classical_terminal / equilibrium - 1.0)),
            "minimum_state_before_exit": float(np.min(classical.y)),
            "terminal_state": classical_terminal.tolist(),
        },
        "step_refinement": refinement,
        "refinement_error_ratio": refinement_ratio,
        "observed_refinement_order": observed_order,
        "software": {
            "host": platform.node(),
            "python": platform.python_version(),
            "numpy": np.__version__,
            "scipy": __import__("scipy").__version__,
            "elapsed_seconds": time.time() - started,
        },
        "data_file": os.path.basename(csv_path),
    }
    summary_path = os.path.join(args.output_dir, "nonlinear_caputo_summary.json")
    with open(summary_path, "w", encoding="utf-8") as stream:
        json.dump(summary, stream, indent=2)
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
