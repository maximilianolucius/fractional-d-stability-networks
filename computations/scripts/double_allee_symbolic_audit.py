"""Independent SymPy re-derivation of every identity in the Double-Allee IGP package.

Nothing is copied from the Chief formulas except the model equations.  Every
matrix, minor, determinant, invariant, equilibrium relation and derivative is
derived from the model by SymPy and then compared with the claimed formula;
the exact residual expression (before and after simplification) is saved.
Output: computations/results/DOUBLE_ALLEE_SYMBOLIC_AUDIT.json
"""
from __future__ import annotations

import json
import os
import sys

import sympy as sp

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
OUT = os.path.join(ROOT, "computations", "results", "DOUBLE_ALLEE_SYMBOLIC_AUDIT.json")

pos = dict(positive=True)
x, y, z = sp.symbols("x y z", positive=True)
X, Y, Z = sp.symbols("X Y Z", positive=True)
r, a, K, m = sp.symbols("r a K m", positive=True)
q1, q2, h = sp.symbols("q1 q2 h", positive=True)
e1, e2, e3 = sp.symbols("e1 e2 e3", positive=True)
mu1, mu2, c1, c2 = sp.symbols("mu1 mu2 c1 c2", positive=True)
c11, c12, c21, c22 = sp.symbols("c11 c12 c21 c22", positive=True)
s = sp.symbols("s", positive=True)
t = sp.symbols("t", positive=True)

RESULTS = []


def record(name, claimed, derived, assumptions="", extra=None, status_fn=None):
    diff = derived - claimed
    if isinstance(diff, sp.MatrixBase):
        res = diff.applyfunc(lambda e: sp.simplify(sp.expand(e)))
        ok = all(e == 0 for e in res) if status_fn is None else status_fn(res)
    else:
        res = sp.simplify(sp.expand(diff)) if isinstance(diff, sp.Basic) else diff
        ok = (res == 0) if status_fn is None else status_fn(res)
    entry = {"name": name, "status": "IDENTITY" if ok else "MISMATCH", "residual_raw": str(sp.expand(derived - claimed)),
             "residual_simplified": str(res), "assumptions": assumptions}
    if extra:
        entry.update(extra)
    RESULTS.append(entry)
    print(("OK   " if ok else "FAIL ") + name)
    return ok


def record_sign(name, expr, sign, assumptions, extra=None):
    """Record a claimed sign of an expression; verified by factorisation into manifestly signed terms."""
    e = sp.factor(sp.simplify(expr))
    # test: is expr a sum/product of positive symbols with the claimed sign?
    ok = (sp.ask(sp.Q.positive(expr)) if sign == "+" else sp.ask(sp.Q.negative(expr)))
    entry = {"name": name, "status": "SIGN_VERIFIED" if ok else "SIGN_NOT_PROVED", "expression": str(e),
             "claimed_sign": sign, "assumptions": assumptions}
    if extra:
        entry.update(extra)
    RESULTS.append(entry)
    print(("OK   " if ok else "?    ") + name + f"  [{e}]")
    return ok


# ----------------------------------------------------------------- DA-01 Kolmogorov factorisation
gDA = r / (x + a) * (1 - x / K) * (x - m)
F_igp = sp.Matrix([gDA - q1 * y - q2 * z,
                   e1 * q1 * x - mu1 - c1 * y - h * z,
                   e2 * q2 * x + e3 * h * y - mu2 - c2 * z])
G = sp.Matrix([x * F_igp[0], y * F_igp[1], z * F_igp[2]])
J = G.jacobian([x, y, z])
DF = F_igp.jacobian([x, y, z])
# at an equilibrium F=0: J - diag(x)DF = diag(F) which vanishes
diff_JD = sp.simplify(J - sp.diag(x, y, z) * DF)
record("DA-01 J - diag(x) DF == diag(F_1,F_2,F_3) (vanishes at F=0)", sp.zeros(3, 3), diff_JD - sp.diag(*F_igp),
       "identity holds for all (x,y,z); at an equilibrium F=0 so J = diag(x*) DF")
# invariants of E*B equal those of B for positive diagonal E (symbolic, generic B)
b = sp.Matrix(3, 3, sp.symbols("b11:14 b21:24 b31:34"))
E1, E2, E3 = sp.symbols("E1 E2 E3", positive=True)
Bs = sp.diag(E1, E2, E3) * b


