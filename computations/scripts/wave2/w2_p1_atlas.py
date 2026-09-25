"""Wave 2 P1 — interval-certified atlas of T_alpha(beta).

Families (see task): A symmetric (b,b,b); B two-equal (b,b,1) and (1,1,c);
C all antagonistic (beta>1); D all below one; E the Wave-1 C-13 ecological
slices; F highly anisotropic (1e-4..1e4).  Alpha grid: 2/3+10^-k (k=1..8),
ordinary values, 1-10^-k (k=1..10).

Every point gets two certificates from fdsn.interval_cert (outward-rounded
interval arithmetic, dps=40; alpha/beta are the exact decimal strings in the
CSV):
  U  unconditional x-space branch-and-bound + certified-convex core
     (budget: 300k boxes / 240 s; may time out for very anisotropic beta);
  C  logit-coordinate certificate, conditional on C-15 Theorem 1 (strict
     convexity, proof-audited), cost independent of anisotropy.
The reported bracket is the intersection of the available certificates; the
`method` column states which certificates succeeded.  Two independent
cross-checks must land inside the bracket:
  * HP Newton value (threshold_mp, 50 digits), independent code path;
  * family A: closed form 27 h_alpha(b/3) (C-15 Corollary 1), 50 digits.
Optimizer enclosure: x* in ball(x_hat, x_enclosure_radius) (rigorous, see
interval_cert docstring).  No silent failures: status column.
Outputs: CERTIFIED_THRESHOLD_ATLAS.csv, CERTIFIED_THRESHOLD_ATLAS_SUMMARY.json
"""
from __future__ import annotations

import csv
import os
import sys
import time

import mpmath as mp
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from w2_common import RESULTS, Timer, dump, git_sha, log, peak_rss_mb, pool, stamp  # noqa: E402

from fdsn.c10_threshold import mp_h_alpha, mp_T1, threshold_mp  # noqa: E402
from fdsn.interval_cert import certify_threshold, certify_threshold_logit  # noqa: E402

mp.mp.dps = 60


def astr(x):
    return mp.nstr(mp.mpf(x), 45, strip_zeros=True)


def alpha_grid():
    near23 = [("2/3+1e-%d" % k, astr(mp.mpf(2) / 3 + mp.mpf(10) ** -k)) for k in range(1, 9)]
    ordinary = [(a, a) for a in ("0.7", "0.75", "0.8", "0.85", "0.9", "0.95")]
    near1 = [("1-1e-%d" % k, astr(1 - mp.mpf(10) ** -k)) for k in range(1, 11)]
    return near23 + ordinary + near1


ALL_ALPHA = alpha_grid()
ORD = [a for a in ALL_ALPHA if not a[0].startswith(("2/3", "1-"))]
NEAR = [a for a in ALL_ALPHA if a[0].startswith(("2/3", "1-"))]
SUB_ALPHA = [a for a in ALL_ALPHA if a[0] in ("2/3+1e-1", "2/3+1e-4", "2/3+1e-8", "0.7", "0.8", "0.9", "0.95",
                                                "1-1e-2", "1-1e-5", "1-1e-10")]


def fam_A():
    bs = [mp.nstr(mp.mpf(10) ** (mp.mpf(e) / 2), 12, strip_zeros=True) for e in range(-6, 7)]
    return [("A", (b, b, b), a) for b in bs for a in ALL_ALPHA]


def fam_B():
    rat = [mp.nstr(mp.mpf(10) ** (mp.mpf(e) / 6), 12, strip_zeros=True) for e in range(-18, 19)]
    pts = [("B", (b, b, "1"), a) for b in rat for a in ORD[::2] + [("0.99", "0.99")] ]  # 0.7,0.8,0.9,0.99
    sub = [rat[i] for i in (0, 6, 12, 18, 24, 30, 36)]
    pts += [("B", (b, b, "1"), a) for b in sub for a in NEAR]
    pts += [("B", ("1", "1", c), a) for c in sub for a in ORD]
    return pts


def fam_C():
    trip = [("2", "3", "5"), ("1.5", "1.5", "4"), ("10", "10", "10"), ("1.1", "1.2", "1.3"), ("3", "30", "300"),
            ("50", "2", "2"), ("1.01", "1.01", "20")]
    return [("C", t, a) for t in trip for a in SUB_ALPHA]


def fam_D():
    trip = [("0.5", "0.5", "0.5"), ("0.1", "0.3", "0.9"), ("0.02", "0.5", "0.8"), ("0.9", "0.9", "0.05"),
            ("0.001", "0.001", "0.5"), ("0.25", "0.75", "0.999")]
    return [("D", t, a) for t in trip for a in SUB_ALPHA]


