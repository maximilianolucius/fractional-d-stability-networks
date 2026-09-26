"""Part A — search for a less scale-separated biological re-embedding (alpha = 0.9).

Design variables (all decimal, so the final design is exactly reproducible in interval arithmetic):
  target invariants (b12, b13, b23, kappa) inside the band T1 < kappa < T_0.9 at the ANCHOR m_A;
  scales s, c1, c2; efficiency eta (e1 = e3 = eta, e2 = eta^2/tau^2 from DA-06); split xi;
  prey geometry X = 1, a, m_A, K = X + rho_K (K_max - X) with K_max = X + (X-m)(X+a)/(m+a).
Construction: DA-06 realize_invariants + DA-07 embed_double_allee at m_A.  Then, with every non-m
parameter fixed, the branch is continued in m to locate the exact Cain crossing m0 < m_A (kappa = T1),
the feasibility range, and the fractional margin along the branch.
Acceptance: positive parameters, e in (0,1), positive coexistence, strict-P, (kappa-T1)/T1 >= 0.10,
(T_0.9-kappa)/T_0.9 >= 0.20, unique classical crossing on the feasible branch below m_A, feasibility
on both sides of m0.  Visual targets: Y/X, Z/X >= 1e-2, max/min density ratio < 100 (prefer < 30).
Output: computations/figures_wave2/data/reembedding_candidates.json
"""
import json, os, sys, time
import numpy as np
from fdsn.double_allee import PARAM_NAMES, Params, coexistence_equilibria, embed_double_allee, realize_invariants, reduced_matrix, with_m
from fdsn.c10_threshold import T1, invariants_batch, threshold_batch
from fdsn.direct_margin import min_margin

ALPHA = 0.9
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "data", "reembedding_candidates.json")
rng = np.random.default_rng(20260926)


def classify(P, alpha=ALPHA):
    eqs = coexistence_equilibria(P)
    if not eqs:
        return None
    e = eqs[0]
    B = np.array(reduced_matrix(e["X"], e["Y"], e["Z"], P), float)
    p, mm, q, beta, kappa = invariants_batch(B[None])
    if not (p.min() > 0 and mm.min() > 0 and q[0] > 0):
        return {"strictP": False, "eq": e}
    t1 = float(T1(beta[0])); Ta = float(threshold_batch(beta, alpha).T[0])
    return {"strictP": True, "eq": e, "B": B, "beta": beta[0].tolist(), "kappa": float(kappa[0]), "T1": t1, "T_alpha": Ta, "n_eq": len(eqs), "s": float(-B[0, 0])}


def build(d):
    """d: dict of design decimals -> Params (float)."""
    X = 1.0
    b = (d["b12"], d["b13"], d["b23"])
    q1, q2, h, e1, e2, e3 = realize_invariants(*b, d["kappa"], s=d["s"], c1=d["c1"], c2=d["c2"], eta=d["eta"])
    Kmax = X + (X - d["m"]) * (X + d["a"]) / (d["m"] + d["a"])
    K = X + d["rhoK"] * (Kmax - X)
    P, Y, Z, Q, H = embed_double_allee(d["s"], X, d["m"], d["a"], K, q1, q2, h, e1, e2, e3, d["c1"], d["c2"], d["xi"])
    return P, (X, Y, Z), K


def crossing(P, mA):
    """Continue the branch downward in m from mA; return m0 (kappa=T1), feasibility range, uniqueness flag."""
    ms = np.linspace(0.005, min(0.98, mA + 0.5), 500)
    G = []
    for m in ms:
        c = classify(with_m(P, m))
        G.append(np.nan if (c is None or not c["strictP"]) else c["kappa"] - c["T1"])
    G = np.array(G); feas = ~np.isnan(G)
    # contiguous feasible segment containing mA
    iA = int(np.argmin(np.abs(ms - mA)))
    if not feas[iA]:
        return None
    lo = iA
    while lo > 0 and feas[lo - 1]:
        lo -= 1
    hi = iA
    while hi < len(ms) - 1 and feas[hi + 1]:
        hi += 1
    seg = slice(lo, hi + 1)
    sgn = np.sign(G[seg]); ch = np.nonzero(np.diff(sgn))[0]
    out = {"m_feasible_lo": float(ms[lo]), "m_feasible_hi": float(ms[hi]), "n_crossings": int(len(ch))}
    if len(ch) != 1:
        return out
    i = lo + ch[0]
    a_, b_ = ms[i], ms[i + 1]
    f = lambda m: classify(with_m(P, m))["kappa"] - classify(with_m(P, m))["T1"]
    for _ in range(60):
        mid = 0.5 * (a_ + b_)
        if f(mid) * f(a_) <= 0:
            b_ = mid
        else:
            a_ = mid
    out["m0"] = 0.5 * (a_ + b_)
    # fractional margin minimum on the feasible segment above m0
    return out


