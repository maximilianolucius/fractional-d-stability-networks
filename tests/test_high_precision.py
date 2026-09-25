"""Deterministic high-precision (mpmath, >= 80 digits) checks of C-07..C-14.

NUMERICAL CORROBORATION ONLY.  None of these tests proves a theorem; they
check the algebra/formulas of the analytic proofs at 80+ decimal digits on
fixed, reproducible inputs.
"""
import itertools

import mpmath as mp
import numpy as np
import pytest

from fdsn.c10_threshold import (
    matrix_from_invariants,
    mp_h_alpha,
    mp_rate_constant,
    mp_siami_R3,
    mp_T1,
    mp_uk,
    threshold_mp,
)
from fdsn.direct_margin import mp_margin

DPS = 90
TIGHT = mp.mpf(10) ** -75


@pytest.fixture(autouse=True)
def _prec():
    with mp.workdps(DPS):
        yield


def mpmat(rows):
    return mp.matrix([[mp.mpf(v) for v in r] for r in rows])


def margin_of(M, alpha):
    ev = mp.eig(M, left=False, right=False)
    return min(abs(mp.arg(e)) for e in ev) - mp.mpf(alpha) * mp.pi / 2


def scaled(d, A):
    n = A.rows
    return mp.matrix([[d[i] * A[i, j] for j in range(n)] for i in range(n)])


# ---------------------------------------------------------------- C-07 (2x2)

@pytest.mark.parametrize("alpha", ["0.3", "0.9", "0.9999"])
def test_c07_zero_diagonal_class_is_fractional_not_hurwitz(alpha):
    A = mpmat([[0, 2], [-3, 0]])            # bc < 0, a = d = 0
    for d in [(1, 1), (mp.mpf(10) ** 30, 1), (1, mp.mpf(10) ** -30), ("0.37", "5.1")]:
        M = scaled([mp.mpf(v) for v in d], A)
        ev = mp.eig(M, left=False, right=False)
        # purely imaginary spectrum: |arg| = pi/2 exactly (up to 1e-75)
        assert all(abs(abs(mp.arg(e)) - mp.pi / 2) < TIGHT for e in ev)
        assert margin_of(M, alpha) > 0
        assert max(mp.re(e) for e in ev) > -TIGHT     # not Hurwitz


@pytest.mark.parametrize("alpha", ["0.5", "0.95"])
def test_c07_boundary_positive_diagonal_entry_is_excluded(alpha):
    eps = mp.mpf(10) ** -40
    A = mpmat([[eps, 1], [-1, -1]])          # det = 1 - eps > 0 but a > 0
    # witness: shrink the second row far below eps^2 so trace^2 > 4 det:
    # both eigenvalues are then real and positive (~eps and ~d2/eps)
    M = scaled([mp.mpf(1), mp.mpf(10) ** -100], A)
    assert margin_of(M, alpha) < 0


@pytest.mark.parametrize("alpha", ["0.5", "0.95"])
def test_c07_boundary_det_zero_gives_zero_eigenvalue(alpha):
    A = mpmat([[-1, 2], [1, -2]])            # det = 0
    ev = mp.eig(A, left=False, right=False)
    assert min(abs(e) for e in ev) < TIGHT


def test_c07_negative_diagonal_positive_det_is_in_F_on_sampled_orbit():
    A = mpmat([[-1, 5], [-3, "-0.01"]])
    for e in range(-20, 21, 4):
        M = scaled([mp.mpf(10) ** e, mp.mpf(1)], A)
        assert margin_of(M, "0.999") > 0     # Hurwitz 2x2 => |arg| > pi/2


# ---------------------------------------------------------------- C-09 witness

def a_gamma(g):
    g = mp.mpf(g)
    return mp.matrix([[-1, 0, -g], [g, -1, 0], [0, g, -1]])


@pytest.mark.parametrize("k", [2, 4, 8, 16, 30])
def test_c09_witness_family_as_alpha_to_one(k):
    alpha = 1 - mp.mpf(10) ** -k
    theta = alpha * mp.pi / 2
    rho = (1 - 2 * mp.cos(theta)) ** 2
    gphi = (9 / rho - 1) ** (mp.mpf(1) / 3)
    R3 = mp_siami_R3(alpha)
    assert 2 < gphi < R3                       # strict gap theorem (C-10 sec. 8)
    g = (2 + gphi) / 2
    A = a_gamma(g)
    L = 9 / (1 + g ** 3)                       # L(A_gamma) = Phi(A_gamma)
    assert L > rho
    ev = mp.eig(A, left=False, right=False)
    assert max(mp.re(e) for e in ev) > 0       # not Hurwitz at D = I
    assert margin_of(A, alpha) > 0
    # the interval (2, gamma_Phi) shrinks linearly: gamma_Phi - 2 ~ c (1-alpha)
    eps = 1 - alpha
    slope = (gphi - 2) / eps
    # rho ~ 1 - 2 pi eps  =>  gphi ~ (8 + 18 pi eps)^{1/3} ~ 2 + (3/2) pi eps
    assert abs(slope - 3 * mp.pi / 2) < 100 * eps


