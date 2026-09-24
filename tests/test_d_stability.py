import numpy as np

from fdsn.d_stability import fractional_d_stability_sample


def test_negative_diagonal_matrix_passes_sample():
    A = np.diag([-1.0, -2.0, -3.0])
    out = fractional_d_stability_sample(A, 1.0, n_samples=100, seed=42)
    assert out.passed
    assert out.worst_margin > 0