def evaluate(d):
    try:
        P, (X, Y, Z), K = build(d)
    except Exception as exc:
        return {"design": d, "reject": f"construction failed: {exc}"}
    vals = P.as_list()
    if not all(v > 0 for v in vals) or not all(0 < v < 1 for v in (P.e1, P.e2, P.e3)):
        return {"design": d, "reject": "nonpositive parameter or efficiency outside (0,1)"}
    c = classify(P)
    if c is None or not c["strictP"]:
        return {"design": d, "reject": "no feasible strict-P coexistence at the anchor"}
    if abs(c["eq"]["X"] - X) > 1e-9 or abs(c["eq"]["Y"] - Y) > 1e-9 * max(1, Y) or abs(c["eq"]["Z"] - Z) > 1e-9 * max(1, Z):
        return {"design": d, "reject": "quadratic root does not reproduce the embedded equilibrium (other root selected)"}
    mC, mF = (c["kappa"] - c["T1"]) / c["T1"], (c["T_alpha"] - c["kappa"]) / c["T_alpha"]
    dens = np.array([X, Y, Z]); ratio = dens.max() / dens.min()
    rec = {"design": d, "params": dict(zip(PARAM_NAMES, vals)), "K": K, "X": X, "Y": Y, "Z": Z, "Y_over_X": Y / X, "Z_over_X": Z / X, "density_ratio": ratio,
           "beta": c["beta"], "kappa": c["kappa"], "T1": c["T1"], "T_alpha": c["T_alpha"], "rel_classical_margin": mC, "rel_fractional_margin": mF, "s": c["s"], "n_eq": c["n_eq"]}
    if mC < 0.10 or mF < 0.20:
        rec["reject"] = "margins below targets"; return rec
    if c["n_eq"] > 1:
        rec["reject"] = "two coexistence equilibria"; return rec
    cr = crossing(P, d["m"])
    if cr is None or "m0" not in cr:
        rec["reject"] = "no unique classical crossing on the feasible branch below the anchor"; rec["crossing"] = cr; return rec
    rec["crossing"] = cr
    if cr["m0"] <= cr["m_feasible_lo"] + 0.02 or d["m"] >= cr["m_feasible_hi"] - 0.02:
        rec["reject"] = "crossing or anchor too close to feasibility loss"; return rec
    # conditioning of the classical margin (sum |d(kappa-T1)/dlog p| / (kappa-T1))
    def F1(v):
        cc = classify(Params(*v)); return cc["kappa"] - cc["T1"], cc["T_alpha"] - cc["kappa"]
    v0 = np.array(vals); g1 = []; g2 = []
    for i in range(14):
        hh = 1e-6; vp = v0.copy(); vp[i] *= 1 + hh; vm = v0.copy(); vm[i] *= 1 - hh
        a1, b1 = F1(vp); a2, b2 = F1(vm); g1.append((a1 - a2) / (2 * hh)); g2.append((b1 - b2) / (2 * hh))
    rec["cond_classical"] = float(np.sum(np.abs(g1)) / (c["kappa"] - c["T1"])); rec["cond_fractional"] = float(np.sum(np.abs(g2)) / (c["T_alpha"] - c["kappa"]))
    dm = min_margin(c["B"][None], ALPHA, half_width=14, step=0.5, n_starts=3); d1 = min_margin(c["B"][None], 1.0, half_width=14, step=0.5, n_starts=3)
    rec["direct_margin_alpha"] = float(dm["margin"][0]); rec["direct_margin_1"] = float(d1["margin"][0])
    rec["accept"] = bool(rec["direct_margin_alpha"] > 0 and rec["direct_margin_1"] < 0)
    return rec


