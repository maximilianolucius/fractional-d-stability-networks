"""Wave 2 P2 — canonical genuinely fractional witness library (3x3).

A witness is a real 3x3 matrix A with -A strict P and, for the stated alpha,
    T_1(beta) < kappa < T_alpha(beta)          (genuinely fractional band, C-10)
so A is in F_alpha for the whole positive diagonal orbit but is not Hurwitz
D-stable.  Entries are integers / small rationals / short decimals.

Construction: (i) exhaustive small-integer search (diag in {-1,-2}, off-diag
in {-3,-2,-3/2,-1,-1/2,0,1/2,1,3/2,2,3}) filtered by strict-P and band membership on an alpha grid, then
representatives chosen by interpretability (few nonzeros, small entries);
(ii) hand-built families (Siami cyclic A_gamma, boundary-tuned decimals).
For 'close to boundary' witnesses one 3-cycle entry whose reciprocal partner
is zero is tuned: it moves kappa linearly and leaves beta unchanged.

Per witness: invariants (exact rationals), T_1, T_alpha (HP 40 digits and,
for >= 8 witnesses, CERTIFIED interval bracket on the exact rational beta),
margins, x*, D*, direct Matignon margin at D* (mp.eig 40 digits), independent
global direct margin minimisation (float, fdsn.direct_margin), Hurwitz status
at D=I, explicit D_H (Cain minimiser) with a nonnegative-real-part eigenvalue
verified in mp, loop coordinates g_ij, L3, l123, l132, Phi and the C-11 test.
Outputs: CANONICAL_WITNESSES.{csv,json}, CANONICAL_WITNESSES_README.md
"""
from __future__ import annotations

import csv
import itertools
import os
import sys
from fractions import Fraction as Fr

import mpmath as mp
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from w2_common import RESULTS, Timer, dump, git_sha, log, pool, stamp  # noqa: E402

from fdsn.c10_threshold import T1, invariants_batch, mp_T1, rho_alpha, threshold_batch, threshold_mp  # noqa: E402
from fdsn.direct_margin import min_margin, mp_margin  # noqa: E402
from fdsn.interval_cert import certify_threshold  # noqa: E402

ALPHAS = [0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 0.99]


# ----------------------------------------------------------------- exact invariants

def fr(x):
    return x if isinstance(x, Fr) else Fr(str(x))


def inv_exact(A):
    a = [[fr(v) for v in row] for row in A]
    p = [-a[i][i] for i in range(3)]
    m12 = a[0][0] * a[1][1] - a[0][1] * a[1][0]
    m13 = a[0][0] * a[2][2] - a[0][2] * a[2][0]
    m23 = a[1][1] * a[2][2] - a[1][2] * a[2][1]
    det = (a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1]) - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0])
           + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0]))
    q = -det
    P = p[0] * p[1] * p[2]
    beta = (m12 / (p[0] * p[1]), m13 / (p[0] * p[2]), m23 / (p[1] * p[2]))
    kappa = q / P
    g = (a[0][1] * a[1][0] / (p[0] * p[1]), a[0][2] * a[2][0] / (p[0] * p[2]), a[1][2] * a[2][1] / (p[1] * p[2]))
    l123 = a[0][1] * a[1][2] * a[2][0] / P
    l132 = a[0][2] * a[2][1] * a[1][0] / P
    return {"p": p, "m": (m12, m13, m23), "q": q, "beta": beta, "kappa": kappa, "g": g, "l123": l123, "l132": l132,
            "L3": l123 + l132, "strictP": all(v > 0 for v in p) and all(v > 0 for v in (m12, m13, m23)) and q > 0}


def fs(x):
    """Fraction -> short string."""
    x = fr(x)
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


# ----------------------------------------------------------------- integer search

def _search_job(diag):
    vals = [-3, -2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2, 3]
    found = []
    As = []
    for off in itertools.product(vals, repeat=6):
        A = np.array([[diag[0], off[0], off[1]], [off[2], diag[1], off[3]], [off[4], off[5], diag[2]]], float)
        As.append(A)
    As = np.array(As)
    p, m, q, beta, kappa = invariants_batch(As)
    del p
    ok = np.all(m > 0, 1) & (q > 0)
    As, beta, kappa = As[ok], beta[ok], kappa[ok]
    t1 = T1(beta)
    above = kappa > t1
    As, beta, kappa, t1 = As[above], beta[above], kappa[above], t1[above]
    for a in ALPHAS:
        Ta = threshold_batch(beta, a).T
        inb = kappa < Ta
        for i in np.nonzero(inb)[0]:
            found.append((As[i].tolist(), a, float(kappa[i] / t1[i] - 1), float(1 - kappa[i] / Ta[i])))
    return found


