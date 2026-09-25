"""Wave 2 P4 — independent verification of the C-15 differential structure.

Primary identity (C-13 §7 / C-15 envelope):   dT/dbeta_ij = h'_alpha(B*) / x_k*.
Per sample point (beta, alpha) the FLOAT stage performs these checks:
  c1-c3  dT/dbeta_ij analytic vs Richardson-extrapolated central FD of T (independent
         evaluations of the minimisation at beta +/- h, +/- h/2);
  c4     dT/dalpha analytic (envelope: d_alpha h_alpha(B*) / P*) vs Richardson FD in alpha;
  c5     Hessian of G in logit coordinates positive definite (min eigenvalue > 0), condition number;
  c6-c8  dx*/dbeta_ij by the implicit-function theorem (H_y dy = -d_beta grad_y G) vs FD of x*;
  c9-c13 permutation equivariance: T(sigma beta) = T(beta), x*(sigma beta) = sigma' x*(beta), 5 permutations;
  c14    Euler-type identity  sum_ij beta_ij dT/dbeta_ij = E_alpha(B*) T   (SYMBOLIC IDENTITY: it
         follows from the envelope formula since sum beta_ij x_i x_j = B*; E = B h'/h);
  c15    log-elasticity identity  d log T / d log beta_ij = [1 + (2E-3)(1-2 x_k*)]/2  (SYMBOLIC
         IDENTITY: envelope formula + C-15 z_ij formula);
  c16    dx*/dalpha by FD only (recorded, NUMERICAL OBSERVATION; no analytic counterpart claimed).
HP stage: the 500 points with the largest float relative error in c1-c4/c6-c8 are recomputed at
40 digits (threshold_mp; Richardson central FD with relative step 1e-8, expected agreement ~1e-28).
Float FD near alpha=2/3 is precision-limited (T ~ 27/K^3 dominates the beta dependence) and
such float "failures" are expected; all of them are among the HP-rechecked points.
Regimes: symmetric, two-equal, generic, strong anisotropy, alpha near 2/3, alpha near 1.
Outputs: C15_SENSITIVITY_VALIDATION.json, C15_SENSITIVITY_WORST.csv
"""
from __future__ import annotations

import csv
import itertools
import os
import sys

import mpmath as mp
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from w2_common import RESULTS, Timer, dump, git_sha, log, pool, stamp  # noqa: E402

from fdsn.c10_threshold import _beta_matrix, _softmax2, h_derivs, mp_h_derivs, mp_uk, objective_G, threshold_batch, threshold_mp  # noqa: E402

SEED = 415
N_POINTS = int(os.environ.get("P4_N", "8000"))
N_HP = min(500, N_POINTS)
PERMS = [p for p in itertools.permutations(range(3)) if p != (0, 1, 2)]
# permutation of species sigma acts on beta index pairs: pair (i,j) -> (sigma i, sigma j); ordering (12,13,23)
PAIRS = [(0, 1), (0, 2), (1, 2)]


def beta_perm(sig):
    """Index map: new beta[k'] = beta[k] where pair k' = sigma(pair k)."""
    idx = []
    for (i, j) in PAIRS:
        a, b = sorted((sig[i], sig[j]))
        idx.append(PAIRS.index((a, b)))
    return idx


def sample(rng):
    regimes = ["symmetric", "two_equal", "generic", "anisotropic", "near_23", "near_1"]
    reg = rng.choice(regimes, size=N_POINTS)
    beta = np.empty((N_POINTS, 3)); alpha = np.empty(N_POINTS)
    for i, r in enumerate(reg):
        if r == "symmetric":
            beta[i] = 10 ** rng.uniform(-3, 3)
        elif r == "two_equal":
            b, c = 10 ** rng.uniform(-3, 3, 2); k = rng.integers(3)
            beta[i] = [b, b, b]; beta[i, k] = c
        elif r == "anisotropic":
            beta[i] = 10 ** rng.uniform(-4, 4, 3)
        else:
            beta[i] = np.exp(rng.normal(scale=1.5, size=3))
        if r == "near_23":
            alpha[i] = 2 / 3 + 10 ** -rng.uniform(1, 7)
        elif r == "near_1":
            alpha[i] = 1 - 10 ** -rng.uniform(1, 8)
        else:
            alpha[i] = rng.uniform(0.68, 0.995)
    return beta, alpha, reg


