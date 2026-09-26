"""Shared tools for the Wave-2 ecological figures: exact decimal design -> parameters (float or interval),
branch continuation in m, boundary tracing in the (m, K) plane, certification at points.

A design is a dict of DECIMAL STRINGS {b12, b13, b23, kappa, s, c1, c2, eta, xi, a, m, rhoK} with X = 1; the
biological parameters follow from the DA-06 realization and the DA-07 embedding, so the same strings define
the model exactly in float and in interval arithmetic.
"""
from __future__ import annotations

import json
import os

import mpmath as mp
import numpy as np
from mpmath import iv

from fdsn.c10_threshold import T1, invariants_batch, threshold_batch
from fdsn.double_allee import PARAM_NAMES, Params, coexistence_equilibria, embed_double_allee, realize_invariants, reduced_matrix, with_m

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "data")
ALPHA = 0.9


def params_from_design(d, conv=float):
    """conv: float, mp.mpf or iv.mpf (strings are converted exactly)."""
    one = conv("1")
    X = one
    b = (conv(d["b12"]), conv(d["b13"]), conv(d["b23"]))
    q1, q2, h, e1, e2, e3 = realize_invariants(*b, conv(d["kappa"]), s=conv(d["s"]), c1=conv(d["c1"]), c2=conv(d["c2"]), eta=conv(d["eta"]))
    m, a = conv(d["m"]), conv(d["a"])
    Kmax = X + (X - m) * (X + a) / (m + a)
    K = X + conv(d["rhoK"]) * (Kmax - X)
    P, Y, Z, Q, H = embed_double_allee(conv(d["s"]), X, m, a, K, q1, q2, h, e1, e2, e3, conv(d["c1"]), conv(d["c2"]), conv(d["xi"]))
    return P, (X, Y, Z)


def point(P, m, alpha=ALPHA):
    Pm = with_m(P, m)
    eqs = coexistence_equilibria(Pm)
    if not eqs:
        return None
    e = eqs[0]
    B = np.array(reduced_matrix(e["X"], e["Y"], e["Z"], Pm), float)
    p, mm, q, beta, kappa = invariants_batch(B[None])
    if not (p.min() > 0 and mm.min() > 0 and q[0] > 0):
        return {"m": m, "strictP": False, "X": e["X"], "Y": e["Y"], "Z": e["Z"], "n_eq": len(eqs)}
    tb = threshold_batch(beta, alpha)
    return {"m": m, "strictP": True, "X": e["X"], "Y": e["Y"], "Z": e["Z"], "s": float(-B[0, 0]), "beta": beta[0].tolist(), "kappa": float(kappa[0]),
            "T1": float(T1(beta[0])), "T_alpha": float(tb.T[0]), "x_star": tb.x[0].tolist(), "n_eq": len(eqs), "B": B.tolist()}


def bisect(f, a, b, n=80):
    fa = f(a)
    for _ in range(n):
        mid = 0.5 * (a + b); fm = f(mid)
        if fm is None or fa * fm <= 0:
            b = mid
        else:
            a, fa = mid, fm
    return 0.5 * (a + b)


def crossing_hp(design, lo, hi, dps=60):
    """Exact-formula 60-digit bisection of kappa - T1 = 0 along the branch (all non-m parameters fixed)."""
    from fdsn.double_allee import invariants_of_matrix, prey_roots, yz_of_x
    with mp.workdps(dps):
        P, _ = params_from_design(design, mp.mpf)
        def G(m):
            Pq = with_m(P, m); X = max(prey_roots(Pq)); Y, Z = yz_of_x(X, Pq)
            I = invariants_of_matrix(reduced_matrix(X, Y, Z, Pq)); b = I["beta"]
            return I["kappa"] - (mp.sqrt(b[0]) + mp.sqrt(b[1]) + mp.sqrt(b[2])) ** 2
        a_, b_ = mp.mpf(lo), mp.mpf(hi)
        for _ in range(200):
            mid = (a_ + b_) / 2
            if G(mid) * G(a_) <= 0:
                b_ = mid
            else:
                a_ = mid
        return mp.nstr((a_ + b_) / 2, 50), mp.nstr(G((a_ + b_) / 2), 5)


def classify_pt(P, m, K=None, alpha=ALPHA):
    """0 classical, 1 fractional-only, 2 unstable/non-strict-P, 3 infeasible."""
    v = P.as_list(); Pq = Params(*v); Pq = with_m(Pq, m)
    if K is not None:
        Pq = Params(*[K if n == "K" else getattr(Pq, n) for n in PARAM_NAMES])
    r = point(Pq, m, alpha)
    if r is None:
        return 3
    if not r["strictP"]:
        return 2
    return 0 if r["kappa"] < r["T1"] else (1 if r["kappa"] < r["T_alpha"] else 2)


def trace_boundaries(P, Ks, m_lo=0.005, m_hi=0.99, n_scan=400, alpha=ALPHA):
    """For each K: scan m, find the class transitions and refine each by bisection on the defining exact
    function (kappa-T1 for classical|fractional, T_alpha-kappa for fractional|unstable, feasibility otherwise).
    Returns dict of boundary curves {name: [(K, m), ...]}."""
    curves = {"classical_fractional": [], "fractional_unstable": [], "feasibility_low": [], "feasibility_high": []}
    ms = np.linspace(m_lo, m_hi, n_scan)
    for K in Ks:
        Pk = Params(*[K if n == "K" else getattr(P, n) for n in PARAM_NAMES])
        cls = np.array([classify_pt(Pk, m) for m in ms])
        feas = cls < 3
        if not feas.any():
            continue
        idx = np.nonzero(feas)[0]
        # feasibility edges (bisection on "feasible" predicate)
        if idx[0] > 0:
            curves["feasibility_low"].append((K, bisect(lambda m: 1.0 if classify_pt(Pk, m) < 3 else -1.0, ms[idx[0]], ms[idx[0] - 1])))
        else:
            curves["feasibility_low"].append((K, ms[0]))
        if idx[-1] < n_scan - 1:
            curves["feasibility_high"].append((K, bisect(lambda m: 1.0 if classify_pt(Pk, m) < 3 else -1.0, ms[idx[-1]], ms[idx[-1] + 1])))
        for i in range(len(ms) - 1):
            a, b = cls[i], cls[i + 1]
            if a == b or a == 3 or b == 3:
                continue
            if {a, b} == {0, 1}:
                f = lambda m: (lambda r: r["kappa"] - r["T1"])(point(Pk, m))
                curves["classical_fractional"].append((K, bisect(f, ms[i], ms[i + 1])))
            elif {a, b} == {1, 2}:
                f = lambda m: (lambda r: (r["T_alpha"] - r["kappa"]) if r["strictP"] else -1.0)(point(Pk, m))
                curves["fractional_unstable"].append((K, bisect(f, ms[i], ms[i + 1])))
    return curves


def save_json(name, obj):
    with open(os.path.join(DATA, name), "w") as f:
        json.dump(obj, f, indent=1, default=str)