def integer_search(P):
    diags = list(itertools.product([-1, -2], repeat=3))
    res = P.map(_search_job, diags)
    return [f for r in res for f in r]


def score(A):
    A = np.asarray(A)
    off = A - np.diag(np.diag(A))
    return (np.count_nonzero(off), np.abs(off).sum(), np.abs(np.diag(A)).sum())


def hurwitz_at_I(A):
    ev = np.linalg.eigvals(np.asarray(A, float))
    return float(ev.real.max()) < -1e-12


def pick(found, pred, n, key=None, used=None):
    cand = [f for f in found if pred(f)]
    cand.sort(key=key or (lambda f: (score(f[0]), -min(f[2], f[3]))))
    out = []
    for f in cand:
        key_ = tuple(map(tuple, f[0]))
        if used is not None and key_ in used:
            continue
        out.append(f)
        if used is not None:
            used.add(key_)
        if len(out) == n:
            break
    return out


# ----------------------------------------------------------------- hand-built families

def a_gamma(g):
    return [[-1, 0, -fr(g)], [fr(g), -1, 0], [0, fr(g), -1]]


def tune_entry(A, ij, target_kappa, digits=3, side="below"):
    """Set A[i][j] (whose partner A[j][i] must be 0) so that kappa hits target, rounded to
    `digits` significant decimals, rounding so that kappa stays on `side` of target."""
    i, j = ij
    A = [[fr(v) for v in r] for r in A]
    assert A[j][i] == 0
    A0 = [r[:] for r in A]; A0[i][j] = Fr(0)
    A1 = [r[:] for r in A]; A1[i][j] = Fr(1)
    k0, k1 = inv_exact(A0)["kappa"], inv_exact(A1)["kappa"]
    slope = k1 - k0
    exact = (fr(target_kappa) - k0) / slope
    # round to `digits` significant figures
    mag = 10 ** (digits - 1 - int(mp.floor(mp.log10(abs(float(exact))))))
    lo = Fr(int(mp.floor(float(exact) * mag)), mag)
    hi = Fr(int(mp.ceil(float(exact) * mag)), mag)
    for cand in ([lo, hi] if (slope > 0) == (side == "below") else [hi, lo]):
        A[i][j] = cand
        k = inv_exact(A)["kappa"]
        if (side == "below" and k < fr(target_kappa)) or (side == "above" and k > fr(target_kappa)):
            return A
    raise RuntimeError("tuning failed")


def kappa_target(beta, alpha, frac):
    """kappa at position `frac` of the band [T1, T_alpha] (HP)."""
    with mp.workdps(40):
        b = [mp.mpf(v.numerator) / v.denominator for v in beta]
        t1 = mp_T1(b)
        Ta = threshold_mp([mp.nstr(v, 45) for v in b], repr(alpha), dps=40)["T"]
        return t1 + (Ta - t1) * mp.mpf(frac)


# ----------------------------------------------------------------- full characterisation

