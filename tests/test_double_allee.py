"""Deterministic tests for the Double-Allee IGP audit (corroboration, not proof)."""
from fractions import Fraction as Fr

import mpmath as mp
import numpy as np
import pytest

from fdsn.c10_threshold import T1, invariants_batch, threshold, threshold_mp
from fdsn.direct_margin import min_margin, mp_margin
from fdsn.double_allee import (Params, chief_witness, coexistence_equilibria, embed_double_allee, g_da, g_da_prime, H_A,
                               invariants_of_matrix, prey_roots, quadratic_coeffs, realize_invariants, reduced_matrix,
                               residuals, with_m, yz_of_x)
from fdsn.interval_cert import certify_threshold_logit


def rnd_params(seed):
    rng = np.random.default_rng(seed)
    v = np.exp(rng.normal(size=14))
    v[7:10] = rng.uniform(0.1, 0.9, 3)          # efficiencies in (0,1)
    return Params(*v)


# ---------------------------------------------------------------- symbolic identities at random substitutions

@pytest.mark.parametrize("seed", range(5))
def test_invariant_identities_at_random_points(seed):
    """kappa = sum beta - 2 - L3 and the closed forms of DA-03, exactly in rational arithmetic."""
    rng = np.random.default_rng(seed)
    s, q1, q2, h, e1, e2, e3, c1, c2 = [Fr(int(rng.integers(1, 50)), int(rng.integers(1, 50))) for _ in range(9)]
    B = [[-s, -q1, -q2], [e1 * q1, -c1, -h], [e2 * q2, e3 * h, -c2]]
    inv = invariants_of_matrix(B)
    assert inv["m"] == (s * c1 + e1 * q1 ** 2, s * c2 + e2 * q2 ** 2, c1 * c2 + e3 * h ** 2)
    assert inv["q"] == s * (c1 * c2 + e3 * h ** 2) + c1 * e2 * q2 ** 2 + c2 * e1 * q1 ** 2 + h * q1 * q2 * (e1 * e3 - e2)
    assert inv["beta"] == (1 + e1 * q1 ** 2 / (s * c1), 1 + e2 * q2 ** 2 / (s * c2), 1 + e3 * h ** 2 / (c1 * c2))
    assert inv["L3"] == h * q1 * q2 * (e2 - e1 * e3) / (s * c1 * c2)
    assert inv["kappa"] == sum(inv["beta"]) - 2 - inv["L3"]


@pytest.mark.parametrize("seed", range(5))
def test_two_consumer_no_go_at_random_points(seed):
    rng = np.random.default_rng(seed)
    s, q1, q2, e1, e2, c11, c12, c21, c22 = [Fr(int(rng.integers(1, 50)), int(rng.integers(1, 50))) for _ in range(9)]
    B = [[-s, -q1, -q2], [e1 * q1, -c11, -c12], [e2 * q2, -c21, -c22]]
    inv = invariants_of_matrix(B)
    assert inv["L3"] == q1 * q2 * (c12 * e2 + c21 * e1) / (s * c11 * c22) > 0
    if min(inv["m"]) > 0:
        assert float(inv["kappa"]) < float(T1(np.array(inv["beta"], float)))


@pytest.mark.parametrize("seed", range(6))
def test_equilibrium_reconstruction(seed):
    """Quadratic roots, Y(X), Z(X) satisfy the three per-capita equations; J = diag(x) DF."""
    P = rnd_params(seed)
    P = Params(*[v for v in P.as_list()])
    for X in prey_roots(P):
        Y, Z = yz_of_x(X, P)
        res = residuals(X, Y, Z, P)
        assert max(abs(v) for v in res) < 1e-10 * (1 + abs(X) + abs(Y) + abs(Z))
    # numerical Jacobian of x_i F_i vs diag(x) DF at a (possibly non-positive) root: identity holds where F = 0
    roots = prey_roots(P)
    if not roots:
        return
    X = roots[0]; Y, Z = yz_of_x(X, P)
    if X > P.m:
        B = np.array(reduced_matrix(X, Y, Z, P), float)
        hstep = 1e-6

        def G(v):
            x, y, z = v
            f = residuals(x, y, z, P)
            return np.array([x * f[0], y * f[1], z * f[2]])
        v0 = np.array([X, Y, Z]); J = np.zeros((3, 3))
        for j in range(3):
            e = np.zeros(3); e[j] = hstep * max(1, abs(v0[j]))
            J[:, j] = (G(v0 + e) - G(v0 - e)) / (2 * e[j])
        assert np.allclose(J, np.diag(v0) @ B, rtol=1e-6, atol=1e-8)


