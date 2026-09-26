"""Audit 2 (blind phase) — independent checks of the Double-Allee IGP theorem package.

Written from the model equations only (no import of src/fdsn/double_allee.py or any Audit-1
script).  Routes deliberately different from a symbolic re-derivation:
  * exact rational (Fraction) Schwartz-Zippel style identity tests at random rational points for
    every polynomial/rational identity (DA-01..DA-06, DA-09, DA-10, DA-12);
  * own numerical evaluation of the exact C-10 threshold T_alpha(beta) by direct minimisation on
    the simplex in barycentric coordinates (multi-start Nelder-Mead), cross-checked against the
    closed symmetric form 1 + R3(alpha)^3;
  * a NEW fractional-only witness (alpha = 0.8, beta = (1.5, 2.5, 2)) built from the DA-06/DA-07
    constructions, plus the Chief design (alpha = 0.9, m0 = 0.2, beta = (2,2,2), kappa = 18);
  * direct spectral checks with scale-invariant objectives (min |arg lambda(DB)| over log d);
  * time-domain corroboration: fractional Adams-Bashforth-Moulton (Diethelm PECE) simulation of the
    Caputo system D^alpha x = D x o F(x) at the worst diagonal (alpha = 0.9) and an RK45 simulation
    at alpha = 1 at the classical-instability diagonal;
  * 25,000 randomised joint parameter perturbations with theorem-vs-spectral comparison on a subset;
  * targeted degeneracy hunts: two admissible prey roots, r + K chi <= 0, feasibility loss along m.
Output: computations/audit2/DOUBLE_ALLEE_AUDIT2_RESULTS.json
"""
from __future__ import annotations

import json
import math
import os
import random
import sys
import time
from fractions import Fraction as Fr

import mpmath as mp
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import differential_evolution, minimize

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "DOUBLE_ALLEE_AUDIT2_RESULTS.json")
R = {}                                                       # results accumulator
random.seed(2)
rng = np.random.default_rng(20260926 + 2)


def log(*a):
    print(time.strftime("%H:%M:%S"), *a, file=sys.stderr, flush=True)


# ============================================================================ model (own implementation)
# parameters as a dict: a, K, r, m, q1, q2, h, e1, e2, e3, mu1, mu2, c1, c2
NAMES = ["a", "K", "r", "m", "q1", "q2", "h", "e1", "e2", "e3", "mu1", "mu2", "c1", "c2"]


def g(x, p):
    return p["r"] * (1 - x / p["K"]) * (x - p["m"]) / (x + p["a"])


def dg(x, p):
    """d/dx of g via the quotient rule on N(x) = r (1 - x/K)(x - m), D(x) = x + a."""
    r, K, m, a = p["r"], p["K"], p["m"], p["a"]
    N = r * (1 - x / K) * (x - m)
    dN = r * ((1 - x / K) - (x - m) / K)
    return (dN * (x + a) - N) / (x + a) ** 2


def F(x, y, z, p):
    """Per-capita growth rates of the IGP model."""
    return (g(x, p) - p["q1"] * y - p["q2"] * z,
            p["e1"] * p["q1"] * x - p["mu1"] - p["c1"] * y - p["h"] * z,
            p["e2"] * p["q2"] * x + p["e3"] * p["h"] * y - p["mu2"] - p["c2"] * z)


def DF(x, y, z, p):
    """Jacobian of F w.r.t. (x,y,z): only F_1 depends on x nonlinearly."""
    return [[dg(x, p), -p["q1"], -p["q2"]],
            [p["e1"] * p["q1"], -p["c1"], -p["h"]],
            [p["e2"] * p["q2"], p["e3"] * p["h"], -p["c2"]]]


def det3(M):
    return (M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1]) - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
            + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0]))


def c10_invariants(B):
    """Normalised principal-minor invariants exactly as defined in C-10 / C-13 (from the entries)."""
    p1, p2, p3 = -B[0][0], -B[1][1], -B[2][2]
    m12 = B[0][0] * B[1][1] - B[0][1] * B[1][0]
    m13 = B[0][0] * B[2][2] - B[0][2] * B[2][0]
    m23 = B[1][1] * B[2][2] - B[1][2] * B[2][1]
    q = -det3(B)
    P = p1 * p2 * p3
    L3 = (B[0][1] * B[1][2] * B[2][0] + B[0][2] * B[2][1] * B[1][0]) / P
    return dict(p=(p1, p2, p3), m=(m12, m13, m23), q=q, beta=(m12 / (p1 * p2), m13 / (p1 * p3), m23 / (p2 * p3)), kappa=q / P, L3=L3)


def sqrt_(v):
    return mp.sqrt(v) if isinstance(v, mp.mpf) else math.sqrt(v)


def T1(beta):
    return (sqrt_(beta[0]) + sqrt_(beta[1]) + sqrt_(beta[2])) ** 2


def solve_yz(x, p):
    """Cramer's rule on the two linear consumer equations at prey level x."""
    A1 = p["e1"] * p["q1"] * x - p["mu1"]
    A2 = p["e2"] * p["q2"] * x - p["mu2"]
    a11, a12, a21, a22 = p["c1"], p["h"], -p["e3"] * p["h"], p["c2"]
    det = a11 * a22 - a12 * a21
    return (A1 * a22 - a12 * A2) / det, (a11 * A2 - a21 * A1) / det


