"""P2 — adversarial stress test of C-10 at scale (float stage).

For every case (A, alpha):
  * THEOREM side: -A strict P, invariants (beta, kappa); for 2/3 < alpha < 1
    predict membership in F_alpha iff kappa < T_alpha(beta); for alpha <= 2/3
    predict membership for every strict-P(-A).
  * DIRECT side (independent of the proof): minimize the Matignon margin
    min_i |arg lambda_i(DA)| - alpha pi/2 over positive diagonal D using only
    LAPACK eigenvalues of the full matrix, with
       (O1) log-grid [-16,16]^2 step 0.5 + batched pattern search from 3 starts,
       (O2) scipy Nelder-Mead from the O1 point + 2 random starts (subset),
       (O3) scipy differential evolution on [-16,16]^2 (subset).
Mismatches / near-zero margins / near-boundary cases are written to
computations/raw/p2_flagged.npz for the high-precision stage p2_hp_verify.py.

Mechanisms (all seeds recorded, derived from MASTER_SEED and job index):
  M1  entry space with rejection (normal / heavy tail / sparse), x all alphas
  M2  invariant coordinates, kappa = T_alpha * f, f log-uniform [0.1, 10]
  M3  perturbations of the C-09 cyclic witness A_gamma
  M4a kappa = T_alpha (1 + delta), |delta| = 10^-U[1,9]
  M4b kappa = T_1 (1 + delta)       (classical Cain boundary)
  M4c principal-minor boundary: tiny beta_ij and/or tiny kappa
  M4d alpha = 2/3 + 10^-U[1,8], kappa = T_alpha (1 +- delta)
  M4e alpha = 1 - 10^-U[1,6], kappa inside/outside the thin band
  M4f extreme beta ratios (1e-6 .. 1e6), kappa = T_alpha (1 +- delta)
  C5  controls: -A NOT P0 or det<=0 (Lemma 2 predicts non-membership for all alpha)
  C6  classical control alpha = 1: Hurwitz D-stability iff kappa < T_1 (Cain)
"""
from __future__ import annotations

import hashlib
import os
import sys
import time

import numpy as np
from scipy.optimize import differential_evolution, minimize

sys.path.insert(0, os.path.dirname(__file__))
from _common import RAW, Timer, dump, log, peak_rss_mb, pool  # noqa: E402

from fdsn.c10_threshold import T1, invariants_batch, matrix_from_invariants, siami_R3, threshold_batch  # noqa: E402
from fdsn.direct_margin import margins_batch, min_margin  # noqa: E402

MASTER_SEED = 20260925
ALPHA_GRID = np.array([0.10, 0.30, 0.60, 2 / 3, 2 / 3 + 1e-7, 2 / 3 + 1e-4, 0.70, 0.80, 0.90,
                       0.95, 0.99, 0.999, 0.9999])
HW, STEP = 16.0, 0.5
TOL_M = 1e-12          # float margin decision floor (radians); per-case 10x a-posteriori error
TOL_K = 1e-10          # theorem near-boundary tolerance |kappa/T - 1|


# ----------------------------------------------------------------- generators

def _random_similarity(rng, A):
    """Apply positive diagonal similarity S A S^-1, a permutation and a row scaling E.

    Similarity and permutation preserve every principal minor up to relabelling;
    E is a positive left-diagonal move.  None changes membership in F_alpha."""
    n = A.shape[0]
    s = np.exp(rng.normal(scale=1.5, size=n))
    A = (s[:, None] * A) / s[None, :]
    P = rng.permutation(n)
    A = A[np.ix_(P, P)]
    e = np.exp(rng.normal(scale=2.0, size=n))
    return e[:, None] * A


def _from_inv(rng, beta, kappa):
    for br in rng.permutation(2):
        A = matrix_from_invariants(beta, kappa, p=np.exp(rng.normal(size=3)),
                                   cw=np.exp(rng.normal(scale=0.7, size=3)), branch=int(br), rng=rng)
        if A is not None:
            return _random_similarity(rng, A)
    return None