def test_realization_reconstructs_exact_invariants():
    rng = np.random.default_rng(3)
    for _ in range(20):
        beta = 1 + np.exp(rng.normal(size=3)); kappa = beta.sum() - 2 + np.exp(rng.normal())
        s, c1, c2 = np.exp(rng.normal(size=3)); eta = rng.uniform(0.05, 0.95)
        q1, q2, h, e1, e2, e3 = realize_invariants(*beta, kappa, s=s, c1=c1, c2=c2, eta=eta)
        assert 0 < e2 < e1 * e3 < 1
        inv = invariants_of_matrix([[-s, -q1, -q2], [e1 * q1, -c1, -h], [e2 * q2, e3 * h, -c2]])
        assert np.allclose(inv["beta"], beta, rtol=1e-12) and abs(inv["kappa"] / kappa - 1) < 1e-12


def test_embedding_reproduces_slope_and_equilibrium():
    rng = np.random.default_rng(4)
    for _ in range(20):
        s = np.exp(rng.normal()); X = rng.uniform(0.5, 2); m = rng.uniform(0.05, 0.9) * X; a = np.exp(rng.normal())
        K = X + rng.uniform(0.01, 0.5) * (X - m) * (X + a) / (m + a)   # guarantees H_A > 0
        q1, q2, h = np.exp(rng.normal(size=3)); e1, e2, e3 = rng.uniform(0.1, 0.9, 3); c1, c2 = np.exp(rng.normal(size=2))
        P, Y, Z, Q, H = embed_double_allee(s, X, m, a, K, q1, q2, h, e1, e2, e3, c1, c2, rng.uniform(0.1, 0.9))
        assert H > 0 and Y > 0 and Z > 0
        assert abs(g_da(X, P) - Q) < 1e-12 * Q and abs(-g_da_prime(X, P) - s) < 1e-10 * s
        assert max(abs(v) for v in residuals(X, Y, Z, P)) < 1e-12


def test_m0_is_exactly_on_the_cain_boundary_hp():
    with mp.workdps(80):
        P = chief_witness(lambda v: mp.mpf(v))
        X = max(prey_roots(P)); Y, Z = yz_of_x(X, P)
        B = reduced_matrix(X, Y, Z, P); inv = invariants_of_matrix(B)
        assert abs(X - 1) < mp.mpf(10) ** -70
        assert all(abs(b - 2) < mp.mpf(10) ** -70 for b in inv["beta"])
        assert abs(inv["kappa"] - 18) < mp.mpf(10) ** -70          # T1(2,2,2) = 18


@pytest.mark.parametrize("m,expected", [(0.19, "classical"), (0.21, "frac_only")])
def test_one_point_each_side_of_the_crossing(m, expected):
    P = with_m(chief_witness(), m)
    eqs = coexistence_equilibria(P)
    assert len(eqs) == 1
    e = eqs[0]
    B = np.array(reduced_matrix(e["X"], e["Y"], e["Z"], P), float)
    p, mm, q, beta, kappa = invariants_batch(B[None])
    t1 = T1(beta[0]); Ta = threshold(beta[0], 0.9).T[0]
    cls = "classical" if kappa[0] < t1 else ("frac_only" if kappa[0] < Ta else "unstable")
    assert cls == expected
    # direct spectral route agrees
    assert min_margin(B[None], 0.9, half_width=14)["margin"][0] > 0
    assert (min_margin(B[None], 1.0, half_width=14)["margin"][0] > 0) == (expected == "classical")


