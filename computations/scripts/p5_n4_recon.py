"""P5 — n = 4 reconnaissance (EXPLORATORY; nothing here is a theorem).

Direct Matignon margin minimised over positive diagonal D (3 free log-ratios,
LAPACK eigenvalues, grid + pattern search), for alpha and for alpha = 1
(Hurwitz).  "Genuinely fractional" = min_D margin_alpha > 0 and
min_D margin_1 < 0.

Studies
  S1 single negative-feedback 4-cycle  -I + gamma C4  vs Siami R4(alpha) = sin t/sin(t - pi/4)
  S2 two 3-cycles sharing the edge 1->2 (cycles 1-2-3-1 and 1-2-4-1)
  S3 cactus: 3-cycle (1,2,3) + reciprocal pair (1,4)
  S4 block coupling: 3x3 cyclic witness (+) node 4, two-way coupling eps
  S5 random strict-P 4x4 (entry space), fraction genuinely fractional per alpha,
     and the alpha <= 1/2 Kellogg regime
  S6 orbit-coefficient reduction check: min over D of eigen-margin == min over
     the 3-simplex of the root margin of the normalised quartic built from the
     11 normalised principal-minor invariants
  S7 adversarial search: maximise the robust genuinely-fractional score
     min(m_alpha, -m_1) over normalised 4x4 matrices (differential evolution)
Outputs: computations/results/N4_RECON.json (+ report written by hand from it)
"""
from __future__ import annotations

import itertools
import os
import sys

import numpy as np
from scipy.optimize import differential_evolution

sys.path.insert(0, os.path.dirname(__file__))
from _common import Timer, dump, log, peak_rss_mb, pool  # noqa: E402

from fdsn.direct_margin import min_margin  # noqa: E402

HW, STEP = 9.0, 0.75


def mm(As, alpha, hw=HW, step=STEP, n_starts=3):
    return min_margin(np.asarray(As, float), alpha, half_width=hw, step=step, n_starts=n_starts)["margin"]


def R4(alpha):
    t = alpha * np.pi / 2
    return np.sin(t) / np.sin(t - np.pi / 4)


def cyc4(g):
    A = -np.eye(4)
    A[1, 0] = A[2, 1] = A[3, 2] = g
    A[0, 3] = -g
    return A


def s1():
    out = []
    for a in (0.55, 0.6, 2 / 3, 0.75, 0.9, 0.99):
        gs = np.linspace(1.0, min(R4(a) * 1.3, 12), 60)
        m = mm([cyc4(g) for g in gs], a)
        h = mm([cyc4(g) for g in gs], 1.0)
        # first sign change of direct margin
        i = np.nonzero(m < 0)[0]
        gcrit = gs[i[0] - 1:i[0] + 1].tolist() if i.size else None
        out.append({"alpha": a, "R4": float(R4(a)), "direct_crossing_bracket": gcrit,
                    "hurwitz_crossing_bracket": gs[np.nonzero(h < 0)[0][0] - 1:np.nonzero(h < 0)[0][0] + 1].tolist(),
                    "sqrt2": float(np.sqrt(2))})
    return out


def two_cycles(g1, g2):
    A = -np.eye(4)
    A[1, 0] = 1.0          # shared edge 1->2 (a_21)
    A[2, 1] = g1; A[0, 2] = -g1 ** 2      # cycle 1->2->3->1, product -g1^3
    A[3, 1] = g2; A[0, 3] = -g2 ** 2      # cycle 1->2->4->1, product -g2^3
    return A


def cactus(g, c):
    A = -np.eye(4)
    A[1, 0] = g; A[2, 1] = g; A[0, 2] = -g       # 3-cycle, product -g^3
    A[0, 3] = c; A[3, 0] = -c                    # antagonistic pair (1,4)
    return A


def block(g, eps, s):
    A = -np.eye(4)
    A[1, 0] = g; A[2, 1] = g; A[0, 2] = -g
    A[3, 0] = eps; A[0, 3] = s * eps
    return A


def phase_scan(builder, xs, ys, alphas):
    res = {}
    for a in alphas:
        pts = list(itertools.product(xs, ys))
        As = [builder(x, y) for x, y in pts]
        mf = mm(As, a)
        mh = mm(As, 1.0)
        gf = (mf > 1e-9) & (mh < -1e-9)
        res[str(a)] = {"n": len(pts), "genuinely_fractional": int(gf.sum()),
                       "F_member": int((mf > 1e-9).sum()), "hurwitz_D_stable": int((mh > 1e-9).sum()),
                       "best_gf_point": list(pts[int(np.argmax(np.where(gf, np.minimum(mf, -mh), -np.inf)))]) if gf.any() else None,
                       "best_gf_score": float(np.max(np.where(gf, np.minimum(mf, -mh), -np.inf))) if gf.any() else None}
    return res


def strictP(A):
    n = A.shape[0]
    M = -A
    for k in range(1, n + 1):
        for S in itertools.combinations(range(n), k):
            if np.linalg.det(M[np.ix_(S, S)]) <= 0:
                return False
    return True


def _s5_job(args):
    seed, n = args
    rng = np.random.default_rng(seed)
    As = []
    while len(As) < n:
        A = rng.normal(scale=10 ** rng.uniform(-0.5, 0.7), size=(4, 4))
        A[np.diag_indices(4)] = -np.exp(rng.normal(size=4))
        if strictP(A):
            As.append(A)
    As = np.array(As)
    out = {"mh": mm(As, 1.0)}
    for a in (0.3, 0.5, 0.55, 0.6, 2 / 3, 0.75, 0.9, 0.99):
        out[a] = mm(As, a)
    return out