# ------------------------------------------------------ C-10 fixed cubic boundary

def H_theta(a, b, alpha):
    u, K = mp_uk(alpha)
    r = (u * a + mp.sqrt(u * u * a * a + K * b)) / K
    return r * r * (a + 2 * u * r)


@pytest.mark.parametrize("alpha", ["0.667", "0.7", "0.8", "0.9", "0.99", "0.999999"])
@pytest.mark.parametrize("ab", [("1", "1"), ("0.01", "3"), ("7", "0.002"), ("1e5", "1e-4")])
def test_c10_fixed_cubic_boundary_is_exact(alpha, ab):
    a, b = (mp.mpf(v) for v in ab)
    c = H_theta(a, b, alpha)
    theta = mp.mpf(alpha) * mp.pi / 2
    roots = mp.polyroots([1, a, b, c], maxsteps=400, extraprec=400)
    ang = min(abs(mp.arg(z)) for z in roots)
    assert abs(ang - theta) < TIGHT
    for sgn, expect in ((-1, 1), (1, -1)):
        cc = c * (1 + sgn * mp.mpf(10) ** -30)
        roots = mp.polyroots([1, a, b, cc], maxsteps=400, extraprec=400)
        m = min(abs(mp.arg(z)) for z in roots) - theta
        assert m * expect > 0


def test_c10_homogeneity_of_H():
    for s in ("0.001", "3", "1e7"):
        s = mp.mpf(s)
        a, b = mp.mpf("0.7"), mp.mpf("2.3")
        assert abs(H_theta(s * a, s * s * b, "0.83") / (s ** 3 * H_theta(a, b, "0.83")) - 1) < TIGHT


# ------------------------------------------------------ C-10 simplex normalization

def charpoly3(M):
    """Coefficients (a, b, c) of det(lambda I - M) = l^3 + a l^2 + b l + c from eigenvalues."""
    ev = mp.eig(M, left=False, right=False)
    a = -(ev[0] + ev[1] + ev[2])
    b = ev[0] * ev[1] + ev[0] * ev[2] + ev[1] * ev[2]
    c = -(ev[0] * ev[1] * ev[2])
    return mp.re(a), mp.re(b), mp.re(c)


@pytest.mark.parametrize("seed", range(6))
def test_c10_simplex_normalization(seed):
    rng = np.random.default_rng(seed)
    beta = np.exp(rng.normal(size=3))
    kappa = float(np.sum(np.sqrt(beta)) ** 2 * rng.uniform(0.3, 1.8))
    A = None
    while A is None:
        A = matrix_from_invariants(beta, kappa, p=np.exp(rng.normal(size=3)), rng=rng,
                                   dtype=mp.mpf, branch=int(rng.integers(2)))
        if A is None:
            kappa *= 1.1
    p = [-A[i, i] for i in range(3)]
    bet = [mp.mpf(float(v)) for v in beta]
    kap = mp.mpf(float(kappa))
    for _ in range(3):
        d = [mp.exp(mp.mpf(float(v))) for v in rng.normal(scale=3, size=3)]
        a_D, b_D, c_D = charpoly3(scaled(d, A))
        s = sum(p[i] * d[i] for i in range(3))
        x = [p[i] * d[i] / s for i in range(3)]
        B = bet[0] * x[0] * x[1] + bet[1] * x[0] * x[2] + bet[2] * x[1] * x[2]
        rel = mp.mpf(10) ** -60   # eigen-based coefficients lose some digits
        assert abs(a_D / s - 1) < rel
        assert abs(b_D / (s * s * B) - 1) < rel
        assert abs(c_D / (s ** 3 * kap * x[0] * x[1] * x[2]) - 1) < rel
        assert abs(sum(x) - 1) < TIGHT


# ------------------------------------------------------ C-11 exact Phi minimizer

@pytest.mark.parametrize("seed", range(5))
def test_c11_phi_minimizer_exact(seed):
    rng = np.random.default_rng(100 + seed)
    p = [mp.mpf(float(v)) for v in np.exp(rng.normal(size=3))]
    m = [mp.mpf(float(v)) for v in np.exp(rng.normal(size=3))]   # m12, m13, m23
    q = mp.mpf(float(np.exp(rng.normal())))

    def ratio(d):
        a = sum(p[i] * d[i] for i in range(3))
        b = m[0] * d[0] * d[1] + m[1] * d[0] * d[2] + m[2] * d[1] * d[2]
        return a * b / (q * d[0] * d[1] * d[2])

    Phi = (mp.sqrt(p[0] * m[2]) + mp.sqrt(p[1] * m[1]) + mp.sqrt(p[2] * m[0])) ** 2 / q
    dstar = [mp.sqrt(m[2] / p[0]), mp.sqrt(m[1] / p[1]), mp.sqrt(m[0] / p[2])]
    assert abs(ratio(dstar) / Phi - 1) < TIGHT
    # stationarity (gradient in log d vanishes) via high-precision differentiation
    for i in range(3):
        f = lambda t, i=i: ratio([dstar[j] * (mp.exp(t) if j == i else 1) for j in range(3)])
        assert abs(mp.diff(f, 0)) < mp.mpf(10) ** -60
    for _ in range(20):
        d = [dstar[i] * mp.exp(mp.mpf(float(rng.normal(scale=2)))) for i in range(3)]
        assert ratio(d) >= Phi * (1 - TIGHT)