def prey_equation_roots(p):
    """Roots of x -> g(x) - q1 Y(x) - q2 Z(x) = 0 obtained by clearing (x+a): a quadratic; also the
    linear function chi, nu are recovered NUMERICALLY (two-point fit), not from the claimed formula."""
    L0 = p["q1"] * solve_yz(0, p)[0] + p["q2"] * solve_yz(0, p)[1]
    L1 = p["q1"] * solve_yz(1, p)[0] + p["q2"] * solve_yz(1, p)[1]
    chi, nu = L1 - L0, -L0
    r, K, m, a = p["r"], p["K"], p["m"], p["a"]
    # r(1 - x/K)(x - m) = (chi x - nu)(x + a)
    A = chi + r / K
    Bc = chi * a - nu - r * (1 + m / K)
    C = -nu * a + r * m
    return A, Bc, C, chi, nu


def coexistence(p):
    A, Bc, C, chi, nu = prey_equation_roots(p)
    disc = Bc * Bc - 4 * A * C
    out = []
    if disc < 0:
        return out
    for sgn in (1, -1):
        x = (-Bc + sgn * math.sqrt(disc)) / (2 * A)
        if p["m"] < x < p["K"]:
            y, z = solve_yz(x, p)
            if y > 0 and z > 0:
                out.append((x, y, z))
    return out


# ============================================================================ exact identity tests (Fraction)

def rfrac(lo=1, hi=60):
    return Fr(random.randint(lo, hi), random.randint(lo, hi))


def exact_identity_tests(n=400):
    fails = {}
    for _ in range(n):
        s, q1, q2, h, e1, e2, e3, c1, c2 = [rfrac() for _ in range(9)]
        B = [[-s, -q1, -q2], [e1 * q1, -c1, -h], [e2 * q2, e3 * h, -c2]]
        I = c10_invariants(B)
        chk = {
            "DA-03 m12": I["m"][0] == s * c1 + e1 * q1 ** 2,
            "DA-03 m13": I["m"][1] == s * c2 + e2 * q2 ** 2,
            "DA-03 m23": I["m"][2] == c1 * c2 + e3 * h ** 2,
            "DA-03 q": I["q"] == s * (c1 * c2 + e3 * h ** 2) + c1 * e2 * q2 ** 2 + c2 * e1 * q1 ** 2 + h * q1 * q2 * (e1 * e3 - e2),
            "DA-03 beta": I["beta"] == (1 + e1 * q1 ** 2 / (s * c1), 1 + e2 * q2 ** 2 / (s * c2), 1 + e3 * h ** 2 / (c1 * c2)),
            "DA-03 L3": I["L3"] == h * q1 * q2 * (e2 - e1 * e3) / (s * c1 * c2),
            "DA-03 kappa=sum beta-2-L3": I["kappa"] == sum(I["beta"]) - 2 - I["L3"],
        }
        # DA-01: left scaling invariance on a random dense matrix
        E = [rfrac() for _ in range(3)]
        M = [[rfrac() * random.choice([-1, 1]) for _ in range(3)] for _ in range(3)]
        for i in range(3):
            M[i][i] = -abs(M[i][i])
        EM = [[E[i] * M[i][j] for j in range(3)] for i in range(3)]
        I1, I2 = c10_invariants(M), c10_invariants(EM)
        chk["DA-01 invariants(EM)=invariants(M)"] = (I1["beta"], I1["kappa"], I1["L3"]) == (I2["beta"], I2["kappa"], I2["L3"])
        # DA-02 two-consumer
        c11, c12, c21, c22 = [rfrac() for _ in range(4)]
        B2 = [[-s, -q1, -q2], [e1 * q1, -c11, -c12], [e2 * q2, -c21, -c22]]
        J2 = c10_invariants(B2)
        chk["DA-02 L3 = q1q2(c12e2+c21e1)/(s c11 c22)"] = J2["L3"] == q1 * q2 * (c12 * e2 + c21 * e1) / (s * c11 * c22)
        chk["DA-02 L3>0"] = J2["L3"] > 0
        chk["DA-02 kappa=sum beta-2-L3"] = J2["kappa"] == sum(J2["beta"]) - 2 - J2["L3"]
        chk["DA-02 kappa < sum beta - 2 <= ... T1 (float)"] = float(J2["kappa"]) < float(sum(J2["beta"])) - 2 and (
            float(sum(J2["beta"])) - 2 < float(T1([float(b) for b in J2["beta"]])) if min(J2["beta"]) > 0 else True)
        # DA-05: Y(X), Z(X) satisfy the two consumer equations exactly; affine identity exact
        X = rfrac(); mu1, mu2 = rfrac(), rfrac()
        pp = dict(a=rfrac(), K=rfrac(), r=rfrac(), m=rfrac(), q1=q1, q2=q2, h=h, e1=e1, e2=e2, e3=e3, mu1=mu1, mu2=mu2, c1=c1, c2=c2)
        Y, Z = solve_yz(X, pp)
        chk["DA-05 consumer eqs at (X,Y(X),Z(X))"] = (e1 * q1 * X - mu1 - c1 * Y - h * Z == 0) and (e2 * q2 * X + e3 * h * Y - mu2 - c2 * Z == 0)
        Delta = c1 * c2 + e3 * h ** 2
        chi_c = (e1 * c2 * q1 ** 2 + e2 * c1 * q2 ** 2 + h * q1 * q2 * (e1 * e3 - e2)) / Delta
        nu_c = (mu1 * (q1 * c2 + q2 * e3 * h) + mu2 * (q2 * c1 - q1 * h)) / Delta
        chk["DA-05 q1Y+q2Z = chi X - nu (claimed chi, nu)"] = q1 * Y + q2 * Z == chi_c * X - nu_c
        chk["DA-05 Y(X),Z(X) claimed closed forms"] = (Y == (c2 * (e1 * q1 * X - mu1) - h * (e2 * q2 * X - mu2)) / Delta) and (
            Z == (e3 * h * (e1 * q1 * X - mu1) + c1 * (e2 * q2 * X - mu2)) / Delta)
        A_, B_, C_ = pp["r"] + pp["K"] * chi_c, pp["r"] * (pp["K"] + pp["m"]) - pp["K"] * chi_c * pp["a"] + pp["K"] * nu_c, pp["r"] * pp["K"] * pp["m"] - pp["K"] * nu_c * pp["a"]
        # the claimed quadratic must vanish at every root of the prey equation: test the identity
        # K (X+a) [g(X) - (chi X - nu)] == -(A X^2 - B X + C) as rational functions (random X)
        lhs = pp["K"] * (X + pp["a"]) * (g(X, pp) - (chi_c * X - nu_c))
        chk["DA-05 quadratic identity"] = lhs == -(A_ * X ** 2 - B_ * X + C_)
        # DA-06 residual (needs sqrt: use squares) — test tau-1/tau = rho with rational tau
        tau = 1 + rfrac(); rho = tau - 1 / tau
        chk["DA-06 tau=(rho+sqrt(rho^2+4))/2 <=> tau^2 - rho tau - 1 = 0"] = tau * tau - rho * tau - 1 == 0
        # DA-06: with e1=e3=eta, e2=eta^2/tau^2 and q1,q2,h squared-defined, residual^2 == R^2 (all rational)
        eta = rfrac(1, 9) / 10; Aq, Bq, Cq = rfrac(), rfrac(), rfrac()
        e1r, e3r, e2r = eta, eta, eta * eta / (tau * tau)
        q1s, q2s, hs = Aq * s * c1 / e1r, Bq * s * c2 / e2r, Cq * c1 * c2 / e3r         # squares of q1, q2, h
        resid_sq = hs * q1s * q2s * (e1r * e3r - e2r) ** 2 / (s * c1 * c2) ** 2
        R_sq = (rho * rho) * (Aq * Bq * Cq)                                             # R = rho sqrt(A B C)
        chk["DA-06 residual^2 == R^2 (exact)"] = resid_sq == R_sq
        chk["DA-06 beta targets exact"] = (e1r * q1s / (s * c1), e2r * q2s / (s * c2), e3r * hs / (c1 * c2)) == (Aq, Bq, Cq)
        # DA-09/DA-07: g'(x) = g(x) [-1/(K-x) + 1/(x-m) - 1/(x+a)] exact
        xx = pp["m"] + rfrac(); pp["K"] = xx + rfrac()
        chk["DA-07 g' = g[-1/(K-x)+1/(x-m)-1/(x+a)]"] = dg(xx, pp) == g(xx, pp) * (-1 / (pp["K"] - xx) + 1 / (xx - pp["m"]) - 1 / (xx + pp["a"]))
        # DA-12 m_c
        Xc, ac = rfrac(), rfrac(); Kc = Xc + rfrac()
        mc = (Xc * Xc + 2 * ac * Xc - Kc * ac) / (Kc + ac)
        chk["DA-12 H_A(m_c)=0 and m_c = X-(K-X)(X+a)/(K+a)"] = (1 / (Kc - Xc) - 1 / (Xc - mc) + 1 / (Xc + ac) == 0) and (mc == Xc - (Kc - Xc) * (Xc + ac) / (Kc + ac))
        for k, v in chk.items():
            if not v:
                fails[k] = fails.get(k, 0) + 1
    R["exact_identity_tests"] = {"n_random_rational_points": n, "checks_per_point": 20, "failures": fails}
    log("exact identities failures:", fails)