def _beta_sample(rng, kind="wide"):
    if kind == "wide":
        return np.exp(rng.normal(scale=1.5, size=3))
    if kind == "extreme":
        return 10.0 ** rng.uniform(-6, 6, size=3)
    if kind == "ecology":
        # antagonistic (>1), mutualistic/competitive (<1), absent pair (=1)
        out = []
        for _ in range(3):
            c = rng.integers(3)
            out.append(1 + np.exp(rng.normal(scale=1.5)) if c == 0 else
                       (rng.uniform(0.01, 0.999) if c == 1 else 1.0))
        return np.array(out)
    raise ValueError(kind)


def _T(beta, alpha):
    return threshold_batch(beta[None], alpha).T[0]


def gen_M1(rng, n):
    As, als = [], []
    while len(As) < n:
        kind = rng.integers(3)
        s = 10 ** rng.uniform(-1, 1)
        if kind == 0:
            A = rng.normal(scale=s, size=(3, 3))
        elif kind == 1:
            A = s * rng.standard_t(1.5, size=(3, 3))
        else:
            A = rng.normal(scale=s, size=(3, 3)) * (rng.random((3, 3)) > 0.35)
        A[np.diag_indices(3)] = -np.exp(rng.normal(size=3))
        _, _, _, beta, kappa = invariants_batch(A[None])
        if np.all(beta[0] > 1e-12) and kappa[0] > 1e-12:
            A = _random_similarity(rng, A)
            for a in ALPHA_GRID:
                As.append(A)
                als.append(a)
    return np.array(As[:n]), np.array(als[:n]), {}


def gen_M2(rng, n):
    As, als, f = [], [], []
    while len(As) < n:
        a = rng.choice(ALPHA_GRID)
        beta = _beta_sample(rng, rng.choice(["wide", "ecology"]))
        ref = _T(beta, a) if a > 2 / 3 else T1(beta)
        ff = 10 ** rng.uniform(-1, 1)
        A = _from_inv(rng, beta, ref * ff)
        if A is not None:
            As.append(A); als.append(a); f.append(ff)
    return np.array(As), np.array(als), {"f": np.array(f)}


def gen_M3(rng, n):
    As, als, g = [], [], []
    while len(As) < n:
        a = rng.choice(ALPHA_GRID)
        hi = siami_R3(a) * 1.15 if a > 2 / 3 + 1e-3 else 5.0
        gam = rng.uniform(1.8, min(hi, 50.0))
        A = np.array([[-1, 0, -gam], [gam, -1, 0], [0, gam, -1.0]])
        A = A + rng.normal(scale=10 ** rng.uniform(-4, -0.5), size=(3, 3)) * (1 + gam * (rng.random() < 0.3))
        _, _, _, beta, kappa = invariants_batch(A[None])
        if np.all(np.diag(A) < 0) and np.all(beta[0] > 1e-12) and kappa[0] > 1e-12:
            As.append(_random_similarity(rng, A)); als.append(a); g.append(gam)
    return np.array(As), np.array(als), {"gamma": np.array(g)}


def _boundary_cases(rng, n, alpha_fn, beta_kind, ref="Talpha", umin=1, umax=9):
    As, als, dl = [], [], []
    while len(As) < n:
        a = alpha_fn(rng)
        beta = _beta_sample(rng, beta_kind)
        if ref == "Talpha" and a > 2 / 3:
            base = _T(beta, a)
        else:
            base = T1(beta)
        d = rng.choice([-1, 1]) * 10 ** -rng.uniform(umin, umax)
        A = _from_inv(rng, beta, base * (1 + d))
        if A is not None:
            As.append(A); als.append(a); dl.append(d)
    return np.array(As), np.array(als), {"delta": np.array(dl)}


