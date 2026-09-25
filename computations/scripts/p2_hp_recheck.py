"""Re-check the strict-P controls that p2_hp_controls.py reported inconsistent.

Hypothesis: the mp pattern search (step doubling on success, no bound) runs
away to |w| >> 16, i.e. diagonal ratios e^|w|, where dps=40 cannot resolve the
eigenvalues of relative size e^-|w|: an eigenvalue with arg exactly 0 appears.
For each case: rerun the same search, record the final w, re-evaluate the
margin there with dps = 60 + 2*|w|_max*log10(e), and also run a BOUNDED
search (|w| <= 16) at 60 digits.
"""
import json, os, sys
import mpmath as mp
import numpy as np
sys.path.insert(0, os.path.dirname(__file__))
from _common import RESULTS, dump, pool
import p2_hp_controls as C
import p2_hp_verify as H
from fdsn.direct_margin import min_margin, mp_margin


def bounded_search(As, alpha, w0, dps, bound=16.0, min_step=1e-15, max_evals=600):
    w = [mp.mpf(float(w0[0])), mp.mpf(float(w0[1]))]
    f = lambda v: mp_margin(As, [mp.exp(v[0]), mp.exp(v[1]), mp.mpf(1)], alpha, dps)[0]
    best, step, ev = f(w), mp.mpf("0.01"), 1
    while step > min_step and ev < max_evals:
        imp = False
        for dx, dy in H.DIRS:
            t = [w[0] + step * dx, w[1] + step * dy]
            if abs(t[0]) > bound or abs(t[1]) > bound:
                continue
            v = f(t); ev += 1
            if v < best:
                best, w, imp = v, t, True
                break
        step = step * 2 if imp else step / 2
    return best, w


def job(c):
    r = min_margin(c["A"][None], c["alpha"], half_width=16, step=0.5, n_starts=3)
    w0 = r["w"][0]
    with mp.workdps(60):
        A = mp.matrix([[mp.mpf(float(v)) for v in row] for row in c["A"]])
        p, beta, kappa, sp = H.mp_inv(A)
        As = mp.matrix([[A[i, j] / p[i] for j in range(3)] for i in range(3)])
        alpha = mp.mpf(c["alpha"])
        m40, wf, ev = H.search(As, alpha, w0, 40, mp.mpf(10) ** -18)
        wmax = float(max(abs(wf[0]), abs(wf[1])))
        dps_hi = int(60 + 2 * wmax / np.log(10))
    with mp.workdps(dps_hi + 20):
        m_hi = mp_margin(As, [mp.exp(wf[0]), mp.exp(wf[1]), mp.mpf(1)], alpha, dps_hi)[0]
    with mp.workdps(80):
        mb, wb = bounded_search(As, alpha, w0, 60)
    return {"mech": c["mech"], "i": c["i"], "alpha": c["alpha"], "strictP": bool(sp),
            "unbounded_search_margin_dps40": float(m40), "final_|w|max": wmax,
            "margin_at_that_w_dps": dps_hi, "margin_at_that_w": float(m_hi),
            "bounded_search_margin_dps60": float(mb)}


if __name__ == "__main__":
    d = json.load(open(os.path.join(RESULTS, "P2_HP_CONTROLS.json")))
    bad = {(b["mech"], b["i"]) for b in d["control_sample_v2"]["inconsistent_float_global_start"]}
    cs = [c for c in C.controls() if (c["mech"], c["i"]) in bad]
    with pool() as P:
        res = P.map(job, cs, chunksize=1)
    sp = [r for r in res if r["strictP"]]
    out = {"n": len(res), "n_strictP": len(sp),
           "strictP_negative_at_adequate_precision": [r for r in sp if r["margin_at_that_w"] < 0],
           "strictP_negative_bounded_search": [r for r in sp if r["bounded_search_margin_dps60"] < 0],
           "max_final_|w|": max(r["final_|w|max"] for r in res),
           "min_final_|w|_strictP": min(r["final_|w|max"] for r in sp) if sp else None,
           "nonP_C5": [r for r in res if not r["strictP"]],
           "rows": res}
    dump("P2_HP_RECHECK.json", out)