# ============================================================================ own T_alpha evaluator

def h_alpha(b, alpha):
    u = math.cos(alpha * math.pi / 2); Kt = 1 - 4 * u * u
    rr = (u + math.sqrt(u * u + Kt * b)) / Kt
    return rr * rr * (1 + 2 * u * rr)


def T_alpha(beta, alpha, starts=6):
    """min over the open simplex of h_alpha(B(x))/(x1 x2 x3), barycentric parametrisation (own code)."""
    def f(v):
        x1, x2 = v
        x3 = 1 - x1 - x2
        if x1 <= 1e-9 or x2 <= 1e-9 or x3 <= 1e-9:
            return 1e300
        Bx = beta[0] * x1 * x2 + beta[1] * x1 * x3 + beta[2] * x2 * x3
        return h_alpha(Bx, alpha) / (x1 * x2 * x3)
    best = None
    pts = [(1 / 3, 1 / 3)] + [tuple(rng.dirichlet([1, 1, 1])[:2]) for _ in range(starts - 1)]
    for s0 in pts:
        res = minimize(f, s0, method="Nelder-Mead", options={"xatol": 1e-13, "fatol": 1e-14, "maxfev": 20000})
        if best is None or res.fun < best.fun:
            best = res
    x1, x2 = best.x
    return best.fun, (x1, x2, 1 - x1 - x2)


def R3(alpha):
    t = alpha * math.pi / 2
    return math.sin(t) / math.sin(t - math.pi / 3)


