"""Wave-2 regression tests: certificates, canonical witnesses, C-15 sensitivities.

NUMERICAL CORROBORATION; the interval routines produce rigorous brackets for
the variational value but the tests themselves only check consistency.
"""
import mpmath as mp
import numpy as np
import pytest

from fdsn.c10_threshold import T1, h_derivs, invariants_batch, threshold, threshold_batch, threshold_mp
from fdsn.direct_margin import min_margin, mp_margin
from fdsn.interval_cert import certify_threshold, certify_threshold_logit

CASES = [(("1", "1", "1"), "0.9"), (("0.3", "2", "5"), "0.8"), (("5/2", "1/3", "7"), "0.95"),
         (("1e-4", "1", "1e4"), "0.7")]


def _dec(b):
    return b if "/" not in b else mp.nstr(mp.mpf(b.split("/")[0]) / mp.mpf(b.split("/")[1]), 45)


@pytest.mark.parametrize("beta,alpha", CASES)
def test_logit_certificate_brackets_hp_value(beta, alpha):
    r = certify_threshold_logit(beta, alpha, dps=40)
    assert r["certified"]
    with mp.workdps(50):
        v = threshold_mp([_dec(b) for b in beta], alpha, dps=45)
        assert r["L"] <= v["T"] <= r["U"]
        assert r["rel_width"] < mp.mpf(10) ** -30
        # rigorous optimizer enclosure contains the HP minimiser
        d = mp.sqrt(sum((v["x"][i] - r["x_hat"][i]) ** 2 for i in range(3)))
        assert d <= r["x_enclosure_radius"]


@pytest.mark.parametrize("beta,alpha", CASES[:3])
def test_two_certificates_agree(beta, alpha):
    a = certify_threshold(beta, alpha, dps=35, time_limit=200)
    b = certify_threshold_logit(beta, alpha, dps=35)
    assert a["certified"] and b["certified"]
    assert max(a["L"], b["L"]) <= min(a["U"], b["U"])


# canonical witnesses (subset of computations/results/wave2/CANONICAL_WITNESSES.csv)
WITNESSES = [
    ([[-1, 0, -2.5], [2.5, -1, 0], [0, 2.5, -1]], 0.9),
    ([[-1, -3, 0], [0, -1, -2], [-2, 0, -1]], 0.8),
    ([[-1, -3, -0.5], [0.5, -1, 3], [3, -0.5, -1]], 0.7),
    ([[-1, -1.5, 0], [-0.5, -1, -3], [-3, 0, -2]], 0.7),
    ([[-1, -0.5, -3], [2, -1, -0.5], [0, 2, -1]], 0.99),
]


@pytest.mark.parametrize("A,alpha", WITNESSES)
def test_witness_is_genuinely_fractional_two_routes(A, alpha):
    A = np.array(A, float)
    p, m, q, beta, kappa = invariants_batch(A[None])
    assert np.all(m > 0) and q > 0
    Ta = threshold(beta[0], alpha).T[0]
    assert T1(beta[0]) < kappa[0] < Ta                     # C-10 band
    assert min_margin(A[None], alpha, half_width=14)["margin"][0] > 0     # in F_alpha (direct)
    assert min_margin(A[None], 1.0, half_width=14)["margin"][0] < 0       # not Hurwitz D-stable (direct)


def test_c15_sensitivity_identity_float():
    rng = np.random.default_rng(9)
    beta = np.exp(rng.normal(scale=1.5, size=(40, 3)))
    alpha = rng.uniform(0.7, 0.99, 40)
    tb = threshold_batch(beta, alpha)
    t = alpha * np.pi / 2
    u, K = np.cos(t), -np.sin(3 * t) / np.sin(t)
    B = beta[:, 0] * tb.x[:, 0] * tb.x[:, 1] + beta[:, 1] * tb.x[:, 0] * tb.x[:, 2] + beta[:, 2] * tb.x[:, 1] * tb.x[:, 2]
    h, h1, _ = h_derivs(B, u, K)
    for k, xk in ((0, 2), (1, 1), (2, 0)):
        an = h1 / tb.x[:, xk]
        hk = 1e-3 * beta[:, k]
        def f(s):
            b2 = beta.copy(); b2[:, k] += s
            return threshold_batch(b2, alpha).T
        fd = (4 * (f(hk / 2) - f(-hk / 2)) / hk - (f(hk) - f(-hk)) / (2 * hk)) / 3
        assert np.max(np.abs(fd / an - 1)) < 1e-6
    E = B * h1 / h
    euler = (beta * np.stack([h1 / tb.x[:, 2], h1 / tb.x[:, 1], h1 / tb.x[:, 0]], 1)).sum(1) / (E * tb.T)
    assert np.max(np.abs(euler - 1)) < 1e-12
    assert np.all((E > 0) & (E < 1.5))


def test_d_star_direct_margin_positive_for_witness_hp():
    A = [[-1, -3, 0], [0, -1, -2], [-2, 0, -1]]
    with mp.workdps(40):
        Am = mp.matrix(A)
        r = threshold_mp(["3", "1", "1"], "0.8", dps=35)       # beta of this matrix: m12=1,m13=1,m23=1? recomputed below
        p, m, q, beta, kappa = invariants_batch(np.array(A, float)[None])
        r = threshold_mp([repr(float(b)) for b in beta[0]], "0.8", dps=35)
        d = [r["x"][i] / mp.mpf(float(p[0][i])) for i in range(3)]
        assert mp_margin(Am, d, "0.8", 35)[0] > 0