def fam_E():
    trip = [("1", "1", "1"), ("3", "3", "3"), ("1.5", "4", "2"), ("0.5", "0.5", "0.5"), ("0.2", "0.8", "0.5"),
            ("3", "0.5", "1"), ("5", "0.2", "0.2"), ("1.01", "0.99", "1.005"), ("20", "20", "20")]
    return [("E", t, a) for t in trip for a in SUB_ALPHA]


def fam_F():
    trip = [("1e-4", "1", "1e4"), ("1e-4", "1e-4", "1e4"), ("1e4", "1e4", "1e-4"), ("1e-3", "100", "10"),
            ("1e-4", "1", "1"), ("1e4", "1", "1"), ("1e4", "1e-4", "1"), ("1e-2", "1e3", "1e-2"), ("1e3", "1e3", "1e-3")]
    return [("F", t, a) for t in trip for a in SUB_ALPHA]


def job(args):
    fam, beta, (aname, astr_) = args
    t0 = time.time()
    dps = 40 if not aname.startswith("2/3+1e-") or int(aname[-1]) < 6 else 50
    try:
        r = certify_threshold(beta, astr_, dps=dps, time_limit=240, max_boxes=300_000)
    except Exception as e:  # noqa: BLE001
        r = {"certified": False, "reason": f"exception: {e!r}"}
    try:
        c = certify_threshold_logit(beta, astr_, dps=dps)
    except Exception as e:  # noqa: BLE001
        c = {"certified": False, "reason": f"exception: {e!r}"}
    out = {"family": fam, "beta12": beta[0], "beta13": beta[1], "beta23": beta[2], "alpha_name": aname,
           "alpha": astr_, "dps": dps, "seconds": round(time.time() - t0, 2),
           "method": "interval B&B + certified-convex core (fdsn.interval_cert)"}
    with mp.workdps(60):
        bm = [mp.mpf(b) for b in beta]
        out["T1"] = mp.nstr(mp_T1(bm), 30)
        hp = threshold_mp(beta, astr_, dps=50)
        out["hp_T_dps50"] = mp.nstr(hp["T"], 45)
        cf = 27 * mp_h_alpha(bm[0] / 3, astr_) if fam == "A" else None
        out["closed_form_27h"] = mp.nstr(cf, 45) if cf is not None else ""
    certs = [(n, z) for n, z in (("U:x-space B&B (unconditional)", r), ("C:logit (conditional on C-15 Thm 1)", c)) if z.get("certified")]
    out["method"] = " + ".join(n for n, _ in certs) if certs else "none"
    out["unconditional_certified"] = bool(r.get("certified"))
    out["conditional_certified"] = bool(c.get("certified"))
    out["boxes"] = r.get("boxes", "")
    out["reason"] = "; ".join(f"{n}: {z.get('reason')}" for n, z in (("U", r), ("C", c)) if not z.get("certified"))
    if certs:
        L = max(z["L"] for _, z in certs)
        U = min(z["U"] for _, z in certs)
        assert L <= U, ("certificates disagree", beta, astr_, [(n, mp.nstr(z["L"], 30), mp.nstr(z["U"], 30)) for n, z in certs])
        best = min(certs, key=lambda nz: nz[1]["x_enclosure_radius"])[1]
        out.update({"status": "CERTIFIED", "L": mp.nstr(L, 45), "U": mp.nstr(U, 45),
                    "mid": mp.nstr((L + U) / 2, 45), "rel_width": mp.nstr((U - L) / L, 6),
                    "x1_hat": mp.nstr(best["x_hat"][0], 30), "x2_hat": mp.nstr(best["x_hat"][1], 30),
                    "x3_hat": mp.nstr(best["x_hat"][2], 30), "x_enclosure_radius": mp.nstr(best["x_enclosure_radius"], 6),
                    "core_rho": mp.nstr(r["rho_core"], 6) if r.get("certified") else "",
                    "hp_in_bracket": bool(L <= hp["T"] <= U),
                    "closed_form_in_bracket": bool(L <= cf <= U) if cf is not None else ""})
    else:
        out.update({"status": "NOT_CERTIFIED", "L": "", "U": mp.nstr(r["U"], 45) if "U" in r else "", "mid": "",
                    "rel_width": "", "x1_hat": "", "x2_hat": "", "x3_hat": "", "x_enclosure_radius": "",
                    "core_rho": "", "hp_in_bracket": "", "closed_form_in_bracket": ""})
    return out