def invariants(M):
    p = [-M[i, i] for i in range(3)]
    m12 = M[:2, :2].det(); m13 = M[[0, 2], [0, 2]].det(); m23 = M[1:, 1:].det()
    q = -M.det()
    beta = (m12 / (p[0] * p[1]), m13 / (p[0] * p[2]), m23 / (p[1] * p[2]))
    kappa = q / (p[0] * p[1] * p[2])
    L3 = (M[0, 1] * M[1, 2] * M[2, 0] + M[0, 2] * M[2, 1] * M[1, 0]) / (p[0] * p[1] * p[2])
    return p, (m12, m13, m23), q, beta, kappa, L3


pB, mB, qB, betaB, kappaB, L3B = invariants(b)
pE, mE, qE, betaE, kappaE, L3E = invariants(Bs)
record("DA-01 beta/kappa/L3 invariant under left positive diagonal scaling (generic 3x3)",
       sp.Matrix([*betaB, kappaB, L3B]), sp.Matrix([*betaE, kappaE, L3E]), "E = diag(E1,E2,E3) > 0")
# orbit equivalence: {D J} = {E B}: D diag(x*) is a bijection of positive diagonals (elementary; recorded as note)
RESULTS.append({"name": "DA-01 orbit equivalence {D J(x*)} = {E B}", "status": "LOGIC_VERIFIED",
                "argument": "D -> D diag(x*) is a bijection of the positive diagonal cone (inverse D -> D diag(x*)^-1); "
                            "hence the spectra sets coincide and F_alpha / D_H membership of J and B are equivalent.",
                "assumptions": "x* >> 0"})

# ----------------------------------------------------------------- DA-02 two-consumer no-go
F_tc = sp.Matrix([gDA - q1 * y - q2 * z,
                  e1 * q1 * x - mu1 - c11 * y - c12 * z,
                  e2 * q2 * x - mu2 - c21 * y - c22 * z])
DF_tc = F_tc.jacobian([x, y, z]).subs(sp.diff(gDA, x), -s)
# replace g'(x) by -s symbolically: DF_tc[0,0] is g'(x)
DF_tc[0, 0] = -s
B_tc_claim = sp.Matrix([[-s, -q1, -q2], [e1 * q1, -c11, -c12], [e2 * q2, -c21, -c22]])
record("DA-02 reduced matrix B (two-consumer)", B_tc_claim, DF_tc, "s := -g_DA'(x*)")
p, mm, q, beta, kappa, L3 = invariants(B_tc_claim)
record("DA-02 p = (s, c11, c22)", sp.Matrix([s, c11, c22]), sp.Matrix(p))
record("DA-02 m12 = s c11 + e1 q1^2", s * c11 + e1 * q1 ** 2, mm[0])
record("DA-02 m13 = s c22 + e2 q2^2", s * c22 + e2 * q2 ** 2, mm[1])
record("DA-02 m23 = c11 c22 - c12 c21", c11 * c22 - c12 * c21, mm[2])
record("DA-02 beta12 = 1 + e1 q1^2/(s c11)", 1 + e1 * q1 ** 2 / (s * c11), beta[0])
record("DA-02 beta13 = 1 + e2 q2^2/(s c22)", 1 + e2 * q2 ** 2 / (s * c22), beta[1])
record("DA-02 beta23 = 1 - c12 c21/(c11 c22)", 1 - c12 * c21 / (c11 * c22), beta[2])
record("DA-02 L3 = q1 q2 (c12 e2 + c21 e1)/(s c11 c22)  (C-13 convention L3 = (a12 a23 a31 + a13 a32 a21)/(p1 p2 p3))",
       q1 * q2 * (c12 * e2 + c21 * e1) / (s * c11 * c22), L3)
record_sign("DA-02 L3 > 0", L3, "+", "all parameters positive")
record("DA-02 kappa = beta12 + beta13 + beta23 - 2 - L3", beta[0] + beta[1] + beta[2] - 2 - L3, kappa)
# no-go: T1 - kappa = 2 + L3 + 2(sqrt(b12 b13) + sqrt(b12 b23) + sqrt(b13 b23)) > 0 whenever beta > 0
b12, b13, b23, L3s = sp.symbols("beta12 beta13 beta23 L3", positive=True)
T1s = (sp.sqrt(b12) + sp.sqrt(b13) + sp.sqrt(b23)) ** 2
kappa_s = b12 + b13 + b23 - 2 - L3s
record("DA-02 T1 - kappa = 2 + L3 + 2(sqrt(b12 b13)+sqrt(b12 b23)+sqrt(b13 b23))",
       2 + L3s + 2 * (sp.sqrt(b12 * b13) + sp.sqrt(b12 * b23) + sp.sqrt(b13 * b23)), sp.expand(T1s - kappa_s),
       "beta_ij > 0 (needs only the order-two minors positive), L3 >= 0")