def characterise(A, alpha, tags, certify=False):
    A = [[fr(v) for v in r] for r in A]
    inv = inv_exact(A)
    assert inv["strictP"], A
    beta_s = [fs(v) for v in inv["beta"]]
    dps = 40
    with mp.workdps(dps + 10):
        b = [mp.mpf(v.numerator) / v.denominator for v in inv["beta"]]
        kap = mp.mpf(inv["kappa"].numerator) / inv["kappa"].denominator
        t1 = mp_T1(b)
        beta_dec = [mp.nstr(v, 45) for v in b]
        r = threshold_mp(beta_dec, repr(alpha), dps=dps)
        Ta, xs = r["T"], r["x"]
        p = [mp.mpf(v.numerator) / v.denominator for v in inv["p"]]
        Am = mp.matrix([[mp.mpf(v.numerator) / v.denominator for v in row] for row in A])
        # D* from x*: x_i = p_i d_i / a_D  ->  d_i = x_i / p_i (common scale free)
        d = [xs[i] / p[i] for i in range(3)]
        gm = (d[0] * d[1] * d[2]) ** (mp.mpf(1) / 3)
        d = [v / gm for v in d]
        m_at_dstar, ev_dstar = mp_margin(Am, d, alpha, dps)
        # D_H: Cain minimiser d_i ∝ sqrt(m_jk/p_i); Routh-Hurwitz ab/c = Phi < 1 there
        m12, m13, m23 = (mp.mpf(v.numerator) / v.denominator for v in inv["m"])
        dh = [mp.sqrt(m23 / p[0]), mp.sqrt(m13 / p[1]), mp.sqrt(m12 / p[2])]
        gmh = (dh[0] * dh[1] * dh[2]) ** (mp.mpf(1) / 3)
        dh = [v / gmh for v in dh]
        MH = mp.matrix([[dh[i] * Am[i, j] for j in range(3)] for i in range(3)])
        evH = mp.eig(MH, left=False, right=False)
        maxreH = max(mp.re(e) for e in evH)
        evI = mp.eig(Am, left=False, right=False)
        maxreI = max(mp.re(e) for e in evI)
        margin_I = min(abs(mp.arg(e)) for e in evI) - mp.mpf(alpha) * mp.pi / 2
        phi = t1 / kap
        W = Ta - t1
        out = {
            "tags": tags, "A": [[fs(v) for v in row] for row in A], "A_float": [[float(v) for v in row] for row in A],
            "alpha": alpha,
            "p": [fs(v) for v in inv["p"]], "m12_m13_m23": [fs(v) for v in inv["m"]], "q": fs(inv["q"]),
            "beta": beta_s, "beta_float": [float(v) for v in inv["beta"]], "kappa": fs(inv["kappa"]),
            "kappa_float": float(inv["kappa"]),
            "g": [fs(v) for v in inv["g"]], "l123": fs(inv["l123"]), "l132": fs(inv["l132"]), "L3": fs(inv["L3"]),
            "T1": mp.nstr(t1, 30), "T_alpha_hp40": mp.nstr(Ta, 35), "T_alpha_label": "HP (40 digits)",
            "m_Cain": mp.nstr(kap - t1, 20), "m_frac": mp.nstr(Ta - kap, 20),
            "m_Cain_over_T1": mp.nstr((kap - t1) / t1, 12), "m_frac_over_Talpha": mp.nstr((Ta - kap) / Ta, 12),
            "band_position_(kappa-T1)/(Talpha-T1)": mp.nstr((kap - t1) / W, 12),
            "band_width_W": mp.nstr(W, 20), "band_relative_width_W_over_T1": mp.nstr(W / t1, 12),
            "x_star": [mp.nstr(v, 25) for v in xs], "D_star_geomean1": [mp.nstr(v, 25) for v in d],
            "direct_margin_at_D_star_rad": mp.nstr(m_at_dstar, 20),
            "eig_D_star_A": [mp.nstr(e, 15) for e in ev_dstar],
            "hurwitz_at_I": bool(maxreI < 0), "max_Re_eig_A": mp.nstr(maxreI, 15),
            "matignon_margin_at_I_rad": mp.nstr(margin_I, 15),
            "D_H_cain_minimiser_geomean1": [mp.nstr(v, 25) for v in dh],
            "max_Re_eig_D_H_A": mp.nstr(maxreH, 15), "D_H_witnesses_classical_failure": bool(maxreH >= 0),
            "Phi": mp.nstr(phi, 15), "rho_alpha": rho_alpha(alpha), "C11_certificate_passes": bool(phi > rho_alpha(alpha)),
            "hp_grad_norm": mp.nstr(r["grad_norm"], 5),
        }
    # independent global direct check (float): min over D of margin at alpha and at alpha=1
    Af = np.array(out["A_float"])[None]
    dm = min_margin(Af, alpha, half_width=14, step=0.5, n_starts=3)
    dh1 = min_margin(Af, 1.0, half_width=14, step=0.5, n_starts=3)
    out["direct_global_min_margin_float"] = float(dm["margin"][0])
    out["direct_global_min_margin_alpha1_float"] = float(dh1["margin"][0])
    out["direct_worst_D_float_geomean1"] = (dm["d"][0] / np.prod(dm["d"][0]) ** (1 / 3)).tolist()
    out["independent_checks_consistent"] = bool(dm["margin"][0] > 0 and dh1["margin"][0] < 0 and maxreH >= 0
                                                and float(out["direct_margin_at_D_star_rad"]) > 0)
    if certify:
        c = certify_threshold(beta_s, repr(alpha), dps=40, time_limit=1500, max_boxes=2_000_000)
        if c.get("certified"):
            out.update({"T_alpha_certified_L": mp.nstr(c["L"], 35), "T_alpha_certified_U": mp.nstr(c["U"], 35),
                        "T_alpha_certified_rel_width": mp.nstr(c["rel_width"], 5),
                        "T_alpha_label": "CERTIFIED (interval) + HP", "certified_boxes": c["boxes"],
                        "x_enclosure_radius": mp.nstr(c["x_enclosure_radius"], 5),
                        "kappa_below_certified_L": bool(mp.mpf(out["kappa_float"]) < c["L"]) and
                        bool(mp.mpf(inv["kappa"].numerator) / inv["kappa"].denominator < c["L"])})
        else:
            out.update({"T_alpha_label": "HP (40 digits); certification FAILED: " + str(c.get("reason"))})
    return out


