import numpy as np

from fdsn.cubic_certificate import (
    cubic_coefficient_ratio,
    fractional_cain_phi,
    fractional_cain_threshold,
    negative_is_strict_p_matrix,
    orbit_minimizing_diagonal,
    passes_fractional_cain_certificate,
    fractional_orbit_invariants,
    fractional_orbit_threshold,
    classical_cain_threshold_from_invariants,
    passes_exact_variational_certificate,
)
from fdsn.spectral import is_integer_order_stable


def a_gamma(gamma: float) -> np.ndarray:
    return np.array(
        [
            [-1.0, 0.0, -gamma],
            [gamma, -1.0, 0.0],
            [0.0, gamma, -1.0],
        ]
    )


def test_phi_matches_closed_form_for_c09_witness():
    gamma = 2.1
    A = a_gamma(gamma)
    assert negative_is_strict_p_matrix(A)
    np.testing.assert_allclose(
        fractional_cain_phi(A),
        9.0 / (1.0 + gamma**3),
        rtol=1e-12,
        atol=1e-12,
    )


def test_orbit_optimizer_attains_exact_phi_after_nonuniform_row_scaling():
    A = a_gamma(2.05)
    E = np.diag([0.4, 2.0, 5.0])
    B = E @ A

    d_star = orbit_minimizing_diagonal(B)
    np.testing.assert_allclose(
        cubic_coefficient_ratio(B, d_star),
        fractional_cain_phi(B),
        rtol=1e-12,
        atol=1e-12,
    )


def test_phi_is_invariant_under_positive_left_diagonal_scaling():
    A = a_gamma(2.02)
    E = np.diag([0.2, 3.0, 7.0])
    np.testing.assert_allclose(
        fractional_cain_phi(E @ A),
        fractional_cain_phi(A),
        rtol=1e-12,
        atol=1e-12,
    )


def test_high_order_fractional_certificate_can_hold_beyond_hurwitz_d_stability():
    alpha = 0.99
    gamma = 2.001
    A = a_gamma(gamma)

    assert fractional_cain_phi(A) > fractional_cain_threshold(alpha)
    assert passes_fractional_cain_certificate(A, alpha)
    assert not is_integer_order_stable(A)


def test_fractional_threshold_tends_to_classical_cain_threshold():
    values = [fractional_cain_threshold(a) for a in (0.9, 0.99, 0.9999)]
    assert values[0] < values[1] < values[2] < 1.0
    assert abs(values[-1] - 1.0) < 1e-3



def test_c10_invariants_are_left_diagonal_invariant():
    A = a_gamma(2.3)
    E = np.diag([0.3, 2.0, 6.0])
    beta_a, kappa_a = fractional_orbit_invariants(A)
    beta_b, kappa_b = fractional_orbit_invariants(E @ A)
    np.testing.assert_allclose(beta_a, beta_b, rtol=1e-12, atol=1e-12)
    np.testing.assert_allclose(kappa_a, kappa_b, rtol=1e-12, atol=1e-12)


def test_c10_symmetric_cycle_threshold_matches_siami_formula():
    alpha = 0.9
    A = a_gamma(2.2)
    threshold = fractional_orbit_threshold(A, alpha)

    theta = alpha * np.pi / 2.0
    r3 = np.sin(theta) / np.sin(theta - np.pi / 3.0)
    expected_kappa_threshold = 1.0 + r3**3

    np.testing.assert_allclose(
        threshold,
        expected_kappa_threshold,
        rtol=1e-8,
        atol=1e-8,
    )


def test_c10_classical_limit_is_cain_threshold_for_symmetric_cycle():
    A = a_gamma(2.2)
    np.testing.assert_allclose(
        classical_cain_threshold_from_invariants(A),
        9.0,
        rtol=1e-12,
        atol=1e-12,
    )


def test_phi_certificate_is_not_necessary_but_c10_accepts_gap_point():
    alpha = 0.9
    theta = alpha * np.pi / 2.0
    rho = (1.0 - 2.0 * np.cos(theta)) ** 2
    gamma_phi = (9.0 / rho - 1.0) ** (1.0 / 3.0)
    r3 = np.sin(theta) / np.sin(theta - np.pi / 3.0)

    gamma = 0.5 * (gamma_phi + r3)
    A = a_gamma(gamma)

    assert gamma > 2.0
    assert fractional_cain_phi(A) < fractional_cain_threshold(alpha)
    assert not passes_fractional_cain_certificate(A, alpha)
    assert passes_exact_variational_certificate(A, alpha)