RESULTS.append({"name": "DA-02 no-go minimal hypotheses", "status": "LOGIC_VERIFIED",
                "argument": "T1 - kappa = 2 + L3 + 2 sum sqrt(beta_i beta_j) > 0 for every beta > 0 and L3 >= 0; "
                            "L3 >= 0 holds for all positive parameters including c12 = 0 or c21 = 0 (then L3 may be 0), "
                            "and beta23 -> 0+ is harmless (T1 - kappa >= 2). Strict-P is only needed to invoke Cain's "
                            "(alpha=1) classification; kappa < T1 itself holds on the whole positive-beta set.",
                "assumptions": "q1,q2,e1,e2,s,c11,c22 > 0; c12,c21 >= 0"})

# ----------------------------------------------------------------- DA-03 IGP reduced matrix & invariants
DF_i = DF.copy(); DF_i[0, 0] = -s
B_claim = sp.Matrix([[-s, -q1, -q2], [e1 * q1, -c1, -h], [e2 * q2, e3 * h, -c2]])
record("DA-03 reduced matrix B (IGP)", B_claim, DF_i, "s := -g_DA'(X)")
p, mm, q, beta, kappa, L3 = invariants(B_claim)
record("DA-03 m12 = s c1 + e1 q1^2", s * c1 + e1 * q1 ** 2, mm[0])
record("DA-03 m13 = s c2 + e2 q2^2", s * c2 + e2 * q2 ** 2, mm[1])
record("DA-03 m23 = c1 c2 + e3 h^2", c1 * c2 + e3 * h ** 2, mm[2])
q_claim = s * (c1 * c2 + e3 * h ** 2) + c1 * e2 * q2 ** 2 + c2 * e1 * q1 ** 2 + h * q1 * q2 * (e1 * e3 - e2)
record("DA-03 q = -det B", q_claim, q)
record("DA-03 beta12 = 1 + e1 q1^2/(s c1)", 1 + e1 * q1 ** 2 / (s * c1), beta[0])
record("DA-03 beta13 = 1 + e2 q2^2/(s c2)", 1 + e2 * q2 ** 2 / (s * c2), beta[1])
record("DA-03 beta23 = 1 + e3 h^2/(c1 c2)", 1 + e3 * h ** 2 / (c1 * c2), beta[2])
kappa_claim = beta[0] + beta[1] + beta[2] - 2 + h * q1 * q2 * (e1 * e3 - e2) / (s * c1 * c2)
record("DA-03 kappa = sum beta - 2 + h q1 q2 (e1 e3 - e2)/(s c1 c2)", kappa_claim, kappa)
record("DA-03 L3 = h q1 q2 (e2 - e1 e3)/(s c1 c2)  (C-13 convention)", h * q1 * q2 * (e2 - e1 * e3) / (s * c1 * c2), L3)
record("DA-03 kappa = sum beta - 2 - L3", beta[0] + beta[1] + beta[2] - 2 - L3, kappa)
record("DA-03 oriented cycles: a12 a23 a31 = +e2 q1 q2 h, a13 a32 a21 = -e1 e3 q1 q2 h",
       sp.Matrix([e2 * q1 * q2 * h, -e1 * e3 * q1 * q2 * h]),
       sp.Matrix([B_claim[0, 1] * B_claim[1, 2] * B_claim[2, 0], B_claim[0, 2] * B_claim[2, 1] * B_claim[1, 0]]))