def gen_M4a(rng, n):
    hi = ALPHA_GRID[ALPHA_GRID > 2 / 3]
    return _boundary_cases(rng, n, lambda r: r.choice(hi) if r.random() < 0.7 else r.uniform(0.6667, 0.99999),
                           "wide")


def gen_M4b(rng, n):
    return _boundary_cases(rng, n, lambda r: r.choice(ALPHA_GRID), "wide", ref="T1")


def gen_M4c(rng, n):
    As, als, meta = [], [], []
    while len(As) < n:
        a = rng.choice(ALPHA_GRID)
        beta = _beta_sample(rng, "wide")
        k = rng.integers(1, 4)
        idx = rng.choice(3, size=k, replace=False)
        beta[idx] = 10 ** rng.uniform(-9, -2, size=k)
        mode = rng.integers(3)
        if mode == 0:
            kappa = 10 ** rng.uniform(-9, -2)                      # q -> 0+
        elif mode == 1 and a > 2 / 3:
            kappa = _T(beta, a) * (1 + rng.choice([-1, 1]) * 10 ** -rng.uniform(1, 8))
        else:
            kappa = T1(beta) * 10 ** rng.uniform(-1, 1)
        A = _from_inv(rng, beta, kappa)
        if A is not None:
            As.append(A); als.append(a); meta.append(mode)
    return np.array(As), np.array(als), {"mode": np.array(meta)}


def gen_M4d(rng, n):
    return _boundary_cases(rng, n, lambda r: 2 / 3 + 10 ** -r.uniform(1, 8), "wide", umax=8)


def gen_M4e(rng, n):
    As, als, dl = [], [], []
    while len(As) < n:
        a = 1 - 10 ** -rng.uniform(1, 6)
        beta = _beta_sample(rng, "wide")
        Ta, t1 = _T(beta, a), T1(beta)
        mode = rng.integers(3)
        if mode == 0:     # uniformly inside the band
            kappa = t1 + rng.uniform(0.001, 0.999) * (Ta - t1)
            d = kappa / Ta - 1
        else:             # just outside/inside the fractional edge, relative to band width
            d = rng.choice([-1, 1]) * 10 ** -rng.uniform(0, 6) * (Ta - t1) / Ta
            kappa = Ta * (1 + d)
        A = _from_inv(rng, beta, kappa)
        if A is not None:
            As.append(A); als.append(a); dl.append(d)
    return np.array(As), np.array(als), {"delta": np.array(dl)}


def gen_M4f(rng, n):
    hi = ALPHA_GRID[ALPHA_GRID > 2 / 3]
    return _boundary_cases(rng, n, lambda r: r.choice(hi), "extreme", umax=7)


def gen_C5(rng, n):
    As, als, viol = [], [], []
    while len(As) < n:
        a = rng.choice(np.append(ALPHA_GRID, 1.0))
        A = rng.normal(size=(3, 3))
        A[np.diag_indices(3)] = -np.exp(rng.normal(size=3))
        v = rng.integers(3)
        mag = 10 ** rng.uniform(-3, 0)
        if v == 0:
            i = rng.integers(3)
            A[i, i] = mag                                         # positive diagonal entry
        elif v == 1:                                              # negative 2x2 principal minor
            i, j = sorted(rng.choice(3, 2, replace=False))
            prod = A[i, i] * A[j, j]
            A[i, j] = np.sign(rng.normal()) * np.sqrt(prod * (1 + mag))
            A[j, i] = np.sign(A[i, j]) * np.sqrt(prod * (1 + mag))
        else:                                                     # det(-A) <= 0
            p, m, q, beta, kappa = invariants_batch(A[None])
            # rescale the 3-cycle so that kappa = -mag
            L3 = beta[0].sum() - 2 + mag
            B = matrix_from_invariants(beta[0], -mag, p=-np.diag(A), rng=rng)
            if B is None or not np.all(beta[0] > 0):
                continue
            A = B
            del L3
        As.append(_random_similarity(rng, A)); als.append(a); viol.append(v)
    return np.array(As), np.array(als), {"violation": np.array(viol)}


