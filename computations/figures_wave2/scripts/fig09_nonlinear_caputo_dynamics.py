"""FIG-09 — full nonlinear time-domain comparison for the W2-A model."""
from __future__ import annotations

import csv
import json
import os

import matplotlib.pyplot as plt
import numpy as np

import figstyle as S

S.setup()
summary_path = os.path.join(S.DATA, "nonlinear_caputo_summary.json")
series_path = os.path.join(S.DATA, "nonlinear_caputo_timeseries.csv")
with open(summary_path, encoding="utf-8") as stream:
    M = json.load(stream)
with open(series_path, encoding="utf-8") as stream:
    rows = list(csv.DictReader(stream))

t = np.array([float(row["t"]) for row in rows])
eq = np.asarray(M["equilibrium"], dtype=float)
frac = np.array([[float(row[f"{name}_alpha_0.9"]) for name in ("x", "y", "z")] for row in rows])
classic = np.array(
    [
        [float(row[f"{name}_alpha_1"]) if row[f"{name}_alpha_1"] else np.nan for name in ("x", "y", "z")]
        for row in rows
    ]
)
frac_rel = frac / eq - 1.0
classic_rel = classic / eq - 1.0
frac_norm = np.linalg.norm(frac_rel, axis=1)
classic_norm = np.linalg.norm(classic_rel, axis=1)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(S.W2, S.W2 * 0.37))
for j, (label, color) in enumerate(((r"$x$", S.BIO), (r"$y$", S.NDARK), (r"$z$", S.FRAC))):
    ax1.plot(t, frac_rel[:, j], color=color, lw=1.15, label=label)
ax1.axhline(0.0, color=S.NLIGHT, lw=S.LW_AUX)
ax1.set_xlabel(r"nondimensional time $t$")
ax1.set_ylabel(r"relative deviation $u_i/u_i^*-1$")
ax1.set_title(r"full nonlinear Caputo model, $\alpha=0.9$")
ax1.legend(ncol=3, loc="upper right", columnspacing=0.9, handlelength=1.5)
S.panel_label(ax1, "(a)")

ax2.semilogy(t, frac_norm, color=S.FRAC, lw=S.LW_THM, label=r"Caputo, $\alpha=0.9$")
ax2.semilogy(t, classic_norm, color=S.CLAS, lw=S.LW_CMP, ls="--", label=r"classical, $\alpha=1$")
exit_radius = float(M["classical"]["exit_radius"])
exit_time = M["classical"]["exit_time"]
ax2.axhline(exit_radius, color=S.NOGO, lw=S.LW_AUX, ls=":", label="local-neighborhood exit")
if exit_time is not None:
    ax2.axvline(float(exit_time), color=S.NOGO, lw=S.LW_AUX, ls=":")
    ax2.text(float(exit_time) + 0.8, exit_radius * 0.72, rf"$t_{{\rm exit}}={float(exit_time):.2f}$", color=S.NOGO, fontsize=7)
ax2.set_xlabel(r"nondimensional time $t$")
ax2.set_ylabel(r"relative distance $\|u/u^*-\mathbf{1}\|_2$")
ax2.set_title(r"same parameters, scaling and initial state")
ax2.legend(loc="best", fontsize=6.7)
S.panel_label(ax2, "(b)")

fig.subplots_adjust(wspace=0.31)
S.export(
    fig,
    "fig09_nonlinear_caputo_dynamics",
    {
        "claims": ["time-domain numerical corroboration of the W2-A fractional-only realization"],
        "objects": {
            "both panels": "NUMERICAL CORROBORATION (full nonlinear model; no empirical calibration)",
            "alpha=0.9": "fractional Adams--Bashforth--Moulton PECE with step refinement",
            "alpha=1": "adaptive DOP853 integration stopped at the declared local-neighborhood exit",
        },
        "summary": M,
        "data": [
            "computations/figures_wave2/data/nonlinear_caputo_summary.json",
            "computations/figures_wave2/data/nonlinear_caputo_timeseries.csv",
        ],
    },
)
