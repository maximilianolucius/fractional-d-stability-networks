"""Ecological-network helpers, including generalized Lotka--Volterra models."""
from __future__ import annotations

import numpy as np
from numpy.typing import ArrayLike


def glv_equilibrium(interaction: ArrayLike, growth: ArrayLike) -> np.ndarray:
    """Solve A x* + r = 0 for a GLV equilibrium."""
    A = np.asarray(interaction, dtype=float)
    r = np.asarray(growth, dtype=float)
    return np.linalg.solve(A, -r)


def glv_jacobian_at_equilibrium(interaction: ArrayLike, equilibrium: ArrayLike) -> np.ndarray:
    """For a GLV equilibrium, J = diag(x*) A."""
    A = np.asarray(interaction, dtype=float)
    x = np.asarray(equilibrium, dtype=float)
    return np.diag(x) @ A