def gen_C6(rng, n):
    return _boundary_cases(rng, n, lambda r: 1.0, "wide", ref="T1", umin=1, umax=9)


GENERATORS = {"M1": gen_M1, "M2": gen_M2, "M3": gen_M3, "M4a": gen_M4a, "M4b": gen_M4b,
              "M4c": gen_M4c, "M4d": gen_M4d, "M4e": gen_M4e, "M4f": gen_M4f,
              "C5": gen_C5, "C6": gen_C6}
PLAN = {"M1": 520_000, "M2": 300_000, "M3": 150_000, "M4a": 450_000, "M4b": 100_000,
        "M4c": 120_000, "M4d": 120_000, "M4e": 180_000, "M4f": 120_000,
        "C5": 60_000, "C6": 60_000}
JOB = 2000


# ----------------------------------------------------------------- per job

def _nm_min(A, alpha, w0s):
    best, wb = np.inf, None
    for w0 in w0s:
        f = lambda w: margins_batch(A[None], np.asarray(w)[None, None, :], np.array([alpha]))[0, 0]
        r = minimize(f, w0, method="Nelder-Mead",
                     options={"xatol": 1e-12, "fatol": 1e-16, "maxfev": 3000})
        if r.fun < best:
            best, wb = r.fun, r.x
    return best, wb


def _de_min(A, alpha, seed):
    f = lambda w: margins_batch(A[None], np.asarray(w)[None, None, :], np.array([alpha]))[0, 0]
    r = differential_evolution(f, [(-HW, HW)] * 2, seed=seed, tol=1e-12, maxiter=300,
                               popsize=20, polish=True)
    return r.fun, r.x


def run_job(spec):
    mech, j = spec
    seed = MASTER_SEED * 1000 + hash_mech(mech) * 100000 + j
    rng = np.random.default_rng(seed)
    t0 = time.time()
    A, alpha, meta = GENERATORS[mech](rng, JOB)
    n = A.shape[0]
    p, m, q, beta, kappa = invariants_batch(A)
    strictP = np.all(p > 0, 1) & np.all(beta > 0, 1) & (kappa > 0)
    T = np.full(n, np.nan)
    xs = np.full((n, 3), np.nan)
    hi = strictP & (alpha > 2 / 3) & (alpha < 1)
    if hi.any():
        tb = threshold_batch(beta[hi], alpha[hi], n_starts=2)
        T[hi], xs[hi] = tb.T, tb.x
    c6 = strictP & (alpha >= 1)
    T[c6] = T1(beta[c6])
    pred = np.where(alpha <= 2 / 3, strictP, np.where(strictP, kappa < T, False))
    gap = np.where(np.isfinite(T), kappa / T - 1, np.nan)
    # ---- direct O1
    dm = min_margin(A, alpha, half_width=HW, step=STEP, n_starts=3)
    marg = dm["margin"].copy()
    d = dm["d"]
    # orbit coordinates of the direct worst D (for comparison with theorem x*)
    with np.errstate(invalid="ignore"):
        xh = (np.abs(p) * d) / np.sum(np.abs(p) * d, 1, keepdims=True)
    # ---- subset for O2 / O3
    near = (np.abs(gap) < 1e-3) | (np.abs(marg) < 1e-6)
    prelim_mis = (pred & (marg < -TOL_M)) | (~pred & (marg > TOL_M))
    sub2 = near | prelim_mis | (rng.random(n) < 0.02)
    sub3 = prelim_mis | (rng.random(n) < 0.003) | (near & (rng.random(n) < 0.05))
    m2 = np.full(n, np.nan)
    m3 = np.full(n, np.nan)
    scale = np.where(np.abs(np.diagonal(A, axis1=1, axis2=2)) > 0,
                     1 / np.abs(np.diagonal(A, axis1=1, axis2=2)), 1.0)
    for i in np.nonzero(sub2)[0]:
        As = scale[i][:, None] * A[i]
        m2[i], _ = _nm_min(As, alpha[i], [dm["w"][i], rng.uniform(-8, 8, 2), rng.uniform(-8, 8, 2)])
    for i in np.nonzero(sub3)[0]:
        As = scale[i][:, None] * A[i]
        m3[i], _ = _de_min(As, alpha[i], int(rng.integers(2**31)))
    allm = np.fmin(np.fmin(marg, m2), m3)
    opt_disagree = np.nan_to_num(np.maximum(marg - np.fmin(m2, m3), 0.0))
    tol = np.maximum(TOL_M, 10 * dm["err"])
    direct_stable = allm > tol
    direct_unstable = allm < -tol
    mismatch = (pred & direct_unstable) | (~pred & direct_stable)
    near_zero = ~direct_stable & ~direct_unstable
    theorem_near = np.abs(gap) < TOL_K
    flag = mismatch | near_zero | theorem_near
    out = {
        "mech": mech, "job": j, "seed": seed, "n": n, "seconds": time.time() - t0,
        "alpha": alpha, "strictP": strictP, "pred": pred, "gap": gap, "T": T,
        "kappa": kappa, "beta": beta, "margin_O1": marg, "margin_O2": m2, "margin_O3": m3,
        "margin": allm, "margin_err": dm["err"], "mismatch": mismatch, "near_zero": near_zero, "theorem_near": theorem_near,
        "opt_disagree": opt_disagree, "x_theorem": xs, "x_direct": xh,
        "flag_A": A[flag], "flag_idx": np.nonzero(flag)[0], "flag_w": dm["w"][flag],
        "meta": meta,
    }
    return out