def test_interval_witness_m021():
    from mpmath import iv
    iv.dps = 40
    P = with_m(chief_witness(lambda v: iv.mpf(v)), iv.mpf("0.21"))
    X = prey_roots(P)[0]; Y, Z = yz_of_x(X, P)
    assert X.a > P.m.b and X.b < P.K.a and Y.a > 0 and Z.a > 0
    inv = invariants_of_matrix(reduced_matrix(X, Y, Z, P))
    beta = inv["beta"]; kappa = inv["kappa"]
    t1 = (iv.sqrt(beta[0]) + iv.sqrt(beta[1]) + iv.sqrt(beta[2])) ** 2
    assert (kappa - t1).a > mp.mpf("0.145")
    c = certify_threshold_logit([mp.nstr(mp.mpf(b.a), 35) for b in beta], "0.9", dps=40)
    assert c["certified"] and kappa.b < c["L"]                       # exact C-10 certificate (monotone in beta)


def test_direct_vs_c10_for_representative_perturbations():
    rng = np.random.default_rng(11)
    P0 = np.array(chief_witness().as_list())
    n_checked = 0
    while n_checked < 15:
        P = Params(*(P0 * np.exp(rng.normal(scale=0.15, size=14))))
        eqs = coexistence_equilibria(P)
        if not eqs:
            continue
        e = eqs[0]
        B = np.array(reduced_matrix(e["X"], e["Y"], e["Z"], P), float)
        p, mm, q, beta, kappa = invariants_batch(B[None])
        if not (mm.min() > 0 and q[0] > 0):
            continue
        Ta = threshold(beta[0], 0.9).T[0]; t1 = T1(beta[0])
        ma = min_margin(B[None], 0.9, half_width=14)["margin"][0]; m1 = min_margin(B[None], 1.0, half_width=14)["margin"][0]
        assert (ma > 0) == (kappa[0] < Ta) and (m1 > 0) == (kappa[0] < t1)
        n_checked += 1


def test_2d_critical_allee_threshold():
    rng = np.random.default_rng(5)
    for _ in range(10):
        X = rng.uniform(0.5, 2); a = np.exp(rng.normal()); K = X + np.exp(rng.normal())
        mc = (X ** 2 + 2 * a * X - K * a) / (K + a)
        assert abs(1 / (K - X) - 1 / (X - mc) + 1 / (X + a)) < 1e-10


def test_e1e3_gt_e2_is_sufficient_not_necessary_for_strict_P():
    """Matrix-level counterexample to necessity (DA-04): e2 > e1 e3 with -B strict P."""
    s, c1, c2, q1, q2, h, e1, e2, e3 = [Fr(1)] * 6 + [Fr(1, 2), Fr(1, 2), Fr(1, 2)]
    assert e2 > e1 * e3
    inv = invariants_of_matrix([[-s, -q1, -q2], [e1 * q1, -c1, -h], [e2 * q2, e3 * h, -c2]])
    assert min(inv["m"]) > 0 and inv["q"] == Fr(9, 4) > 0
    # and the sharp condition: q > 0 iff h q1 q2 (e2 - e1 e3) < s(c1c2+e3h^2) + c1 e2 q2^2 + c2 e1 q1^2
    assert h * q1 * q2 * (e2 - e1 * e3) < s * (c1 * c2 + e3 * h ** 2) + c1 * e2 * q2 ** 2 + c2 * e1 * q1 ** 2


def test_meanvalue_full_parameter_box_small_delta():
    """Rigorous first-order interval enclosure over a 14-parameter box around the m=0.21 witness."""
    import importlib, os, sys
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "computations", "scripts"))
    mv = importlib.import_module("double_allee_box_meanvalue")
    center = mv.with_m(mv.chief_witness(lambda v: mp.mpf(v)), mp.mpf("0.21")).as_list()
    res = mv.certify_box(center, [mp.mpf("1e-4")] * 14, {})
    assert res["ok"], res.get("fail")
    assert all(res["checks"].values())
