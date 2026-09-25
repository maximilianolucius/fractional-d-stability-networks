"""Wave 2 P3 — quantitative robustness of canonical witnesses.

P3A (invariant space): m_frac = T_alpha - kappa, m_Cain = kappa - T1, normalised
versions, and C-15 first-order sensitivities dT/dbeta_ij = h'(B*)/x_k*, dT/dalpha
(envelope), dkappa/dbeta at fixed L3, etc.  (HP 40 digits.)

P3B (entry space): smallest real perturbation Delta of the 3x3 matrix reaching
  (1) exact fractional boundary  g_frac(A) := T_alpha(beta(A)) - kappa(A) = 0,
  (2) Cain boundary              g_cain(A) := kappa(A) - T_1(beta(A)) = 0,
  (3) strict-P boundary          g_P(A)    := min(p_i, m_ij, q) = 0,
in the Frobenius norm and the max-entry norm.  Methods:
  L  local first-order estimate |g| / ||grad g||_2 (Frobenius), |g| / ||grad g||_1 (max);
  S  constrained local optimisation (SLSQP), 8 starts (local-estimate direction + random);
  D  directional root-finding: 3000 random unit directions (+ the coordinate/sign
     directions), bisection on g(A + t U) = 0 -> global-type upper bound;
  G  differential evolution over Delta in a box, penalised constraint;
  H  HP refinement (mpmath, 40 digits) of the best candidate along its direction:
     reported bound and residual |g| are HP.
For the strict-P boundary the Frobenius distance to each component is EXACT
(Eckart-Young: min_i |a_ii| for p_i=0, sigma_min(A[ij]) for m_ij=0, sigma_min(A)
for q=0) and a rigorous max-norm lower bound follows from ||Delta||_max >= ||Delta||_F/3.
No rigorous lower bound is claimed for boundaries (1)-(2); all their numbers are
UPPER bounds (NUMERICAL / HP).  Outputs ROBUSTNESS_SUMMARY.csv, ROBUSTNESS_DETAILS.json.
"""
from __future__ import annotations

import csv
import json
import os
import sys
import time

import mpmath as mp
import numpy as np
from scipy.optimize import differential_evolution, minimize

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from w2_common import RESULTS, Timer, dump, git_sha, log, pool, stamp  # noqa: E402

from fdsn.c10_threshold import T1, h_derivs, invariants_batch, mp_h_derivs, mp_uk, threshold_batch, threshold_mp, uk  # noqa: E402

N_DIRS = 3000
SEED = 2026


# ----------------------------------------------------------------- boundary functions (float)

def inv1(A):
    p, m, q, beta, kappa = invariants_batch(A[None])
    return p[0], m[0], q[0], beta[0], kappa[0]


def strictP_val(A):
    p, m, q, _, _ = inv1(A)
    return float(min(p.min(), m.min(), q))


def g_frac(A, alpha):
    p, m, q, beta, kappa = inv1(A)
    if min(p.min(), m.min(), q) <= 0:
        return np.nan
    return float(threshold_batch(beta[None], alpha).T[0] - kappa)


def g_cain(A):
    p, m, q, beta, kappa = inv1(A)
    if min(p.min(), m.min(), q) <= 0:
        return np.nan
    return float(kappa - T1(beta))


def G(A, alpha, which):
    if which == "frac":
        return g_frac(A, alpha)
    if which == "cain":
        return g_cain(A)
    return strictP_val(A)


def grad_fd(A, alpha, which, h=1e-6):
    g = np.zeros((3, 3))
    for i in range(3):
        for j in range(3):
            E = np.zeros((3, 3)); E[i, j] = h * max(1.0, abs(A[i, j]))
            g[i, j] = (G(A + E, alpha, which) - G(A - E, alpha, which)) / (2 * E[i, j])
    return g


# ----------------------------------------------------------------- methods

def local_estimate(A, alpha, which):
    g0 = G(A, alpha, which)
    gr = grad_fd(A, alpha, which)
    return {"g0": g0, "frob": abs(g0) / np.linalg.norm(gr), "max": abs(g0) / np.abs(gr).sum(),
            "grad": gr.tolist(), "direction_frob": (-np.sign(g0) * gr / np.linalg.norm(gr)).tolist()}