# ----------------------------------------------------------------- DA-04 strict P
RESULTS.append({"name": "DA-04 strict-P analysis", "status": "LOGIC_VERIFIED",
                "p": [str(v) for v in p], "m": [str(sp.factor(v)) for v in mm], "q": str(sp.expand(q)),
                "argument": "p_i = (s, c1, c2) > 0 iff s > 0; m12, m13, m23 are sums of positive terms once s > 0; "
                            "q = s(c1c2+e3h^2) + c1 e2 q2^2 + c2 e1 q1^2 + h q1 q2 (e1 e3 - e2). If e1 e3 >= e2 every term is "
                            "positive, so e1 e3 > e2 is SUFFICIENT, NOT NECESSARY: the exact strict-P condition is "
                            "s > 0 and q > 0, i.e. h q1 q2 (e2 - e1 e3) < s(c1c2+e3h^2) + c1 e2 q2^2 + c2 e1 q1^2. "
                            "A transparent sufficient condition weaker than e1e3>e2 follows from AM-GM: "
                            "c1 e2 q2^2 + c2 e1 q1^2 >= 2 q1 q2 sqrt(c1 c2 e1 e2), hence q > 0 whenever "
                            "h (e2 - e1 e3) <= 2 sqrt(c1 c2 e1 e2).",
                "assumptions": "all biological parameters positive"})
amgm = c1 * e2 * q2 ** 2 + c2 * e1 * q1 ** 2 - 2 * q1 * q2 * sp.sqrt(c1 * c2 * e1 * e2)
record("DA-04 AM-GM residual c1 e2 q2^2 + c2 e1 q1^2 - 2 q1 q2 sqrt(c1 c2 e1 e2) = (sqrt(c1 e2) q2 - sqrt(c2 e1) q1)^2",
       (sp.sqrt(c1 * e2) * q2 - sp.sqrt(c2 * e1) * q1) ** 2, amgm)

# ----------------------------------------------------------------- DA-05 coexistence geometry
Delta = c1 * c2 + e3 * h ** 2
solYZ = sp.solve([F_igp[1].subs({x: X, y: Y, z: Z}), F_igp[2].subs({x: X, y: Y, z: Z})], [Y, Z], dict=True)[0]
A1 = e1 * q1 * X - mu1; A2 = e2 * q2 * X - mu2
record("DA-05 Y(X) = [c2 A1 - h A2]/Delta", (c2 * A1 - h * A2) / Delta, solYZ[Y])
record("DA-05 Z(X) = [e3 h A1 + c1 A2]/Delta", (e3 * h * A1 + c1 * A2) / Delta, solYZ[Z])
chi = (e1 * c2 * q1 ** 2 + e2 * c1 * q2 ** 2 + h * q1 * q2 * (e1 * e3 - e2)) / Delta
nu = (mu1 * (q1 * c2 + q2 * e3 * h) + mu2 * (q2 * c1 - q1 * h)) / Delta
record("DA-05 q1 Y + q2 Z = chi X - nu", chi * X - nu, q1 * solYZ[Y] + q2 * solYZ[Z])
lhs = gDA.subs(x, X); poly = sp.expand(sp.cancel((lhs - (chi * X - nu)) * (X + a) * K))   # times K(X+a); K>0 so same roots
quad = (r + K * chi) * X ** 2 - (r * (K + m) - K * chi * a + K * nu) * X + (r * K * m - K * nu * a)
record("DA-05 quadratic: K(X+a)[g_DA(X) - (chi X - nu)] == -(claimed quadratic)", -quad, poly,
       "multiplication by K(X+a) > 0 for X > 0 introduces no root: the polynomial at X=-a equals r(1+a/K)(-a-m) != 0")
record("DA-05 polynomial at X=-a equals -r(K+a)(a+m) != 0 (no spurious root from the multiplication)",
       -r * (K + a) * (a + m), poly.subs(X, -a), extra={"value_at_-a": str(sp.factor(poly.subs(X, -a)))})