def talpha_selfcheck():
    errs = []
    for al in (0.7, 0.8, 0.9, 0.99):
        for b in (0.3, 1.0, 4.0):
            T, x = T_alpha((b, b, b), al)
            errs.append(abs(T / (27 * h_alpha(b / 3, al)) - 1))
        errs.append(abs(T_alpha((1, 1, 1), al)[0] / (1 + R3(al) ** 3) - 1))
    R["T_alpha_selfcheck"] = {"max_rel_err_vs_closed_forms": max(errs), "note": "27 h(b/3) symmetric slice and Siami 1+R3^3"}
    log("T_alpha selfcheck", max(errs))


# ============================================================================ direct spectral checks (scale invariant)

def min_arg_over_D(B, alpha, hw=18.0, seeds=(1, 2, 3)):
    B = np.array(B, float)
    def f(w):
        d = np.exp([w[0], w[1], 0.0])
        ev = np.linalg.eigvals(np.diag(d) @ B)
        return float(np.min(np.abs(np.angle(ev))))
    best = None
    for sd in seeds:
        res = differential_evolution(f, [(-hw, hw)] * 2, seed=sd, tol=1e-13, maxiter=300, popsize=20, polish=True)
        if best is None or res.fun < best.fun:
            best = res
    # refine
    res = minimize(f, best.x, method="Nelder-Mead", options={"xatol": 1e-12, "fatol": 1e-15, "maxfev": 4000})
    if res.fun < best.fun:
        best = res
    return float(best.fun) - alpha * math.pi / 2, np.exp([best.x[0], best.x[1], 0.0])


def classify_direct(B, alpha):
    m_a, d_a = min_arg_over_D(B, alpha)
    m_1, d_1 = min_arg_over_D(B, 1.0)
    return {"margin_alpha": m_a, "d_alpha": d_a.tolist(), "margin_1": m_1, "d_1": d_1.tolist(),
            "class": "frac_only" if (m_a > 0 and m_1 < 0) else ("classical" if m_1 > 0 else "unstable")}


def classify_theorem(B, alpha):
    I = c10_invariants(B)
    if not (min(I["p"]) > 0 and min(I["m"]) > 0 and I["q"] > 0):
        return {"strictP": False}
    t1 = T1(I["beta"])
    Ta = T_alpha(I["beta"], alpha)[0] if alpha > 2 / 3 else math.inf
    return {"strictP": True, "kappa": I["kappa"], "T1": t1, "T_alpha": Ta,
            "class": "classical" if I["kappa"] < t1 else ("frac_only" if I["kappa"] < Ta else "unstable")}


# ============================================================================ constructions (DA-06 / DA-07)

def realize(beta, kappa, s, c1, c2, eta):
    A, B0, C = beta[0] - 1, beta[1] - 1, beta[2] - 1
    Rres = kappa - (sum(beta) - 2)
    rho = Rres / math.sqrt(A * B0 * C)
    tau = (rho + math.sqrt(rho * rho + 4)) / 2
    e1 = e3 = eta; e2 = eta * eta / tau ** 2
    return dict(q1=math.sqrt(A * s * c1 / e1), q2=math.sqrt(B0 * s * c2 / e2), h=math.sqrt(C * c1 * c2 / e3), e1=e1, e2=e2, e3=e3)


def embed(s, X, m, a, K, mat, c1, c2, xi):
    H = 1 / (K - X) - 1 / (X - m) + 1 / (X + a)
    Q = s / H
    Y, Z = xi * Q / mat["q1"], (1 - xi) * Q / mat["q2"]
    p = dict(a=a, K=K, m=m, c1=c1, c2=c2, **mat)
    p["mu1"] = mat["e1"] * mat["q1"] * X - c1 * Y - mat["h"] * Z
    p["mu2"] = mat["e2"] * mat["q2"] * X + mat["e3"] * mat["h"] * Y - c2 * Z
    p["r"] = Q * (X + a) / ((1 - X / K) * (X - m))
    return p, (X, Y, Z), Q, H


def build_witness(alpha, beta, frac, s, c1, c2, eta, X, m, a, K, xi):
    t1 = T1(beta); Ta = T_alpha(beta, alpha)[0]
    kappa = t1 + frac * (Ta - t1)
    mat = realize(beta, kappa, s, c1, c2, eta)
    p, eq, Q, H = embed(s, X, m, a, K, mat, c1, c2, xi)
    return p, eq, dict(kappa_target=kappa, T1=t1, T_alpha=Ta, Q=Q, H=H)


