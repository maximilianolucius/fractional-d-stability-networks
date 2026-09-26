"""FIG-01 — Matignon sector versus Hurwitz half-plane (THEOREM VISUALIZATION, exact sector)."""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Wedge, Polygon
import figstyle as S

S.setup()
fig, axes = plt.subplots(1, 2, figsize=(S.W2, S.W2 * 0.42))
for ax, alpha, label in zip(axes, (None, 0.9), ("(a)", "(b)")):
    a = 0.75 if alpha is None else alpha
    th = a * np.pi / 2
    R = 1.0
    ax.set_aspect("equal"); ax.set_xlim(-R, R); ax.set_ylim(-R, R)
    # classical Hurwitz half-plane: Re z < 0
    ax.add_patch(Polygon([[-R, -R], [0, -R], [0, R], [-R, R]], closed=True, facecolor=S.CLAS, alpha=0.12, edgecolor="none"))
    # fractional-only sliver: theta < |arg z| <= pi/2, Re z >= 0  (two wedges)
    for sgn in (1, -1):
        ax.add_patch(Wedge((0, 0), R * 1.5, np.degrees(sgn * th) if sgn > 0 else 90 * sgn, 90 if sgn > 0 else np.degrees(-th),
                           facecolor=S.FRAC, alpha=0.38, edgecolor="none"))
    # unstable Matignon sector |arg z| < theta (excluded)
    ax.add_patch(Wedge((0, 0), R * 1.5, -np.degrees(th), np.degrees(th), facecolor=S.NOGO, alpha=0.08, edgecolor="none"))
    # rays |arg z| = alpha pi/2
    for sgn in (1, -1):
        ax.plot([0, R * 1.5 * np.cos(th)], [0, sgn * R * 1.5 * np.sin(th)], color=S.FRAC, lw=S.LW_THM, solid_capstyle="round")
    ax.axhline(0, color=S.NDARK, lw=S.LW_AUX); ax.axvline(0, color=S.NDARK, lw=S.LW_AUX)
    ax.set_xticks([]); ax.set_yticks([])
    for sp in ax.spines.values():
        sp.set_visible(False)
    ax.text(R * 0.97, -0.06, r"$\mathrm{Re}\,z$", ha="right", va="top", fontsize=8, color=S.NDARK)
    ax.text(-0.04, R * 0.97, r"$\mathrm{Im}\,z$", ha="right", va="top", fontsize=8, color=S.NDARK)
    ax.text(-0.55, 0.55, "Hurwitz\n$\\mathrm{Re}\\,z<0$", ha="center", va="center", color=S.CLAS, fontsize=8)
    ax.text(0.30, 0.78, "fractional-only\n$\\alpha\\pi/2<|\\arg z|\\leq\\pi/2$", ha="center", va="center", color=S.FRAC, fontsize=7.5)
    ax.text(0.62, -0.42, "unstable\n$|\\arg z|<\\alpha\\pi/2$", ha="center", va="center", color=S.NOGO, fontsize=7.5)
    # angle arc
    t = np.linspace(0, th, 50); ax.plot(0.28 * np.cos(t), 0.28 * np.sin(t), color=S.NDARK, lw=S.LW_AUX)
    ax.text(0.33 * np.cos(th / 2), 0.33 * np.sin(th / 2), r"$\alpha\pi/2$", fontsize=7.5, color=S.NDARK, ha="left", va="bottom")
    S.panel_label(ax, label, x=0.0, y=0.98)
    ax.set_title(r"representative order, $\alpha=0.75$" if alpha is None else f"$\\alpha={alpha}$", fontsize=8.5, color=S.NDARK, pad=2)
fig.subplots_adjust(wspace=0.05)
S.export(fig, "fig01_matignon_hurwitz", {
    "claims": ["C-01 (Matignon, imported)", "C-02", "C-04 definition of F_alpha"],
    "formulas": ["Sigma_alpha = {z != 0 : |arg z| > alpha pi/2}", "Hurwitz: Re z < 0"],
    "parameters": {"panel_a_alpha_for_drawing": 0.75, "panel_b_alpha": 0.9},
    "objects": {"Matignon rays": "EXACT THEOREM CURVE", "Hurwitz half-plane": "EXACT THEOREM CURVE", "shaded regions": "SCHEMATIC (exact sectors)"},
    "notes": "Panel (a) is labelled as the representative order alpha=0.75 (Wave-2 fix); no numerical approximation involved."})