def hash_mech(m):
    return int(hashlib.sha256(m.encode()).hexdigest(), 16) % 97


# ----------------------------------------------------------------- aggregation

def main():
    only = sys.argv[1:] or list(PLAN)
    T = Timer()
    specs = [(m, j) for m in only for j in range(PLAN[m] // JOB)]
    log("P2 jobs", len(specs), "cases", len(specs) * JOB)
    agg = {}
    keep_keys = ["alpha", "strictP", "pred", "gap", "kappa", "margin", "margin_err", "margin_O1", "margin_O2",
                 "margin_O3", "mismatch", "near_zero", "theorem_near", "opt_disagree", "T"]
    per_mech = {m: {k: [] for k in keep_keys + ["beta", "x_theorem", "x_direct", "A_flag",
                                                "flag_global", "w_flag", "meta"]} for m in only}
    done = 0
    with pool() as P:
        for out in P.imap_unordered(run_job, specs, chunksize=1):
            m = out["mech"]
            for k in keep_keys:
                per_mech[m][k].append(out[k])
            per_mech[m]["beta"].append(out["beta"])
            per_mech[m]["x_theorem"].append(out["x_theorem"])
            per_mech[m]["x_direct"].append(out["x_direct"])
            per_mech[m]["A_flag"].append(out["flag_A"])
            per_mech[m]["flag_global"].append(out["flag_idx"] + out["job"] * JOB)
            per_mech[m]["w_flag"].append(out["flag_w"])
            done += 1
            if done % 50 == 0:
                log(f"{done}/{len(specs)} jobs, {T()} s, last job {out['seconds']:.1f}s")
    for m in only:
        arr = {k: np.concatenate(v) if k != "meta" else None for k, v in per_mech[m].items()}
        del arr["meta"]
        path = os.path.join(RAW, f"p2_{m}.npz")
        np.savez_compressed(path, **arr)
        agg[m] = path
    dump("P2_RAW_INDEX.json", {"files": agg, "wall_seconds": T(), "memory": peak_rss_mb(),
                               "master_seed": MASTER_SEED, "job_size": JOB, "plan": {m: PLAN[m] for m in only}})


if __name__ == "__main__":
    main()