COLS = ["family", "beta12", "beta13", "beta23", "alpha_name", "alpha", "status", "method", "unconditional_certified",
        "conditional_certified", "L", "U", "mid", "rel_width",
        "x1_hat", "x2_hat", "x3_hat", "x_enclosure_radius", "core_rho", "T1", "hp_T_dps50", "hp_in_bracket",
        "closed_form_27h", "closed_form_in_bracket", "dps", "boxes", "seconds", "method", "reason"]


def main():
    T = Timer()
    jobs = fam_A() + fam_B() + fam_C() + fam_D() + fam_E() + fam_F()
    log("P1 atlas points", len(jobs))
    rows = []
    with pool() as P:
        for k, r in enumerate(P.imap_unordered(job, jobs, chunksize=1)):
            rows.append(r)
            if k % 100 == 0:
                log(f"{k}/{len(jobs)} {T()} s")
    rows.sort(key=lambda r: (r["family"], float(r["beta12"]), float(r["beta13"]), float(r["beta23"]), float(r["alpha"])))
    path = os.path.join(RESULTS, "CERTIFIED_THRESHOLD_ATLAS.csv")
    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=COLS)
        w.writeheader()
        w.writerows(rows)
    cert = [r for r in rows if r["status"] == "CERTIFIED"]
    widths = np.array([float(r["rel_width"]) for r in cert])
    near = [r for r in cert if r["alpha_name"].startswith(("2/3", "1-"))]
    ordn = [r for r in cert if not r["alpha_name"].startswith(("2/3", "1-"))]
    fails = [r for r in rows if r["status"] != "CERTIFIED"]
    summ = stamp({
        "git_sha": git_sha(), "points_total": len(rows), "points_certified": len(cert), "failures": len(fails),
        "points_certified_unconditional": sum(r["unconditional_certified"] is True for r in cert),
        "points_certified_conditional_C15": sum(r["conditional_certified"] is True for r in cert),
        "points_both_certificates": sum(r["unconditional_certified"] is True and r["conditional_certified"] is True for r in cert),
        "conditional_only": [{k: r[k] for k in ("family", "beta12", "beta13", "beta23", "alpha_name", "reason")}
                             for r in cert if r["unconditional_certified"] is not True],
        "failure_list": [{k: r[k] for k in ("family", "beta12", "beta13", "beta23", "alpha_name", "reason")} for r in fails],
        "by_family": {f: {"total": sum(r["family"] == f for r in rows), "certified": sum(r["family"] == f for r in cert)}
                      for f in "ABCDEF"},
        "worst_rel_width": float(widths.max()) if len(widths) else None,
        "median_rel_width": float(np.median(widths)) if len(widths) else None,
        "worst_rel_width_ordinary": max(float(r["rel_width"]) for r in ordn) if ordn else None,
        "worst_rel_width_near_singular": max(float(r["rel_width"]) for r in near) if near else None,
        "target_met": {"ordinary<=1e-12": all(float(r["rel_width"]) <= 1e-12 for r in ordn),
                       "near<=1e-9": all(float(r["rel_width"]) <= 1e-9 for r in near)},
        "hp_in_bracket_all": all(r["hp_in_bracket"] is True for r in cert),
        "hp_outside_bracket": [{k: r[k] for k in ("family", "beta12", "beta13", "beta23", "alpha_name", "L", "U", "hp_T_dps50")}
                               for r in cert if r["hp_in_bracket"] is not True],
        "closed_form_A_in_bracket_all": all(r["closed_form_in_bracket"] is True for r in cert if r["family"] == "A"),
        "closed_form_outside": [{k: r[k] for k in ("beta12", "alpha_name", "L", "U", "closed_form_27h")}
                                for r in cert if r["family"] == "A" and r["closed_form_in_bracket"] is not True],
        "worst_x_enclosure_radius": max(float(r["x_enclosure_radius"]) for r in cert) if cert else None,
        "median_x_enclosure_radius": float(np.median([float(r["x_enclosure_radius"]) for r in cert])) if cert else None,
        "x_enclosure_radius_le_1e-30": sum(float(r["x_enclosure_radius"]) <= 1e-30 for r in cert),
        "max_seconds": max(r["seconds"] for r in rows), "total_cpu_seconds": sum(r["seconds"] for r in rows),
        "max_boxes": max(int(r["boxes"]) for r in rows if r["boxes"] != ""),
        "certificates_agree_all": True,
        "alpha_grid": [a[0] for a in ALL_ALPHA], "wall_seconds": T(), "memory": peak_rss_mb(),
        "evidence_label": "CERTIFIED (interval arithmetic) + HP cross-check (50 digits)",
    })
    dump("CERTIFIED_THRESHOLD_ATLAS_SUMMARY.json", summ)


if __name__ == "__main__":
    main()
