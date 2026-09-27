"""Time integration helpers for commensurate Caputo initial-value problems.

The predictor--evaluate--corrector--evaluate routine below is the standard
fractional Adams--Bashforth--Moulton (PECE) discretization.  It is intentionally
small and transparent: manuscript computations use it as numerical
corroboration, never as a replacement for the analytic stability criterion.
"""
from __future__ import annotations

import math
from collections.abc import Callable

import numpy as np

Array = np.ndarray


def caputo_pece(
    rhs: Callable[[float, Array], Array],
    initial: Array,
    alpha: float,
    t_end: float,
    step: float,
) -> tuple[Array, Array]:
    """Integrate ``C D_t^alpha y = rhs(t, y)`` with one PECE correction.

    Parameters
    ----------
    rhs:
        Right-hand side of the Caputo system.
    initial:
        State at ``t=0``.
    alpha:
        Commensurate derivative order in ``(0, 1]``.
    t_end, step:
        Final time and uniform step. ``t_end / step`` must be integral to
        floating-point tolerance.

    Notes
    -----
    The direct history sum is quadratic in the number of time steps.  This is
    adequate for the short, three-state convergence study used in the paper
    and keeps the numerical method independently auditable.
    """
    if not 0.0 < alpha <= 1.0:
        raise ValueError("alpha must lie in (0, 1]")
    if t_end <= 0.0 or step <= 0.0:
        raise ValueError("t_end and step must be positive")

    n_steps = int(round(t_end / step))
    if not math.isclose(n_steps * step, t_end, rel_tol=1e-12, abs_tol=1e-12):
        raise ValueError("t_end must be an integer multiple of step")

    y0 = np.asarray(initial, dtype=float)
    if y0.ndim != 1:
        raise ValueError("initial must be a one-dimensional state vector")

    times = np.linspace(0.0, t_end, n_steps + 1)
    states = np.empty((n_steps + 1, y0.size), dtype=float)
    values = np.empty_like(states)
    states[0] = y0
    values[0] = np.asarray(rhs(0.0, y0), dtype=float)

    lag = np.arange(n_steps + 2, dtype=float)
    predictor_weights = (lag + 1.0) ** alpha - lag**alpha
    corrector_weights = np.zeros(n_steps + 2, dtype=float)
    k = lag[1:]
    corrector_weights[1:] = (
        (k + 1.0) ** (alpha + 1.0)
        - 2.0 * k ** (alpha + 1.0)
        + (k - 1.0) ** (alpha + 1.0)
    )
    predictor_scale = step**alpha / math.gamma(alpha + 1.0)
    corrector_scale = step**alpha / math.gamma(alpha + 2.0)

    for n in range(1, n_steps + 1):
        predictor_history = predictor_weights[n - 1 :: -1] @ values[:n]
        predicted = y0 + predictor_scale * predictor_history

        first_weight = (n - 1.0) ** (alpha + 1.0) - (n - 1.0 - alpha) * n**alpha
        corrector_history = first_weight * values[0]
        if n > 1:
            corrector_history += corrector_weights[n - 1 : 0 : -1] @ values[1:n]
        states[n] = y0 + corrector_scale * (
            np.asarray(rhs(times[n], predicted), dtype=float) + corrector_history
        )
        values[n] = np.asarray(rhs(times[n], states[n]), dtype=float)

        if not np.all(np.isfinite(states[n])):
            raise FloatingPointError(f"non-finite PECE state at step {n}")

    return times, states