def root_along(A, alpha, which, U, tmax=None, tol=1e-12):
    """Smallest t>0 with g(A+tU)=0 (sign change) and strict-P kept up to there (for frac/cain)."""
    g0 = G(A, alpha, which)
    tmax = tmax or 10.0 * max(1.0, np.abs(A).max())
    # march to bracket
    t_prev, g_prev = 0.0, g0
    t = 1e-3 * max(1.0, np.abs(A).max())
    while t <= tmax:
        g = G(A + t * U, alpha, which)
        if np.isnan(g):            # left strict-P before reaching the boundary
            if which == "P":
                return None
            # strict-P crossed first: the target boundary is not reached along U
            return None
        if g * g0 <= 0:
            lo, hi = t_prev, t
            for _ in range(80):
                mid = 0.5 * (lo + hi)
                gm = G(A + mid * U, alpha, which)
                if np.isnan(gm) or gm * g0 <= 0:
                    hi = mid
                else:
                    lo = mid
                if hi - lo < tol * hi:
                    break
            return 0.5 * (lo + hi)
        t_prev, g_prev = t, g
        t *= 1.25
    return None


def directional_scan(A, alpha, which, rng, n=N_DIRS):
    dirs = [rng.normal(size=(3, 3)) for _ in range(n)]
    for i in range(3):
        for j in range(3):
            for s in (1, -1):
                E = np.zeros((3, 3)); E[i, j] = s
                dirs.append(E)
    best = {"frob": (np.inf, None), "max": (np.inf, None)}
    for U in dirs:
        Uf = U / np.linalg.norm(U)
        t = root_along(A, alpha, which, Uf)
        if t is None:
            continue
        D = t * Uf
        for nm, val in (("frob", np.linalg.norm(D)), ("max", np.abs(D).max())):
            if val < best[nm][0]:
                best[nm] = (val, D)
    return best


def slsqp(A, alpha, which, norm, starts, rng):
    def cons(v):
        g = G(A + v[:9].reshape(3, 3), alpha, which)
        return 1e3 if np.isnan(g) else g          # nan -> infeasible-looking, drives back inside
    best = (np.inf, None, None)
    n_runs = 0
    for D0 in starts:
        n_runs += 1
        if norm == "frob":
            obj = lambda v: float(np.dot(v[:9], v[:9]))
            r = minimize(obj, D0.ravel(), method="SLSQP", constraints=[{"type": "eq", "fun": cons}],
                         options={"maxiter": 300, "ftol": 1e-14})
            D = r.x[:9].reshape(3, 3); val = np.linalg.norm(D)
        else:
            t0 = np.abs(D0).max() + 1e-9
            v0 = np.concatenate([D0.ravel(), [t0]])
            r = minimize(lambda v: v[9], v0, method="SLSQP",
                         constraints=[{"type": "eq", "fun": cons},
                                      {"type": "ineq", "fun": lambda v: v[9] - v[:9]},
                                      {"type": "ineq", "fun": lambda v: v[9] + v[:9]}],
                         options={"maxiter": 300, "ftol": 1e-14})
            D = r.x[:9].reshape(3, 3); val = np.abs(D).max()
        g = G(A + D, alpha, which)
        if np.isfinite(g) and abs(g) < 1e-7 * (1 + abs(G(A, alpha, which))) and val < best[0]:
            best = (val, D, g)
    return best, n_runs


def de_global(A, alpha, which, norm, box, seed):
    g0 = G(A, alpha, which)
    scale = abs(g0)

    def obj(v):
        D = v.reshape(3, 3)
        g = G(A + D, alpha, which)
        pen = 10.0 if np.isnan(g) else abs(g) / scale
        val = np.linalg.norm(D) if norm == "frob" else np.abs(D).max()
        return val / box + 50.0 * pen

    r = differential_evolution(obj, [(-box, box)] * 9, seed=seed, maxiter=150, popsize=15, tol=1e-10, polish=True)
    D = r.x.reshape(3, 3)
    # project onto the boundary along the found direction
    U = D / np.linalg.norm(D)
    t = root_along(A, alpha, which, U)
    if t is None:
        return (np.inf, None)
    D = t * U
    return ((np.linalg.norm(D) if norm == "frob" else np.abs(D).max()), D)


