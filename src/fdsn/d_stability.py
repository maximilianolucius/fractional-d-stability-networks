"""Numerical diagnostics related to fractional D-stability.

IMPORTANT: finite sampling over positive diagonal matrices D cannot prove
D-stability. These routines are falsification/exploration tools only.
"""
from __future__ import annotations

from dataclasses import dataclass
import numpy as np
from numpy.typing import ArrayLike

from .spectral import fractional_stability_margin


@dataclass(frozen=True)
class DStabilitySampleResult:
    passed: bool
    worst_margin: float
    worst_diagonal: np.ndarray
    samples: int
    alpha: float


def fractional_d_stability_sample(
    matrix: ArrayLike,
    alpha: float,
    *,
    n_samples: int = 10_000,
    log10_scale: tuple[float, float] = (-3.0, 3.0),
    seed: int = 0,
) -> DStabilitySampleResult:
    """Sample positive diagonal scalings D and test D @ A numerically.

    Diagonal entries are sampled log-uniformly over 10**log10_scale.
    A negative worst margin gives a concrete numerical counterexample candidate;
    a positive result is evidence only, never a proof.
    """
    A = np.asarray(matrix, dtype=float)
    if A.ndim != 2 or A.shape[0] != A.shape[1]:
        raise ValueError("matrix must be square")
    if n_samples < 1:
        raise ValueError("n_samples must be positive")

    rng = np.random.default_rng(seed)
    lo, hi = log10_scale
    worst_margin = np.inf
    worst_d = np.ones(A.shape[0])

    for _ in range(n_samples):
        d = 10.0 ** rng.uniform(lo, hi, size=A.shape[0])
        margin = fractional_stability_margin(np.diag(d) @ A, alpha)
        if margin < worst_margin:
            worst_margin = margin
            worst_d = d.copy()

    return DStabilitySampleResult(
        passed=bool(worst_margin > 0.0),
        worst_margin=float(worst_margin),
        worst_diagonal=worst_d,
        samples=n_samples,
        alpha=alpha,
    )