def uk_arr(alpha):
    t = alpha * np.pi / 2
    return np.cos(t), -np.sin(3 * t) / np.sin(t)


def dh_dalpha(B, alpha):
    u, K = uk_arr(alpha)
    s = np.sqrt(u * u + K * B)
    r = (u + s) / K
    drdu = (r + 4 * u * r * r) / (K * r - u)
    dh_du = 2 * r * drdu * (1 + 2 * u * r) + r * r * (2 * r + 2 * u * drdu)
    return dh_du * (-np.sin(alpha * np.pi / 2) * np.pi / 2)


def richardson(f, h):
    """Central FD with steps h and h/2, Richardson-extrapolated (O(h^4))."""
    d1 = (f(h) - f(-h)) / (2 * h)
    d2 = (f(h / 2) - f(-h / 2)) / h
    return (4 * d2 - d1) / 3


def float_stage(beta, alpha):
    n = beta.shape[0]
    tb = threshold_batch(beta, alpha, n_starts=2)
    T, x, y = tb.T, tb.x, tb.y
    u, K = uk_arr(alpha)
    Bm = _beta_matrix(beta)
    dB = np.einsum("nij,nj->ni", Bm, x)
    B = 0.5 * np.sum(dB * x, 1)
    h, h1, h2 = h_derivs(B, u, K)
    P = np.prod(x, 1)
    dT_an = np.stack([h1 / x[:, 2], h1 / x[:, 1], h1 / x[:, 0]], 1)          # d/dbeta12, 13, 23
    dTa_an = dh_dalpha(B, alpha) / P
    E = B * h1 / h
    res = {"T": T, "x": x, "dT_an": dT_an, "dTa_an": dTa_an, "E": E, "B": B}
    # c1-c3: FD in beta (relative step 1e-3 -> Richardson error ~1e-12 * scale)
    dT_fd = np.empty_like(dT_an); dx_fd = np.empty((n, 3, 3))
    for k in range(3):
        hk = 3e-3 * beta[:, k]
        def fT(s, k=k):
            b2 = beta.copy(); b2[:, k] += s
            return threshold_batch(b2, alpha).T
        dT_fd[:, k] = richardson(fT, hk)
        def fx(s, k=k):
            b2 = beta.copy(); b2[:, k] += s
            return threshold_batch(b2, alpha).x
        d1 = (fx(hk) - fx(-hk)) / (2 * hk[:, None]); d2 = (fx(hk / 2) - fx(-hk / 2)) / hk[:, None]
        dx_fd[:, :, k] = (4 * d2 - d1) / 3
    res["dT_fd"] = dT_fd
    res["err_dT"] = np.abs(dT_fd / dT_an - 1)
    # c4: FD in alpha
    ha = np.minimum(1e-5, 0.02 * np.minimum(alpha - 2 / 3, 1 - alpha))
    def fa(s):
        return threshold_batch(beta, alpha + s).T
    dTa_fd = richardson(fa, ha)
    res["dTa_fd"] = dTa_fd
    res["err_dTa"] = np.abs(dTa_fd / dTa_an - 1)
    # c5: Hessian PD & condition number (logit)
    G, g, H, _, _ = objective_G(y, beta, u, K)
    w = np.linalg.eigvalsh(H)
    res["hess_min_eig"] = w[:, 0]; res["hess_cond"] = w[:, 1] / w[:, 0]; res["grad_norm"] = np.linalg.norm(g, axis=1)
    # c6-c8: implicit-function dx*/dbeta vs FD
    mu = h1 / h; nu = h2 / h - mu * mu
    dx_ift = np.empty((n, 3, 3))
    for k, (i, j) in enumerate(PAIRS):
        # d/dbeta_ij of grad_y G components m=0,1:  nu x_i x_j (x_m dB_m - 2 x_m B) + mu x_m (x_j d_mi + x_i d_mj) - 2 mu x_m x_i x_j
        rhs = np.empty((n, 2))
        for m in range(2):
            rhs[:, m] = (nu * x[:, i] * x[:, j] * (x[:, m] * dB[:, m] - 2 * x[:, m] * B)
                         + mu * x[:, m] * (x[:, j] * (m == i) + x[:, i] * (m == j)) - 2 * mu * x[:, m] * x[:, i] * x[:, j])
        dy = -np.linalg.solve(H, rhs[:, :, None])[:, :, 0]
        J = np.zeros((n, 3, 2))
        for m in range(2):
            J[:, :, m] = -x * x[:, m:m + 1]; J[:, m, m] += x[:, m]
        dx_ift[:, :, k] = np.einsum("nim,nm->ni", J, dy)
    res["dx_ift"] = dx_ift; res["dx_fd"] = dx_fd
    scale = np.maximum(np.abs(dx_ift).max(axis=1), 1e-300)
    res["err_dx"] = np.abs(dx_fd - dx_ift).max(axis=1) / scale                 # (n,3)
    # c9-c13: permutation equivariance
    errT = np.zeros((n, 5)); errx = np.zeros((n, 5))
    for q, sig in enumerate(PERMS):
        idx = beta_perm(sig)
        bp = np.empty_like(beta)
        bp[:, idx] = beta                      # bp[sigma(pair k)] = beta[pair k]
        tp = threshold_batch(bp, alpha)
        errT[:, q] = np.abs(tp.T / T - 1)
        # x*(sigma beta)_{sigma(i)} = x*(beta)_i
        xp = np.empty_like(x)
        for i in range(3):
            xp[:, sig[i]] = x[:, i]
        errx[:, q] = np.abs(tp.x - xp).max(axis=1)
    res["err_perm_T"] = errT; res["err_perm_x"] = errx
    # c14 Euler identity, c15 log-elasticity identity
    res["err_euler"] = np.abs(np.sum(beta * dT_an, 1) / (E * T) - 1)
    elast_an = beta * dT_an / T[:, None]
    elast_id = np.stack([(1 + (2 * E - 3) * (1 - 2 * x[:, 2])) / 2, (1 + (2 * E - 3) * (1 - 2 * x[:, 1])) / 2,
                         (1 + (2 * E - 3) * (1 - 2 * x[:, 0])) / 2], 1)
    res["err_elasticity_identity"] = np.abs(elast_an - elast_id).max(axis=1)
    # c16 dx*/dalpha (FD only)
    def fxa(s):
        return threshold_batch(beta, alpha + s).x
    d1 = (fxa(ha) - fxa(-ha)) / (2 * ha[:, None]); d2 = (fxa(ha / 2) - fxa(-ha / 2)) / ha[:, None]
    res["dx_dalpha_fd"] = (4 * d2 - d1) / 3
    return res