def witness_checks():
    out = {}
    # (i) NEW witness: alpha = 0.8, beta = (1.5, 2.5, 2), kappa at 40% of the band, X = 2, m = 0.5, a = 1, K = 2.3
    p, (X, Y, Z), info = build_witness(0.8, (1.5, 2.5, 2.0), 0.4, s=0.1, c1=0.2, c2=0.1, eta=0.6, X=2.0, m=0.5, a=1.0, K=2.3, xi=0.4)
    eqs = coexistence(p)
    B = DF(X, Y, Z, p)
    th = classify_theorem(B, 0.8); dr = classify_direct(B, 0.8)
    out["new_witness_alpha0.8"] = {"params": p, "equilibrium": (X, Y, Z), "all_feasible_equilibria_from_quadratic": eqs,
                                   "residuals": [abs(v) for v in F(X, Y, Z, p)], "s_target_0.1_vs_-g'": -dg(X, p),
                                   "info": info, "theorem": th, "direct": dr, "e_in_(0,1)": all(0 < p[k] < 1 for k in ("e1", "e2", "e3")),
                                   "e1e3_gt_e2": p["e1"] * p["e3"] > p["e2"], "all_params_positive": all(v > 0 for v in p.values()),
                                   "consistent": th["class"] == dr["class"] == "frac_only"}
    # (ii) Chief design: alpha=0.9, m0=0.2, beta=(2,2,2), kappa=18 (=T1) — own scale choices s=c=0.05, eta=0.5, X=1, a=0.5, K=1.1, xi=1/2
    mat = realize((2, 2, 2), 18.0, 0.05, 0.05, 0.05, 0.5)
    p0, (X0, Y0, Z0), Q0, H0 = embed(0.05, 1.0, 0.2, 0.5, 1.1, mat, 0.05, 0.05, 0.5)
    pts = {}
    for m in (0.19, 0.20, 0.21, 0.30, 0.45):
        pm = dict(p0); pm["m"] = m
        eqs = coexistence(pm)
        if not eqs:
            pts[str(m)] = "infeasible"; continue
        x, y, z = eqs[0]
        B = DF(x, y, z, pm)
        th = classify_theorem(B, 0.9); dr = classify_direct(B, 0.9)
        pts[str(m)] = {"n_eq": len(eqs), "X": x, "s": -dg(x, pm), "kappa": th["kappa"], "T1": th["T1"], "T_alpha": th["T_alpha"],
                       "theorem": th["class"], "direct": dr["class"], "direct_margin_alpha": dr["margin_alpha"], "direct_margin_1": dr["margin_1"]}
    out["chief_design_m_points"] = {"params_m0": p0, "points": pts}
    # HP check that m0=0.2 is exactly on the boundary (own mp arithmetic)
    with mp.workdps(60):
        s_, c_, eta_ = mp.mpf("0.05"), mp.mpf("0.05"), mp.mpf("0.5")
        A = mp.mpf(1); Rr = mp.mpf(14); rho = Rr; tau = (rho + mp.sqrt(rho * rho + 4)) / 2
        e1 = e3 = eta_; e2 = eta_ ** 2 / tau ** 2
        q1 = mp.sqrt(A * s_ * c_ / e1); q2 = mp.sqrt(A * s_ * c_ / e2); h = mp.sqrt(A * c_ * c_ / e3)
        Bm = [[-s_, -q1, -q2], [e1 * q1, -c_, -h], [e2 * q2, e3 * h, -c_]]
        I = c10_invariants(Bm)
        out["chief_design_hp"] = {"beta": [mp.nstr(b, 40) for b in I["beta"]], "kappa": mp.nstr(I["kappa"], 40), "kappa_minus_T1": mp.nstr(I["kappa"] - T1(I["beta"]), 10)}
    R["witnesses"] = out
    log("witness new consistent:", out["new_witness_alpha0.8"]["consistent"], "chief pts:", {k: (v["theorem"], v["direct"]) if isinstance(v, dict) else v for k, v in pts.items()})
    return p, (X, Y, Z), p0


# ============================================================================ time-domain corroboration

def caputo_pece(fun, x0, alpha, T, h):
    """Diethelm-Ford-Freed predictor-corrector for D^alpha x = fun(x), 0<alpha<=1 (own implementation)."""
    N = int(T / h)
    n = len(x0)
    x = np.zeros((N + 1, n)); f = np.zeros((N + 1, n))
    x[0] = x0; f[0] = fun(x0)
    ga = math.gamma(alpha + 2)
    k = np.arange(N + 2, dtype=float)
    b = (k + 1) ** alpha - k ** alpha                                    # predictor weights b_k
    a = np.empty(N + 2); a[0] = 0
    a[1:] = (k[1:] + 1) ** (alpha + 1) - 2 * k[1:] ** (alpha + 1) + (k[1:] - 1) ** (alpha + 1)   # corrector a_j (j>=1)
    for j in range(1, N + 1):
        # predictor: x0 + h^a/Gamma(a+1) sum_{i<j} b_{j-1-i} f_i
        idx = np.arange(j)
        pred = x0 + h ** alpha / math.gamma(alpha + 1) * (b[j - 1 - idx][:, None] * f[:j]).sum(0)
        # corrector: x0 + h^a/Gamma(a+2) [ f(pred) + ((j-1)^{a+1} - (j-1-a) j^a) f_0 + sum_{i=1}^{j-1} a_{j-i} f_i ]
        c0 = (j - 1) ** (alpha + 1) - (j - 1 - alpha) * j ** alpha
        ssum = c0 * f[0] + (a[j - idx[1:]][:, None] * f[1:j]).sum(0) if j > 1 else c0 * f[0]
        x[j] = x0 + h ** alpha / ga * (fun(pred) + ssum)
        f[j] = fun(x[j])
    return x