def _char_job(args):
    return characterise(*args)


def build_library(found):
    used = set()
    W = []  # (A, alpha, tags, certify)

    def add(A, alpha, tags, certify=False):
        W.append((A, alpha, tags, certify))
        used.add(tuple(map(tuple, [[float(fr(v)) for v in r] for r in A])))

    # 1 + 10: Siami cyclic slice (non-Hurwitz at I for gamma > 2)
    add(a_gamma(Fr(5, 2)), 0.9, ["1 symmetric cyclic (Siami)", "10 non-Hurwitz at I"], True)
    add(a_gamma(3), 0.8, ["1 symmetric cyclic (Siami)", "10 non-Hurwitz at I"], True)
    add(a_gamma(Fr(21, 10)), 0.95, ["1 symmetric cyclic (Siami)", "10 non-Hurwitz at I"], True)
    # 6: close to exact fractional boundary on the Siami slice (R3(0.9)=2.7563..)
    add(a_gamma(Fr(275, 100)), 0.9, ["1 symmetric cyclic (Siami)", "6 close to fractional boundary", "10 non-Hurwitz at I"], True)
    # 5: close to Cain boundary on the Siami slice
    add(a_gamma(Fr(201, 100)), 0.9, ["1 symmetric cyclic (Siami)", "5 close to Cain boundary", "10 non-Hurwitz at I"])
    # 7: close to alpha=2/3 (R3(0.67)=165.9, R3(0.68)=...)
    add(a_gamma(150), 0.67, ["1 symmetric cyclic (Siami)", "7 close to alpha=2/3", "10 non-Hurwitz at I"], True)
    add(a_gamma(40), 0.68, ["1 symmetric cyclic (Siami)", "7 close to alpha=2/3", "10 non-Hurwitz at I"])
    # 8: close to alpha=1 (R3(0.999)=2.0055, R3(0.99)=2.0541)
    add(a_gamma(Fr(2005, 1000)), 0.999, ["1 symmetric cyclic (Siami)", "8 close to alpha=1", "6 close to fractional boundary"], True)
    add(a_gamma(Fr(203, 100)), 0.99, ["1 symmetric cyclic (Siami)", "8 close to alpha=1"])
    # integer-search representatives
    is_hur = lambda f: hurwitz_at_I(f[0])
    strong_ant = lambda f: all(g < -1 for g in inv_exact(f[0])["g"])
    mixed = lambda f: (any(g > 0 for g in inv_exact(f[0])["g"]) and any(g < 0 for g in inv_exact(f[0])["g"]))
    for f in pick(found, lambda f: f[1] in (0.8, 0.9) and f[2] > 0.15 and f[3] > 0.15 and not is_hur(f), 4, used=used):
        add(f[0], f[1], ["2 generic nonsymmetric strict-P", "10 non-Hurwitz at I"], len(W) < 12)
    for f in pick(found, lambda f: strong_ant(f) and f[3] > 0.05 and f[2] > 0.05, 4, used=used):
        add(f[0], f[1], ["3 strong antagonistic pair loops"] + (["9 Hurwitz at I, not D-stable"] if is_hur(f) else ["10 non-Hurwitz at I"]))
    for f in pick(found, lambda f: mixed(f) and f[3] > 0.05 and f[2] > 0.05, 4, used=used):
        add(f[0], f[1], ["4 mixed ecological signs"] + (["9 Hurwitz at I, not D-stable"] if is_hur(f) else ["10 non-Hurwitz at I"]))
    for f in pick(found, lambda f: is_hur(f) and f[3] > 0.05 and f[2] > 0.05, 4, used=used):
        add(f[0], f[1], ["9 Hurwitz at I, not D-stable", "2 generic nonsymmetric strict-P"], len(W) < 20)
    def exact_band(f):
        e = inv_exact(f[0]); b = e["beta"]
        # exact strictness: kappa > T1 requires kappa - sum(beta) > 2*sum(sqrt(bi bj)) -> compare in HP (60 digits)
        with mp.workdps(60):
            bb = [mp.mpf(v.numerator) / v.denominator for v in b]
            return mp.mpf(e["kappa"].numerator) / e["kappa"].denominator - mp_T1(bb) > mp.mpf(10) ** -50
    for f in pick(found, lambda f: 1e-9 < f[2] < 0.05 and f[3] > 0.1 and exact_band(f), 2, key=lambda f: (f[2], score(f[0])), used=used):
        add(f[0], f[1], ["5 close to Cain boundary (integer)"])
    for f in pick(found, lambda f: 0 < f[3] < 0.05 and f[2] > 0.1, 2, key=lambda f: (f[3], score(f[0])), used=used):
        add(f[0], f[1], ["6 close to fractional boundary (integer)"])
    # decimal-tuned boundary witnesses: integer matrix with a free 3-cycle entry (partner zero)
    tunable = [f for f in found if any(fr(f[0][i][j]) != 0 and fr(f[0][j][i]) == 0 for i in range(3) for j in range(3) if i != j)]
    tunable.sort(key=lambda f: score(f[0]))
    done = 0
    for f in tunable:
        A = f[0]
        ij = next((i, j) for i in range(3) for j in range(3) if i != j and fr(A[i][j]) != 0 and fr(A[j][i]) == 0)
        beta = inv_exact(A)["beta"]
        try:
            A6 = tune_entry(A, ij, kappa_target(beta, f[1], 0.99), digits=4, side="below")
            A5 = tune_entry(A, ij, kappa_target(beta, f[1], 0.01), digits=4, side="above")
        except Exception:
            continue
        if tuple(map(tuple, [[float(fr(v)) for v in r] for r in A6])) in used:
            continue
        add(A6, f[1], ["6 close to fractional boundary (decimal-tuned)", "2 generic nonsymmetric strict-P"], done == 0)
        add(A5, f[1], ["5 close to Cain boundary (decimal-tuned)", "2 generic nonsymmetric strict-P"])
        done += 1
        if done == 2:
            break
    # near alpha=1 / 2/3 with generic integer matrices
    for f in pick(found, lambda f: f[1] == 0.99 and f[2] > 0.02 and f[3] > 0.02, 2, used=used):
        add(f[0], 0.99, ["8 close to alpha=1 (integer)"])
    # alpha = 0.68 with a generic matrix: kappa must be far above T1 but below T_0.68
    for f in pick(found, lambda f: f[1] == 0.7 and f[2] > 3, 2, key=lambda f: (-f[2], score(f[0])), used=used):
        add(f[0], 0.68, ["7 close to alpha=2/3 (integer, alpha=0.68)"])
    return W


