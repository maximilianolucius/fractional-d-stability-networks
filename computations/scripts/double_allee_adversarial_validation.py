"""Adversarial numerical audit of the Double-Allee IGP package (task §3).

3.1 witness reconstructed from the declared design only (alpha=0.9, m0=0.2, beta=(2,2,2), kappa=18),
    evaluated at m in {0.19, 0.20, 0.21} in float64, 100-digit mpmath and (for the classification)
    the certified T_alpha bracket of fdsn.interval_cert;
3.2 direct all-D spectral attack at m=0.21: log d_i in [-20,20], pattern search / Nelder-Mead / DE
    with several seeds, Matignon angular margin minimised and spectral abscissa maximised, HP recheck
    (mp.eig, 50 digits) around the worst diagonals, comparison with C-10 and C-11;
3.3 random falsification: >= 160,000 joint perturbations of all 14 biological parameters (three noise
    levels, boundary-heavy m samples, samples pushed towards positivity / strict-P / e1e3=e2 boundaries);
    coexistence solved from the quadratic, infeasible points rejected explicitly, multiple equilibria
    counted, C-10 / C-11 / Cain classification, and direct spectral optimisation on an adversarial subset;
plus the m-branch (DA-09/10/11): monotonicity of s(m), t(m), the unique classical crossing and the
second (fractional) crossing / feasibility loss along the branch.
Outputs: DOUBLE_ALLEE_ADVERSARIAL_SUMMARY.json, DOUBLE_ALLEE_WORST_CASES.csv
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

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
RES = os.path.join(ROOT, "computations", "results")
sys.path.insert(0, os.path.join(ROOT, "computations", "scripts"))
from _common import Timer, log, peak_rss_mb, pool, to_jsonable  # noqa: E402

from fdsn.c10_threshold import T1, invariants_batch, rho_alpha, threshold_batch, threshold_mp  # noqa: E402
from fdsn.direct_margin import margins_batch, min_margin, mp_margin  # noqa: E402
from fdsn.double_allee import (PARAM_NAMES, Params, chief_witness, coexistence_equilibria, g_da_prime,  # noqa: E402
                               invariants_of_matrix, prey_roots, reduced_matrix, residuals, with_m, yz_of_x)
from fdsn.interval_cert import certify_threshold_logit  # noqa: E402

ALPHA = 0.9
SEED = 20260926
HW = 20.0


def dump(name, obj):
    with open(os.path.join(RES, name), "w") as f:
        json.dump(to_jsonable(obj), f, indent=2)


# ----------------------------------------------------------------- 3.1 witness reconstruction

def witness_point(P, m, alpha=ALPHA):
    Pm = with_m(P, m)
    eqs = coexistence_equilibria(Pm)
    out = {"m": m, "n_feasible_equilibria": len(eqs), "prey_roots": [float(v) for v in prey_roots(Pm)]}
    if not eqs:
        return out
    e = eqs[0]
    B = reduced_matrix(e["X"], e["Y"], e["Z"], Pm)
    inv = invariants_of_matrix(B)
    beta = np.array(inv["beta"], float); kappa = float(inv["kappa"])
    tb = threshold_batch(beta[None], alpha)
    out.update({"X": e["X"], "Y": e["Y"], "Z": e["Z"], "max_residual": e["max_residual"], "s": float(-B[0][0]),
                "beta": beta.tolist(), "kappa": kappa, "L3": float(inv["L3"]), "T1": float(T1(beta)),
                "T_alpha_float": float(tb.T[0]), "x_star": tb.x[0].tolist(),
                "kappa_minus_T1": kappa - float(T1(beta)), "T_alpha_minus_kappa": float(tb.T[0]) - kappa,
                "Phi": float(T1(beta)) / kappa, "rho_alpha": rho_alpha(alpha),
                "class_C10": "F_alpha & not D_H" if T1(beta) < kappa < tb.T[0] else ("D_H" if kappa < T1(beta) else "not F_alpha"),
                "C11_certificate": bool(T1(beta) / kappa > rho_alpha(alpha)), "strictP": bool(min(inv["m"]) > 0 and inv["q"] > 0 and -B[0][0] > 0)})
    return out


def witness_point_hp(m_str, alpha_str="0.9", dps=100):
    with mp.workdps(dps + 10):
        P = chief_witness(lambda v: mp.mpf(v))
        Pm = with_m(P, mp.mpf(m_str))
        roots = prey_roots(Pm)
        X = max(roots)
        Y, Z = yz_of_x(X, Pm)
        res = residuals(X, Y, Z, Pm)
        B = reduced_matrix(X, Y, Z, Pm)
        inv = invariants_of_matrix(B)
        beta = inv["beta"]; kappa = inv["kappa"]
        t1 = (mp.sqrt(beta[0]) + mp.sqrt(beta[1]) + mp.sqrt(beta[2])) ** 2
        r = threshold_mp([mp.nstr(b, dps + 5) for b in beta], alpha_str, dps=dps)
        bs = [mp.nstr(b, 60) for b in beta]
        cert = certify_threshold_logit(bs, alpha_str, dps=50)
        return {"m": m_str, "dps": dps, "X": mp.nstr(X, 60), "Y": mp.nstr(Y, 60), "Z": mp.nstr(Z, 60),
                "other_root": mp.nstr(min(roots), 30), "max_residual": mp.nstr(max(abs(v) for v in res), 5),
                "s": mp.nstr(-B[0][0], 60), "beta": [mp.nstr(b, 60) for b in beta], "kappa": mp.nstr(kappa, 60),
                "T1": mp.nstr(t1, 60), "kappa_minus_T1": mp.nstr(kappa - t1, 40), "T_alpha_hp": mp.nstr(r["T"], 60),
                "T_alpha_minus_kappa": mp.nstr(r["T"] - kappa, 40), "x_star": [mp.nstr(v, 40) for v in r["x"]],
                "T_alpha_certified": {"L": mp.nstr(cert["L"], 50), "U": mp.nstr(cert["U"], 50), "rel_width": mp.nstr(cert["rel_width"], 5),
                                      "note": "bracket for beta rounded to 60 digits; conditional on C-15 Thm 1"} if cert.get("certified") else cert,
                "kappa_below_certified_L": bool(kappa < cert["L"]) if cert.get("certified") else None,
                "Phi_minus_rho": mp.nstr(t1 / kappa - (1 - 2 * mp.cos(mp.mpf(alpha_str) * mp.pi / 2)) ** 2, 40)}


# ----------------------------------------------------------------- 3.2 direct spectral attack

def spectral_attack(B, alpha=ALPHA, seed=SEED):
    B = np.asarray(B, float)
    out = {"log_d_range": [-HW, HW]}
    r = min_margin(B[None], alpha, half_width=HW, step=0.5, n_starts=4)
    out["pattern_search"] = {"min_margin": float(r["margin"][0]), "d": r["d"][0].tolist()}
    scale = 1.0 / np.abs(np.diag(B))
    Bs = scale[:, None] * B

    def marg(w, al=alpha):
        return margins_batch(Bs[None], np.asarray(w)[None, None, :], np.array([al]))[0, 0]

    def abscissa(w):
        d = np.exp([w[0], w[1], 0.0])
        return float(np.linalg.eigvals(np.diag(d) @ Bs).real.max())

    def norm_abscissa(w):
        """Scale-invariant classical-instability objective: max_i Re(lambda_i)/|lambda_i| = cos(min |arg|)."""
        d = np.exp([w[0], w[1], 0.0])
        ev = np.linalg.eigvals(np.diag(d) @ Bs)
        return float((ev.real / np.abs(ev)).max())

    rng = np.random.default_rng(seed)
    nm = [minimize(marg, rng.uniform(-HW, HW, 2), method="Nelder-Mead", options={"xatol": 1e-12, "fatol": 1e-15, "maxfev": 5000}) for _ in range(12)]
    best_nm = min(nm, key=lambda q: q.fun)
    out["nelder_mead_12_seeds"] = {"min_margin": float(best_nm.fun), "w": best_nm.x.tolist(), "all": sorted(float(q.fun) for q in nm)}
    de = [differential_evolution(marg, [(-HW, HW)] * 2, seed=seed + k, tol=1e-13, maxiter=400, popsize=25, polish=True) for k in range(3)]
    best_de = min(de, key=lambda q: q.fun)
    out["differential_evolution_3_seeds"] = {"min_margin": float(best_de.fun), "w": best_de.x.tolist(), "all": [float(q.fun) for q in de]}
    # spectral abscissa maximisation (classical instability witness)
    de_a = [differential_evolution(lambda w: -norm_abscissa(w), [(-HW, HW)] * 2, seed=seed + 10 + k, tol=1e-13, maxiter=400, popsize=25, polish=True) for k in range(3)]
    best_a = max(de_a, key=lambda q: -q.fun)
    out["max_normalized_abscissa_cos_minarg"] = {"value": float(-best_a.fun), "w": best_a.x.tolist(), "all": [float(-q.fun) for q in de_a],
                                                 "raw_abscissa_at_maximizer_(prescaled_B)": abscissa(best_a.x)}
    de_raw = differential_evolution(lambda w: -abscissa(w), [(-HW, HW)] * 2, seed=seed + 20, tol=1e-13, maxiter=400, popsize=25, polish=True)
    out["raw_abscissa_DE_note"] = {"value": float(-de_raw.fun), "w": de_raw.x.tolist(),
                                   "note": "raw max Re lambda is NOT scale-invariant: outside the unstable sliver it tends to 0- as d -> 0, "
                                           "so a global optimizer drifts to the box corner; the normalized objective above is the meaningful one"}
    r1 = min_margin(B[None], 1.0, half_width=HW, step=0.5, n_starts=4)
    out["pattern_search_alpha1"] = {"min_margin": float(r1["margin"][0]), "d": r1["d"][0].tolist()}
    # HP recheck around the worst diagonals (bounded local search, 50 digits)
    with mp.workdps(60):
        Bm = mp.matrix([[mp.mpf(float(v)) for v in row] for row in Bs])
        wbest = min([best_nm.x, best_de.x, np.log(r["d"][0] / scale)[:2] - np.log(r["d"][0][2] / scale[2])], key=lambda w: marg(w))
        w = [mp.mpf(float(v)) for v in wbest]
        f = lambda v: mp_margin(Bm, [mp.exp(v[0]), mp.exp(v[1]), mp.mpf(1)], alpha, 50)[0]
        best = f(w); step = mp.mpf("1e-3"); ev = 1
        while step > mp.mpf("1e-25") and ev < 600:
            imp = False
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)):
                t = [w[0] + step * dx, w[1] + step * dy]
                if max(abs(t[0]), abs(t[1])) > HW:
                    continue
                v = f(t); ev += 1
                if v < best:
                    best, w, imp = v, t, True
                    break
            step = step * 2 if imp else step / 2
        ev_at = mp.eig(mp.diag([mp.exp(w[0]), mp.exp(w[1]), mp.mpf(1)]) * Bm, left=False, right=False)
        out["hp_recheck_50_digits"] = {"min_margin": mp.nstr(best, 25), "w": [mp.nstr(v, 20) for v in w],
                                       "eigenvalues_at_worst_D": [mp.nstr(e, 20) for e in ev_at]}
        wa = [mp.mpf(float(v)) for v in best_a.x]
        eva = mp.eig(mp.diag([mp.exp(wa[0]), mp.exp(wa[1]), mp.mpf(1)]) * Bm, left=False, right=False)
        out["hp_abscissa_at_DE_witness"] = {"max_Re": mp.nstr(max(mp.re(e) for e in eva), 25), "eigenvalues": [mp.nstr(e, 20) for e in eva]}
    p, m_, q, beta, kappa = invariants_batch(B[None])
    tb = threshold_batch(beta, alpha)
    out["C10"] = {"kappa": float(kappa[0]), "T1": float(T1(beta[0])), "T_alpha": float(tb.T[0]),
                  "prediction": "in F_alpha (kappa < T_alpha) and NOT D_H (kappa > T1)" if T1(beta[0]) < kappa[0] < tb.T[0] else "other",
                  "x_star": tb.x[0].tolist(), "D_star_from_x_star(d_i=x_i/p_i, geomean 1)": (lambda d: (d / np.prod(d) ** (1 / 3)).tolist())(tb.x[0] / p[0])}
    out["C11"] = {"Phi": float(T1(beta[0]) / kappa[0]), "rho_alpha": rho_alpha(alpha), "certificate": bool(T1(beta[0]) / kappa[0] > rho_alpha(alpha))}
    ka, t1a, Ta_ = float(kappa[0]), float(T1(beta[0])), float(tb.T[0])
    frac_ok = (out["pattern_search"]["min_margin"] > 0 and best_nm.fun > 0 and best_de.fun > 0 and best > 0) == (ka < Ta_)
    if abs(ka / t1a - 1) < 1e-12:      # exactly on the Cain boundary: expect a zero alpha=1 margin
        cls_ok = abs(r1["margin"][0]) < 1e-9 and abs(out["max_normalized_abscissa_cos_minarg"]["value"]) < 1e-7
    else:
        cls_ok = (out["max_normalized_abscissa_cos_minarg"]["value"] > 0) == (ka > t1a) and (r1["margin"][0] < 0) == (ka > t1a)
    out["consistent"] = bool(frac_ok and cls_ok)
    return out


# ----------------------------------------------------------------- 3.3 random falsification

def _sample_job(args):
    seed, n, mode, base = args
    rng = np.random.default_rng(seed)
    base = np.array(base, float)
    rows = []
    for _ in range(n):
        v = base.copy()
        if mode.startswith("lognormal"):
            sig = float(mode.split(":")[1])
            v = v * np.exp(rng.normal(scale=sig, size=14))
        elif mode == "m_sweep":
            v = v * np.exp(rng.normal(scale=0.02, size=14)); v[3] = rng.uniform(0.15, 0.25)
        elif mode == "boundary":
            v = v * np.exp(rng.normal(scale=0.05, size=14))
            k = rng.integers(5)
            if k == 0:      # push K towards X (H_A -> 0)
                v[1] = 1.0 + 10 ** rng.uniform(-3, -0.5)
            elif k == 1:    # e2 towards / beyond e1 e3
                v[8] = v[7] * v[9] * 10 ** rng.uniform(-1, 1)
            elif k == 2:    # mortalities up (Y or Z -> 0)
                v[10] *= 1 + 10 ** rng.uniform(-3, 0); v[11] *= 1 + 10 ** rng.uniform(-3, 0)
            elif k == 3:    # m up towards X
                v[3] = rng.uniform(0.25, 0.99)
            else:           # a small / large
                v[0] = 10 ** rng.uniform(-3, 1)
        P = Params(*v)
        rec = {"params": v.tolist(), "mode": mode}
        try:
            eqs = coexistence_equilibria(P)
        except Exception:
            eqs = []
        rec["n_eq"] = len(eqs)
        if not eqs:
            rec["status"] = "infeasible"
            rows.append(rec); continue
        e = eqs[0]
        B = np.array(reduced_matrix(e["X"], e["Y"], e["Z"], P), float)
        p, mm_, q, beta, kappa = invariants_batch(B[None])
        sP = bool(p[0].min() > 0 and mm_[0].min() > 0 and q[0] > 0)
        rec.update({"status": "feasible", "X": e["X"], "Y": e["Y"], "Z": e["Z"], "s": float(-B[0, 0]), "strictP": sP,
                    "e1e3_gt_e2": bool(v[7] * v[9] > v[8]), "beta": beta[0].tolist(), "kappa": float(kappa[0]), "q": float(q[0])})
        if sP:
            t1 = float(T1(beta[0])); Ta = float(threshold_batch(beta, ALPHA).T[0])
            rec.update({"T1": t1, "T_alpha": Ta, "gap_cain": kappa[0] / t1 - 1, "gap_frac": kappa[0] / Ta - 1,
                        "class": "frac_only" if t1 < kappa[0] < Ta else ("classical" if kappa[0] < t1 else "unstable"),
                        "C11": bool(t1 / kappa[0] > rho_alpha(ALPHA))})
        rows.append(rec)
    return rows


def _direct_job(args):
    Bs, alphas = args
    Bs = np.array(Bs)
    r = min_margin(Bs, ALPHA, half_width=16, step=0.5, n_starts=3)
    r1 = min_margin(Bs, 1.0, half_width=16, step=0.5, n_starts=3)
    return r["margin"].tolist(), r1["margin"].tolist(), r["err"].tolist()


def random_falsification(P, Pool):
    base = P.as_list()
    plan = [("lognormal:0.02", 40000), ("lognormal:0.1", 40000), ("lognormal:0.3", 40000), ("m_sweep", 20000), ("boundary", 20000)]
    jobs = []
    k = 0
    for mode, n in plan:
        for j in range(n // 2000):
            jobs.append((SEED * 100 + k, 2000, mode, base)); k += 1
    rows = [r for rr in Pool.map(_sample_job, jobs, chunksize=1) for r in rr]
    feas = [r for r in rows if r["status"] == "feasible"]
    sp_ = [r for r in feas if r["strictP"]]
    summ = {"n_total": len(rows), "n_feasible": len(feas), "n_infeasible": len(rows) - len(feas),
            "n_multiple_equilibria": sum(r["n_eq"] > 1 for r in feas),
            "n_strictP": len(sp_), "n_feasible_not_strictP": len(feas) - len(sp_),
            "strictP_with_e1e3_le_e2": sum((not r["e1e3_gt_e2"]) for r in sp_),
            "feasible_e1e3_le_e2_not_strictP": sum((not r["e1e3_gt_e2"]) and not r["strictP"] for r in feas),
            "class_counts": {c: sum(r.get("class") == c for r in sp_) for c in ("classical", "frac_only", "unstable")},
            "C11_pass_among_frac_only": sum(r["C11"] for r in sp_ if r.get("class") == "frac_only"),
            "by_mode": {}}
    for mode, _ in plan:
        rm = [r for r in rows if r["mode"] == mode]
        fm = [r for r in rm if r["status"] == "feasible"]
        sm = [r for r in fm if r["strictP"]]
        summ["by_mode"][mode] = {"n": len(rm), "feasible": len(fm), "strictP": len(sm),
                                 "class_counts": {c: sum(r.get("class") == c for r in sm) for c in ("classical", "frac_only", "unstable")}}
    # adversarial subset for direct spectral comparison: nearest to either boundary + random
    rng = np.random.default_rng(SEED + 7)
    near = sorted(sp_, key=lambda r: min(abs(r["gap_cain"]), abs(r["gap_frac"])))[:2500]
    rand = [sp_[i] for i in rng.choice(len(sp_), size=1500, replace=False)]
    notP = [r for r in feas if not r["strictP"]][:500]
    subset = near + rand + notP
    Bs = []
    for r in subset:
        P_ = Params(*r["params"])
        Bs.append(reduced_matrix(r["X"], r["Y"], r["Z"], P_))
    chunks = [(Bs[i:i + 100], None) for i in range(0, len(Bs), 100)]
    res = Pool.map(_direct_job, chunks, chunksize=1)
    m_a = np.concatenate([np.array(a) for a, _, _ in res]); m_1 = np.concatenate([np.array(b) for _, b, _ in res])
    err = np.concatenate([np.array(c) for _, _, c in res])
    tol = np.maximum(1e-11, 10 * err)
    worst = []
    mism = 0; near_zero = 0
    for r, ma, m1, tl in zip(subset, m_a, m_1, tol):
        if r["strictP"]:
            pred_F = r["class"] in ("classical", "frac_only"); pred_H = r["class"] == "classical"
        else:
            pred_F = False; pred_H = False        # Lemma 2: not interior; direct margin should be <= 0 up to tolerance
        okF = (ma > tl) == pred_F or abs(ma) <= tl
        okH = (m1 > tl) == pred_H or abs(m1) <= tl
        if abs(ma) <= tl or abs(m1) <= tl:
            near_zero += 1
        if not (okF and okH):
            mism += 1
        worst.append({**{k_: r.get(k_) for k_ in ("mode", "status", "strictP", "class", "kappa", "T1", "T_alpha", "gap_cain", "gap_frac", "X", "Y", "Z", "s")},
                      "params": r["params"], "direct_min_margin_alpha": float(ma), "direct_min_margin_alpha1": float(m1),
                      "float_err_est": float(err[len(worst)]), "mismatch": not (okF and okH)})
    summ["direct_subset"] = {"n": len(subset), "n_near_boundary": len(near), "n_random": len(rand), "n_not_strictP": len(notP),
                             "float_mismatches": mism, "near_zero_undecided": near_zero,
                             "min_abs_gap_cain": float(min(abs(r["gap_cain"]) for r in near)),
                             "min_abs_gap_frac": float(min(abs(r["gap_frac"]) for r in near))}
    worst.sort(key=lambda w: (not w["mismatch"], min(abs(w.get("gap_cain") or 1), abs(w.get("gap_frac") or 1))))
    return summ, worst, rows


def _hp_mismatch(w):
    """HP recheck of a flagged case: 40-digit invariants + threshold vs mp.eig margin at the float worst D (bounded search)."""
    with mp.workdps(50):
        P_ = Params(*[mp.mpf(v) for v in w["params"]])
        roots = prey_roots(P_); X = max(roots); Y, Z = yz_of_x(X, P_)
        B = reduced_matrix(X, Y, Z, P_)
        inv = invariants_of_matrix(B)
        beta = inv["beta"]; kappa = inv["kappa"]
        t1 = (mp.sqrt(beta[0]) + mp.sqrt(beta[1]) + mp.sqrt(beta[2])) ** 2
        Ta = threshold_mp([mp.nstr(b, 45) for b in beta], repr(ALPHA), dps=40)["T"]
        Bf = np.array([[float(v) for v in row] for row in B])
        r = min_margin(Bf[None], ALPHA, half_width=16); r1 = min_margin(Bf[None], 1.0, half_width=16)
        Bm = mp.matrix([[B[i][j] / (-B[i][i]) for j in range(3)] for i in range(3)])
        d = r["d"][0] * np.abs(np.diag(Bf)); d = d / d[2]
        ma = mp_margin(Bm, [mp.mpf(float(v)) for v in d], ALPHA, 40)[0]
        d1 = r1["d"][0] * np.abs(np.diag(Bf)); d1 = d1 / d1[2]
        m1 = mp_margin(Bm, [mp.mpf(float(v)) for v in d1], 1.0, 40)[0]
        return {"kappa": mp.nstr(kappa, 25), "T1": mp.nstr(t1, 25), "T_alpha": mp.nstr(Ta, 25),
                "hp_margin_at_float_worst_D_alpha": mp.nstr(ma, 15), "hp_margin_at_float_worst_D_alpha1": mp.nstr(m1, 15),
                "consistent": bool(((kappa < Ta) == (ma > 0)) and ((kappa < t1) == (m1 > 0)))}


# ----------------------------------------------------------------- m-branch (DA-09/10/11)

def m_branch(P, alpha=ALPHA):
    ms = np.linspace(0.005, 0.995, 3000)
    rows = []
    for m in ms:
        Pm = with_m(P, m)
        eqs = coexistence_equilibria(Pm)
        if not eqs:
            rows.append({"m": m, "feasible": False}); continue
        e = eqs[0]
        B = np.array(reduced_matrix(e["X"], e["Y"], e["Z"], Pm), float)
        p, mm_, q, beta, kappa = invariants_batch(B[None])
        t1 = float(T1(beta[0])); Ta = float(threshold_batch(beta, alpha).T[0])
        rows.append({"m": m, "feasible": True, "n_eq": len(eqs), "X": e["X"], "s": float(-B[0, 0]), "t": 1 / float(-B[0, 0]),
                     "kappa": float(kappa[0]), "T1": t1, "T_alpha": Ta, "G1": float(kappa[0]) - t1, "Gfrac": Ta - float(kappa[0])})
    feas = [r for r in rows if r["feasible"]]
    s_arr = np.array([r["s"] for r in feas]); m_arr = np.array([r["m"] for r in feas])
    G1 = np.array([r["G1"] for r in feas]); Gf = np.array([r["Gfrac"] for r in feas])
    sign_changes_G1 = np.nonzero(np.diff(np.sign(G1)))[0]
    sign_changes_Gf = np.nonzero(np.diff(np.sign(Gf)))[0]

    def root(f, lo, hi):
        for _ in range(80):
            mid = 0.5 * (lo + hi)
            if f(mid) * f(lo) <= 0:
                hi = mid
            else:
                lo = mid
        return 0.5 * (lo + hi)

    def G1_of(m):
        Pm = with_m(P, m); e = coexistence_equilibria(Pm)[0]
        B = np.array(reduced_matrix(e["X"], e["Y"], e["Z"], Pm), float)
        _, _, _, beta, kappa = invariants_batch(B[None]); return float(kappa[0] - T1(beta[0]))

    def Gf_of(m):
        Pm = with_m(P, m); e = coexistence_equilibria(Pm)[0]
        B = np.array(reduced_matrix(e["X"], e["Y"], e["Z"], Pm), float)
        _, _, _, beta, kappa = invariants_batch(B[None]); return float(threshold_batch(beta, alpha).T[0] - kappa[0])

    out = {"m_range_feasible": [float(m_arr.min()), float(m_arr.max())], "n_feasible": len(feas), "n_infeasible": len(rows) - len(feas),
           "feasibility_loss_at": float(m_arr.max()), "max_n_eq": max(r["n_eq"] for r in feas),
           "ds_dm_negative_everywhere": bool(np.all(np.diff(s_arr) < 0)), "s_at_ends": [float(s_arr[0]), float(s_arr[-1])],
           "n_classical_crossings": int(len(sign_changes_G1)), "n_fractional_crossings": int(len(sign_changes_Gf))}
    if len(sign_changes_G1):
        i = sign_changes_G1[0]; out["m_H_classical_crossing"] = root(G1_of, m_arr[i], m_arr[i + 1])
    if len(sign_changes_Gf):
        i = sign_changes_Gf[0]; out["m_2_fractional_crossing"] = root(Gf_of, m_arr[i], m_arr[i + 1])
    else:
        out["m_2_fractional_crossing"] = None
        out["min_Gfrac_on_branch"] = float(Gf.min())
    out["samples"] = [{k: r[k] for k in ("m", "X", "s", "kappa", "T1", "T_alpha")} for r in feas[::150]]
    return out


def main():
    T0 = Timer()
    P = chief_witness()
    summary = {"alpha": ALPHA, "seed": SEED, "witness_params": dict(zip(PARAM_NAMES, P.as_list())),
               "design": "alpha=0.9, m0=0.2, target beta=(2,2,2), kappa=18=T1; free scales s0=c1=c2=0.05, eta=0.5, X0=1, a=0.5, K=1.1, xi=0.5"}
    log("3.1 witness (float)")
    summary["witness_float"] = [witness_point(P, m) for m in (0.19, 0.20, 0.21)]
    log("3.1 witness (100 digits)")
    summary["witness_hp"] = [witness_point_hp(m) for m in ("0.19", "0.2", "0.21")]
    log("3.2 spectral attack at m=0.21")
    e = coexistence_equilibria(with_m(P, 0.21))[0]
    B21 = reduced_matrix(e["X"], e["Y"], e["Z"], with_m(P, 0.21))
    summary["spectral_attack_m021"] = spectral_attack(B21)
    e = coexistence_equilibria(with_m(P, 0.20))[0]
    summary["spectral_attack_m020_boundary"] = spectral_attack(reduced_matrix(e["X"], e["Y"], e["Z"], with_m(P, 0.20)))
    log("m-branch")
    summary["m_branch"] = m_branch(P)
    log("3.3 random falsification")
    with pool() as Pool:
        summ, worst, rows = random_falsification(P, Pool)
        flagged = [w for w in worst if w["mismatch"]]
        hp = Pool.map(_hp_mismatch, flagged[:200], chunksize=2) if flagged else []
    summ["hp_recheck_of_float_mismatches"] = {"n": len(hp), "consistent": sum(h["consistent"] for h in hp), "details": hp[:20]}
    summary["random_falsification"] = summ
    with open(os.path.join(RES, "DOUBLE_ALLEE_WORST_CASES.csv"), "w", newline="") as f:
        cols = ["mode", "status", "strictP", "class", "mismatch", "kappa", "T1", "T_alpha", "gap_cain", "gap_frac",
                "direct_min_margin_alpha", "direct_min_margin_alpha1", "float_err_est", "X", "Y", "Z", "s"] + PARAM_NAMES
        w = csv.writer(f); w.writerow(cols)
        for r in worst[:3000]:
            w.writerow([r.get(c) for c in cols[:17]] + [f"{v:.17g}" for v in r["params"]])
    summary["wall_seconds"] = T0(); summary["memory"] = peak_rss_mb()
    dump("DOUBLE_ALLEE_ADVERSARIAL_SUMMARY.json", summary)
    print(json.dumps({k: summary[k] for k in ("random_falsification",)}, indent=1, default=str)[:3000])
    print("spectral consistent:", summary["spectral_attack_m021"]["consistent"], "m-branch:", {k: v for k, v in summary["m_branch"].items() if k != "samples"})


if __name__ == "__main__":
    main()
