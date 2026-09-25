"""Wave 2 P6 (optional, exploratory) — n=4: two directed 3-cycles sharing an edge.

Family.  Nodes 1..4, unit negative diagonal, cycle A = 1->2->3->1 and cycle B = 1->2->4->1
sharing the edge 1->2.  Positive diagonal similarity normalises a21 = a32 = a42 = 1, leaving
    a13 = -s,  a14 = -t            (s, t > 0: negative-feedback cycles; s, t > -1 allowed).
C-16 invariants (all pair loops vanish):
    beta_ij = 1 (6 pairs), beta_123 = 1+s, beta_124 = 1+t, beta_134 = beta_234 = 1, kappa4 = 1+s+t,
so the family is the exact 2-parameter slice of the 4x4 invariant space with no reciprocal
pairs and two loaded triples; by C-16 the whole positive-diagonal orbit is captured by the
normalised quartic on the 3-simplex (x_i = d_i / sum d):
    q_x(l) = l^4 + l^3 + e2(x) l^2 + [e3(x) + s x1x2x3 + t x1x2x4] l + (1+s+t) x1x2x3x4.
Membership in F_alpha  <=>  q_x is Matignon-stable for every x in the open simplex.
Symmetry: (s,t) <-> (t,s) (swap nodes 3,4).  Necessary conditions from the 3x3 principal
blocks (C-10 on the Siami slice): s < R3(alpha)^3 and t < R3(alpha)^3 (alpha > 2/3); at
alpha = 1: s < 8, t < 8 (Cain).  Low-order: Kellogg wedge guarantees F_alpha for alpha <= 1/2 only.

Computations (NUMERICAL, float; boundary points refined to ~1e-10 and cross-checked by
direct eigenvalues of D A at the worst diagonal):
  1. boundary t*(s) = sup{t : (s,t) in F_alpha} for alpha in {1, .99, .95, .9, .85, .8, .75, .7}
     by bisection, each membership test = global minimisation of the Matignon root margin of
     q_x over the simplex (grid + Nelder-Mead in logit coordinates);
  2. tests of candidate closed forms: s + t = R^3, (1+s)(1+t) = 1+R^3, s^{1/3}+t^{1/3} = R, ...;
  3. the classical alpha=1 boundary via Routh-Hurwitz  c(e2-c) > (1+s+t) P  and its minimiser;
  4. convexity of the region in (s,t) and in (s^{1/3}, t^{1/3}).
Outputs: N4_SHARED_EDGE_DATA.json, N4_SHARED_EDGE_BOUNDARY.csv (report written separately).
"""
from __future__ import annotations

import csv
import os
import sys

import numpy as np
from scipy.optimize import minimize

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from w2_common import RESULTS, Timer, dump, git_sha, log, pool, stamp  # noqa: E402

from fdsn.c10_threshold import siami_R3  # noqa: E402

ALPHAS = [1.0, 0.99, 0.95, 0.9, 0.85, 0.8, 0.75, 0.7]


def A_st(s, t):
    A = -np.eye(4)
    A[1, 0] = 1.0; A[2, 1] = 1.0; A[0, 2] = -s
    A[3, 1] = 1.0; A[0, 3] = -t
    return A


def quartic_coeffs(x, s, t):
    """x (...,4) -> coefficients (1, 1, c2, c3, c4) of the normalised quartic."""
    x1, x2, x3, x4 = x[..., 0], x[..., 1], x[..., 2], x[..., 3]
    e2 = x1 * x2 + x1 * x3 + x1 * x4 + x2 * x3 + x2 * x4 + x3 * x4
    e3 = x1 * x2 * x3 + x1 * x2 * x4 + x1 * x3 * x4 + x2 * x3 * x4
    c3 = e3 + s * x1 * x2 * x3 + t * x1 * x2 * x4
    c4 = (1 + s + t) * x1 * x2 * x3 * x4
    return e2, c3, c4


def margin_batch(x, s, t, alpha):
    e2, c3, c4 = quartic_coeffs(x, s, t)
    n = e2.shape[0]
    C = np.zeros((n, 5)); C[:, 0] = 1; C[:, 1] = 1; C[:, 2] = e2; C[:, 3] = c3; C[:, 4] = c4
    # companion-matrix eigenvalues, batched
    M = np.zeros((n, 4, 4)); M[:, 0, :] = -C[:, 1:]; M[:, 1, 0] = M[:, 2, 1] = M[:, 3, 2] = 1
    lam = np.linalg.eigvals(M)
    return np.abs(np.angle(lam)).min(axis=1) - alpha * np.pi / 2