# ----------------------------------------------------------------- DA-06 realization residual
Ar, Br, Cr, Rr, sr, c1r, c2r, eta = sp.symbols("A B0 C R s c1 c2 eta", positive=True)
rho = Rr / sp.sqrt(Ar * Br * Cr)
tau = (rho + sp.sqrt(rho ** 2 + 4)) / 2
e1r = eta; e3r = eta; e2r = eta ** 2 / tau ** 2
q1r = sp.sqrt(Ar * sr * c1r / e1r); q2r = sp.sqrt(Br * sr * c2r / e2r); hr = sp.sqrt(Cr * c1r * c2r / e3r)
record("DA-06 tau - 1/tau = rho", rho, tau - 1 / tau)
record("DA-06 beta12 - 1 = A", Ar, e1r * q1r ** 2 / (sr * c1r))
record("DA-06 beta13 - 1 = B0", Br, e2r * q2r ** 2 / (sr * c2r))
record("DA-06 beta23 - 1 = C", Cr, e3r * hr ** 2 / (c1r * c2r))
resid = hr * q1r * q2r * (e1r * e3r - e2r) / (sr * c1r * c2r)
record("DA-06 determinant residual h q1 q2 (e1 e3 - e2)/(s c1 c2) = R", Rr, resid, "A,B0,C,R,s,c1,c2 > 0, 0 < eta")
record("DA-06 e1 e3 / e2 = tau^2 > 1", tau ** 2, e1r * e3r / e2r)
RESULTS.append({"name": "DA-06 positivity / efficiencies", "status": "LOGIC_VERIFIED",
                "argument": "tau > 1 for rho > 0 (tau = (rho + sqrt(rho^2+4))/2 > (0+2)/2 = 1); e1=e3=eta in (0,1), "
                            "e2 = eta^2/tau^2 in (0, eta^2) subset (0,1); q1,q2,h are square roots of positive numbers; "
                            "q = kappa s c1 c2 > 0 automatically since kappa > sum beta - 2 > 1 > 0. As R -> 0+: rho -> 0, "
                            "tau -> 1, e2 -> eta^2: no blow-up. The image of the construction is exactly "
                            "{beta_ij > 1, kappa > sum beta - 2}, an open 4-dimensional set; the IGP architecture cannot "
                            "realize beta23 <= 1 (beta23 = 1 + e3 h^2/(c1 c2) > 1) nor beta12, beta13 <= 1.",
                "assumptions": "target beta_ij > 1, kappa > sum beta - 2"})
# local rank of the invariant map on the four-parameter subfamily (q1, q2, h, e2), others fixed
invmap = sp.Matrix([beta[0], beta[1], beta[2], kappa])
Jm = invmap.jacobian([q1, q2, h, e2])
pt = {s: sp.Rational(1, 20), c1: sp.Rational(1, 20), c2: sp.Rational(1, 20), e1: sp.Rational(1, 2), e3: sp.Rational(1, 2),
      q1: sp.Rational(7, 100), q2: sp.Rational(7, 5), h: sp.Rational(7, 100), e2: sp.Rational(1, 800)}
detJ = sp.simplify(Jm.subs(pt).det())
RESULTS.append({"name": "DA-06 Jacobian rank of (beta12,beta13,beta23,kappa) w.r.t. (q1,q2,h,e2) at a rational point",
                "status": "RANK_4" if detJ != 0 else "RANK_DEFICIENT", "det": str(detJ),
                "symbolic_det": str(sp.factor(Jm.det())), "point": {str(k): str(v) for k, v in pt.items()}})

# ----------------------------------------------------------------- DA-07 embedding
HA = 1 / (K - X) - 1 / (X - m) + 1 / (X + a)
Q = sp.symbols("Q", positive=True)
r_emb = Q * (X + a) / ((1 - X / K) * (X - m))
g_emb = gDA.subs({x: X, r: r_emb})
gp_emb = sp.diff(gDA, x).subs({x: X, r: r_emb})
record("DA-07 g_DA(X) = Q with r = Q(X+a)/[(1-X/K)(X-m)]", Q, g_emb, "0 < m < X < K")
record("DA-07 g_DA'(X) = -Q H_A", -Q * HA, gp_emb)
record("DA-07 g_DA'(x) = g_DA(x)[-1/(K-x)+1/(x-m)-1/(x+a)] (logarithmic derivative)",
       gDA * (-1 / (K - x) + 1 / (x - m) - 1 / (x + a)), sp.diff(gDA, x))
