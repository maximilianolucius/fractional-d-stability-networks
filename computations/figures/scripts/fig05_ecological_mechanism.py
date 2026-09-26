"""FIG-05 — ecological architecture: competitive no-go versus IGP signed-cycle mechanism (THEOREM DIAGRAM).

Arrows j -> i are drawn for every nonzero off-diagonal entry a_ij of the reduced matrix B = DF (effect of species
j on the per-capita growth of species i), labelled with the sign of a_ij.  The two oriented 3-cycle products are
written explicitly; their sum is L3 (C-13), and kappa = sum beta - 2 - L3 (C-10/C-13).
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch
import figstyle as S

S.setup()
fig, axes = plt.subplots(1, 2, figsize=(S.W2, S.W2 * 0.46))
POS = {"x": (0.0, -0.05), "y": (-0.85, 0.95), "z": (0.85, 0.95)}
NAMES = {"x": ("$x$", "basal prey\n(double Allee)"), "y": ("$y$", "consumer"), "z": ("$z$", "consumer")}


def node(ax, k, label, color):
    x, y = POS[k]
    sym, role = label
    ax.add_patch(Circle((x, y), 0.2, facecolor="white", edgecolor=color, lw=1.6, zorder=3))
    ax.text(x, y, sym, ha="center", va="center", fontsize=9, zorder=4)
    if k == "x":
        ax.text(x + 0.26, y, role, ha="left", va="center", fontsize=6.5, color=S.NDARK, zorder=4)
    else:
        ax.text(x, y + 0.3, role, ha="center", va="bottom", fontsize=6.5, color=S.NDARK, zorder=4)


def arrow(ax, src, dst, sign, curve, color=S.NDARK, lw=1.2):
    (x1, y1), (x2, y2) = POS[src], POS[dst]
    a = FancyArrowPatch((x1, y1), (x2, y2), connectionstyle=f"arc3,rad={curve}", arrowstyle="-|>", mutation_scale=9,
                        shrinkA=13, shrinkB=13, lw=lw, color=color, zorder=2)
    ax.add_patch(a)
    # sign label at the Bezier midpoint of the arc3 path: M + 0.5*rad*(-dy, dx)  (plus a small outward offset)
    dx, dy = x2 - x1, y2 - y1
    mx, my = (x1 + x2) / 2 + (0.5 * curve + 0.03 * np.sign(curve)) * (-dy), (y1 + y2) / 2 + (0.5 * curve + 0.03 * np.sign(curve)) * dx
    ax.text(mx, my, sign, color=color, fontsize=8, ha="center", va="center", fontweight="bold",
            bbox=dict(boxstyle="circle,pad=0.12", fc="white", ec="none"), zorder=5)


for ax, arch in zip(axes, ("competitive", "igp")):
    ax.set_xlim(-1.5, 1.5); ax.set_ylim(-1.05, 1.6); ax.set_aspect("equal"); ax.axis("off")
    ncol = S.NOGO if arch == "competitive" else S.BIO
    node(ax, "x", NAMES["x"], ncol); node(ax, "y", NAMES["y"], ncol)
    node(ax, "z", ("$z$", "consumer" if arch == "competitive" else "omnivore\n(IG predator)"), ncol)
    # trophic links: y on x negative (a12=-q1), x on y positive (a21=e1 q1); same for z
    arrow(ax, "y", "x", "$-$", 0.25); arrow(ax, "x", "y", "$+$", 0.25)
    arrow(ax, "z", "x", "$-$", -0.25); arrow(ax, "x", "z", "$+$", -0.25)
    if arch == "competitive":
        arrow(ax, "z", "y", "$-$", 0.25); arrow(ax, "y", "z", "$-$", 0.25)
        ax.text(0, 1.5, "competition $y\\leftrightarrow z$ ($-c_{12}$, $-c_{21}$)", ha="center", fontsize=7, color=S.NDARK)
        txt = ("$a_{12}a_{23}a_{31}=(-q_1)(-c_{12})(e_2q_2)>0$\n$a_{13}a_{32}a_{21}=(-q_2)(-c_{21})(e_1q_1)>0$\n"
               "$\\Rightarrow L_3>0,\\ \\kappa=\\sum\\beta-2-L_3<T_1(\\beta)$\ncannot reach $\\kappa>T_1$ on the strict-P stratum")
        ax.text(0, -0.8, txt, ha="center", va="center", fontsize=6.6, color=S.NOGO,
                bbox=dict(boxstyle="round,pad=0.35", fc="white", ec=S.NOGO, lw=0.8))
        ax.set_title("(a) two competing consumers: no-go", fontsize=8.2, color=S.NDARK, pad=2)
    else:
        arrow(ax, "z", "y", "$-$", 0.25, color=S.FRAC, lw=1.6); arrow(ax, "y", "z", "$+$", 0.25, color=S.FRAC, lw=1.6)
        ax.text(0, 1.5, "intraguild predation: $z$ eats $y$ ($-h$, $+e_3h$)", ha="center", fontsize=7, color=S.FRAC)
        txt = ("$a_{12}a_{23}a_{31}=(-q_1)(-h)(e_2q_2)=+e_2hq_1q_2$\n$a_{13}a_{32}a_{21}=(-q_2)(e_3h)(e_1q_1)=-e_1e_3hq_1q_2$\n"
               "$\\Rightarrow L_3=hq_1q_2(e_2-e_1e_3)/(sc_1c_2)<0$ if $e_1e_3>e_2$\nsigned 3-cycles lift $\\kappa$ above $T_1$: open band reachable")
        ax.text(0, -0.8, txt, ha="center", va="center", fontsize=6.6, color=S.BIO,
                bbox=dict(boxstyle="round,pad=0.35", fc="white", ec=S.BIO, lw=0.8))
        ax.set_title("(b) intraguild predation: signed 3-cycles", fontsize=8.2, color=S.NDARK, pad=2)
fig.subplots_adjust(wspace=0.05)
S.export(fig, "fig05_ecological_mechanism", {
    "claims": ["DA-02 (two-consumer no-go)", "DA-03 (IGP invariants)", "C-13 (loop coordinates)"],
    "formulas": ["L3=(a12 a23 a31 + a13 a32 a21)/(p1 p2 p3)", "kappa = beta12+beta13+beta23-2-L3", "T1 - kappa = 2 + L3 + 2 sum sqrt(beta_i beta_j) (two-consumer)"],
    "objects": {"network diagrams": "SCHEMATIC (THEOREM DIAGRAM: arrows = nonzero entries of DF with their exact signs)", "cycle formulas": "EXACT THEOREM CURVE (algebraic identities)"},
    "notes": "No data plotted; arrows j->i correspond to entries a_ij of the reduced matrix B = DF at a positive equilibrium."})