def hp_refine(A, alpha, which, D, dps=40):
    """Refine the root along U = D/|D| at high precision; return (t, |Delta|_F, |Delta|_max, residual)."""
    U = D / np.linalg.norm(D)
    with mp.workdps(dps):
        Am = mp.matrix([[mp.mpf(float(v)) for v in row] for row in A])
        Um = mp.matrix([[mp.mpf(float(v)) for v in row] for row in U])

        def inv(M):
            a = [[M[i, j] for j in range(3)] for i in range(3)]
            p = [-a[i][i] for i in range(3)]
            m = [a[0][0] * a[1][1] - a[0][1] * a[1][0], a[0][0] * a[2][2] - a[0][2] * a[2][0],
                 a[1][1] * a[2][2] - a[1][2] * a[2][1]]
            q = -mp.det(M)
            beta = [m[0] / (p[0] * p[1]), m[1] / (p[0] * p[2]), m[2] / (p[1] * p[2])]
            return p, m, q, beta, q / (p[0] * p[1] * p[2])

        def gm(t):
            M = Am + t * Um
            p, m, q, beta, kappa = inv(M)
            if which == "P":
                return min(p + m + [q])
            if min(p + m + [q]) <= 0:
                return mp.nan
            if which == "cain":
                return kappa - (mp.sqrt(beta[0]) + mp.sqrt(beta[1]) + mp.sqrt(beta[2])) ** 2
            T = threshold_mp([mp.nstr(b, dps) for b in beta], repr(alpha), dps=dps)["T"]
            return T - kappa

        t0 = mp.mpf(float(np.linalg.norm(D)))
        # secant iterations around t0
        t1 = t0 * (1 + mp.mpf(10) ** -6)
        f0, f1 = gm(t0), gm(t1)
        for _ in range(60):
            if f1 == f0:
                break
            t2 = t1 - f1 * (t1 - t0) / (f1 - f0)
            t0, f0, t1, f1 = t1, f1, t2, gm(t2)
            if abs(f1) < mp.mpf(10) ** (-(dps - 6)):
                break
        Dm = [[t1 * Um[i, j] for j in range(3)] for i in range(3)]
        frob = mp.sqrt(sum(v * v for row in Dm for v in row))
        mx = max(abs(v) for row in Dm for v in row)
        return {"t": mp.nstr(t1, 30), "frob": mp.nstr(frob, 30), "max": mp.nstr(mx, 30), "residual": mp.nstr(f1, 5),
                "Delta": [[mp.nstr(v, 20) for v in row] for row in Dm]}


def exact_strictP_distances(A):
    """Frobenius distances to each strict-P component (Eckart-Young), HP."""
    with mp.workdps(40):
        Am = mp.matrix([[mp.mpf(float(v)) for v in row] for row in A])
        comps = {}
        for i in range(3):
            comps[f"p{i + 1}"] = abs(Am[i, i])
        for (i, j) in ((0, 1), (0, 2), (1, 2)):
            B = mp.matrix([[Am[i, i], Am[i, j]], [Am[j, i], Am[j, j]]])
            comps[f"m{i + 1}{j + 1}"] = min(mp.svd_r(B, compute_uv=False))
        comps["q"] = min(mp.svd_r(Am, compute_uv=False))
        k = min(comps, key=comps.get)
        return {"components_frobenius_exact": {c: mp.nstr(v, 20) for c, v in comps.items()},
                "min_component": k, "frobenius_exact": mp.nstr(comps[k], 20),
                "max_norm_lower_bound_rigorous": mp.nstr(comps[k] / 3, 20),
                "max_norm_upper_bound_single_entry": mp.nstr(min(abs(Am[i, i]) for i in range(3)), 20)}


# ----------------------------------------------------------------- P3A