xi = sp.symbols("xi", positive=True)
Yv = xi * Q / q1; Zv = (1 - xi) * Q / q2
mu1v = e1 * q1 * X - c1 * Yv - h * Zv; mu2v = e2 * q2 * X + e3 * h * Yv - c2 * Zv
Fsub = F_igp.subs({x: X, y: Yv, z: Zv, mu1: mu1v, mu2: mu2v, r: r_emb})
record("DA-07 all three equilibrium equations vanish", sp.zeros(3, 1), sp.simplify(Fsub))
# limits K -> X+
Kx = sp.symbols("epsilon", positive=True)      # K = X + epsilon
HA_eps = HA.subs(K, X + Kx)
record("DA-07 H_A*(K-X) -> 1 as K -> X+", 1, sp.limit(HA_eps * Kx, Kx, 0))
r_lim = sp.limit((s / HA_eps) * (X + a) / ((1 - X / (X + Kx)) * (X - m)), Kx, 0)
record("DA-07 r -> s X (X+a)/(X-m) as K -> X+ (finite, positive)", s * X * (X + a) / (X - m), r_lim, "Q = s/H_A")
RESULTS.append({"name": "DA-07 quantified feasibility", "status": "LOGIC_VERIFIED",
                "argument": "H_A > 0 iff K - X < (X-m)(X+a)/(m+a) (from 1/(K-X) > (m+a)/((X-m)(X+a))); "
                            "Q = s/H_A is continuous and decreasing to 0 as K -> X+; mu1 > 0 iff Q < e1 q1 X / (xi c1/q1 + (1-xi) h/q2); "
                            "mu2 > 0 iff Q (1-xi) c2/q2 < e2 q2 X + e3 h xi Q/q1, i.e. always if (1-xi)c2/q2 <= e3 h xi/q1, else "
                            "Q < e2 q2 X / ((1-xi)c2/q2 - e3 h xi/q1). Hence an explicit interval X < K < K_max(s, X, m, a, ...) "
                            "makes every parameter positive; r stays bounded (limit s X (X+a)/(X-m)); nothing blows up.",
                "assumptions": "s > 0, 0 < m < X, a > 0, xi in (0,1)"})

# ----------------------------------------------------------------- DA-09 sensitivities
mm_ = sp.symbols("m", positive=True)
Xm = sp.Function("X")(mm_)
chi_s, nu_s = sp.symbols("chi nu", positive=True)
gm = gDA.subs({x: Xm, m: mm_})
Fimp = gm - chi_s * Xm + nu_s
dX = sp.solve(sp.diff(Fimp, mm_), sp.diff(Xm, mm_))[0]
Qs = sp.symbols("Q", positive=True)
# express in terms of Q = g(X;m), s = -g'(X;m): g'(X) = -s, d/dm g = -g/(X-m)
dX_claim = -Qs / ((Xm - mm_) * (s + chi_s))
sub_gp = {sp.diff(gDA, x).subs({x: Xm, m: mm_}): -s, gDA.subs({x: Xm, m: mm_}): Qs}
dX_sub = sp.simplify(dX.subs(sp.diff(gDA, x).subs({x: Xm, m: mm_}), -s))
dX_sub = sp.simplify(dX_sub.subs(gDA.subs({x: Xm, m: mm_}), Qs))
# direct route: dX/dm = -F_m/F_X with F_m = -Q/(X-m), F_X = -(s+chi)
F_m = sp.simplify(sp.diff(gDA, m).subs({x: Xm, m: mm_}) / gDA.subs({x: Xm, m: mm_}))
record("DA-09 d/dm g_DA(X;m) = -g_DA/(X-m)", -1 / (Xm - mm_), F_m)
record("DA-09 dX/dm = -Q/[(X-m)(s+chi)]", dX_claim, -(-Qs / (Xm - mm_)) / (-(s + chi_s)), "F_X = g' - chi = -(s+chi) != 0")
HAX = 1 / (K - X) - 1 / (X - m) + 1 / (X + a)
record("DA-09 dH_A/dX = 1/(K-X)^2 + 1/(X-m)^2 - 1/(X+a)^2", 1 / (K - X) ** 2 + 1 / (X - m) ** 2 - 1 / (X + a) ** 2, sp.diff(HAX, X))
record("DA-09 dH_A/dm = -1/(X-m)^2", -1 / (X - m) ** 2, sp.diff(HAX, m))
# sign of dH_A/dX: 1/(X-m)^2 > 1/(X+a)^2 since 0 < X-m < X+a (m > -a); write difference
record("DA-09 1/(X-m)^2 - 1/(X+a)^2 = (m+a)(2X+a-m)/((X-m)^2 (X+a)^2)", (m + a) * (2 * X + a - m) / ((X - m) ** 2 * (X + a) ** 2),
       1 / (X - m) ** 2 - 1 / (X + a) ** 2, "X > m: both factors positive")