def softmax3(y):
    z = np.concatenate([y, np.zeros(y.shape[:-1] + (1,))], -1)
    z = z - z.max(-1, keepdims=True); e = np.exp(z)
    return e / e.sum(-1, keepdims=True)


_GRID = None


def grid():
    global _GRID
    if _GRID is None:
        g = np.linspace(-6, 6, 25)
        Y = np.stack(np.meshgrid(g, g, g, indexing="ij"), -1).reshape(-1, 3)
        _GRID = Y
    return _GRID


def min_margin(s, t, alpha, n_local=4):
    Y = grid()
    m = margin_batch(softmax3(Y), s, t, alpha)
    order = np.argsort(m)[:n_local]
    best = (m[order[0]], softmax3(Y[order[0]]))
    for i in order:
        r = minimize(lambda y: margin_batch(softmax3(y[None]), s, t, alpha)[0], Y[i], method="Nelder-Mead",
                     options={"xatol": 1e-9, "fatol": 1e-13, "maxfev": 4000})
        if r.fun < best[0]:
            best = (r.fun, softmax3(r.x))
    return best


def in_F(s, t, alpha):
    return min_margin(s, t, alpha)[0] > 0


def boundary_t(s, alpha, t_hi):
    if not in_F(s, 0.0, alpha):
        return None
    lo, hi = 0.0, t_hi
    if in_F(s, hi, alpha):
        return hi                         # not reached within the search range
    for _ in range(45):
        mid = 0.5 * (lo + hi)
        if in_F(s, mid, alpha):
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def direct_check(s, t, alpha):
    """Independent route: eigenvalues of D A at the worst simplex point mapped back to D."""
    m, x = min_margin(s, t, alpha)
    D = np.diag(x)                       # p_i = 1 so d_i = x_i
    ev = np.linalg.eigvals(D @ A_st(s, t))
    return m, np.abs(np.angle(ev)).min() - alpha * np.pi / 2


def _job(args):
    alpha, s = args
    R3 = 2.0 if alpha == 1.0 else siami_R3(alpha)
    tb = boundary_t(s, alpha, 1.5 * R3 ** 3)
    if tb is None:
        return alpha, s, None, None, None
    m_in, dm_in = direct_check(s, tb * (1 - 1e-6), alpha)
    m_out, dm_out = direct_check(s, tb * (1 + 1e-6), alpha)
    return alpha, s, tb, (m_in, dm_in), (m_out, dm_out)


def routh_hurwitz_min(s, t):
    """alpha = 1: min over simplex of R(x) = c3 (e2 - c3) / P - (1+s+t); D-stable iff > 0."""
    def f(y):
        x = softmax3(y[None])
        e2, c3, c4 = quartic_coeffs(x, s, t)
        P = np.prod(x, -1)
        return float((c3 * (e2 - c3) / P - (1 + s + t))[0])
    Y = grid()
    x = softmax3(Y)
    e2, c3, c4 = quartic_coeffs(x, s, t)
    vals = c3 * (e2 - c3) / np.prod(x, -1) - (1 + s + t)
    i = int(np.argmin(vals))
    r = minimize(f, Y[i], method="Nelder-Mead", options={"xatol": 1e-10, "fatol": 1e-14, "maxfev": 5000})
    return r.fun, softmax3(r.x).tolist()