def p3a(w):
    alpha = w["alpha"]
    with mp.workdps(45):
        beta = [mp.mpf(b) if "/" not in b else mp.mpf(b.split("/")[0]) / mp.mpf(b.split("/")[1]) for b in w["beta"]]
        kap = mp.mpf(w["kappa"]) if "/" not in w["kappa"] else mp.mpf(w["kappa"].split("/")[0]) / mp.mpf(w["kappa"].split("/")[1])
        r = threshold_mp([mp.nstr(b, 45) for b in beta], repr(alpha), dps=40)
        T, x, B = r["T"], r["x"], r["B"]
        u, K = mp_uk(alpha)
        h, h1, h2 = mp_h_derivs(B, u, K)
        P = x[0] * x[1] * x[2]
        dT_dbeta = [h1 / x[2], h1 / x[1], h1 / x[0]]           # d/dbeta12, d/dbeta13, d/dbeta23
        # d/dalpha (envelope): dh/du * du/dalpha / P, with r from the quadratic
        rr = (u + mp.sqrt(u * u + K * B)) / K
        drdu = (rr + 4 * u * rr * rr) / (K * rr - u)
        dh_du = 2 * rr * drdu * (1 + 2 * u * rr) + rr * rr * (2 * rr + 2 * u * drdu)
        du_da = -mp.sin(mp.mpf(alpha) * mp.pi / 2) * mp.pi / 2
        dT_da = dh_du * du_da / P
        t1 = (mp.sqrt(beta[0]) + mp.sqrt(beta[1]) + mp.sqrt(beta[2])) ** 2
        dT1 = [t1 ** mp.mpf(0.5) / mp.sqrt(beta[i]) for i in range(3)]    # dT1/dbeta_ij = S/sqrt(beta_ij)
        E = B * h1 / h
        return {
            "m_frac": mp.nstr(T - kap, 20), "m_Cain": mp.nstr(kap - t1, 20),
            "m_frac_over_Talpha": mp.nstr((T - kap) / T, 12), "m_Cain_over_T1": mp.nstr((kap - t1) / t1, 12),
            "band_position": mp.nstr((kap - t1) / (T - t1), 12),
            "dT_dbeta_[12,13,23]": [mp.nstr(v, 20) for v in dT_dbeta],
            "dT_dalpha": mp.nstr(dT_da, 20), "dT1_dbeta_[12,13,23]": [mp.nstr(v, 20) for v in dT1],
            "elasticity_E(B*)": mp.nstr(E, 15), "euler_check_sum_beta_dT_dbeta_over_T": mp.nstr(sum(beta[i] * dT_dbeta[i] for i in range(3)) / T, 20),
            # at fixed L3, dkappa/dbeta_ij = 1 (C-13): first-order change of m_frac per unit beta_ij
            "d_mfrac_dbeta_fixed_L3_[12,13,23]": [mp.nstr(v - 1, 15) for v in dT_dbeta],
            "d_mfrac_dalpha": mp.nstr(dT_da, 15),
            "alpha_to_fractional_boundary_first_order": mp.nstr(-(T - kap) / dT_da, 10),
            "alpha_to_fractional_boundary_first_order_note": "alpha + m_frac/|dT/dalpha| (T decreases in alpha); first-order only",
        }


# ----------------------------------------------------------------- P3B driver per witness

def p3b(w):
    t0 = time.time()
    A = np.array(w["A_float"])
    alpha = w["alpha"]
    rng = np.random.default_rng(SEED + int(w["id"][1:]))
    out = {"id": w["id"], "alpha": alpha, "A": w["A"], "boundaries": {}, "n_optimizations": 0, "n_root_solves": 0}
    for which in ("frac", "cain", "P"):
        rec = {"g0": G(A, alpha, which)}
        loc = local_estimate(A, alpha, which)
        rec["L_local_first_order"] = {"frob": loc["frob"], "max": loc["max"]}
        scan = directional_scan(A, alpha, which, rng)
        out["n_root_solves"] += N_DIRS + 18
        rec["D_directional_scan"] = {nm: (v if np.isfinite(v) else None) for nm, (v, _) in scan.items()}
        box = 3.0 * min([v for v, _ in scan.values() if np.isfinite(v)] + [loc["frob"]] if np.isfinite(loc["frob"]) else [1.0])
        for nm in ("frob", "max"):
            starts = [np.array(loc["direction_frob"]) * loc["frob"]]
            if scan[nm][1] is not None:
                starts.append(scan[nm][1])
            starts += [rng.normal(size=(3, 3)) * box / 3 for _ in range(6)]
            (sv, sD, sg), nrun = slsqp(A, alpha, which, nm, starts, rng)
            out["n_optimizations"] += nrun
            dv, dD = de_global(A, alpha, which, nm, box, seed=SEED)
            out["n_optimizations"] += 1
            cands = [(sv, sD, "SLSQP"), (dv, dD, "DE"), (scan[nm][0], scan[nm][1], "scan")]
            cands = [c for c in cands if c[1] is not None and np.isfinite(c[0])]
            if not cands:
                rec[nm] = {"best_upper_bound_float": None, "best_method": None, "S_slsqp": None, "G_de": None,
                           "hp_refined_bound": None, "hp_residual": None, "perturbation_matrix": None,
                           "label": "NOT REACHED: the strict-P boundary is crossed first along every tried direction "
                                    "(the target boundary is not the nearest boundary of the class)",
                           "ratio_to_local_first_order": None}
                continue
            bv, bD, bm = min(cands, key=lambda c: c[0])
            hp = hp_refine(A, alpha, which, bD)
            rec[nm] = {"best_upper_bound_float": bv, "best_method": bm,
                       "S_slsqp": (sv if np.isfinite(sv) else None), "G_de": (dv if np.isfinite(dv) else None),
                       "hp_refined_bound": hp["frob"] if nm == "frob" else hp["max"], "hp_residual": hp["residual"],
                       "perturbation_matrix": hp["Delta"], "label": "HP upper bound (40 digits) - no rigorous lower bound"
                       if which != "P" else "HP; see exact Eckart-Young values",
                       "ratio_to_local_first_order": bv / (loc["frob"] if nm == "frob" else loc["max"])}
        if which == "P":
            rec["exact"] = exact_strictP_distances(A)
        out["boundaries"][which] = rec
    out["seconds"] = round(time.time() - t0, 1)
    return out