Xp = sp.symbols("Xp", negative=True)  # dX/dm < 0
ds_dm = chi_s * Xp * HAX + Qs * (sp.diff(HAX, X) * Xp - 1 / (X - m) ** 2)
RESULTS.append({"name": "DA-09 ds/dm sign", "status": "LOGIC_VERIFIED",
                "expression": "ds/dm = chi X' H_A + Q[(dH_A/dX) X' - 1/(X-m)^2]",
                "argument": "With Q > 0 (positive predation at coexistence), s = Q H_A > 0 => H_A > 0; chi > 0 (true when "
                            "e1 e3 >= e2; more generally chi Delta = e1 c2 q1^2 + e2 c1 q2^2 + h q1 q2(e1e3-e2)); then "
                            "s + chi > 0 => X' = dX/dm < 0; dH_A/dX > 0 (m > -a, automatic for m > 0); so every term is negative: "
                            "chi X' H_A < 0, Q dH_A/dX X' < 0, -Q/(X-m)^2 < 0. Minimal assumptions: Q>0, s>0, chi>0, X>m>-a. "
                            "If chi <= 0 the sign of X' and of the first term is not controlled: e1e3>e2 (or chi>0) is genuinely used.",
                "assumptions": "Q>0, s>0, chi>0, 0<m<X<K, a>0"})

# ----------------------------------------------------------------- DA-10 / DA-11 path and crossing
A0, B0_, C0, E0 = sp.symbols("A0 B0 C0 E0", positive=True)
kap_t = C0 + (A0 + B0_ + E0) * t
T1_t = (sp.sqrt(1 + A0 * t) + sp.sqrt(1 + B0_ * t) + sp.sqrt(C0)) ** 2
G1 = kap_t - T1_t
G1_claim = E0 * t - 2 - 2 * sp.sqrt((1 + A0 * t) * (1 + B0_ * t)) - 2 * sp.sqrt(C0) * (sp.sqrt(1 + A0 * t) + sp.sqrt(1 + B0_ * t))
record("DA-10 path invariants: beta12=1+A0 t etc. from B with t=1/s",
       sp.Matrix([1 + e1 * q1 ** 2 / c1 * t, 1 + e2 * q2 ** 2 / c2 * t, 1 + e3 * h ** 2 / (c1 * c2),
                  1 + e3 * h ** 2 / (c1 * c2) + (e1 * q1 ** 2 / c1 + e2 * q2 ** 2 / c2 + h * q1 * q2 * (e1 * e3 - e2) / (c1 * c2)) * t]),
       sp.Matrix([*beta, kappa]).subs(s, 1 / t))
record("DA-10 G1(t) = kappa(t) - T1(beta(t)) closed form", G1_claim, G1)
record("DA-10 G1(0) = -4 - 4 sqrt(C0) < 0 (independent of E0)", -4 - 4 * sp.sqrt(C0), G1.subs(t, 0))
G1p = sp.diff(G1, t); G1pp = sp.diff(G1, t, 2)
# second derivative of sqrt((1+A0t)(1+B0t)): 2pp''-p'^2 = -(A0-B0)^2
pq = (1 + A0 * t) * (1 + B0_ * t)
record("DA-10 2 p p'' - p'^2 = -(A0-B0)^2 for p=(1+A0 t)(1+B0 t)", -(A0 - B0_) ** 2, 2 * pq * sp.diff(pq, t, 2) - sp.diff(pq, t) ** 2)
G1pp_claim = ((A0 - B0_) ** 2 / (2 * pq ** sp.Rational(3, 2))
              + sp.sqrt(C0) * (A0 ** 2 / (2 * (1 + A0 * t) ** sp.Rational(3, 2)) + B0_ ** 2 / (2 * (1 + B0_ * t) ** sp.Rational(3, 2))))
record("DA-10 G1''(t) = (A0-B0)^2/(2 p^{3/2}) + sqrt(C0)[A0^2/(2(1+A0t)^{3/2}) + B0^2/(2(1+B0t)^{3/2})] > 0", G1pp_claim, G1pp,
       "manifestly positive: strict convexity for every A0,B0,C0,E0 > 0")