# ------------------------------------------------------ C-12/C-13 invariance

@pytest.mark.parametrize("seed", range(6))
def test_c12_c13_left_diagonal_invariance_and_loop_identity(seed):
    rng = np.random.default_rng(200 + seed)
    A = mp.matrix([[mp.mpf(float(v)) for v in row] for row in rng.normal(size=(3, 3))])
    for i in range(3):
        A[i, i] = -abs(A[i, i]) - mp.mpf("0.1")

    def coords(M):
        p = [-M[i, i] for i in range(3)]
        g = {(i, j): M[i, j] * M[j, i] / (p[i] * p[j]) for i, j in ((0, 1), (0, 2), (1, 2))}
        beta = {k: 1 - v for k, v in g.items()}
        kappa = -mp.det(M) / (p[0] * p[1] * p[2])
        l123 = M[0, 1] * M[1, 2] * M[2, 0] / (p[0] * p[1] * p[2])
        l132 = M[0, 2] * M[2, 1] * M[1, 0] / (p[0] * p[1] * p[2])
        return beta, kappa, l123, l132

    b0, k0, l0, m0 = coords(A)
    assert abs(k0 - (sum(b0.values()) - 2 - (l0 + m0))) < TIGHT
    for _ in range(4):
        e = [mp.exp(mp.mpf(float(v))) for v in rng.normal(scale=4, size=3)]
        b1, k1, l1, m1 = coords(scaled(e, A))
        assert all(abs(b1[k] - b0[k]) < TIGHT * (1 + abs(b0[k])) for k in b0)
        assert abs(k1 - k0) < TIGHT * (1 + abs(k0))
        assert abs(l1 - l0) < TIGHT * (1 + abs(l0)) and abs(m1 - m0) < TIGHT * (1 + abs(m0))


# ------------------------------------------------------ C-10 symmetric slice / Siami

@pytest.mark.parametrize("alpha", ["0.67", "0.75", "0.9", "0.99", "0.99999"])
def test_c10_symmetric_threshold_equals_siami_and_center_formula(alpha):
    r = threshold_mp(["1", "1", "1"], alpha, dps=85)
    siami = 1 + mp_siami_R3(alpha) ** 3
    center = 27 * mp_h_alpha(mp.mpf(1) / 3, alpha)
    assert abs(r["T"] / siami - 1) < TIGHT
    assert abs(r["T"] / center - 1) < TIGHT
    assert all(abs(xi - mp.mpf(1) / 3) < mp.mpf(10) ** -70 for xi in r["x"])


# ------------------------------------------------------ C-14

BETAS = [("1", "1", "1"), ("0.2", "3", "1.5"), ("5", "0.01", "40"), ("0.5", "0.5", "2")]


@pytest.mark.parametrize("beta", BETAS)
def test_c14_monotone_in_alpha(beta):
    alphas = ["0.6667", "0.7", "0.8", "0.9", "0.99", "0.9999"]
    vals = [threshold_mp(beta, a, dps=82)["T"] for a in alphas]
    assert all(v1 > v2 for v1, v2 in zip(vals, vals[1:]))
    assert vals[-1] > mp_T1([mp.mpf(b) for b in beta])


@pytest.mark.parametrize("beta", BETAS)
def test_c14_first_order_rate(beta):
    bm = [mp.mpf(b) for b in beta]
    T1 = mp_T1(bm)
    C = mp_rate_constant(bm)
    errs = []
    for k in (4, 6, 8):
        eps = mp.mpf(10) ** -k
        r = threshold_mp(beta, 1 - eps, dps=85)
        errs.append(abs((r["T"] - T1) / eps - C))
    # residual is O(eps): each 100x decrease of eps reduces the error ~100x
    assert errs[1] < errs[0] / 50 and errs[2] < errs[1] / 50
    assert errs[2] / C < mp.mpf(10) ** -6


def test_c14_symmetric_constant_is_12_pi_sqrt3():
    assert abs(mp_rate_constant([1, 1, 1]) - 12 * mp.pi * mp.sqrt(3)) < TIGHT


# ------------------------------------------------------ C-10 low-order transition

@pytest.mark.parametrize("beta", BETAS)
def test_c10_blowup_at_two_thirds(beta):
    """T_alpha K^3 -> 27 as alpha -> 2/3+ (derived in the compute report)."""
    for k in (6, 10):
        alpha = mp.mpf(2) / 3 + mp.mpf(10) ** -k
        u, K = mp_uk(alpha)
        r = threshold_mp(beta, alpha, dps=85)
        assert abs(r["T"] * K ** 3 / 27 - 1) < mp.mpf(10) ** (-k + 2)


def test_exactness_list():
    # guard: every beta used above is strictly positive
    for b in itertools.chain.from_iterable(BETAS):
        assert mp.mpf(b) > 0
