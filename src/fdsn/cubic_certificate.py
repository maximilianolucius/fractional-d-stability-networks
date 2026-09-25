"""Analytic 3x3 invariants used by the C-09/C-11 theorem package.

These functions implement exact algebraic quantities from the proofs.  They do
not replace the proofs in research/THEOREM_C09_DIMENSION_THRESHOLD.md and
research/THEOREM_C11_FRACTIONAL_CAIN_CERTIFICATE.md.
"""
from __future__ import annotations

import numpy as np
from numpy.typing import ArrayLike


def _as_3x3(matrix: ArrayLike) -> np.ndarray:
    A = np.asarray(matrix, dtype=float)
    if A.shape != (3, 3):
        raise ValueError("matrix must be real 3x3")
    return A


def signed_principal_data(matrix: ArrayLike) -> tuple[np.ndarray, np.ndarray, float]:
    """Return (p, m, q) for the strict-P analysis of -A.

    p[i] = -a_ii.
    m = (m12, m13, m23), the order-two principal minors of A.
    q = -det(A).

    For -A to be a strict P-matrix all seven returned quantities must be
    strictly positive.
    """
    A = _as_3x3(matrix)
    p = -np.diag(A).copy()
    m12 = float(np.linalg.det(A[np.ix_([0, 1], [0, 1])]))
    m13 = float(np.linalg.det(A[np.ix_([0, 2], [0, 2])]))
    m23 = float(np.linalg.det(A[np.ix_([1, 2], [1, 2])]))
    q = float(-np.linalg.det(A))
    return p, np.array([m12, m13, m23], dtype=float), q


def negative_is_strict_p_matrix(matrix: ArrayLike, tol: float = 0.0) -> bool:
    """Whether -A is a strict P-matrix, using its principal minors."""
    p, m, q = signed_principal_data(matrix)
    return bool(np.all(p > tol) and np.all(m > tol) and q > tol)


def fractional_cain_phi(matrix: ArrayLike) -> float:
    """Exact minimum of (a_D b_D)/c_D over all positive diagonal D.

    Requires -A to be a strict P-matrix.  In the notation of Cain's complete
    3x3 D-stability criterion, Phi = Delta^2 / q.
    """
    p, m, q = signed_principal_data(matrix)
    if not (np.all(p > 0.0) and np.all(m > 0.0) and q > 0.0):
        raise ValueError("-matrix must be a strict P-matrix")

    m12, m13, m23 = m
    delta = (
        np.sqrt(p[0] * m23)
        + np.sqrt(p[1] * m13)
        + np.sqrt(p[2] * m12)
    )
    return float(delta * delta / q)


def orbit_minimizing_diagonal(matrix: ArrayLike, normalize: str = "geomean") -> np.ndarray:
    """Return a positive diagonal vector attaining the C-11 orbit minimum.

    The optimizer is unique up to a common positive scalar.
    """
    p, m, q = signed_principal_data(matrix)
    del q
    if not (np.all(p > 0.0) and np.all(m > 0.0)):
        raise ValueError("-matrix must have positive order-one and order-two principal minors")
    m12, m13, m23 = m
    d = np.array(
        [
            np.sqrt(m23 / p[0]),
            np.sqrt(m13 / p[1]),
            np.sqrt(m12 / p[2]),
        ],
        dtype=float,
    )
    if normalize == "geomean":
        d /= float(np.prod(d) ** (1.0 / 3.0))
    elif normalize == "first":
        d /= d[0]
    elif normalize != "none":
        raise ValueError("normalize must be 'geomean', 'first', or 'none'")
    return d


def cubic_coefficient_ratio(matrix: ArrayLike, diagonal: ArrayLike) -> float:
    """Compute (a_D b_D)/c_D for det(lambda I - D A)."""
    A = _as_3x3(matrix)
    d = np.asarray(diagonal, dtype=float)
    if d.shape != (3,) or np.any(d <= 0.0):
        raise ValueError("diagonal must contain three positive entries")
    p, m, q = signed_principal_data(A)
    m12, m13, m23 = m
    d1, d2, d3 = d
    a = p[0] * d1 + p[1] * d2 + p[2] * d3
    b = m12 * d1 * d2 + m13 * d1 * d3 + m23 * d2 * d3
    c = q * d1 * d2 * d3
    return float(a * b / c)


def fractional_cain_threshold(alpha: float) -> float:
    """rho_alpha=(1-2 cos(alpha*pi/2))^2 for the high-order cubic regime."""
    if not (2.0 / 3.0 < alpha < 1.0):
        raise ValueError("this threshold is used for 2/3 < alpha < 1")
    theta = alpha * np.pi / 2.0
    return float((1.0 - 2.0 * np.cos(theta)) ** 2)


def passes_fractional_cain_certificate(matrix: ArrayLike, alpha: float) -> bool:
    """Sufficient analytic certificate for 3x3 fractional D-stability.

    For 2/3 < alpha < 1, strict-P(-A) plus Phi(A)>rho_alpha implies
    sigma(D A) is inside the Matignon region for every positive diagonal D.
    """
    if not negative_is_strict_p_matrix(matrix):
        return False
    return fractional_cain_phi(matrix) > fractional_cain_threshold(alpha)