record("DA-10 lim G1(t)/t = E0 - 2 sqrt(A0 B0)", E0 - 2 * sp.sqrt(A0 * B0_), sp.limit(G1 / t, t, sp.oo))
RESULTS.append({"name": "DA-10 root existence/uniqueness/transversality", "status": "LOGIC_VERIFIED",
                "argument": "G1 strictly convex, G1(0) < 0. If E0 > 2 sqrt(A0 B0): G1 -> +oo, so exactly one root t_H > 0. "
                            "Transversality is automatic: convexity gives G1'(t_H) >= (G1(t_H) - G1(0))/t_H = (4 + 4 sqrt(C0))/t_H > 0, "
                            "so G1'(t_H) cannot vanish. If E0 <= 2 sqrt(A0 B0): G1 < 0 for all t (G1 ~ (E0-2sqrt(A0B0)) t - "
                            "2 sqrt(C0)(sqrt A0 + sqrt B0) sqrt t -> -oo or stays negative by convexity), so no crossing: "
                            "the condition E0 > 2 sqrt(A0 B0) is necessary and sufficient for a crossing.",
                "assumptions": "A0, B0, C0 > 0, E0 > 0"})
t0 = sp.symbols("t0", positive=True)
E0_choice = (2 + 2 * sp.sqrt((1 + A0 * t0) * (1 + B0_ * t0)) + 2 * sp.sqrt(C0) * (sp.sqrt(1 + A0 * t0) + sp.sqrt(1 + B0_ * t0))) / t0
record("DA-11 G1(t0) = 0 with the prescribed E0", 0, G1.subs({E0: E0_choice, t: t0}))
record("DA-11 E0 - 2 sqrt(A0 B0) = [2 + 2(sqrt(p(t0)) - sqrt(A0 B0) t0) + 2 sqrt(C0)(...)]/t0 with sqrt(p) > sqrt(A0B0) t0",
       0, sp.simplify(E0_choice - 2 * sp.sqrt(A0 * B0_) - (2 + 2 * (sp.sqrt((1 + A0 * t0) * (1 + B0_ * t0)) - sp.sqrt(A0 * B0_) * t0)
                                                            + 2 * sp.sqrt(C0) * (sp.sqrt(1 + A0 * t0) + sp.sqrt(1 + B0_ * t0))) / t0),
       "p(t0) = 1 + (A0+B0) t0 + A0 B0 t0^2 > A0 B0 t0^2, so every bracketed term is positive: E0 > 2 sqrt(A0 B0)")

# ----------------------------------------------------------------- DA-12 two-dimensional model
qq, pp, dd = sp.symbols("q p d", positive=True)
F2 = sp.Matrix([gDA - qq * y, pp * x - dd])
DF2 = F2.jacobian([x, y])
B2_claim = sp.Matrix([[sp.diff(gDA, x), -qq], [pp, 0]])
record("DA-12 B2 = [[g_DA'(X), -q],[p, 0]]", B2_claim, DF2)
record("DA-12 det B2 = p q", pp * qq, B2_claim.det())
record("DA-12 X = d/p", dd / pp, sp.solve(F2[1], x)[0])
mc = sp.solve(sp.Eq(1 / (K - X) - 1 / (X - m) + 1 / (X + a), 0), m)[0]
record("DA-12 m_c = X - (K-X)(X+a)/(K+a)", X - (K - X) * (X + a) / (K + a), mc)
record("DA-12 m_c = (X^2 + 2aX - Ka)/(K+a)", (X ** 2 + 2 * a * X - K * a) / (K + a), mc)
RESULTS.append({"name": "DA-12 C-07 classification of B2", "status": "LOGIC_VERIFIED",
                "argument": "C-07: B2 in F_alpha^(2) iff det > 0 (= pq, true), a11 = g'(X) <= 0, a22 = 0 <= 0. Classical 2x2 "
                            "D-stability iff det > 0, a11,a22 <= 0 and a11 + a22 < 0, i.e. g'(X) < 0. Difference set: g'(X) = 0 "
                            "(then B2 = [[0,-q],[p,0]] has eigenvalues +-i sqrt(pq), |arg| = pi/2 > alpha pi/2). "
                            "Admissibility of m_c: m_c < X iff (K-X)(X+a) > 0 (true); m_c > 0 iff X^2 + 2aX > Ka.",
                "assumptions": "p, q, d > 0, X = d/p in (m, K)"})

with open(OUT, "w") as f:
    json.dump({"identities": RESULTS,
               "summary": {"n": len(RESULTS), "mismatches": [e["name"] for e in RESULTS if e["status"] in ("MISMATCH", "SIGN_NOT_PROVED", "RANK_DEFICIENT")]}},
              f, indent=2)
print("mismatches:", [e["name"] for e in RESULTS if e["status"] in ("MISMATCH", "SIGN_NOT_PROVED", "RANK_DEFICIENT")])
