"""Round-1 R2-4: certified 14-parameter box around the published W2-A parameters (Table 3).

Box: every biological parameter p_i ranges independently over [p_i(1-delta), p_i(1+delta)]
(e1 and e3 are varied independently), centred at the printed Table-3 decimals, alpha = 0.9.
On every (sub)box we certify with outward-rounded mpmath.iv arithmetic (50 digits):
  * a unique prey root X of the scalar equilibrium equation in a verified enclosure (interval Newton),
    with F_X != 0 on the hull (implicit-function / mean-value validity);
  * feasibility  Y > 0, Z > 0, m < X < K, s = -g'(X) > 0  (hence strict-P, see below);
  * the fractional-only band  kappa - T1 > 0  and  T_0.9(beta) - kappa > 0, the latter via the
    certified lower bracket L <= T_0.9(beta_lo) at the componentwise-lower beta corner (T_alpha is
    nondecreasing in every beta_ij) and kappa_hi < L.
Enclosures use the first-order mean-value form G(P) in G(c) + sum_i dG/dp_i(hull) [-w_i, w_i]
(as in computations/scripts/double_allee_box_meanvalue.py); failing boxes are bisected along the
coordinate with the largest contribution until certified or a depth limit is hit.
Strict-P: p = (s, c1, c2) > 0, the order-two minors s c1 + e1 q1^2, s c2 + e2 q2^2, c1 c2 + e3 h^2 are
positive, and -det B = kappa s c1 c2 > 0.
Output: computations/figures_wave2/data/param_box_certificate.json
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time
from multiprocessing import Pool

import mpmath as mp
import sympy as sp
from mpmath import iv

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "src"))
from fdsn.double_allee import PARAM_NAMES, Params, quadratic_coeffs  # noqa: E402
from fdsn.interval_cert import certify_threshold_logit  # noqa: E402

iv.dps = 50
mp.mp.dps = 50
ALPHA = "0.9"

# printed Table-3 values (the box centre is what the reader sees)
TABLE = {"a": "0.229", "K": "1.4913425743", "r": "7.8104480113", "m": "0.511", "q1": "0.5121684678",
         "q2": "3.2338213736", "h": "0.1404219270", "e1": "0.773", "e2": "0.01404592165", "e3": "0.773",
         "mu1": "0.3178535346", "mu2": "0.1209173583", "c1": "0.065", "c2": "0.0509"}

X = sp.Symbol("X")
p = sp.symbols(" ".join(PARAM_NAMES))
a, K, r, m, q1, q2, h, e1, e2, e3, mu1, mu2, c1, c2 = p
g = r / (X + a) * (1 - X / K) * (X - m)
Delta = c1 * c2 + e3 * h ** 2
chi = (e1 * c2 * q1 ** 2 + e2 * c1 * q2 ** 2 + h * q1 * q2 * (e1 * e3 - e2)) / Delta
nu = (mu1 * (q1 * c2 + q2 * e3 * h) + mu2 * (q2 * c1 - q1 * h)) / Delta
F = g - (chi * X - nu)
A1 = e1 * q1 * X - mu1
A2 = e2 * q2 * X - mu2
Yx = (c2 * A1 - h * A2) / Delta
Zx = (e3 * h * A1 + c1 * A2) / Delta
s = -sp.diff(g, X)
beta12 = 1 + e1 * q1 ** 2 / (s * c1)
beta13 = 1 + e2 * q2 ** 2 / (s * c2)
beta23 = 1 + e3 * h ** 2 / (c1 * c2)
kappa = beta12 + beta13 + beta23 - 2 + h * q1 * q2 * (e1 * e3 - e2) / (s * c1 * c2)
T1 = (sp.sqrt(beta12) + sp.sqrt(beta13) + sp.sqrt(beta23)) ** 2
TARGETS = {"X": X, "Y": Yx, "Z": Zx, "s": s, "X_minus_m": X - m, "K_minus_X": K - X,
           "kappa_minus_T1": kappa - T1, "beta12": beta12, "beta13": beta13, "beta23": beta23, "kappa": kappa}
POSITIVE = ["Y", "Z", "s", "X_minus_m", "K_minus_X", "kappa_minus_T1"]
MODS = [{"sqrt": iv.sqrt}]


def lam(expr):
    return sp.lambdify((X,) + p, expr, modules=MODS)


F_l = lam(F)
F_X = lam(sp.diff(F, X))
F_p = [lam(sp.diff(F, pi)) for pi in p]
TOTAL = {n: (lam(G), lam(sp.diff(G, X)), [lam(sp.diff(G, pi)) for pi in p]) for n, G in TARGETS.items()}


def lo(x):
    return mp.mpf(x.a)


def hi(x):
    return mp.mpf(x.b)


def root_near_one(P):
    A_, B_, C_ = quadratic_coeffs(P)
    d = mp.sqrt(B_ * B_ - 4 * A_ * C_)
    return min(((B_ + d) / (2 * A_), (B_ - d) / (2 * A_)), key=lambda v: abs(v - 1))


def hull_X(center, box, half):
    """Verified enclosure of X over the box by a parametric interval Newton step on F(X, p) = 0:
    N = x~ - F(x~, P) / F_X(Xb, P), with F(x~, P) enclosed by its mean-value form in p.  If N lies in the
    interior of Xb, then for every p in P the equation F(., p) = 0 has exactly one root in Xb, and it lies in N."""
    xh = root_near_one(Params(*center))
    cen = [iv.mpf(v) for v in center]
    xt = iv.mpf(xh)
    Fx = F_l(xt, *cen)
    for i in range(14):
        Fx = Fx + F_p[i](xt, *box) * iv.mpf([-half[i], half[i]])
    for w in ("1e-6", "1e-5", "1e-4", "1e-3", "3e-3", "1e-2", "3e-2", "0.1"):
        Xb = iv.mpf([xh - mp.mpf(w), xh + mp.mpf(w)])
        fp = F_X(Xb, *box)
        if not (lo(fp) > 0 or hi(fp) < 0):
            continue
        Xn = xt - Fx / fp
        if lo(Xn) > lo(Xb) and hi(Xn) < hi(Xb):
            return Xn, xh
    return None, xh


def certify(task):
    try:
        return _certify(task)
    except Exception as exc:  # e.g. an interval sqrt of a sign-indefinite enclosure on a wide box
        return {"ok": False, "fail": [f"exception: {type(exc).__name__}"], "split": _fallback_split(task)}


def _fallback_split(task):
    """Coordinate with the largest first-order effect on X at the box centre (point evaluation)."""
    lows = [mp.mpf(v) for v in task[0]]
    highs = [mp.mpf(v) for v in task[1]]
    center = [(l + u) / 2 for l, u in zip(lows, highs)]
    half = [(u - l) / 2 for l, u in zip(lows, highs)]
    xh = root_near_one(Params(*center))
    cen = [iv.mpf(v) for v in center]
    fx = F_X(iv.mpf(xh), *cen)
    eff = [abs(lo(F_p[i](iv.mpf(xh), *cen)) / lo(fx)) * half[i] for i in range(14)]
    return int(max(range(14), key=lambda i: eff[i]))


def _certify(task):
    """task = (lows, highs) as decimal strings.  Returns dict with ok flag, enclosure bounds, split hint."""
    lows = [mp.mpf(v) for v in task[0]]
    highs = [mp.mpf(v) for v in task[1]]
    center = [(l + u) / 2 for l, u in zip(lows, highs)]
    half = [(u - l) / 2 for l, u in zip(lows, highs)]
    box = [iv.mpf([l, u]) for l, u in zip(lows, highs)]
    Xb, xh = hull_X(center, box, half)
    if Xb is None:
        return {"ok": False, "fail": ["X hull"], "split": _fallback_split(task)}
    cen = [iv.mpf(v) for v in center]
    Xi = iv.mpf([xh - mp.mpf("1e-8"), xh + mp.mpf("1e-8")])
    Xc = iv.mpf(xh) - F_l(iv.mpf(xh), *cen) / F_X(Xi, *cen)
    if not (lo(Xc) > lo(Xi) and hi(Xc) < hi(Xi)):
        return {"ok": False, "fail": ["centre Newton"], "split": 0}
    fxh = F_X(Xb, *box)
    if not (lo(fxh) > 0 or hi(fxh) < 0):
        return {"ok": False, "fail": ["F_X"], "split": _fallback_split(task)}
    dX = [-fp(Xb, *box) / fxh for fp in F_p]
    enc, contrib = {}, {}
    for name, (Gf, GXf, Gpf) in TOTAL.items():
        val = Gf(Xc, *cen)
        GX = GXf(Xb, *box)
        cs = []
        for i in range(14):
            dG = Gpf[i](Xb, *box) + GX * dX[i]
            term = dG * iv.mpf([-half[i], half[i]])
            cs.append(hi(abs(term)))
            val = val + term
        enc[name] = (lo(val), hi(val))
        contrib[name] = cs
    checks = {n: bool(enc[n][0] > 0) for n in POSITIVE}
    bl = [mp.nstr(enc[b][0], 40) for b in ("beta12", "beta13", "beta23")]
    L = None
    if all(mp.mpf(b) > 0 for b in bl):
        c = certify_threshold_logit(bl, ALPHA, dps=40)
        L = c["L"] if c.get("certified") else None
    checks["Talpha_minus_kappa"] = bool(L is not None and enc["kappa"][1] < L)
    fails = [k for k, v in checks.items() if not v]
    if fails:
        key = fails[0] if fails[0] != "Talpha_minus_kappa" else "kappa"
        split = int(max(range(14), key=lambda i: contrib[key][i]))
    else:
        split = -1
    return {"ok": not fails, "fail": fails, "split": split,
            "lb": {**{n: float(enc[n][0]) for n in POSITIVE},
                   "Talpha_minus_kappa": float(L - enc["kappa"][1]) if L is not None else None},
            "X": (float(enc["X"][0]), float(enc["X"][1])), "Y": (float(enc["Y"][0]), float(enc["Y"][1])),
            "Z": (float(enc["Z"][0]), float(enc["Z"][1])), "kappa": (float(enc["kappa"][0]), float(enc["kappa"][1]))}


def certify_delta(delta, pool, max_depth=24, max_boxes=200000):
    dl = mp.mpf(delta)
    c = [mp.mpf(TABLE[n]) for n in PARAM_NAMES]
    tasks = [([mp.nstr(v * (1 - dl), 45) for v in c], [mp.nstr(v * (1 + dl), 45) for v in c])]
    certified, lbmin, depth, t0 = [], {}, 0, time.time()
    Xr = [mp.inf, -mp.inf]; Yr = [mp.inf, -mp.inf]; Zr = [mp.inf, -mp.inf]; kr = [mp.inf, -mp.inf]
    while tasks:
        if depth > max_depth or len(tasks) > max_boxes:
            return {"delta": delta, "certified": False, "reason": f"depth {depth}, open boxes {len(tasks)}",
                    "seconds": round(time.time() - t0, 1)}
        res = pool.map(certify, tasks, chunksize=1)
        nxt = []
        for t, rr in zip(tasks, res):
            if rr["ok"]:
                certified.append(1)
                for k, v in rr["lb"].items():
                    lbmin[k] = min(lbmin.get(k, mp.inf), v)
                for rng, key in ((Xr, "X"), (Yr, "Y"), (Zr, "Z"), (kr, "kappa")):
                    rng[0] = min(rng[0], rr[key][0]); rng[1] = max(rng[1], rr[key][1])
                continue
            if rr["fail"] and rr["fail"][0] == "centre Newton":
                return {"delta": delta, "certified": False, "reason": "centre Newton failed"}
            i = rr["split"]
            lw, up = [mp.mpf(v) for v in t[0]], [mp.mpf(v) for v in t[1]]
            mid = (lw[i] + up[i]) / 2
            a1, b1 = list(t[0]), list(t[1]); b1[i] = mp.nstr(mid, 45)
            a2, b2 = list(t[0]), list(t[1]); a2[i] = mp.nstr(mid, 45)
            nxt += [(a1, b1), (a2, b2)]
        print(f"delta={delta} depth={depth} boxes={len(tasks)} certified_so_far={len(certified)} open={len(nxt)} "
              f"t={time.time() - t0:.0f}s", flush=True)
        tasks, depth = nxt, depth + 1
    return {"delta": delta, "certified": True, "n_boxes": len(certified), "max_depth": depth - 1,
            "min_lower_bounds": {k: float(v) for k, v in lbmin.items()},
            "X_range": [float(v) for v in Xr], "Y_range": [float(v) for v in Yr], "Z_range": [float(v) for v in Zr],
            "kappa_range": [float(v) for v in kr], "seconds": round(time.time() - t0, 1)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--workers", type=int, default=os.cpu_count())
    ap.add_argument("--deltas", default="0.005,0.01,0.02,0.03,0.05,0.075,0.1")
    ap.add_argument("--max-boxes", type=int, default=200000)
    args = ap.parse_args()
    out = {"method": __doc__.strip().splitlines()[0], "alpha": ALPHA, "center_table3": TABLE, "dps": 50, "runs": []}
    with Pool(args.workers) as pool:
        for d in args.deltas.split(","):
            res = certify_delta(d, pool, max_boxes=args.max_boxes)
            print(json.dumps(res), flush=True)
            out["runs"].append(res)
            path = os.path.join(HERE, "..", "data", "param_box_certificate.json")
            json.dump(out, open(path, "w"), indent=2)
            if not res["certified"]:
                break
    ok = [r["delta"] for r in out["runs"] if r["certified"]]
    out["largest_certified_delta"] = ok[-1] if ok else None
    json.dump(out, open(os.path.join(HERE, "..", "data", "param_box_certificate.json"), "w"), indent=2)


if __name__ == "__main__":
    main()
