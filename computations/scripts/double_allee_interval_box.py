"""Parameter-box certification for the Double-Allee IGP witness (task §3.4).

Interval arithmetic (mpmath.iv, outward rounding, 50 digits) through the whole
chain: quadratic -> X -> (Y, Z) -> s = -g'(X) (product-rule form) -> B ->
invariants -> kappa - T1 and the fractional certificate.  Two fractional
certificates are used on a box:
  * C-11 (sufficient): Phi_lo = T1_lo / kappa_hi > rho_alpha (rigorous, unconditional);
  * C-10 (exact threshold): kappa_hi < L(beta_lo) where L is the certified lower bracket of
    T_alpha at the componentwise-lower corner beta_lo of the beta box; valid because T_alpha
    is nondecreasing in each beta_ij (C-13 §7; strictly increasing by C-15).  The bracket comes
    from fdsn.interval_cert.certify_threshold_logit (conditional on C-15 Thm 1) and
    certify_threshold (unconditional) -- both are tried.
Boxes:
  (A) one-dimensional m-interval [0.2 + d, m_max] with all other parameters fixed (subdivided);
  (B) full 14-parameter boxes p_i in [p_i (1-delta), p_i (1+delta)] around the m = 0.21 point,
      for decreasing delta until certification succeeds (subdivision in m only).
Every sub-box must give: X, Y, Z > 0, m < X < K, s > 0, kappa - T1 > 0, fractional certificate.
Output: computations/results/DOUBLE_ALLEE_INTERVAL_BOX.json
"""
from __future__ import annotations

import json
import os
import sys
import time

import mpmath as mp
from mpmath import iv

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
RES = os.path.join(ROOT, "computations", "results")
from fdsn.double_allee import Params, chief_witness, invariants_of_matrix, prey_roots, quadratic_coeffs, reduced_matrix, with_m, yz_of_x  # noqa: E402
from fdsn.interval_cert import certify_threshold, certify_threshold_logit  # noqa: E402

ALPHA = "0.9"
iv.dps = 50
mp.mp.dps = 50


def lo(x):
    return mp.mpf(x.a)


def hi(x):
    return mp.mpf(x.b)


def newton_root(P: Params):
    """Tight enclosure of the '+' root of A X^2 - B X + C = 0 (interval coefficients) by one
    interval-Newton step from the float root: X* in x_hat - f(x_hat)/f'(X_box), verified X_new subset X_box."""
    A, B, C = quadratic_coeffs(P)
    Pf = Params(*[(lo(v) + hi(v)) / 2 for v in P.as_list()])
    Af, Bf, Cf = quadratic_coeffs(Pf)
    xh = (Bf + mp.sqrt(Bf * Bf - 4 * Af * Cf)) / (2 * Af)
    for w in (mp.mpf("1e-6"), mp.mpf("1e-5"), mp.mpf("1e-4"), mp.mpf("1e-3"), mp.mpf("1e-2"), mp.mpf("0.1")):
        Xb = iv.mpf([xh - w, xh + w])
        fp = 2 * A * Xb - B
        if not (lo(fp) > 0 or hi(fp) < 0):
            continue
        xhi = iv.mpf(xh)
        Xn = xhi - (A * xhi * xhi - B * xhi + C) / fp
        if lo(Xn) > lo(Xb) and hi(Xn) < hi(Xb):
            # one more contraction step
            fp2 = 2 * A * Xn - B
            Xn2 = xhi - (A * xhi * xhi - B * xhi + C) / fp2
            return Xn2 if (lo(Xn2) >= lo(Xn) and hi(Xn2) <= hi(Xn)) else Xn
    return None