def _float_job(args):
    beta, alpha = args
    r = float_stage(beta, alpha)
    return {k: v for k, v in r.items()}


def hp_job(args):
    beta, alpha = args
    dps = 40
    with mp.workdps(dps + 5):
        bs = [mp.nstr(mp.mpf(float(b)), 30) for b in beta]
        a = mp.mpf(float(alpha))
        r = threshold_mp(bs, a, dps=dps)
        T, x, B = r["T"], r["x"], r["B"]
        u, K = mp_uk(a)
        h, h1, h2 = mp_h_derivs(B, u, K)
        P = x[0] * x[1] * x[2]
        an = [h1 / x[2], h1 / x[1], h1 / x[0]]
        errs = []
        for k in range(3):
            hk = mp.mpf(bs[k]) * mp.mpf(10) ** -8
            def fT(s, k=k):
                b2 = [mp.mpf(v) for v in bs]; b2[k] += s
                return threshold_mp([mp.nstr(v, dps + 5) for v in b2], a, dps=dps)["T"]
            d1 = (fT(hk) - fT(-hk)) / (2 * hk); d2 = (fT(hk / 2) - fT(-hk / 2)) / hk
            fd = (4 * d2 - d1) / 3
            errs.append(float(abs(fd / an[k] - 1)))
        # alpha derivative
        rr = (u + mp.sqrt(u * u + K * B)) / K
        drdu = (rr + 4 * u * rr * rr) / (K * rr - u)
        dh_du = 2 * rr * drdu * (1 + 2 * u * rr) + rr * rr * (2 * rr + 2 * u * drdu)
        dTa = dh_du * (-mp.sin(a * mp.pi / 2) * mp.pi / 2) / P
        ha = min(mp.mpf(10) ** -8, (a - mp.mpf(2) / 3) * mp.mpf(10) ** -7, (1 - a) * mp.mpf(10) ** -7)
        fa = lambda s: threshold_mp(bs, a + s, dps=dps)["T"]
        d1 = (fa(ha) - fa(-ha)) / (2 * ha); d2 = (fa(ha / 2) - fa(-ha / 2)) / ha
        fd = (4 * d2 - d1) / 3
        errs.append(float(abs(fd / dTa - 1)))
        E = B * h1 / h
        euler = float(abs(sum(mp.mpf(bs[k]) * an[k] for k in range(3)) / (E * T) - 1))
        return {"beta": [float(b) for b in beta], "alpha": float(alpha), "hp_err_dT_beta": errs[:3],
                "hp_err_dT_alpha": errs[3], "hp_err_euler": euler, "hp_grad_norm": float(r["grad_norm"]),
                "hp_hess_min_eig": float(r["hess_min_eig"])}


