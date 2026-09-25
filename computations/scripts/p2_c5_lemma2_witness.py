"""Analytic Lemma-2 (P0 necessity) witnesses for C5 controls, verified at 150 digits.

For -A not P0-with-positive-determinant, C-10 Lemma 2 predicts A not in F_alpha.
Witness D (explicit, from the proof sketch):
  a_ii > 0                 : d_i = 1, other d = 10^-60   -> eigenvalue ~ a_ii > 0
  det A[{i,j}] < 0         : d_i = d_j = 1, d_k = 10^-60 -> 2x2 block with det < 0
  det(A) >= 0 (q <= 0)     : D = I; real 3x3 with det >= 0 has a real eigenvalue >= 0
Applied to every C5 control whose float witness was not confirmed in mp
(P2_HP_RECHECK.json -> nonP_C5), and to all 150 C5 controls in the sample.
"""
import json, os, sys, itertools
import mpmath as mp
sys.path.insert(0, os.path.dirname(__file__))
from _common import RESULTS, dump
import p2_hp_controls as C
from fdsn.direct_margin import mp_margin


def witness(A):
    a = [[A[i, j] for j in range(3)] for i in range(3)]
    small = mp.mpf(10) ** -60
    for i in range(3):
        if a[i][i] > 0:
            return "positive_diagonal", [mp.mpf(1) if k == i else small for k in range(3)]
    for i, j in itertools.combinations(range(3), 2):
        if a[i][i] * a[j][j] - a[i][j] * a[j][i] < 0:
            k = 3 - i - j
            return "negative_2x2_minor", [small if t == k else mp.mpf(1) for t in range(3)]
    if mp.det(A) >= 0:
        return "det_nonnegative", [mp.mpf(1)] * 3
    return "none", None


if __name__ == "__main__":
    mp.mp.dps = 150
    cs = [c for c in C.controls() if c["mech"] == "C5"]
    rows = []
    for c in cs:
        A = mp.matrix([[mp.mpf(float(v)) for v in row] for row in c["A"]])
        kind, d = witness(A)
        m = mp_margin(A, d, c["alpha"], 150)[0] if d else None
        rows.append({"i": c["i"], "alpha": c["alpha"], "violation": kind,
                     "witness_margin": float(m) if m is not None else None})
    rc = json.load(open(os.path.join(RESULTS, "P2_HP_RECHECK.json")))
    bad = {r["i"] for r in rc["nonP_C5"]}
    out = {"n_C5_controls": len(rows), "witness_negative": sum(r["witness_margin"] is not None and r["witness_margin"] < 0 for r in rows),
           "no_witness_found": [r for r in rows if r["witness_margin"] is None or r["witness_margin"] >= 0],
           "previously_unconfirmed": len(bad),
           "previously_unconfirmed_now_witnessed": sum(1 for r in rows if r["i"] in bad and r["witness_margin"] is not None and r["witness_margin"] < 0),
           "by_violation": {k: sum(r["violation"] == k for r in rows) for k in {r["violation"] for r in rows}}}
    print(json.dumps(out, indent=1))
    dump("P2_C5_LEMMA2_WITNESSES.json", {**out, "rows": rows})