def s5(P):
    res = P.map(_s5_job, [(900 + j, 250) for j in range(32)])
    mh = np.concatenate([r["mh"] for r in res])
    out = {"n": int(mh.size), "hurwitz_D_stable_fraction": float(np.mean(mh > 1e-9))}
    for a in (0.3, 0.5, 0.55, 0.6, 2 / 3, 0.75, 0.9, 0.99):
        m = np.concatenate([r[a] for r in res])
        out[f"alpha={a:.4g}"] = {"F_fraction": float(np.mean(m > 1e-9)),
                                 "genuinely_fractional_fraction": float(np.mean((m > 1e-9) & (mh < -1e-9))),
                                 "non_F_count": int(np.sum(m < -1e-9)), "min_margin": float(m.min())}
    return out


def quartic_root_margin(coeffs, alpha):
    r = np.roots(coeffs)
    return np.min(np.abs(np.angle(r))) - alpha * np.pi / 2


def s6(n_mat=40):
    """Reduction check on the 3-simplex (grid) vs direct eigen margin (random D search)."""
    rng = np.random.default_rng(606)
    errs = []
    for _ in range(n_mat):
        while True:
            A = rng.normal(size=(4, 4)); A[np.diag_indices(4)] = -np.exp(rng.normal(size=4))
            if strictP(A):
                break
        p = -np.diag(A)
        inv = {}
        for k in (2, 3, 4):
            for S in itertools.combinations(range(4), k):
                inv[S] = np.linalg.det((-A)[np.ix_(S, S)]) / np.prod(p[list(S)])
        # sample simplex points; normalized char poly of DA with x_i = p_i d_i / a_D
        X = rng.dirichlet(np.ones(4), size=3000)
        a = 0.85
        red = []
        dirm = []
        for x in X[:300]:
            c = [1.0, 1.0]
            for k in (2, 3, 4):
                c.append(sum(inv[S] * np.prod(x[list(S)]) for S in itertools.combinations(range(4), k)))
            red.append(quartic_root_margin(c, a))
            d = x / p
            ev = np.linalg.eigvals(np.diag(d) @ A)
            dirm.append(np.min(np.abs(np.angle(ev))) - a * np.pi / 2)
        errs.append(float(np.max(np.abs(np.array(red) - np.array(dirm)))))
    return {"n_matrices": n_mat, "points_each": 300, "max_abs_diff_reduction_vs_eigen": max(errs)}


def _score(v, alpha):
    A = -np.eye(4)
    off = [(i, j) for i in range(4) for j in range(4) if i != j]
    for (i, j), val in zip(off, v):
        A[i, j] = val
    if not strictP(A):
        return 1.0
    mf = mm([A], alpha, hw=8, step=1.0, n_starts=2)[0]
    mh = mm([A], 1.0, hw=8, step=1.0, n_starts=2)[0]
    return -min(mf, -mh)


def _s7_job(args):
    alpha, seed = args
    r = differential_evolution(_score, [(-4, 4)] * 12, args=(alpha,), seed=seed, maxiter=60, popsize=12,
                               tol=1e-8, polish=False)
    return alpha, seed, float(-r.fun), r.x.tolist()


def s7(P):
    jobs = [(a, s) for a in (0.75, 0.9, 0.99) for s in range(4)]
    res = P.map(_s7_job, jobs, chunksize=1)
    best = {}
    for a, s, sc, x in res:
        if a not in best or sc > best[a]["score"]:
            best[a] = {"score": sc, "offdiag": x, "seed": s}
    # 3x3 reference: cyclic witness at its optimal gamma embedded with isolated node
    ref = {}
    for a in (0.75, 0.9, 0.99):
        gs = np.linspace(2.0, 6.0, 200)
        As3 = [np.array([[-1, 0, -g], [g, -1, 0], [0, g, -1.0]]) for g in gs]
        sc = np.minimum(mm(As3, a), -mm(As3, 1.0))
        ref[str(a)] = {"best_gamma": float(gs[np.argmax(sc)]), "score_3x3_cycle": float(sc.max())}
    return {"n4_best": {str(k): v for k, v in best.items()}, "3x3_reference": ref,
            "note": "score = min(min_D margin_alpha, -min_D margin_1), unit diagonal, |offdiag|<=4"}


def main():
    T = Timer()
    out = {}
    nw = int(os.environ.get("FDSN_WORKERS", "12"))
    with pool(nw) as P:
        for name, fn in [("S1_single_4cycle", s1),
                         ("S2_two_3cycles_shared_edge", lambda: phase_scan(two_cycles, np.linspace(0.5, 3, 26), np.linspace(0.5, 3, 26), (0.75, 0.9, 0.99))),
                         ("S3_cactus_3cycle_plus_pair", lambda: phase_scan(cactus, np.linspace(1.5, 3.5, 26), np.linspace(0, 3, 26), (0.75, 0.9, 0.99))),
                         ("S4_block_coupled", lambda: {s: phase_scan(lambda g, e: block(g, e, s), np.linspace(1.8, 3.2, 29), np.linspace(0, 1.5, 16), (0.75, 0.9)) for s in (-1.0, 1.0)}),
                         ("S5_random_strictP", lambda: s5(P)),
                         ("S6_orbit_reduction_check", s6),
                         ("S7_adversarial_search", lambda: s7(P))]:
            log("P5", name)
            t = Timer()
            out[name] = fn()
            out[name + "_seconds"] = t()
            dump("N4_RECON.json", out)
    out["wall_seconds"] = T()
    out["memory"] = peak_rss_mb()
    dump("N4_RECON.json", out)


if __name__ == "__main__":
    main()
