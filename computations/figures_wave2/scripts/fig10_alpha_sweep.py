"""FIG-10 — alpha sweep of the full nonlinear W2-A model across the predicted boundary order alpha_*.
(a) envelope (running maximum over 10 time units) of the relative distance from coexistence versus time,
    worst-diagonal row scaling R_*, selected orders on both sides of alpha_*;
(b) late exponential growth rate versus alpha for both row scalings (dense grid if available), with the
    theorem boundary alpha_* (T_{alpha_*}(beta) = kappa).  NUMERICAL CORROBORATION only."""
from __future__ import annotations

import csv
import json
import os

import matplotlib.pyplot as plt
import numpy as np

import figstyle as S

S.setup()
tag = "_dense" if os.path.exists(os.path.join(S.DATA, "alpha_sweep_dense_summary.json")) else ""
M = json.load(open(os.path.join(S.DATA, f"alpha_sweep{tag}_summary.json"), encoding="utf-8"))
# panel (a) uses the base sweep's time series (same orders; the dense time series is not archived, 19 MB)
rows = list(csv.DictReader(open(os.path.join(S.DATA, "alpha_sweep_timeseries.csv"), encoding="utf-8")))
series = {}
for r in rows:
    series.setdefault((r["scaling"], float(r["alpha"])), []).append((float(r["t"]), float(r["relative_distance"])))
a_star = M["alpha_star_theorem"]; R = M["exit_radius"]
worst = sorted((r for r in M["runs"] if r["scaling"] == "worst"), key=lambda r: r["alpha"])
unsc = sorted((r for r in M["runs"] if r["scaling"] == "unscaled"), key=lambda r: r["alpha"])
d0 = worst[0]["pece"]["initial_relative_distance"]


def envelope(t, d, win=10.0):
    out = np.empty_like(d)
    j = 0
    for i in range(len(t)):
        while t[i] - t[j] > win:
            j += 1
        out[i] = d[j:i + 1].max()
    return out


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(S.W2, S.W2 * 0.40))
show = [0.80, 0.90, 0.94, round(a_star - 0.002, 4), round(a_star + 0.002, 4), 0.96, 0.98, 1.0]
cmap = plt.get_cmap("viridis")
for i, al in enumerate(show):
    key = ("worst", al)
    if key not in series:
        continue
    arr = np.array(series[key]); col = cmap(0.05 + 0.85 * i / (len(show) - 1))
    ax1.semilogy(arr[:, 0], envelope(arr[:, 0], arr[:, 1]), color=col, lw=1.0, ls="-" if al < a_star else "--", label=rf"$\alpha={al:g}$")
ax1.axhline(R, color=S.NOGO, lw=S.LW_AUX, ls=":")
ax1.text(1990, R * 1.3, "exit radius", color=S.NOGO, fontsize=6.5, ha="right")
ax1.set_xlim(0, 2000); ax1.set_ylim(1e-7, 0.6)
ax1.set_xlabel(r"nondimensional time $t$"); ax1.set_ylabel(r"envelope of $\|u/u^*-\mathbf{1}\|_2$")
ax1.set_title(r"scaling $R_*$: solid $\alpha<\alpha_*$, dashed $\alpha>\alpha_*$", fontsize=7.5, color=S.NDARK)
ax1.legend(fontsize=6, ncol=2, loc="lower right", handlelength=1.6, columnspacing=0.8)
S.panel_label(ax1, "(a)")

def rate(r):
    """late exponential growth rate of the relative distance: fitted on the last half of the run, or,
    for runs stopped at the exit radius, the mean rate log(R/d0)/t_exit (a lower-resolution estimate)."""
    p = r["pece"]
    if p["exit_time"] is None:
        return p["late_exponential_rate"], False
    return float(np.log(R / p["initial_relative_distance"]) / p["exit_time"]), True
lo_, hi_ = 0.940, 0.960
sel = [r for r in worst if lo_ - 1e-9 <= r["alpha"] <= hi_ + 1e-9]
aw = np.array([r["alpha"] for r in sel]); rw = [rate(r) for r in sel]
yw = 1e3 * np.array([v for v, _ in rw]); ew = np.array([e for _, e in rw])
ax2.axvspan(a_star, hi_ + 0.001, color=S.NOGO, alpha=0.08, lw=0)
ax2.axhline(0, color=S.NDARK, lw=S.LW_AUX)
ax2.axvline(a_star, color=S.FRAC, lw=S.LW_THM)
ax2.plot(aw[~ew], yw[~ew], marker="D", ms=3, color=S.FRAC, lw=S.LW_CMP, label=r"late fitted rate (run reaches $t_{\rm end}$)")
ax2.plot(aw[ew], yw[ew], marker="x", ms=4, color=S.NOGO, ls="none", label=r"mean rate $\log(0.2/d_0)/t_{\rm exit}$")
ax2.text(a_star - 0.0006, yw.max() * 0.45, rf"$\alpha_*={a_star:.5f}$" + "\n" + r"$T_{\alpha_*}(\beta)=\kappa$", color=S.FRAC, fontsize=6.8, ha="right", va="bottom")
ax2.text(lo_ + 0.0005, yw.max() * 0.9, "decay", color=S.FRAC, fontsize=7, va="top")
ax2.text(hi_ - 0.0005, yw.min() * 0.9 if False else yw.max() * 0.9, "growth", color=S.NOGO, fontsize=7, va="top", ha="right")
ax2.set_xlabel(r"order $\alpha$ (scaling $R_*$, $\Delta\alpha=0.001$)"); ax2.set_ylabel(r"growth rate of $\|u/u^*-\mathbf{1}\|_2$ $(\times10^{-3})$")
ax2.set_xlim(lo_ - 0.001, hi_ + 0.001)
ax2.legend(fontsize=6, loc="upper left", bbox_to_anchor=(0.0, 0.88), handlelength=1.6, frameon=False)
S.panel_label(ax2, "(b)")
fig.subplots_adjust(wspace=0.3)
S.export(fig, "fig10_alpha_sweep", {
    "claims": ["time-domain corroboration across alpha of the exact boundary order alpha_* (T_alpha(beta)=kappa) for the W2-A realization (reviewer R2-6)"],
    "objects": {"curves/markers": "NUMERICAL CORROBORATION (PECE with step refinement; DOP853 at alpha=1)", "alpha_*": "EXACT THEOREM VALUE (root of T_alpha(beta)=kappa; equals (2/pi) min|arg lambda(D_* B)|)"},
    "summary": {k: M[k] for k in ("alpha_star_theorem", "alpha_c_worst_diagonal", "kappa", "T1", "beta", "exit_radius", "steps", "t_end", "t_end_near")},
    "data": [f"computations/figures_wave2/data/alpha_sweep{tag}_summary.json", "computations/figures_wave2/data/alpha_sweep_timeseries.csv"]})
print("tag", tag, "n_worst", len(aw))
