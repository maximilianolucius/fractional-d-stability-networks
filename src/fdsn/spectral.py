"""Spectral criteria for commensurate Caputo systems.

For 0 < alpha <= 1, Matignon's criterion states that an equilibrium of
D^alpha x = A x is asymptotically stable iff every eigenvalue lambda of A
satisfies |arg(lambda)| > alpha*pi/2.
"""
from __future__ import annotations

import numpy as np
from numpy.typing import ArrayLike


def eigenvalues(matrix: ArrayLike) -> np.ndarray:
    A = np.asarray(matrix, dtype=np.complex128)
    if A.ndim != 2 or A.shape[0] != A.shape[1]:
        raise ValueError("matrix must be square")
    return np.linalg.eigvals(A)


def _validate_alpha(alpha: float) -> None:
    if not (0.0 < alpha <= 1.0):
        raise ValueError("alpha must satisfy 0 < alpha <= 1")


def fractional_stability_margin(matrix: ArrayLike, alpha: float) -> float:
    """Return min_i |arg(lambda_i)| - alpha*pi/2 in radians.

    Positive margin => strict fractional asymptotic stability.
    Zero eigenvalues are unstable and return -alpha*pi/2.
    """
    _validate_alpha(alpha)
    vals = eigenvalues(matrix)
    if np.any(np.isclose(np.abs(vals), 0.0)):
        return float(-alpha * np.pi / 2.0)
    angles = np.abs(np.angle(vals))
    return float(np.min(angles) - alpha * np.pi / 2.0)


def is_fractionally_stable(matrix: ArrayLike, alpha: float, tol: float = 1e-12) -> bool:
    return fractional_stability_margin(matrix, alpha) > tol


def is_integer_order_stable(matrix: ArrayLike, tol: float = 1e-12) -> bool:
    vals = eigenvalues(matrix)
    return bool(np.max(np.real(vals)) < -tol)


def is_purely_fractionally_stabilized(
    matrix: ArrayLike, alpha: float, tol: float = 1e-12
) -> bool:
    """Stable fractionally, but not Hurwitz stable at alpha=1."""
    vals = eigenvalues(matrix)
    frac = fractional_stability_margin(matrix, alpha) > tol
    first_order_unstable = np.max(np.real(vals)) > tol
    return bool(frac and first_order_unstable)


def critical_fractional_order(matrix: ArrayLike) -> float:
    """Spectral threshold alpha_c = (2/pi) min_i |arg(lambda_i)|.

    For a nonsingular matrix, strict Matignon stability holds for alpha < alpha_c.
    The returned value is not clipped to 1 so the geometry remains explicit.
    """
    vals = eigenvalues(matrix)
    if np.any(np.isclose(np.abs(vals), 0.0)):
        return 0.0
    return float((2.0 / np.pi) * np.min(np.abs(np.angle(vals))))