def simulations(p, eq, alpha=0.9):
    """Simulate D^alpha x = D x o F(x) near the equilibrium for the worst diagonal (alpha) and the classical witness (alpha=1)."""
    X, Y, Z = eq
    B = DF(X, Y, Z, p)
    dr = classify_direct(B, alpha)
    out = {}
    # min_i |arg lambda_i(D B)| does not depend on alpha, so the SAME orbit diagonal d* is the worst point for every
    # order: at d* the pair has |arg| = 1.333 rad, i.e. Re > 0 (classically unstable) but > 0.8 pi/2 (Matignon stable).
    # The state-space Jacobian of x' = D_sim x o F(x) is D_sim diag(x*) B, so D_sim = d* / x* realises D B.
    d_star = np.array(dr["d_alpha"])
    out["orbit_worst_d_star"] = d_star.tolist(); out["min_arg_at_d_star_rad"] = dr["margin_alpha"] + alpha * math.pi / 2
    for tag, d, al, T, h in (("alpha=%s_at_d_star" % alpha, d_star, alpha, 400.0, 0.02), ("alpha=1_at_d_star", d_star, 1.0, 3000.0, None)):
        d = np.array(d) / np.array([X, Y, Z]); d = d / np.prod(d) ** (1 / 3)
        def rhs(t, v=None):
            v = t if v is None else v
            x, y, z = v
            fx = F(x, y, z, p)
            return np.array([d[0] * x * fx[0], d[1] * y * fx[1], d[2] * z * fx[2]])
        x0 = np.array([X, Y, Z]) * (1 + 1e-3 * np.array([1, -1, 1]))
        if al == 1.0:
            sol = solve_ivp(lambda t, v: rhs(v), (0, T), x0, rtol=1e-10, atol=1e-14, dense_output=False, max_step=0.5)
            dev = np.abs(sol.y.T / np.array([X, Y, Z]) - 1)
            # linear prediction: growth rate = max Re lambda(D_sim diag(x*) B)
            Jm = np.diag(d) @ np.diag([X, Y, Z]) @ np.array(B)
            out[tag + "_max_Re_eig_state_jacobian"] = float(np.linalg.eigvals(Jm).real.max())
            out[tag] = {"d": d.tolist(), "initial_rel_dev": 1e-3, "final_rel_dev": float(dev[-1].max()), "max_rel_dev": float(dev.max()),
                        "grows": bool(dev[-1].max() > 10 * dev[0].max()), "T": T, "t_at_max": float(sol.t[dev.max(axis=1).argmax()]),
                        "expected": "growth (Re lambda > 0 at this D) if the equilibrium is not Hurwitz D-stable"}
        else:
            xs = caputo_pece(rhs, x0, al, T, h)
            dev = np.abs(xs / np.array([X, Y, Z]) - 1)
            tail = dev[-len(dev) // 4:].max(axis=1); head = dev[len(dev) // 8: len(dev) // 4].max(axis=1)
            out[tag] = {"d": d.tolist(), "initial_rel_dev": 1e-3, "final_rel_dev": float(dev[-1].max()), "max_rel_dev": float(dev.max()),
                        "decays": bool(tail.max() < head.max() and dev[-1].max() < dev[0].max()), "T": T, "h": h, "steps": int(T / h),
                        "envelope_first_quarter": float(head.max()), "envelope_last_quarter": float(tail.max()),
                        "note": "Caputo decay is algebraic (t^-alpha), so a slow monotone envelope decrease is the expected signature",
                        "expected": "decay (Matignon margin > 0 at the worst D) if the equilibrium is in F_alpha"}
    # linearised Caputo dynamics at the same orbit point d*: |arg| = 1.333 rad lies between 0.8 pi/2 = 1.257 and
    # 0.9 pi/2 = 1.414, so the SAME Jacobian must give a bounded/decaying envelope at alpha = 0.8 and growth at alpha = 0.9.
    d = d_star / np.array([X, Y, Z]); d = d / np.prod(d) ** (1 / 3)
    Jm = np.diag(d) @ np.diag([X, Y, Z]) @ np.array(B)
    ev = np.linalg.eigvals(Jm)
    lin = {"eigenvalues": [complex(v).__repr__() for v in ev], "min_arg_rad": float(np.min(np.abs(np.angle(ev))))}
    v0 = np.real(np.linalg.eig(Jm)[1][:, np.argmin(np.abs(np.angle(ev)))]); v0 = v0 / np.linalg.norm(v0) * 1e-3
    for al in (0.8, 0.9):
        xs = caputo_pece(lambda v: Jm @ v, v0, al, 1500.0, 0.05)
        nrm = np.linalg.norm(xs, axis=1)
        q = len(nrm) // 4
        lin["alpha=%s" % al] = {"norm0": float(nrm[0]), "env_q1": float(nrm[q:2 * q].max()), "env_q4": float(nrm[3 * q:].max()), "final": float(nrm[-1]),
                                "expected": "bounded, decaying envelope" if al * math.pi / 2 < lin["min_arg_rad"] else "growth"}
    out["linearised_at_d_star"] = lin
    R["time_domain"] = out
    log("time domain:", {k: (v.get("decays"), v.get("grows"), v.get("final_rel_dev")) for k, v in out.items() if isinstance(v, dict)})


# ============================================================================ random falsification (own generator)

def random_perturbations(p0, n=25000, n_direct=600):
    base = np.array([p0[k] for k in NAMES])
    rows = []
    for i in range(n):
        sig = [0.03, 0.1, 0.25][i % 3]
        v = base * np.exp(rng.normal(scale=sig, size=14))
        if i % 5 == 4:
            v[3] = rng.uniform(0.12, 0.5)                             # m-heavy
        p = dict(zip(NAMES, v))
        eqs = coexistence(p)
        rec = {"sig": sig, "n_eq": len(eqs)}
        if eqs:
            x, y, z = eqs[0]
            B = DF(x, y, z, p)
            th = classify_theorem(B, 0.9)
            rec.update(th); rec["p"] = v.tolist(); rec["eq"] = (x, y, z)
        rows.append(rec)
    feas = [r for r in rows if r["n_eq"] > 0]
    sP = [r for r in feas if r.get("strictP")]
    summ = {"n": n, "feasible": len(feas), "two_admissible_roots": sum(r["n_eq"] == 2 for r in feas), "strictP": len(sP),
            "classes": {c: sum(r["class"] == c for r in sP) for c in ("classical", "frac_only", "unstable")},
            "feasible_not_strictP": len(feas) - len(sP)}
    # subset for direct comparison: nearest to either boundary + random
    def gap(r):
        return min(abs(r["kappa"] / r["T1"] - 1), abs(r["kappa"] / r["T_alpha"] - 1))
    sP.sort(key=gap)
    subset = sP[:n_direct // 2] + [sP[i] for i in rng.choice(len(sP), n_direct // 2, replace=False)]
    mism = []
    for r in subset:
        p = dict(zip(NAMES, r["p"])); x, y, z = r["eq"]
        dr = classify_direct(DF(x, y, z, p), 0.9)
        agree = dr["class"] == r["class"]
        if not agree:
            # tolerate genuinely near-zero margins (float): |margin| < 1e-9
            near = (abs(dr["margin_alpha"]) < 1e-9) or (abs(dr["margin_1"]) < 1e-9)
            if not near:
                mism.append({"p": r["p"], "theorem": r["class"], "direct": dr, "kappa": r["kappa"], "T1": r["T1"], "T_alpha": r["T_alpha"]})
    summ["direct_subset"] = {"n": len(subset), "mismatches": len(mism), "min_gap_in_subset": gap(subset[0]), "examples": mism[:5]}
    R["random_perturbations"] = summ
    log("random:", {k: v for k, v in summ.items() if k != "direct_subset"}, "mismatches", len(mism))


# ============================================================================ targeted attacks

def degeneracy_hunt(p0, n=20000):
    """Search for two admissible prey roots (two coexistence equilibria) and r + K chi <= 0."""
    base = np.array([p0[k] for k in NAMES])
    two = []; lead_nonpos = 0; feas = 0
    for _ in range(n):
        v = base * np.exp(rng.normal(scale=0.6, size=14)); v[7:10] = rng.uniform(0.02, 0.98, 3)
        p = dict(zip(NAMES, v))
        A, Bc, C, chi, nu = prey_equation_roots(p)
        if A <= 0:
            lead_nonpos += 1
        eqs = coexistence(p)
        feas += bool(eqs)
        if len(eqs) == 2:
            two.append({"p": v.tolist(), "equilibria": eqs})
    R["degeneracy_hunt"] = {"n": n, "feasible": feas, "two_coexistence_equilibria_found": len(two), "examples": two[:3],
                            "leading_coefficient_r+K*chi<=0": lead_nonpos}
    log("degeneracy:", len(two), lead_nonpos, feas)


def m_branch(p0, alpha=0.9):
    ms = np.linspace(0.01, 0.99, 981); rows = []
    for m in ms:
        p = dict(p0); p["m"] = m
        eqs = coexistence(p)
        if not eqs:
            rows.append((m, None)); continue
        x, y, z = eqs[0]; B = DF(x, y, z, p); I = c10_invariants(B)
        rows.append((m, dict(X=x, Y=y, Z=z, s=-dg(x, p), kappa=I["kappa"], T1=T1(I["beta"]), n_eq=len(eqs), H=1 / (p["K"] - x) - 1 / (x - m) + 1 / (x + p["a"]))))
    feas = [(m, r) for m, r in rows if r]
    s_ = [r["s"] for _, r in feas]; G1 = [r["kappa"] - r["T1"] for _, r in feas]
    cross = [feas[i][0] for i in range(len(feas) - 1) if G1[i] * G1[i + 1] < 0]
    last = feas[-1][1]
    R["m_branch"] = {"feasible_range": [feas[0][0], feas[-1][0]], "ds_dm_negative": all(np.diff(s_) < 0), "n_classical_crossings": len(cross),
                     "crossings_near": cross, "max_n_eq": max(r["n_eq"] for _, r in feas), "at_feasibility_loss": last,
                     "feasibility_loss_mechanism": "Z->0" if last["Z"] < last["Y"] and last["Z"] < 0.05 * last["X"] else "see values"}
    log("m-branch:", R["m_branch"]["feasible_range"], cross, R["m_branch"]["ds_dm_negative"])


def path_checks(n=3000):
    """DA-10: numeric root count of G1 for random (A0,B0,C0,E0) incl. the no-crossing regime; DA-06 rank via FD Jacobian."""
    bad = 0; nocross_bad = 0; bad_cases = []
    for _ in range(n):
        A0, B0, C0 = np.exp(rng.normal(size=3)); C0 += 1
        E0 = 2 * math.sqrt(A0 * B0) * (1 + rng.uniform(-0.5, 3))
        tt = np.logspace(-6, 14, 12000)
        G1 = E0 * tt - 2 - 2 * np.sqrt((1 + A0 * tt) * (1 + B0 * tt)) - 2 * math.sqrt(C0) * (np.sqrt(1 + A0 * tt) + np.sqrt(1 + B0 * tt))
        nroots = int(np.sum(np.diff(np.sign(G1)) != 0))
        if E0 > 2 * math.sqrt(A0 * B0):
            if nroots != 1:
                bad += 1; bad_cases.append({"A0": A0, "B0": B0, "C0": C0, "E0": E0, "E0-2sqrt(A0B0)": E0 - 2 * math.sqrt(A0 * B0), "nroots_on_grid": nroots})
        else:
            if nroots != 0 or G1.max() >= 0:
                nocross_bad += 1
    # rank of (beta12,beta13,beta23,kappa) wrt (q1,q2,h,e2): finite-difference Jacobian at random points
    ranks = []
    for _ in range(200):
        s, c1, c2, q1, q2, h, e1, e2, e3 = np.exp(rng.normal(size=9)); e1, e2, e3 = rng.uniform(0.05, 0.95, 3)
        def inv(v):
            q1_, q2_, h_, e2_ = v
            B = [[-s, -q1_, -q2_], [e1 * q1_, -c1, -h_], [e2_ * q2_, e3 * h_, -c2]]
            I = c10_invariants(B); return np.array([*I["beta"], I["kappa"]])
        v0 = np.array([q1, q2, h, e2]); J = np.zeros((4, 4))
        for j in range(4):
            e = np.zeros(4); e[j] = 1e-6 * v0[j]
            J[:, j] = (inv(v0 + e) - inv(v0 - e)) / (2 * e[j])
        ranks.append(int(np.linalg.matrix_rank(J, tol=1e-8 * np.abs(J).max())))
    R["path_and_rank"] = {"G1_root_count_violations_when_E0>2sqrt(A0B0)": bad, "violation_cases": bad_cases[:10], "no_crossing_regime_violations": nocross_bad, "n": n,
                          "rank_of_invariant_map_(q1,q2,h,e2)": {"min": min(ranks), "n": len(ranks)}}
    log("path/rank:", R["path_and_rank"])


def da07_quantified(n=2000):
    """K_max = X + (X-m)(X+a)/(m+a) makes H_A > 0 iff K < K_max; check positivity of mu's for K close to X."""
    viol = 0; mu_ok = 0
    for _ in range(n):
        X = rng.uniform(0.5, 3); m = rng.uniform(0.05, 0.9) * X; a = np.exp(rng.normal())
        Kmax = X + (X - m) * (X + a) / (m + a)
        for K in (X + 0.5 * (Kmax - X), X + 0.999 * (Kmax - X), X + 1.001 * (Kmax - X)):
            H = 1 / (K - X) - 1 / (X - m) + 1 / (X + a)
            if (H > 0) != (K < Kmax):
                viol += 1
        s = np.exp(rng.normal()); mat = dict(q1=np.exp(rng.normal()), q2=np.exp(rng.normal()), h=np.exp(rng.normal()), e1=rng.uniform(.1, .9), e2=rng.uniform(.1, .9), e3=rng.uniform(.1, .9))
        K = X + 1e-3 * (Kmax - X)
        p, eq, Q, H = embed(s, X, m, a, K, mat, np.exp(rng.normal()), np.exp(rng.normal()), rng.uniform(.1, .9))
        mu_ok += (p["mu1"] > 0 and p["mu2"] > 0 and p["r"] > 0 and abs(-dg(X, p) - s) < 1e-9 * s and abs(g(X, p) - Q) < 1e-12 * Q)
    R["da07_quantified"] = {"H_A>0 <=> K<K_max violations": viol, "n": n, "embeddings_with_K=X+1e-3(Kmax-X)_all_positive_and_exact": mu_ok}
    log("da07:", R["da07_quantified"])


def main():
    t0 = time.time()
    only = set(sys.argv[1:])
    if only:
        global R
        R = json.load(open(OUT)) if os.path.exists(OUT) else {}
        p_new, eq_new, p0 = witness_checks() if "sim" in only else (None, None, None)
        if "sim" in only:
            simulations(p_new, eq_new, alpha=0.8)
        if "path" in only:
            path_checks()
        json.dump(R, open(OUT, "w"), indent=1, default=lambda o: o.item() if isinstance(o, (np.floating, np.integer)) else (mp.nstr(o, 30) if isinstance(o, mp.mpf) else str(o)))
        return
    exact_identity_tests()
    talpha_selfcheck()
    p_new, eq_new, p0 = witness_checks()
    simulations(p_new, eq_new, alpha=0.8)
    random_perturbations(p0)
    degeneracy_hunt(p0)
    m_branch(p0)
    path_checks()
    da07_quantified()
    R["seconds"] = round(time.time() - t0, 1)
    R["note"] = "Audit 2 blind-phase checks; no Audit-1 code or results used"
    def conv(o):
        if isinstance(o, (np.floating, np.integer)):
            return o.item()
        if isinstance(o, np.ndarray):
            return o.tolist()
        if isinstance(o, Fr):
            return str(o)
        if isinstance(o, mp.mpf):
            return mp.nstr(o, 30)
        return str(o)
    json.dump(R, open(OUT, "w"), indent=1, default=conv)
    log("done", R["seconds"])


if __name__ == "__main__":
    main()


def addendum_schur_identity(n=500):
    """Post-unblinding addendum (exact): q = -det B = Delta (s + chi), i.e. the strict-P determinant
    condition is exactly s + chi > 0, and the scalar prey-equation derivative Phi_X = -(s + chi) = -q/Delta."""
    fails = 0
    for _ in range(n):
        s, q1, q2, h, e1, e2, e3, c1, c2 = [rfrac() for _ in range(9)]
        B = [[-s, -q1, -q2], [e1 * q1, -c1, -h], [e2 * q2, e3 * h, -c2]]
        Delta = c1 * c2 + e3 * h ** 2
        chi = (e1 * c2 * q1 ** 2 + e2 * c1 * q2 ** 2 + h * q1 * q2 * (e1 * e3 - e2)) / Delta
        fails += (-det3(B) != Delta * (s + chi))
    d = json.load(open(OUT))
    d["addendum_q_equals_Delta_times_(s+chi)"] = {"n_exact_points": n, "failures": fails}
    json.dump(d, open(OUT, "w"), indent=1)
    print("addendum failures:", fails)


if __name__ == "__main__" and "addendum" in sys.argv:
    addendum_schur_identity()