def main():
    T = Timer()
    with pool(12) as P:
        jobs = []
        for a in ALPHAS:
            R3 = 2.0 if a == 1.0 else siami_R3(a)
            smax = R3 ** 3
            ss = np.concatenate([[0.0], np.linspace(0.02, 0.98, 25) * smax, [smax * 0.995]])
            jobs += [(a, float(s)) for s in ss]
        res = P.map(_job, jobs, chunksize=1)
    rows, data = [], {}
    for a, s, tb, chk_in, chk_out in res:
        R3 = 2.0 if a == 1.0 else siami_R3(a)
        rows.append([a, R3, R3 ** 3, s, tb if tb is not None else "", chk_in[0] if chk_in else "", chk_in[1] if chk_in else "",
                     chk_out[0] if chk_out else "", chk_out[1] if chk_out else ""])
        data.setdefault(str(a), []).append((s, tb))
    with open(os.path.join(RESULTS, "N4_SHARED_EDGE_BOUNDARY.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["alpha", "R3", "R3^3", "s", "t_boundary", "margin_simplex_inside", "margin_direct_eig_inside",
                    "margin_simplex_outside", "margin_direct_eig_outside"])
        w.writerows(rows)
    # candidate closed forms on the boundary points (s, t*)
    fits = {}
    for a, pts in data.items():
        R3 = 2.0 if float(a) == 1.0 else siami_R3(float(a)); R = R3 ** 3
        P_ = [(s, t) for s, t in pts if t is not None and t < 1.49 * R]
        if not P_:
            continue
        S = np.array([p[0] for p in P_]); Tt = np.array([p[1] for p in P_])
        cands = {
            "s+t=R3^3": (S + Tt) / R - 1,
            "(1+s)(1+t)=1+R3^3": (1 + S) * (1 + Tt) / (1 + R) - 1,
            "s^(1/3)+t^(1/3)=R3": (np.cbrt(S) + np.cbrt(Tt)) / R3 - 1,
            "s^(2/3)+t^(2/3)=R3^2": (np.cbrt(S) ** 2 + np.cbrt(Tt) ** 2) / R3 ** 2 - 1,
            "max(s,t)=R3^3": np.maximum(S, Tt) / R - 1,
            "s^2+t^2=R3^6": (S ** 2 + Tt ** 2) / R ** 2 - 1,
        }
        fits[a] = {k: {"max_abs_rel_dev": float(np.abs(v).max()), "mean_rel_dev": float(v.mean())} for k, v in cands.items()}
        # convexity of the region: t*(s) concave <=> region convex (given symmetry). second differences
        o = np.argsort(S); d2 = np.diff(Tt[o], 2)
        fits[a]["t_star_concave(second_diff<=0)"] = bool(np.all(d2 <= 1e-6 * R))
        fits[a]["t_star_at_s0_over_R3^3"] = float(Tt[o][0] / R)
        fits[a]["symmetric_point_s=t"] = None
        # symmetric boundary point: solve t*(s)=s by interpolation
        g = Tt[o] - S[o]
        k = np.nonzero(np.diff(np.sign(g)))[0]
        if k.size:
            i = k[0]; ss = S[o][i] - g[i] * (S[o][i + 1] - S[o][i]) / (g[i + 1] - g[i])
            fits[a]["symmetric_point_s=t"] = float(ss)
            fits[a]["symmetric_point_over_R3^3"] = float(ss / R)
            fits[a]["(1+2s_sym)_over_(1+R3^3)"] = float((1 + 2 * ss) / (1 + R))
    # alpha = 1 Routh-Hurwitz minimiser at a few boundary points
    rh = []
    for s, t in data["1.0"]:
        if t is not None and t < 11.9:
            val, x = routh_hurwitz_min(s, t)
            rh.append({"s": s, "t": t, "RH_min_over_simplex": val, "x_min": x})
    out = stamp({"git_sha": git_sha(), "alphas": ALPHAS, "candidate_closed_forms": fits, "routh_hurwitz_alpha1": rh,
                 "boundary_points": {a: [(s, t) for s, t in pts] for a, pts in data.items()},
                 "direct_eig_consistency": {"n": sum(1 for r in res if r[2] is not None),
                                            "inside_all_positive_both_routes": all(r[3][0] > 0 and r[3][1] > 0 for r in res if r[2] is not None),
                                            "outside_all_negative_both_routes": all(r[4][0] < 0 and r[4][1] < 0 for r in res if r[2] is not None),
                                            "max_abs_route_difference": max(abs(r[3][0] - r[3][1]) for r in res if r[2] is not None)},
                 "wall_seconds": T(), "label": "NUMERICAL (float; boundary bisection 1e-13 relative; grid 25^3 + Nelder-Mead)"})
    dump("N4_SHARED_EDGE_DATA.json", out)
    print({a: {k: v for k, v in f.items() if not isinstance(v, dict) or v["max_abs_rel_dev"] < 0.05} for a, f in fits.items()})


if __name__ == "__main__":
    main()
