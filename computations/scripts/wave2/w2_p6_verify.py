"""P6 follow-up: HP verification of the cycle-merging identity and sufficiency probe.

Identity (PROOF, invariant subspace): for D = diag(d1, d2, d, d),
    spec(D A_{s,t}) = spec(D' C_{s+t}) U {-d},   D' = diag(d1, d2, d),
where C_g is the 3x3 negative-feedback cycle with product -g.  Hence membership of
A_{s,t} in F_alpha requires s + t < R3(alpha)^3 (necessity).  Sufficiency probe: at
s + t = R3^3 (1 - 1e-6) with s != t the minimum margin over the whole 3-simplex is > 0,
and at s + t = R3^3 (1 + 1e-6) it is < 0 (float, independent of the bisection data).
"""
import json, os, sys
import mpmath as mp
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from w2_common import RESULTS, dump, stamp
from w2_p6_n4_shared_edge import A_st, min_margin
from fdsn.c10_threshold import mp_siami_R3

mp.mp.dps = 50
out = {"identity_checks": [], "sufficiency_probe": []}
rng = np.random.default_rng(6)
for _ in range(20):
    s, t = mp.mpf(rng.uniform(0, 30)), mp.mpf(rng.uniform(0, 30))
    d1, d2, d = (mp.exp(mp.mpf(v)) for v in rng.normal(scale=2, size=3))
    A = mp.matrix([[-1, 0, -s, -t], [1, -1, 0, 0], [0, 1, -1, 0], [0, 1, 0, -1]])
    D = mp.diag([d1, d2, d, d])
    ev4 = sorted(mp.eig(D * A, left=False, right=False), key=lambda z: (mp.re(z), mp.im(z)))
    C = mp.matrix([[-1, 0, -(s + t)], [1, -1, 0], [0, 1, -1]])
    ev3 = sorted(list(mp.eig(mp.diag([d1, d2, d]) * C, left=False, right=False)) + [mp.mpc(-d, 0)], key=lambda z: (mp.re(z), mp.im(z)))
    err = max(max(min(abs(a - b) for b in ev3) for a in ev4), max(min(abs(a - b) for a in ev4) for b in ev3))   # Hausdorff
    out["identity_checks"].append({"s": float(s), "t": float(t), "max_abs_eig_diff": float(err)})
out["identity_max_err"] = max(c["max_abs_eig_diff"] for c in out["identity_checks"])
for a in (0.99, 0.9, 0.8, 0.7):
    R = float(mp_siami_R3(a)) ** 3
    for frac in (0.15, 0.5, 0.85):
        for sgn in (-1, 1):
            tot = R * (1 + sgn * 1e-6)
            s, t = frac * tot, (1 - frac) * tot
            m, x = min_margin(s, t, a, n_local=6)
            out["sufficiency_probe"].append({"alpha": a, "s": s, "t": t, "s+t over R3^3": 1 + sgn * 1e-6,
                                             "min_margin_simplex": float(m), "x_worst": [float(v) for v in x],
                                             "consistent": bool((m > 0) == (sgn < 0))})
out["sufficiency_probe_all_consistent"] = all(p["consistent"] for p in out["sufficiency_probe"])
out["worst_x_has_x3=x4"] = max(abs(p["x_worst"][2] - p["x_worst"][3]) for p in out["sufficiency_probe"])
out.update(stamp({"label": "identity: HP 50 digits (PROOF-level algebra); probe: FLOAT"}))
dump("N4_SHARED_EDGE_VERIFY.json", out)
print(out["identity_max_err"], out["sufficiency_probe_all_consistent"], out["worst_x_has_x3=x4"])
