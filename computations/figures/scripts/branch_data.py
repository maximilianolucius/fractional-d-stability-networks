"""Data generation for FIG-06 / FIG-07 / FIG-08: the Double-Allee coexistence branch as m varies (Chief design,
alpha = 0.9), HP location of the Cain crossing, candidate anchors with certified margins.

Evidence classes: branch quantities = numerical evaluation of exact formulas (float64; HP at the crossing);
T_alpha = exact C-10 minimum (C-15 unique optimiser); anchor margins = CERTIFIED INTERVAL (interval Newton,
outward rounding, 50 digits) via computations/scripts/double_allee_interval_box.check_box.
Output: computations/figures/data/branch_alpha0.9.json
"""
import json, os, sys
import numpy as np
import mpmath as mp
from mpmath import iv
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "computations", "scripts"))
from fdsn.double_allee import PARAM_NAMES, Params, chief_witness, coexistence_equilibria, g_da_prime, invariants_of_matrix, reduced_matrix, with_m
from fdsn.c10_threshold import T1, invariants_batch, threshold_batch, threshold_mp, rho_alpha
from fdsn.direct_margin import min_margin
import double_allee_interval_box as IB

ALPHA = 0.9
P = chief_witness()
OUT = os.path.join(ROOT, "computations", "figures", "data", "branch_alpha0.9.json")


def point(m, alpha=ALPHA):
    Pm = with_m(P, m)
    eqs = coexistence_equilibria(Pm)
    if not eqs:
        return None
    e = eqs[0]
    B = np.array(reduced_matrix(e["X"], e["Y"], e["Z"], Pm), float)
    p, mm, q, beta, kappa = invariants_batch(B[None])
    tb = threshold_batch(beta, alpha)
    return {"m": m, "X": e["X"], "Y": e["Y"], "Z": e["Z"], "s": float(-B[0, 0]), "t": 1 / float(-B[0, 0]),
            "beta": beta[0].tolist(), "kappa": float(kappa[0]), "T1": float(T1(beta[0])), "T_alpha": float(tb.T[0]),
            "x_star": tb.x[0].tolist(), "n_eq": len(eqs), "B": B.tolist()}


ms = np.round(np.arange(0.01, 0.70, 0.0025), 6)
branch = [r for r in (point(float(m)) for m in ms) if r is not None]
# HP crossing: kappa - T1 = 0 by bisection at 60 digits (exact-formula evaluation at each m)
with mp.workdps(60):
    Pm = chief_witness(lambda v: mp.mpf(v))
    from fdsn.double_allee import prey_roots, yz_of_x
    def G1(m):
        Pq = with_m(Pm, m); X = max(prey_roots(Pq)); Y, Z = yz_of_x(X, Pq)
        I = invariants_of_matrix(reduced_matrix(X, Y, Z, Pq)); b = I["beta"]
        return I["kappa"] - (mp.sqrt(b[0]) + mp.sqrt(b[1]) + mp.sqrt(b[2])) ** 2
    lo, hi = mp.mpf("0.19"), mp.mpf("0.21")
    for _ in range(200):
        mid = (lo + hi) / 2
        if G1(mid) * G1(lo) <= 0:
            hi = mid
        else:
            lo = mid
    m0_hp = mp.nstr((lo + hi) / 2, 50)
    G1_at_02 = mp.nstr(G1(mp.mpf("0.2")), 10)
# path constants A0, B0, C0, E0 (exact from parameters)
A0 = P.e1 * P.q1 ** 2 / P.c1; B0 = P.e2 * P.q2 ** 2 / P.c2; C0 = 1 + P.e3 * P.h ** 2 / (P.c1 * P.c2); E0 = P.h * P.q1 * P.q2 * (P.e1 * P.e3 - P.e2) / (P.c1 * P.c2)
# anchor candidates
cands = {}
Pf = chief_witness(lambda v: iv.mpf(v))
base = np.array(P.as_list())
for m in (0.30, 0.33, 0.35, 0.38, 0.40):
    r = point(m)
    B = np.array(r["B"])
    dm = min_margin(B[None], ALPHA, half_width=16, step=0.5, n_starts=4)
    d1 = min_margin(B[None], 1.0, half_width=16, step=0.5, n_starts=4)
    # relative conditioning of the classical margin: sum_i |d(kappa-T1)/dlog p_i| / (kappa-T1)
    def F1(v):
        Pp = Params(*v); e = coexistence_equilibria(Pp)[0]
        Bq = np.array(reduced_matrix(e["X"], e["Y"], e["Z"], Pp)); _, _, _, bb, kk = invariants_batch(Bq[None])
        return kk[0] - T1(bb[0]), threshold_batch(bb, ALPHA).T[0] - kk[0]
    v0 = base.copy(); v0[3] = m
    g1 = []; g2 = []
    for i in range(14):
        h = 1e-6; vp = v0.copy(); vp[i] *= 1 + h; vm = v0.copy(); vm[i] *= 1 - h
        a, b = F1(vp); c, d = F1(vm); g1.append((a - c) / (2 * h)); g2.append((b - d) / (2 * h))
    f1, f2 = F1(v0)
    cert = IB.check_box(with_m(Pf, iv.mpf(repr(m))), cert_cache={})
    ev = np.linalg.eigvals(np.diag(dm["d"][0]) @ B)
    cands[f"{m:.2f}"] = {**r, "direct_min_margin_alpha": float(dm["margin"][0]), "direct_min_margin_1": float(d1["margin"][0]),
                         "worst_d_geomean1": (dm["d"][0] / np.prod(dm["d"][0]) ** (1 / 3)).tolist(), "eig_at_worst_d": [[float(v.real), float(v.imag)] for v in ev],
                         "m_Cain": f1, "m_frac": f2, "m_Cain_over_T1": f1 / r["T1"], "m_frac_over_Talpha": f2 / r["T_alpha"],
                         "cond_classical": float(np.sum(np.abs(g1)) / f1), "cond_fractional": float(np.sum(np.abs(g2)) / f2),
                         "Z_over_X": r["Z"] / r["X"], "Y_over_X": r["Y"] / r["X"], "X_over_K": r["X"] / P.K, "m_over_X": m / r["X"],
                         "Phi": r["T1"] / r["kappa"], "rho_alpha": rho_alpha(ALPHA),
                         "certified": {k: (str(v) if not isinstance(v, (bool, list)) else v) for k, v in cert.items()}}
json.dump({"alpha": ALPHA, "params": dict(zip(PARAM_NAMES, P.as_list())), "branch": branch, "m0_hp": m0_hp, "G1_at_m0=0.2": G1_at_02,
           "path_constants": {"A0": A0, "B0": B0, "C0": C0, "E0": E0}, "candidates": cands,
           "feasible_range": [branch[0]["m"], branch[-1]["m"]]}, open(OUT, "w"), indent=1, default=str)
print("m0_hp", m0_hp, "G1(0.2)", G1_at_02, "range", branch[0]["m"], branch[-1]["m"])
for k, c in cands.items():
    print(k, "X,Y,Z", round(c["X"], 4), round(c["Y"], 5), round(c["Z"], 6), "mCain/T1 %.4f" % c["m_Cain_over_T1"], "mfrac/Ta %.4f" % c["m_frac_over_Talpha"],
          "cond %.1f %.1f" % (c["cond_classical"], c["cond_fractional"]), "direct", round(c["direct_min_margin_alpha"], 4), round(c["direct_min_margin_1"], 4),
          "cert", c["certified"].get("ok"), c["certified"].get("kappa_minus_T1_lo"), c["certified"].get("T_alpha_L_minus_kappa_hi"))
