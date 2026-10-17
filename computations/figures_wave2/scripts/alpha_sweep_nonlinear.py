"""Alpha sweep of the full nonlinear W2-A Caputo model near the predicted stability boundary
(reviewer request R2-6; also documents the role of the row scaling, R1-6).

Two positive row scalings of the same nonlinear model are integrated for a grid of orders alpha:
  * "worst":    R_* = D_* diag(u*)^-1, the diagonal found by the scale-invariant spectral search
                (R_* J = D_* B); the theorem predicts loss of Matignon stability exactly at the order
                alpha_* with T_{alpha_*}(beta) = kappa, and for THIS diagonal the linear boundary order
                is alpha_c = (2/pi) min|arg lambda(D_* B)|;
  * "unscaled": R = I (the original Jacobian J = diag(u*) B), which is Hurwitz stable, so every alpha
                in (0, 1] is predicted locally stable.
For alpha < 1 the fractional Adams-Bashforth-Moulton PECE method (fdsn.caputo.caputo_pece) is used with
two steps (refinement check); at alpha = 1 both PECE (alpha = 1) and an adaptive DOP853 run are
reported.  Unstable trajectories are stopped at the declared relative radius.  Numerical corroboration
only; nothing here is part of a proof.
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
from multiprocessing import Pool

import numpy as np
from scipy.integrate import solve_ivp

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "src"))
sys.path.insert(0, HERE)

from design_tools import params_from_design  # noqa: E402
from fdsn.c10_threshold import T1, invariants_batch, threshold  # noqa: E402
from fdsn.caputo import caputo_pece  # noqa: E402
from fdsn.double_allee import full_jacobian, g_da, reduced_matrix, residuals  # noqa: E402

DATA = os.path.join(HERE, "..", "data")
SEL = json.load(open(os.path.join(DATA, "design_selected.json"), encoding="utf-8"))
PARAMS, EQ_RAW = params_from_design(SEL["design"])
EQ = np.asarray(EQ_RAW, dtype=float)
B = np.asarray(reduced_matrix(*EQ, PARAMS), dtype=float)
J = np.asarray(full_jacobian(*EQ, PARAMS), dtype=float)
D_STAR = np.asarray(SEL["direct"]["worst_d_geomean1"], dtype=float)
SCALINGS = {"worst": D_STAR / EQ, "unscaled": np.ones(3)}
RELATIVE_INITIAL = np.array([1.0e-3, -1.0e-3, 1.0e-3])
INITIAL = EQ * (1.0 + RELATIVE_INITIAL)


def per_capita_rhs(x, y, z):
    p = PARAMS
    return np.array([g_da(x, p) - p.q1 * y - p.q2 * z,
                     p.e1 * p.q1 * x - p.mu1 - p.c1 * y - p.h * z,
                     p.e2 * p.q2 * x + p.e3 * p.h * y - p.mu2 - p.c2 * z])


def make_rhs(rates):
    def rhs(_t, u):
        return rates * u * per_capita_rhs(*u)
    return rhs


def rel_dist(states):
    return np.linalg.norm(states / EQ - 1.0, axis=1)


def theorem_boundary_alpha(beta, kappa, lo=0.70, hi=1.0 - 1e-9, iters=60):
    """alpha_* with T_alpha(beta) = kappa (T_alpha decreases in alpha; T_1 < kappa < T_lo)."""
    f = lambda a: float(threshold(beta, a).T[0]) - kappa
    assert f(lo) > 0 > f(hi)
    for _ in range(iters):
        mid = 0.5 * (lo + hi)
        if f(mid) > 0:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def late_rates(t, dist, frac=0.5):
    """Fit log(dist) = a + p log t (algebraic) and log(dist) = a + s t (exponential) over the last `frac` of the run."""
    m = t > t[-1] * (1 - frac)
    m &= dist > 0
    if m.sum() < 10:
        return None, None
    p = np.polyfit(np.log(t[m]), np.log(dist[m]), 1)[0]
    s = np.polyfit(t[m], np.log(dist[m]), 1)[0]
    return float(p), float(s)


def run_job(job):
    scaling, alpha, t_end, steps, exit_radius, stride = job
    rates = SCALINGS[scaling]
    rhs = make_rhs(rates)
    stop = lambda _t, u: float(np.linalg.norm(u / EQ - 1.0)) > exit_radius
    t0 = time.time()
    out = {"scaling": scaling, "alpha": alpha, "t_end": t_end, "steps": steps}
    runs = {}
    for h in steps:
        tt, uu = caputo_pece(rhs, INITIAL, alpha, t_end, h, stop=stop)
        runs[h] = (tt, uu)
    hf = min(steps)
    t, u = runs[hf]
    dist = rel_dist(u)
    exit_idx = int(np.argmax(dist > exit_radius)) if np.any(dist > exit_radius) else None
    p_alg, s_exp = late_rates(t, dist) if exit_idx is None else (None, None)
    # refinement: compare on the shared grid up to the shorter run
    ref = []
    hs = sorted(steps, reverse=True)
    for hc, hfine in zip(hs[:-1], hs[1:]):
        tc, uc = runs[hc]; tf, uf = runs[hfine]
        r = int(round(hc / hfine)); n = min(len(uc), len(uf[::r]))
        ref.append({"coarse": hc, "fine": hfine, "max_relative_difference": float(np.max(np.abs((uc[:n] - uf[::r][:n]) / EQ))), "compared_points": n})
    out.update({
        "pece": {
            "production_step": hf,
            "n_steps": int(len(t) - 1),
            "initial_relative_distance": float(dist[0]),
            "final_relative_distance": float(dist[-1]),
            "final_time": float(t[-1]),
            "max_relative_distance": float(dist.max()),
            "exit_time": (float(t[exit_idx]) if exit_idx is not None else None),
            "min_state": float(u.min()),
            "late_algebraic_exponent": p_alg,
            "late_exponential_rate": s_exp,
            "refinement": ref,
        }
    })
    if alpha == 1.0:
        ev = lambda _t, u: exit_radius - float(np.linalg.norm(u / EQ - 1.0))
        ev.terminal = True; ev.direction = -1
        sol = solve_ivp(rhs, (0.0, t_end), INITIAL, method="DOP853", rtol=1e-11, atol=1e-13, max_step=0.02, events=ev, dense_output=True)
        dd = rel_dist(sol.y.T)
        out["dop853"] = {"exit_time": (float(sol.t_events[0][0]) if sol.t_events[0].size else None), "final_time": float(sol.t[-1]),
                         "final_relative_distance": float(dd[-1]), "max_relative_distance": float(dd.max()), "success": bool(sol.success)}
    # downsampled series
    ts = t[::stride]
    if ts[-1] != t[-1]:
        ts = np.append(ts, t[-1])
    series = np.column_stack([ts, np.interp(ts, t, dist)])
    out["elapsed_seconds"] = time.time() - t0
    return out, series


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output-dir", default=DATA)
    ap.add_argument("--workers", type=int, default=16)
    ap.add_argument("--t-end", type=float, default=400.0)
    ap.add_argument("--t-end-near", type=float, default=800.0)
    ap.add_argument("--near", type=float, default=0.02, help="|alpha - alpha_*| below which t-end-near is used")
    ap.add_argument("--steps", type=float, nargs="+", default=[0.02, 0.01])
    ap.add_argument("--exit-radius", type=float, default=0.20)
    ap.add_argument("--stride", type=int, default=20)
    ap.add_argument("--quick", action="store_true")
    ap.add_argument("--dense", type=float, default=None, help="use a uniform alpha grid on [0.70, 1] with this spacing for the worst scaling")
    ap.add_argument("--tag", default="", help="suffix for the output file names")
    a = ap.parse_args()
    started = time.time()
    os.makedirs(a.output_dir, exist_ok=True)

    # exact invariants and predicted boundaries
    _, _, _, beta, kappa = invariants_batch(B[None]); beta = beta[0]; kappa = float(kappa[0])
    alpha_star = theorem_boundary_alpha(beta, kappa)
    ev_worst = np.linalg.eigvals(np.diag(D_STAR) @ B)
    alpha_c_worst = 2.0 * float(np.min(np.abs(np.angle(ev_worst)))) / math.pi
    ev_unscaled = np.linalg.eigvals(J)
    assert np.allclose(np.diag(SCALINGS["worst"]) @ J, np.diag(D_STAR) @ B, rtol=1e-12, atol=1e-12)
    assert np.max(np.abs(residuals(*EQ, PARAMS))) < 1e-12

    grid_worst = [0.70, 0.75, 0.80, 0.85, 0.90, 0.92, 0.93, 0.94, 0.96, 0.97, 0.98, 1.0]
    for d in (-0.01, -0.005, -0.002, 0.0, 0.002, 0.005, 0.01):
        grid_worst.append(round(alpha_star + d, 4))
    grid_worst = sorted(set(round(x, 4) for x in grid_worst if 0 < x <= 1.0))
    grid_unscaled = [0.80, 0.90, round(alpha_star, 4), 1.0]
    if a.dense:
        grid_worst = sorted(set([round(float(x), 4) for x in np.arange(0.70, 1.0 + 1e-9, a.dense)] + grid_worst))
        grid_unscaled = sorted(set([round(float(x), 4) for x in np.arange(0.70, 1.0 + 1e-9, 0.01)] + grid_unscaled))
    if a.quick:
        grid_worst = [0.9, round(alpha_star, 4), 1.0]; grid_unscaled = [0.9]
        a.t_end, a.t_end_near = 20.0, 20.0
    jobs = []
    for sc, grid in (("worst", grid_worst), ("unscaled", grid_unscaled)):
        for al in grid:
            t_end = a.t_end_near if (sc == "worst" and abs(al - alpha_star) < a.near) else a.t_end
            jobs.append((sc, al, t_end, tuple(a.steps), a.exit_radius, a.stride))
    with Pool(min(a.workers, len(jobs))) as pool:
        results = pool.map(run_job, jobs)

    rows, series_rows = [], []
    for (out, series) in results:
        sc, al = out["scaling"], out["alpha"]
        evs = ev_worst if sc == "worst" else ev_unscaled
        margin = float(np.min(np.abs(np.angle(evs)))) - al * math.pi / 2
        out["linear_prediction"] = {"angular_margin_rad": margin, "predicted": ("stable" if margin > 0 else "unstable")}
        out["observed"] = ("exits_radius" if out["pece"]["exit_time"] is not None else
                           ("decays" if out["pece"]["final_relative_distance"] < out["pece"]["initial_relative_distance"] else "grows_within_radius"))
        rows.append(out)
        for tt, dd in series:
            series_rows.append((sc, al, tt, dd))
    rows.sort(key=lambda r: (r["scaling"], r["alpha"]))
    summary = {
        "model": "full nonlinear three-species Caputo Double-Allee IGP system W2-A, positively row-scaled",
        "interpretation": "numerical corroboration across orders alpha; not proof, not calibration",
        "equilibrium": EQ.tolist(), "initial_relative_perturbation": RELATIVE_INITIAL.tolist(),
        "beta": beta.tolist(), "kappa": kappa, "T1": float(T1(beta)),
        "alpha_star_theorem": alpha_star, "T_alpha_star": float(threshold(beta, alpha_star).T[0]),
        "alpha_c_worst_diagonal": alpha_c_worst, "min_arg_worst": float(np.min(np.abs(np.angle(ev_worst)))),
        "eigenvalues_worst": [[v.real, v.imag] for v in ev_worst], "eigenvalues_unscaled": [[v.real, v.imag] for v in ev_unscaled],
        "d_star": D_STAR.tolist(), "row_rates": {k: v.tolist() for k, v in SCALINGS.items()},
        "exit_radius": a.exit_radius, "steps": a.steps, "t_end": a.t_end, "t_end_near": a.t_end_near,
        "runs": rows,
        "software": {"host": platform.node(), "python": platform.python_version(), "numpy": np.__version__, "scipy": __import__("scipy").__version__,
                     "elapsed_seconds": time.time() - started, "workers": a.workers},
    }
    with open(os.path.join(a.output_dir, f"alpha_sweep{a.tag}_summary.json"), "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=1)
    with open(os.path.join(a.output_dir, f"alpha_sweep{a.tag}_timeseries.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f); w.writerow(["scaling", "alpha", "t", "relative_distance"]); w.writerows(series_rows)
    print(f"alpha_* (theorem) = {alpha_star:.10f}   alpha_c(D_*) = {alpha_c_worst:.10f}")
    for r in rows:
        p = r["pece"]
        print(f"{r['scaling']:9s} alpha={r['alpha']:.4f} margin={r['linear_prediction']['angular_margin_rad']:+.4f} pred={r['linear_prediction']['predicted']:8s} "
              f"obs={r['observed']:18s} final={p['final_relative_distance']:.3e} exit={p['exit_time']} alg={p['late_algebraic_exponent']} ref={[x['max_relative_difference'] for x in p['refinement']]} {r['elapsed_seconds']:.0f}s")


if __name__ == "__main__":
    main()
