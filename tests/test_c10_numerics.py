"""Float-level and randomized (fixed-seed) checks of the C-10 numerical tools.

NUMERICAL CORROBORATION ONLY.
"""
import numpy as np
import pytest
from hypothesis import given, settings, strategies as st

from fdsn.c10_threshold import (
    T1,
    h_alpha,
    invariants_batch,
    matrix_from_invariants,
    phi_threshold,
    rate_constant,
    siami_R3,
    threshold,
    threshold_batch,
    threshold_mp,
)
from fdsn.direct_margin import margins_batch, min_margin

HYP = settings(max_examples=60, deadline=None, derandomize=True)
pos = st.floats(min_value=1e-3, max_value=1e3, allow_nan=False)
alph = st.floats(min_value=0.67, max_value=0.9999)


@HYP
@given(pos, pos, pos, alph)
def test_threshold_is_permutation_symmetric(b12, b13, b23, alpha):
    base = threshold([b12, b13, b23], alpha).T[0]
    for perm in ([b13, b12, b23], [b23, b13, b12], [b12, b23, b13]):
        # any relabelling of species permutes the three pair invariants
        assert abs(threshold(perm, alpha).T[0] / base - 1) < 1e-11


@HYP
@given(pos, pos, pos, alph, st.integers(0, 2), st.floats(1.001, 3.0))
def test_threshold_monotone_in_each_beta(b12, b13, b23, alpha, k, f):
    b = np.array([b12, b13, b23])
    b2 = b.copy()
    b2[k] *= f
    assert threshold(b2, alpha).T[0] >= threshold(b, alpha).T[0] * (1 - 1e-12)


@HYP
@given(pos, pos, pos, alph)
def test_band_ordering_T1_lt_Tphi_le_Talpha(b12, b13, b23, alpha):
    b = np.array([b12, b13, b23])
    Ta = threshold(b, alpha).T[0]
    assert T1(b) < phi_threshold(b, alpha) <= Ta * (1 + 1e-12)


@HYP
@given(pos, pos, pos, alph)
def test_minimizer_is_interior_nondegenerate(b12, b13, b23, alpha):
    r = threshold([b12, b13, b23], alpha, n_starts=4)
    assert r.grad_norm[0] < 1e-9
    assert r.hess_min_eig[0] > 0
    assert np.all(r.x[0] > 0)


def test_batch_matches_mp():
    rng = np.random.default_rng(7)
    beta = np.exp(rng.normal(scale=1.5, size=(12, 3)))
    alpha = rng.uniform(0.7, 0.999, size=12)
    tb = threshold_batch(beta, alpha)
    for i in range(12):
        m = threshold_mp(beta[i], alpha[i], dps=40)
        assert abs(float(m["T"]) / tb.T[i] - 1) < 1e-12


def test_classical_limit_and_rate_float():
    b = np.array([0.4, 2.0, 1.3])
    for eps in (1e-3, 1e-4):
        T = threshold(b, 1 - eps).T[0]
        assert abs((T - T1(b)) / eps / rate_constant(b) - 1) < 50 * eps


def test_symmetric_matches_siami_float():
    for a in (0.7, 0.8, 0.95):
        assert abs(threshold([1, 1, 1], a).T[0] / (1 + siami_R3(a) ** 3) - 1) < 1e-13


def test_h_alpha_exceeds_b():
    b = np.logspace(-6, 6, 200)
    for a in (0.7, 0.9, 0.999):
        assert np.all(h_alpha(b, a) > b)


@pytest.mark.parametrize("seed", range(3))
def test_matrix_from_invariants_roundtrip(seed):
    rng = np.random.default_rng(seed)
    beta = np.exp(rng.normal(size=3))
    kappa = float(T1(beta) * 1.3)
    A = None
    while A is None:
        A = matrix_from_invariants(beta, kappa, p=np.exp(rng.normal(size=3)), rng=rng)
        kappa *= 1.05
    kappa /= 1.05
    _, _, _, b2, k2 = invariants_batch(A[None])
    assert np.allclose(b2[0], beta, rtol=1e-10) and abs(k2[0] / kappa - 1) < 1e-10


def test_direct_margin_agrees_with_c10_on_fixed_random_sample():
    """Direct eigenvalue optimisation vs C-10 classification (float, fixed seed)."""
    rng = np.random.default_rng(11)
    As, pred = [], []
    alpha = 0.85
    while len(As) < 40:
        beta = np.exp(rng.normal(size=3))
        T = threshold(beta, alpha).T[0]
        f = rng.choice([0.9, 0.99, 1.01, 1.1])
        A = matrix_from_invariants(beta, T * f, p=np.exp(rng.normal(size=3)), rng=rng)
        if A is None:
            continue
        As.append(A)
        pred.append(f < 1)
    r = min_margin(np.array(As), alpha)
    assert np.all((r["margin"] > 0) == np.array(pred))


def test_margins_batch_shape_and_sign():
    A = np.array([[[-1.0, 0, -2.0], [2.0, -1.0, 0], [0, 2.0, -1.0]]])
    m = margins_batch(A, np.zeros((1, 1, 2)), np.array([1.0]))
    assert m.shape == (1, 1) and abs(m[0, 0]) < 1e-12   # gamma = 2: Hurwitz boundary