COLS = ["id", "tags", "alpha", "a11", "a12", "a13", "a21", "a22", "a23", "a31", "a32", "a33", "beta12", "beta13", "beta23",
        "kappa", "T1", "T_alpha_hp40", "T_alpha_label", "T_alpha_certified_L", "T_alpha_certified_U",
        "m_Cain", "m_frac", "m_Cain_over_T1", "m_frac_over_Talpha", "band_position_(kappa-T1)/(Talpha-T1)",
        "x_star", "D_star_geomean1", "direct_margin_at_D_star_rad", "direct_global_min_margin_float",
        "direct_global_min_margin_alpha1_float", "hurwitz_at_I", "max_Re_eig_A", "D_H_cain_minimiser_geomean1",
        "max_Re_eig_D_H_A", "g", "L3", "l123", "l132", "Phi", "C11_certificate_passes", "independent_checks_consistent"]


def main():
    T = Timer()
    with pool() as P:
        found = integer_search(P)
        log("integer search: band cases", len(found))
        W = build_library(found)
        log("library size", len(W))
        res = P.map(_char_job, W, chunksize=1)
    for k, r in enumerate(res):
        r["id"] = f"W{k + 1:02d}"
    rows = []
    for r in res:
        row = {c: r.get(c, "") for c in COLS}
        for i in range(3):
            for j in range(3):
                row[f"a{i + 1}{j + 1}"] = r["A"][i][j]
        row["beta12"], row["beta13"], row["beta23"] = r["beta"]
        row["tags"] = "; ".join(r["tags"])
        row["x_star"] = " ".join(v[:12] for v in r["x_star"])
        row["D_star_geomean1"] = " ".join(v[:12] for v in r["D_star_geomean1"])
        row["D_H_cain_minimiser_geomean1"] = " ".join(v[:12] for v in r["D_H_cain_minimiser_geomean1"])
        row["g"] = " ".join(r["g"])
        rows.append(row)
    with open(os.path.join(RESULTS, "CANONICAL_WITNESSES.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=COLS)
        w.writeheader(); w.writerows(rows)
    cats = {}
    for r in res:
        for t in r["tags"]:
            cats.setdefault(t.split(" ")[0], []).append(r["id"])
    summary = stamp({"git_sha": git_sha(), "n_witnesses": len(res),
                     "n_certified": sum(r["T_alpha_label"].startswith("CERTIFIED") for r in res),
                     "all_independent_checks_consistent": all(r["independent_checks_consistent"] for r in res),
                     "inconsistent_ids": [r["id"] for r in res if not r["independent_checks_consistent"]],
                     "categories": cats, "integer_search_band_cases": len(found),
                     "integer_search_space": "diag in {-1,-2}^3, offdiag in {-3,-2,-3/2,-1,-1/2,0,1/2,1,3/2,2,3}^6, alphas " + str(ALPHAS),
                     "wall_seconds": T()})
    dump("CANONICAL_WITNESSES.json", {"summary": summary, "witnesses": res})
    readme = f"""# Canonical genuinely fractional witnesses (Wave 2, P2)

{len(res)} real 3x3 matrices with -A strict P and T_1(beta) < kappa < T_alpha(beta) at the stated alpha:
in F_alpha over the entire positive diagonal orbit (C-10) but not Hurwitz D-stable (Cain).
Generated by `computations/scripts/wave2/w2_p2_witnesses.py` at commit {git_sha()} (baseline {summary['baseline_sha']}).

Columns / fields
- `A`: exact entries (integers, rationals `p/q`, or short decimals given as rationals).
- `p`, `m12_m13_m23`, `q`: strict-P principal-minor data of -A (exact).
- `beta`, `kappa`: C-10 orbit invariants (exact rationals); `g`, `l123`, `l132`, `L3`: C-13 loop coordinates.
- `T1`: Cain threshold (sqrt b12 + sqrt b13 + sqrt b23)^2; `T_alpha_hp40`: exact C-10 threshold, HP Newton, 40 digits;
  `T_alpha_certified_L/U`: CERTIFIED interval bracket (fdsn.interval_cert) on the exact rational beta
  ({summary['n_certified']} witnesses); label column states which.
- `m_Cain = kappa - T1 > 0` (fails Cain), `m_frac = T_alpha - kappa > 0` (inside F_alpha); normalised versions
  `m_Cain/T1`, `m_frac/T_alpha` and the band position (kappa - T1)/(T_alpha - T1) in (0,1).
- `x_star`: unique simplex minimiser (C-15); `D_star_geomean1`: d_i = x_i*/p_i normalised to unit geometric mean,
  the worst positive diagonal of the orbit; `direct_margin_at_D_star_rad`: min_i |arg lambda_i(D* A)| - alpha pi/2
  by mp.eig (40 digits) -- must be > 0 and is the smallest orbit margin up to the boundary-normalisation;
  `direct_global_min_margin_float`: independent float minimisation over all D (must be > 0);
  `direct_global_min_margin_alpha1_float`: same at alpha = 1 (must be < 0: not Hurwitz D-stable).
- `hurwitz_at_I`, `max_Re_eig_A`: status of A itself (category 9 vs 10).
- `D_H_cain_minimiser_geomean1`: explicit positive diagonal (Cain minimiser d_i ∝ sqrt(m_jk/p_i)) at which
  D_H A has an eigenvalue with Re >= 0 (`max_Re_eig_D_H_A`, mp) -- explicit witness of classical D-instability.
- `Phi`, `rho_alpha`, `C11_certificate_passes`: the C-11 sufficient certificate (sufficient, not necessary).
- `independent_checks_consistent`: all of {{direct margin at D* > 0, global direct margin > 0, global direct
  margin at alpha=1 < 0, Re eig(D_H A) >= 0}} hold -> two code paths agree with the C-10 classification.

Categories (task list): {cats}

Evidence labels: invariants EXACT; T_alpha HP (40 digits) or CERTIFIED; direct margins HP (mp.eig) and FLOAT.
"""
    open(os.path.join(RESULTS, "CANONICAL_WITNESSES_README.md"), "w").write(readme)
    print(summary)


if __name__ == "__main__":
    main()
