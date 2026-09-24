import numpy as np

from fdsn.spectral import (
    critical_fractional_order,
    is_fractionally_stable,
    is_integer_order_stable,
    is_purely_fractionally_stabilized,
)


def test_hurwitz_matrix_is_fractionally_stable_for_alpha_le_1():
    A = np.diag([-1.0, -2.0])
    assert is_integer_order_stable(A)
    assert is_fractionally_stable(A, 1.0)
    assert is_fractionally_stable(A, 0.5)


def test_pure_fractional_stabilization_example():
    A = np.array([[0.1, -1.0], [1.0, 0.1]])
    assert not is_integer_order_stable(A)
    assert critical_fractional_order(A) < 1.0
    assert is_purely_fractionally_stabilized(A, 0.8)


def test_positive_real_eigenvalue_never_fractionally_stable():
    A = np.diag([1.0, -2.0])
    assert not is_fractionally_stable(A, 0.2)