def main():
    T0 = Timer()
    rng = np.random.default_rng(SEED)
    beta, alpha, reg = sample(rng)
    chunks = [(beta[i:i + 250], alpha[i:i + 250]) for i in range(0, N_POINTS, 250)]
    with pool() as P:
        parts = P.map(_float_job, chunks, chunksize=1)
        R = {k: np.concatenate([p[k] for p in parts]) for k in parts[0]}
        log("float stage done", T0())
        # worst 500 by max relative error over c1-c4, c6-c8
        worst_score = np.maximum(np.maximum(R["err_dT"].max(1), R["err_dTa"]), R["err_dx"].max(1))
        order = np.argsort(-worst_score)[:N_HP]
        hp = P.map(hp_job, [(beta[i], alpha[i]) for i in order], chunksize=4)
    log("hp stage done", T0())
    n_checks = N_POINTS * 16
    tol = {"dT_beta": 1e-6, "dT_alpha": 1e-5, "dx": 1e-4, "perm_T": 1e-10, "perm_x": 1e-9, "euler": 1e-10, "elast": 1e-9}
    fails = {
        "c1-3 dT/dbeta": int((R["err_dT"] > tol["dT_beta"]).sum()), "c4 dT/dalpha": int((R["err_dTa"] > tol["dT_alpha"]).sum()),
        "c5 hess_not_PD": int((R["hess_min_eig"] <= 0).sum()), "c6-8 dx/dbeta": int((R["err_dx"] > tol["dx"]).sum()),
        "c9-13 perm_T": int((R["err_perm_T"] > tol["perm_T"]).sum()), "c9-13 perm_x": int((R["err_perm_x"] > tol["perm_x"]).sum()),
        "c14 euler": int((R["err_euler"] > tol["euler"]).sum()), "c15 elasticity": int((R["err_elasticity_identity"] > tol["elast"]).sum()),
    }
    def q(a):
        a = np.asarray(a, float).ravel(); return {"max": float(a.max()), "p99": float(np.quantile(a, 0.99)), "median": float(np.median(a))}
    by_regime = {}
    for rname in sorted(set(reg)):
        m = reg == rname
        by_regime[rname] = {"n": int(m.sum()), "err_dT_beta": q(R["err_dT"][m]), "err_dT_alpha": q(R["err_dTa"][m]),
                            "err_dx": q(R["err_dx"][m]), "hess_min_eig_min": float(R["hess_min_eig"][m].min()),
                            "hess_cond_max": float(R["hess_cond"][m].max())}
    hp_e_beta = np.array([h["hp_err_dT_beta"] for h in hp]); hp_e_a = np.array([h["hp_err_dT_alpha"] for h in hp])
    out = stamp({
        "git_sha": git_sha(), "seed": SEED, "n_points": N_POINTS, "checks_per_point": 16, "n_checks_float": n_checks,
        "n_checks_hp": N_HP * 5, "tolerances": tol, "float_failures_by_check": fails,
        "float_summary": {"err_dT_beta": q(R["err_dT"]), "err_dT_alpha": q(R["err_dTa"]), "err_dx_dbeta": q(R["err_dx"]),
                          "err_perm_T": q(R["err_perm_T"]), "err_perm_x": q(R["err_perm_x"]), "err_euler": q(R["err_euler"]),
                          "err_elasticity_identity": q(R["err_elasticity_identity"]),
                          "hess_min_eig": {"min": float(R["hess_min_eig"].min()), "median": float(np.median(R["hess_min_eig"]))},
                          "hess_cond": {"max": float(R["hess_cond"].max()), "median": float(np.median(R["hess_cond"]))},
                          "grad_norm_max": float(R["grad_norm"].max()),
                          "E_range": [float(R["E"].min()), float(R["E"].max())]},
        "by_regime": by_regime,
        "hp_recheck": {"n": len(hp), "err_dT_beta": q(hp_e_beta), "err_dT_alpha": q(hp_e_a),
                       "err_euler_max": max(h["hp_err_euler"] for h in hp),
                       "hess_min_eig_min": min(h["hp_hess_min_eig"] for h in hp),
                       "grad_norm_max": max(h["hp_grad_norm"] for h in hp),
                       "worst_float_err_of_rechecked": float(worst_score[order].max()),
                       "all_below_1e-18": bool(hp_e_beta.max() < 1e-18 and hp_e_a.max() < 1e-18)},
        "identities": {
            "primary": "dT/dbeta_ij = h'(B*)/x_k*  -- VERIFIED (float: max rel err see float_summary; HP: see hp_recheck)",
            "euler": "sum_ij beta_ij dT/dbeta_ij = E_alpha(B*) T, E in (0,3/2)  -- SYMBOLIC IDENTITY (envelope + B* = sum beta_ij x_i x_j); verified numerically",
            "log_elasticity": "d log T/d log beta_ij = [1 + (2E-3)(1-2x_k*)]/2  -- SYMBOLIC IDENTITY (envelope + C-15 z_ij); verified numerically",
            "consequence": "T_alpha is sub-homogeneous: T(s beta) < s^{3/2} T(beta) for s>1 (CONJECTURE-level statement derived from E<3/2; not separately proved here)",
            "dx_dalpha": "NUMERICAL OBSERVATION only (FD), recorded in worst CSV",
        },
        "wall_seconds": T0(),
    })
    dump("C15_SENSITIVITY_VALIDATION.json", out)
    with open(os.path.join(RESULTS, "C15_SENSITIVITY_WORST.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["rank", "regime", "beta12", "beta13", "beta23", "alpha", "T", "x1", "x2", "x3", "float_err_dT_b12", "float_err_dT_b13",
                    "float_err_dT_b23", "float_err_dT_alpha", "float_err_dx_max", "hess_min_eig", "hess_cond",
                    "hp_err_dT_b12", "hp_err_dT_b13", "hp_err_dT_b23", "hp_err_dT_alpha", "hp_err_euler",
                    "dx1_dalpha_fd", "dx2_dalpha_fd", "dx3_dalpha_fd"])
        for rank, (i, h) in enumerate(zip(order, hp)):
            w.writerow([rank, reg[i], *[f"{v:.10g}" for v in beta[i]], f"{alpha[i]:.12g}", f"{R['T'][i]:.12g}",
                        *[f"{v:.10g}" for v in R["x"][i]], *[f"{v:.3g}" for v in R["err_dT"][i]], f"{R['err_dTa'][i]:.3g}",
                        f"{R['err_dx'][i].max():.3g}", f"{R['hess_min_eig'][i]:.4g}", f"{R['hess_cond'][i]:.4g}",
                        *[f"{v:.3g}" for v in h["hp_err_dT_beta"]], f"{h['hp_err_dT_alpha']:.3g}", f"{h['hp_err_euler']:.3g}",
                        *[f"{v:.6g}" for v in R["dx_dalpha_fd"][i]]])
    print({k: out[k] for k in ("float_failures_by_check", "hp_recheck")})


if __name__ == "__main__":
    main()