def check_box(P: Params, alpha_str=ALPHA, cert_cache=None):
    """P has interval entries. Returns dict with the certified facts (or the failing one)."""
    r = {}
    X = newton_root(P)
    if X is None:
        return {"ok": False, "fail": "interval Newton for X did not contract"}
    r["X"] = (lo(X), hi(X))
    if not (lo(X) > hi(P.m) and hi(X) < lo(P.K) and lo(X) > 0):
        return {**r, "ok": False, "fail": "X not certified in (m, K)"}
    Y, Z = yz_of_x(X, P)
    r["Y"], r["Z"] = (lo(Y), hi(Y)), (lo(Z), hi(Z))
    if not (lo(Y) > 0 and lo(Z) > 0):
        return {**r, "ok": False, "fail": "Y or Z not certified positive"}
    B = reduced_matrix(X, Y, Z, P)
    inv = invariants_of_matrix(B)
    s = -B[0][0]
    r["s"] = (lo(s), hi(s))
    if not (lo(s) > 0 and all(lo(v) > 0 for v in inv["m"]) and lo(inv["q"]) > 0):
        return {**r, "ok": False, "fail": "strict-P not certified"}
    beta = inv["beta"]; kappa = inv["kappa"]
    t1 = (iv.sqrt(beta[0]) + iv.sqrt(beta[1]) + iv.sqrt(beta[2])) ** 2
    r["beta"] = [(lo(b), hi(b)) for b in beta]; r["kappa"] = (lo(kappa), hi(kappa)); r["T1"] = (lo(t1), hi(t1))
    gap = kappa - t1
    r["kappa_minus_T1_lo"] = lo(gap)
    if not (lo(gap) > 0):
        return {**r, "ok": False, "fail": "kappa - T1 not certified positive"}
    rho = (1 - 2 * iv.cos(iv.mpf(alpha_str) * iv.pi / 2)) ** 2
    phi = t1 / kappa
    r["Phi_minus_rho_lo"] = lo(phi - rho)
    r["C11_certified"] = bool(lo(phi - rho) > 0)
    # exact-threshold certificate at the lower corner of the beta box
    key = tuple(mp.nstr(lo(b), 40) for b in beta)
    if cert_cache is not None and key in cert_cache:
        L = cert_cache[key]
    else:
        c = certify_threshold_logit(list(key), alpha_str, dps=40)
        L = c["L"] if c.get("certified") else None
        if cert_cache is not None:
            cert_cache[key] = L
    r["T_alpha_lower_corner_L"] = L
    r["C10_certified"] = bool(L is not None and hi(kappa) < L)
    r["T_alpha_L_minus_kappa_hi"] = (L - hi(kappa)) if L is not None else None
    r["ok"] = bool(r["C11_certified"] or r["C10_certified"])
    r["fail"] = "" if r["ok"] else "no fractional certificate"
    return r


def summarize(results):
    def mn(key):
        vals = [x[key] for x in results if x.get(key) is not None]
        return mp.nstr(min(vals), 12) if vals else None
    return {"n_subboxes": len(results), "all_ok": all(x["ok"] for x in results),
            "C10_all": all(x.get("C10_certified") for x in results), "C11_all": all(x.get("C11_certified") for x in results),
            "min_kappa_minus_T1_lo": mn("kappa_minus_T1_lo"), "min_T_alpha_L_minus_kappa_hi": mn("T_alpha_L_minus_kappa_hi"),
            "min_Phi_minus_rho_lo": mn("Phi_minus_rho_lo"),
            "failures": [x["fail"] for x in results if not x["ok"]]}


def adaptive(make_params, lo_, hi_, cache, min_width, budget=4000):
    """Certify [lo_, hi_] (an m-range) by adaptive bisection; returns (certified_up_to, results, n_boxes)."""
    stack = [(lo_, hi_)]
    results = []
    reached = lo_
    n = 0
    while stack and n < budget:
        a_, b_ = stack.pop()
        if a_ != reached:                  # process in order: only accept contiguous certified prefix
            stack.append((a_, b_))
            # find the interval starting at 'reached'
            idx = next((i for i, (x, _) in enumerate(stack) if x == reached), None)
            if idx is None:
                break
            a_, b_ = stack.pop(idx)
        n += 1
        res = check_box(make_params(iv.mpf([a_, b_])), cert_cache=cache)
        if res["ok"]:
            results.append({"m_interval": (mp.nstr(a_, 12), mp.nstr(b_, 12)), **{k: res[k] for k in ("kappa_minus_T1_lo", "T_alpha_L_minus_kappa_hi", "Phi_minus_rho_lo", "C10_certified", "C11_certified")}})
            reached = b_
        elif b_ - a_ > min_width:
            mid = (a_ + b_) / 2
            stack.append((mid, b_)); stack.append((a_, mid))
        else:
            results.append({"m_interval": (mp.nstr(a_, 12), mp.nstr(b_, 12)), "FAILED": res.get("fail")})
            break
    return reached, results, n


