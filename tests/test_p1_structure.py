"""P1 structural checks: logit convexity, symmetric closed form, interval bracket.

NUMERICAL CORROBORATION except `test_interval_bracket_*`, which exercises the
CERTIFIED interval routine (its output is a rigorous enclosure of the
variational value for the given decimal inputs).
"""
import mpmath as mp
import numpy as np
import pytest

from fdsn.c10_threshold import T1, mp_h_alpha, mp_siami_R3, objective_G, threshold, threshold_mp
from fdsn.interval_cert import certify_threshold


def test_elasticity_of_h_is_increasing_and_below_three_halves():
    for alpha in (0.67, 0.8, 0.95, 0.9999):
        t = alpha * np.pi / 2
        u, K = np.cos(t), -np.sin(3 * t) / np.sin(t)
        r = 2 * u / K * (1 + np.logspace(-8, 8, 4000))
        E = (K * r - 2 * u) * (1 + 3 * u * r) / ((K * r - u) * (1 + 2 * u * r))
        assert np.all(np.diff(E) > 0) and np.all((E > 0) & (E < 1.5))


def test_logit_objective_is_convex_on_random_points():
    rng = np.random.default_rng(3)
    n = 50000
    beta = np.exp(rng.normal(scale=2.5, size=(n, 3)))
    alpha = rng.uniform(0.6667, 0.99999, n)
    t = alpha * np.pi / 2
    u, K = np.cos(t), -np.sin(3 * t) / np.sin(t)
    y = rng.uniform(-12, 12, size=(n, 2))
    H = objective_G(y, beta, u, K)[2]
    assert np.all(np.linalg.eigvalsh(H)[:, 0] > 0)


@pytest.mark.parametrize("b", ["0.001", "0.2", "1", "7", "1000"])
@pytest.mark.parametrize("alpha", ["0.7", "0.9", "0.999"])
def test_symmetric_slice_closed_form(b, alpha):
    with mp.workdps(60):
        r = threshold_mp([b, b, b], alpha, dps=50)
        assert abs(r["T"] / (27 * mp_h_alpha(mp.mpf(b) / 3, alpha)) - 1) < mp.mpf(10) ** -45


def test_two_equal_slice_minimizer_is_symmetric():
    for beta in ([2.0, 2.0, 0.1], [0.05, 0.05, 30.0], [1.0, 1.0, 1.7]):
        x = threshold(beta, 0.85).x[0]
        # beta12 = beta13 is invariant under swapping species 2 and 3
        assert abs(x[1] - x[2]) < 1e-9


def test_siami_identity_symbolic_numeric():
    with mp.workdps(80):
        for a in ("0.68", "0.8", "0.97"):
            assert abs(27 * mp_h_alpha(mp.mpf(1) / 3, a) - 1 - mp_siami_R3(a) ** 3) < mp.mpf(10) ** -70


@pytest.mark.parametrize("beta,alpha", [(("1", "1", "1"), "0.9"), (("0.3", "2", "5"), "0.8")])
def test_interval_bracket_contains_hp_value(beta, alpha):
    r = certify_threshold(beta, alpha, dps=30)
    assert r["certified"]
    with mp.workdps(40):
        v = threshold_mp(beta, alpha, dps=35)["T"]
        assert r["L"] <= v * (1 + mp.mpf(10) ** -25) and v <= r["U"] * (1 + mp.mpf(10) ** -25)
        assert r["L"] > T1(np.array([float(b) for b in beta]))
