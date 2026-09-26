"""Select the Wave-2 biological design from the re-embedding search, certify it, and compute its branch.

Selection: among candidates passing the robust filter, minimise the density ratio subject to the Chief targets;
the winner is re-evaluated from its DECIMAL design (exact reproducibility), its Cain crossing m0 is located to
60 digits, the anchor point and an m-interval around it are interval-certified (interval Newton + outward
rounding, 50 digits; C-11 certificate unconditional, C-10-bracket certificate conditional on C-15 Thm 1), and
the whole branch (all non-m parameters fixed) is tabulated for FIG-06/07/08.
Outputs: data/design_selected.json, data/branch_wave2.json
"""
import json, os, sys
import numpy as np
import mpmath as mp
from mpmath import iv
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "computations", "scripts"))
from design_tools import ALPHA, DATA, crossing_hp, params_from_design, point, save_json
from fdsn.double_allee import PARAM_NAMES, Params, with_m
from fdsn.direct_margin import min_margin
import double_allee_interval_box as IB

cand = json.load(open(os.path.join(DATA, "reembedding_candidates.json")))
robust = [x for x in cand["all_accepted_compact"] if x["robust_filter"]]
# selection rule (internal): conditioning not worse than the Wave-1 anchor (80), anchor at least 0.10 in m from both the
# Cain crossing and the feasibility loss; then the smallest density ratio.  Ties/alternatives listed in `shortlist`.
strong = [x for x in robust if x["cond_classical"] <= 85 and x["design"]["m"] - x["crossing"]["m0"] >= 0.10 and x["crossing"]["m_feasible_hi"] - x["design"]["m"] >= 0.10]
strong.sort(key=lambda x: x["density_ratio"])
robust.sort(key=lambda x: x["density_ratio"])
top = (strong + [x for x in robust if x not in strong])[:10]
chosen = top[0] if len(sys.argv) < 2 else top[int(sys.argv[1])]
d = {k: (str(v)) for k, v in chosen["design"].items()}
P, (X, Y, Z) = params_from_design(d)
mA = float(d["m"])
r = point(P, mA)
assert r and r["strictP"] and r["T1"] < r["kappa"] < r["T_alpha"]
# branch
ms = np.round(np.arange(0.005, 0.99, 0.0025), 6)
branch = []
for m in ms:
    q = point(P, float(m))
    if q is None:
        continue
    q.pop("B", None); branch.append(q)
feas = [q for q in branch if q["strictP"]]
iA = min(range(len(feas)), key=lambda i: abs(feas[i]["m"] - mA))
seg = [feas[iA]]
i = iA - 1
while i >= 0 and abs(feas[i]["m"] - seg[0]["m"]) < 0.003:
    seg.insert(0, feas[i]); i -= 1
i = iA + 1
while i < len(feas) and abs(feas[i]["m"] - seg[-1]["m"]) < 0.003:
    seg.append(feas[i]); i += 1
G1 = np.array([q["kappa"] - q["T1"] for q in seg]); mm = np.array([q["m"] for q in seg])
ch = np.nonzero(np.diff(np.sign(G1)))[0]
assert len(ch) == 1, ("crossings", len(ch))
m0_hp, G_at_m0 = crossing_hp(d, mm[ch[0]], mm[ch[0] + 1])
m0 = float(m0_hp)
mC = round(max(seg[0]["m"] + 0.02, m0 - 0.5 * (m0 - seg[0]["m"])), 3)      # classical point: midway between feasibility start and m0
# certification at the anchor and candidates around it
Pf, _ = params_from_design(d, lambda v: iv.mpf(v))
cache = {}
cert = {}
for m in (mA, round(mA - 0.03, 3), round(mA + 0.03, 3)):
    c = IB.check_box(with_m(Pf, iv.mpf(repr(m))), cert_cache=cache)
    cert[repr(m)] = {k: (str(v) if not isinstance(v, (bool, list)) else v) for k, v in c.items()}