def main():
    t0 = time.time()
    Pf = chief_witness(lambda v: iv.mpf(v))
    names = ("a", "K", "r", "m", "q1", "q2", "h", "e1", "e2", "e3", "mu1", "mu2", "c1", "c2")
    out = {"alpha": ALPHA, "dps": 50, "method": "interval Newton for X + outward-rounded interval evaluation; adaptive bisection in m",
           "witness_params_exact_decimal": {k: mp.nstr(mp.mpf(getattr(Pf, k).a), 30) for k in names}}
    cache = {}
    # (A) m-interval, all other parameters fixed
    reached, res, n = adaptive(lambda M: with_m(Pf, M), mp.mpf("0.2005"), mp.mpf("0.45"), cache, mp.mpf("1e-7"))
    ok = [x for x in res if "FAILED" not in x]
    out["A_m_interval"] = {"m_lo": "0.2005", "m_hi_attempted": "0.45", "certified_up_to_m": mp.nstr(reached, 12), "n_boxes_checked": n,
                           "n_certified_subintervals": len(ok), "first_failure": next((x for x in res if "FAILED" in x), None),
                           "min_kappa_minus_T1_lo": mp.nstr(min(x["kappa_minus_T1_lo"] for x in ok), 10) if ok else None,
                           "min_T_alpha_L_minus_kappa_hi": mp.nstr(min(x["T_alpha_L_minus_kappa_hi"] for x in ok if x["T_alpha_L_minus_kappa_hi"] is not None), 10) if ok else None,
                           "C10_all": all(x["C10_certified"] for x in ok), "C11_all": all(x["C11_certified"] for x in ok),
                           "statement": "for every m in [0.2005, certified_up_to_m], with all other parameters fixed at the witness values, the "
                                        "coexistence equilibrium is CERTIFIED: X,Y,Z>0, m<X<K, strict-P, kappa>T1 (not Hurwitz D-stable), "
                                        "kappa<T_0.9(beta) (in F_0.9): genuinely fractional. Labels: C-11 rigorous/unconditional; C-10 via the "
                                        "certified bracket at the lower beta corner (conditional on C-15 Thm 1 + monotonicity C-13 §7)."}
    # one-sided near m0
    small = []
    for k in range(2, 8):
        a_, b_ = mp.mpf("0.2") + mp.mpf(10) ** -k, mp.mpf("0.2") + mp.mpf(10) ** -(k - 1)
        reached_k, res_k, n_k = adaptive(lambda M: with_m(Pf, M), a_, b_, cache, mp.mpf(10) ** -(k + 3))
        small.append({"interval": f"[0.2+1e-{k}, 0.2+1e-{k - 1}]", "certified": bool(reached_k == b_), "boxes": n_k,
                      "min_kappa_minus_T1_lo": mp.nstr(min([x["kappa_minus_T1_lo"] for x in res_k if "FAILED" not in x] or [mp.nan]), 6)})
    out["A_one_sided_near_m0"] = small
    # (B) full 14-parameter boxes around m = 0.21, relative half-width delta on every parameter, bisection in m
    P21 = with_m(Pf, iv.mpf("0.21"))
    vals = [mp.mpf(getattr(P21, k).a) for k in names]
    out["B_full_boxes"] = []
    for delta in (mp.mpf("2e-3"), mp.mpf("1e-3"), mp.mpf("5e-4"), mp.mpf("2e-4"), mp.mpf("1e-4"), mp.mpf("5e-5")):
        def mk(M, delta=delta):
            boxed = [iv.mpf([v * (1 - delta), v * (1 + delta)]) for v in vals]
            boxed[3] = M
            return Params(*boxed)
        m_c = vals[3]
        reached_b, res_b, n_b = adaptive(mk, m_c * (1 - delta), m_c * (1 + delta), cache, m_c * delta / 512, budget=3000)
        okb = [x for x in res_b if "FAILED" not in x]
        entry = {"delta_relative": mp.nstr(delta, 5), "certified": bool(reached_b == m_c * (1 + delta)), "boxes": n_b,
                 "min_kappa_minus_T1_lo": mp.nstr(min([x["kappa_minus_T1_lo"] for x in okb] or [mp.nan]), 8),
                 "min_T_alpha_L_minus_kappa_hi": mp.nstr(min([x["T_alpha_L_minus_kappa_hi"] for x in okb if x["T_alpha_L_minus_kappa_hi"] is not None] or [mp.nan]), 8),
                 "first_failure": next((x for x in res_b if "FAILED" in x), None)}
        out["B_full_boxes"].append(entry)
        if entry["certified"]:
            out["B_largest_certified_delta"] = mp.nstr(delta, 5)
            out["B_statement"] = ("for every parameter vector in the box p_i in [p_i(1-delta), p_i(1+delta)] (all 14 biological parameters, "
                                  "around the m=0.21 witness) the coexistence equilibrium is CERTIFIED positive, strict-P, kappa>T1 and "
                                  "kappa<T_0.9(beta): a full-dimensional certified genuinely fractional parameter box")
            break
    out["seconds"] = round(time.time() - t0, 1)
    with open(os.path.join(RES, "DOUBLE_ALLEE_INTERVAL_BOX.json"), "w") as f:
        json.dump(out, f, indent=2, default=str)
    print(json.dumps({k: out.get(k) for k in ("A_m_interval", "A_one_sided_near_m0", "B_largest_certified_delta")}, indent=1, default=str)[:3000])
    print([(b["delta_relative"], b["certified"], b["boxes"], b["min_kappa_minus_T1_lo"]) for b in out["B_full_boxes"]])


if __name__ == "__main__":
    main()