def _job(w):
    return w["id"], p3a(w), p3b(w)


def select(ws):
    chosen, seen = [], set()
    for w in ws:
        cat = w["tags"][0].split(" ")[0]
        if cat not in seen:
            chosen.append(w); seen.add(cat)
    for w in ws:
        if len(chosen) >= 14:
            break
        if w not in chosen:
            chosen.append(w)
    return chosen


def main():
    T = Timer()
    lib = json.load(open(os.path.join(RESULTS, "CANONICAL_WITNESSES.json")))["witnesses"]
    ws = select(lib)
    log("robustness on", len(ws), "witnesses")
    with pool(min(16, len(ws))) as P:
        res = P.map(_job, ws, chunksize=1)
    details = {wid: {"P3A": a, "P3B": b} for wid, a, b in res}
    rows = []
    for wid, a, b in res:
        for which in ("frac", "cain", "P"):
            r = b["boundaries"][which]
            for nm in ("frob", "max"):
                rows.append({"id": wid, "alpha": b["alpha"], "boundary": which, "norm": nm, "g0": r["g0"],
                             "local_first_order": r["L_local_first_order"][nm],
                             "directional_scan": r["D_directional_scan"][nm], "slsqp": r[nm]["S_slsqp"], "de": r[nm]["G_de"],
                             "best_upper_bound_hp": r[nm]["hp_refined_bound"], "hp_residual": r[nm]["hp_residual"],
                             "exact_or_lower_bound": (r["exact"]["frobenius_exact"] if nm == "frob" else
                                                      r["exact"]["max_norm_lower_bound_rigorous"]) if which == "P" else "",
                             "label": r[nm]["label"], "m_frac": a["m_frac"], "m_Cain": a["m_Cain"]})
    with open(os.path.join(RESULTS, "ROBUSTNESS_SUMMARY.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader(); w.writerows(rows)
    n_opt = sum(b["n_optimizations"] for _, _, b in res)
    n_root = sum(b["n_root_solves"] for _, _, b in res)
    summ = stamp({"git_sha": git_sha(), "n_witnesses": len(ws), "witness_ids": [w["id"] for w in ws],
                  "n_optimizations_slsqp_de": n_opt, "n_directional_root_solves": n_root,
                  "n_optimizations_total": n_opt + n_root, "wall_seconds": T(),
                  "min_frobenius_upper_bound_to_fractional_boundary": min(float(v) for v in (details[w["id"]]["P3B"]["boundaries"]["frac"]["frob"]["hp_refined_bound"] for w in ws) if v is not None),
                  "min_frobenius_upper_bound_to_cain_boundary": min(float(v) for v in (details[w["id"]]["P3B"]["boundaries"]["cain"]["frob"]["hp_refined_bound"] for w in ws) if v is not None),
                  "not_reached_cases": [(w["id"], which, nm) for w in ws for which in ("frac", "cain", "P") for nm in ("frob", "max")
                                        if details[w["id"]]["P3B"]["boundaries"][which][nm]["hp_refined_bound"] is None],
                  "min_frobenius_exact_to_strictP_boundary": min(float(details[w["id"]]["P3B"]["boundaries"]["P"]["exact"]["frobenius_exact"]) for w in ws),
                  "labels": {"frac/cain": "UPPER bounds, HP-refined (no certificate)", "P": "EXACT (Eckart-Young) Frobenius; rigorous max-norm bounds"}})
    dump("ROBUSTNESS_DETAILS.json", {"summary": summ, "witnesses": details})
    print(json.dumps(summ, indent=1, default=str))


if __name__ == "__main__":
    main()