def sample_design():
    b = rng.uniform(1.5, 6.0, 3)
    frac = rng.uniform(0.35, 0.75)
    t1 = float(T1(b)); Ta = float(threshold_batch(b[None], ALPHA).T[0])
    kappa = t1 + frac * (Ta - t1)
    d = {"b12": round(float(b[0]), 3), "b13": round(float(b[1]), 3), "b23": round(float(b[2]), 3), "kappa": round(kappa, 3),
         "s": round(float(10 ** rng.uniform(-1.3, 0)), 4), "c1": round(float(10 ** rng.uniform(-1.3, 0)), 4), "c2": round(float(10 ** rng.uniform(-1.3, 0)), 4),
         "eta": round(float(rng.uniform(0.5, 0.9)), 3), "xi": round(float(rng.uniform(0.2, 0.8)), 3), "a": round(float(10 ** rng.uniform(-0.7, 0.5)), 3),
         "m": round(float(rng.uniform(0.2, 0.6)), 3), "rhoK": round(float(rng.uniform(0.3, 0.95)), 3)}
    return d


def main():
    t0 = time.time()
    recs = []
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 1500
    for i in range(n):
        d = sample_design(); r = evaluate(d); recs.append(r)
        if i % 100 == 0:
            acc = [x for x in recs if x.get("accept")]
            print(i, "accepted", len(acc), "best ratio", min([x["density_ratio"] for x in acc], default=None), file=sys.stderr, flush=True)
    acc = [x for x in recs if x.get("accept")]
    # ranking: density ratio (visual) subject to margins/conditioning; lexicographic score
    def robust(x):
        cr = x["crossing"]
        return (x["rel_classical_margin"] >= 0.25 and x["rel_fractional_margin"] >= 0.30 and x["cond_classical"] <= 120
                and x["design"]["m"] - cr["m0"] >= 0.08 and cr["m_feasible_hi"] - x["design"]["m"] >= 0.06 and cr["m0"] - cr["m_feasible_lo"] >= 0.05)
    for x in acc:
        x["robust_filter"] = robust(x)
        x["score"] = (np.log10(x["density_ratio"]) + 0.5 * max(0, np.log10(x["cond_classical"] / 80.0)) - 0.3 * min(x["rel_classical_margin"], 0.3) / 0.3
                      + (0 if x["robust_filter"] else 10))
    acc.sort(key=lambda x: x["score"])
    for x in acc:
        x.pop("B", None)
    summ = {"n_sampled": n, "n_accepted": len(acc), "n_robust_filter": sum(x["robust_filter"] for x in acc), "rejections": {}, "top": acc[:40],
            "all_accepted_compact": [{k: x[k] for k in ("design", "density_ratio", "Y_over_X", "Z_over_X", "rel_classical_margin", "rel_fractional_margin",
                                                          "cond_classical", "cond_fractional", "crossing", "robust_filter", "K")} for x in acc],
            "robust_filter": "rel_classical>=0.25, rel_fractional>=0.30, cond_classical<=120, mA-m0>=0.08, feas_hi-mA>=0.06, m0-feas_lo>=0.05",
            "seconds": round(time.time() - t0, 1),
            "wave1_anchor_m035": {"Y_over_X": 0.0369, "Z_over_X": 0.00128, "density_ratio": 780, "rel_classical_margin": 0.141, "rel_fractional_margin": 0.477, "cond_classical": 80.3}}
    for x in recs:
        if "reject" in x:
            k = x["reject"].split(":")[0]; summ["rejections"][k] = summ["rejections"].get(k, 0) + 1
    json.dump(summ, open(OUT, "w"), indent=1, default=float)
    for x in [y for y in acc if y["robust_filter"]][:12]:
        print(f"ratio {x['density_ratio']:.1f}  Y/X {x['Y_over_X']:.3f} Z/X {x['Z_over_X']:.3f}  mC {x['rel_classical_margin']:.3f} mF {x['rel_fractional_margin']:.3f} cond {x['cond_classical']:.0f}/{x['cond_fractional']:.1f}  m0 {x['crossing']['m0']:.3f} mA {x['design']['m']} feas [{x['crossing']['m_feasible_lo']:.3f},{x['crossing']['m_feasible_hi']:.3f}]  K {x['K']:.3f}  design {x['design']}")


if __name__ == "__main__":
    main()