# m-interval certification around the anchor (adaptive bisection as in Audit 1)
def adaptive(lo_, hi_, min_width=1e-6, budget=3000):
    stack = [(mp.mpf(lo_), mp.mpf(hi_))]; ok = []; n = 0; fails = []
    while stack and n < budget:
        a_, b_ = stack.pop(); n += 1
        res = IB.check_box(with_m(Pf, iv.mpf([a_, b_])), cert_cache=cache)
        if res["ok"]:
            ok.append((float(a_), float(b_), float(res["kappa_minus_T1_lo"]), float(res["T_alpha_L_minus_kappa_hi"]) if res.get("T_alpha_L_minus_kappa_hi") is not None else None))
        elif b_ - a_ > min_width:
            mid = (a_ + b_) / 2; stack += [(mid, b_), (a_, mid)]
        else:
            fails.append((float(a_), float(b_), res.get("fail")))
    return ok, fails, n
lo_int, hi_int = round(m0 + 0.02, 3), round(min(seg[-1]["m"] - 0.035, mA + 0.07), 3)
ok, fails, nbox = adaptive(lo_int, hi_int)
covered = sum(b - a for a, b, *_ in ok)
interval_cert = {"attempted": [lo_int, hi_int], "certified_length": covered, "fully_certified": bool(not fails and abs(covered - (hi_int - lo_int)) < 1e-9),
                 "n_boxes": nbox, "n_subintervals": len(ok), "failures": fails[:5],
                 "min_kappa_minus_T1_lo": min(x[2] for x in ok) if ok else None, "min_T_alpha_L_minus_kappa_hi": min(x[3] for x in ok if x[3] is not None) if ok else None}
# direct spectral corroboration at the anchor
B = np.array(point(P, mA)["B"])
dm = min_margin(B[None], ALPHA, half_width=16, step=0.5, n_starts=4); d1 = min_margin(B[None], 1.0, half_width=16, step=0.5, n_starts=4)
ev = np.linalg.eigvals(np.diag(dm["d"][0]) @ B)
sel = {"design": d, "alpha": ALPHA, "params": dict(zip(PARAM_NAMES, P.as_list())), "anchor_m": mA, "classical_m": mC, "m0_hp": m0_hp, "G1_at_m0": G_at_m0,
       "feasible_range": [seg[0]["m"], seg[-1]["m"]], "anchor": {k: r[k] for k in ("X", "Y", "Z", "s", "beta", "kappa", "T1", "T_alpha", "x_star")},
       "margins": {"m_Cain": r["kappa"] - r["T1"], "m_frac": r["T_alpha"] - r["kappa"], "rel_classical": (r["kappa"] - r["T1"]) / r["T1"], "rel_fractional": (r["T_alpha"] - r["kappa"]) / r["T_alpha"]},
       "densities": {"Y_over_X": Y / X, "Z_over_X": Z / X, "ratio": max(X, Y, Z) / min(X, Y, Z)},
       "conditioning": {"classical": chosen["cond_classical"], "fractional": chosen["cond_fractional"]},
       "direct": {"min_margin_alpha": float(dm["margin"][0]), "min_margin_1": float(d1["margin"][0]), "worst_d_geomean1": (dm["d"][0] / np.prod(dm["d"][0]) ** (1 / 3)).tolist(),
                  "eig_at_worst_d": [[float(v.real), float(v.imag)] for v in ev], "min_arg": float(np.min(np.abs(np.angle(ev))))},
       "certified_points": cert, "certified_m_interval": interval_cert, "shortlist": top}
save_json("design_selected.json", sel)
save_json("branch_wave2.json", {"design": d, "alpha": ALPHA, "params": sel["params"], "branch": branch})
print(json.dumps({k: sel[k] for k in ("design", "anchor_m", "classical_m", "m0_hp", "G1_at_m0", "feasible_range", "margins", "densities", "conditioning", "direct")}, indent=1, default=str))
print("cert", {k: (v["ok"], v.get("kappa_minus_T1_lo", "")[:10], v.get("T_alpha_L_minus_kappa_hi", "")[:10]) for k, v in cert.items()}, interval_cert)
