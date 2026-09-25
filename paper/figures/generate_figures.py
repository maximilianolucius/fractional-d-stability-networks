#!/usr/bin/env python3
"""Generate the publication figures used by the manuscript variants.

The visual system is deliberately conservative: an accessible Okabe--Ito
palette, redundant line styles, restrained grids, and type sized for the
figures' final width in the paper. Every output is saved as vector PDF for
the manuscript and as a high-resolution PNG for visual QA.
"""

from pathlib import Path
import math

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
from matplotlib.patches import Arc, Patch, Wedge
from matplotlib.ticker import FixedLocator, LogFormatterMathtext, MaxNLocator
import pandas as pd


ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "paper" / "figures" / "generated"
OUT.mkdir(parents=True, exist_ok=True)
DATA = ROOT / "computations" / "results" / "wave2" / "FIGURE_DATA"

# Okabe--Ito: color-vision-deficiency safe and distinguishable in print when
# paired with the line styles below.
BLUE = "#0072B2"
ORANGE = "#D55E00"
GREEN = "#009E73"
PURPLE = "#CC79A7"
SKY = "#56B4E9"
YELLOW = "#E69F00"
INK = "#202124"
MID_GRAY = "#6B7280"
LIGHT_GRAY = "#D7DCE2"
PANEL_GRAY = "#F4F5F7"

SERIES_COLORS = (BLUE, ORANGE, GREEN, PURPLE)
SERIES_STYLES = ("-", (0, (5, 2)), (0, (5, 1.6, 1.2, 1.6)), (0, (1.2, 1.8)))
SERIES_MARKERS = ("o", "s", "^", "D")


def configure_style() -> None:
    """Set a compact journal style before constructing any figure."""

    plt.rcParams.update(
        {
            "font.family": "serif",
            "font.serif": ["STIX Two Text", "STIXGeneral", "DejaVu Serif"],
            "mathtext.fontset": "stix",
            "font.size": 10.5,
            "axes.titlesize": 11.5,
            "axes.titleweight": "semibold",
            "axes.labelsize": 10.5,
            "axes.labelcolor": INK,
            "axes.edgecolor": INK,
            "axes.linewidth": 0.85,
            "xtick.labelsize": 9.2,
            "ytick.labelsize": 9.2,
            "xtick.color": INK,
            "ytick.color": INK,
            "xtick.direction": "out",
            "ytick.direction": "out",
            "xtick.major.width": 0.8,
            "ytick.major.width": 0.8,
            "xtick.major.size": 4.0,
            "ytick.major.size": 4.0,
            "legend.fontsize": 8.7,
            "legend.title_fontsize": 9.0,
            "lines.linewidth": 2.15,
            "lines.solid_capstyle": "round",
            "lines.dash_capstyle": "round",
            "axes.spines.top": False,
            "axes.spines.right": False,
            "pdf.fonttype": 42,
            "ps.fonttype": 42,
            "savefig.facecolor": "white",
        }
    )


def style_axes(ax, *, grid_axis: str = "y") -> None:
    """Apply the shared low-contrast background and grid treatment."""

    ax.set_facecolor("white")
    ax.grid(
        True,
        axis=grid_axis,
        which="major",
        color=LIGHT_GRAY,
        linewidth=0.65,
        alpha=0.72,
        zorder=0,
    )
    ax.set_axisbelow(True)


def save(fig, name: str) -> None:
    """Write vector and review copies with deterministic geometry."""

    metadata = {
        "Title": name,
        "Creator": "fractional-d-stability-networks figure generator",
    }
    fig.savefig(
        OUT / f"{name}.pdf",
        bbox_inches="tight",
        pad_inches=0.04,
        metadata=metadata,
    )
    fig.savefig(
        OUT / f"{name}.png",
        dpi=320,
        bbox_inches="tight",
        pad_inches=0.04,
    )
    plt.close(fig)


def spectral_geometry() -> None:
    """Matignon geometry without overlapping hatches or in-plot legend boxes."""

    alpha = 0.8
    theta = alpha * math.pi / 2
    theta_deg = math.degrees(theta)
    radius = 1.0

    fig, ax = plt.subplots(figsize=(5.65, 4.65), layout="constrained")

    # Three disjoint visual classes make the set inclusion immediately clear.
    forbidden = Wedge(
        (0, 0),
        radius,
        -theta_deg,
        theta_deg,
        facecolor=PANEL_GRAY,
        edgecolor="none",
        zorder=0,
    )
    hurwitz = Wedge(
        (0, 0),
        radius,
        90,
        270,
        facecolor=SKY,
        alpha=0.28,
        edgecolor=BLUE,
        linewidth=1.0,
        zorder=1,
    )
    upper_sliver = Wedge(
        (0, 0),
        radius,
        theta_deg,
        90,
        facecolor=YELLOW,
        alpha=0.55,
        edgecolor=ORANGE,
        linewidth=1.0,
        hatch="///",
        zorder=2,
    )
    lower_sliver = Wedge(
        (0, 0),
        radius,
        270,
        360 - theta_deg,
        facecolor=YELLOW,
        alpha=0.55,
        edgecolor=ORANGE,
        linewidth=1.0,
        hatch="///",
        zorder=2,
    )
    for patch in (forbidden, hurwitz, upper_sliver, lower_sliver):
        ax.add_patch(patch)

    ax.axhline(0, color=MID_GRAY, linewidth=0.8, zorder=3)
    ax.axvline(0, color=MID_GRAY, linewidth=0.8, zorder=3)
    circle = plt.Circle((0, 0), radius, fill=False, color=INK, linewidth=1.0, zorder=4)
    ax.add_patch(circle)

    ray_end = (radius * math.cos(theta), radius * math.sin(theta))
    for sign in (1, -1):
        ax.plot(
            [0, ray_end[0]],
            [0, sign * ray_end[1]],
            color=ORANGE,
            linestyle=(0, (4, 2)),
            linewidth=1.65,
            zorder=5,
        )

    angle_arc = Arc(
        (0, 0),
        0.52,
        0.52,
        theta1=0,
        theta2=theta_deg,
        color=ORANGE,
        linewidth=1.25,
        zorder=6,
    )
    ax.add_patch(angle_arc)
    ax.annotate(
        r"$\theta=\alpha\pi/2$",
        xy=(0.24 * math.cos(theta / 2), 0.24 * math.sin(theta / 2)),
        xytext=(0.46, 0.39),
        color=INK,
        fontsize=9.5,
        ha="left",
        va="center",
        arrowprops={"arrowstyle": "-", "color": MID_GRAY, "linewidth": 0.8},
    )

    ax.text(-0.55, 0.17, "Hurwitz\nstable", ha="center", va="center", color=BLUE)
    ax.text(0.63, -0.17, "excluded\nwedge", ha="center", va="center", color=MID_GRAY)
    ax.annotate(
        "fractional only",
        xy=(0.11, 0.73),
        xytext=(0.46, 0.72),
        ha="left",
        va="center",
        color=ORANGE,
        fontsize=9.4,
        arrowprops={"arrowstyle": "->", "color": ORANGE, "linewidth": 1.0},
    )

    handles = [
        Patch(facecolor=SKY, alpha=0.28, edgecolor=BLUE, label="Hurwitz stable"),
        Patch(
            facecolor=YELLOW,
            alpha=0.55,
            edgecolor=ORANGE,
            hatch="///",
            label="fractional-only",
        ),
        Patch(facecolor=PANEL_GRAY, edgecolor=LIGHT_GRAY, label="excluded"),
    ]
    ax.legend(
        handles=handles,
        loc="upper center",
        bbox_to_anchor=(0.5, -0.08),
        ncol=3,
        frameon=False,
        handlelength=1.8,
        columnspacing=1.25,
    )

    ax.set_aspect("equal")
    ax.set_xlim(-1.06, 1.06)
    ax.set_ylim(-1.06, 1.06)
    ax.set_xlabel(r"$\operatorname{Re} z$")
    ax.set_ylabel(r"$\operatorname{Im} z$")
    ax.set_title(r"Matignon and Hurwitz regions ($\alpha=0.8$)", pad=8)
    save(fig, "fig_spectral_geometry")


def threshold_ratio() -> None:
    """Exact threshold ratio with a readable near-integer-order inset."""

    df = pd.read_csv(DATA / "F1_T_ratio_vs_alpha" / "F1_T_ratio_vs_alpha.csv")
    chosen = [
        "no_pair_loops_(1,1,1)",
        "all_antagonistic_(3,3,3)",
        "mutualistic_mixed_(0.2,0.8,0.5)",
        "anisotropic_(0.01,1,100)",
    ]
    labels = {
        chosen[0]: r"$(1,1,1)$",
        chosen[1]: r"$(3,3,3)$",
        chosen[2]: r"$(0.2,0.8,0.5)$",
        chosen[3]: r"$(0.01,1,100)$",
    }

    fig, ax = plt.subplots(figsize=(6.35, 4.35), layout="constrained")
    style_axes(ax)
    axins = ax.inset_axes([0.555, 0.47, 0.415, 0.39])
    style_axes(axins)

    for index, name in enumerate(chosen):
        d = df[df["triple"] == name].sort_values("alpha")
        common = {
            "color": SERIES_COLORS[index],
            "linestyle": SERIES_STYLES[index],
            "marker": SERIES_MARKERS[index],
            "markersize": 3.2,
            "markevery": max(len(d) // 10, 1),
            "markerfacecolor": "white",
            "markeredgewidth": 0.8,
        }
        ax.plot(d["alpha"], d["T_alpha_over_T1"], label=labels[name], **common)

        detail = d[d["alpha"] >= 0.82]
        inset_common = dict(common)
        inset_common["markevery"] = max(len(detail) // 5, 1)
        inset_common["markersize"] = 2.5
        axins.plot(detail["alpha"], detail["T_alpha_over_T1"], **inset_common)

    ax.set_yscale("log")
    ax.set_xlim(2 / 3, 1.0)
    ax.set_ylim(0.75, 1.0e23)
    ax.yaxis.set_major_locator(FixedLocator([1, 1e4, 1e8, 1e12, 1e16, 1e20]))
    ax.yaxis.set_major_formatter(LogFormatterMathtext(base=10))
    ax.set_xlabel(r"fractional order $\alpha$")
    ax.set_ylabel(r"threshold ratio $T_\alpha(\beta)/T_1(\beta)$")
    ax.set_title("Fractional enlargement of Cain's threshold", loc="left", pad=8)
    ax.legend(
        title=r"invariants $\beta$",
        loc="upper left",
        bbox_to_anchor=(0.025, 0.975),
        frameon=False,
        borderaxespad=0,
        handlelength=2.7,
        labelspacing=0.55,
    )

    axins.set_xlim(0.82, 1.0)
    axins.set_ylim(0.8, 10.7)
    axins.yaxis.set_major_locator(MaxNLocator(4))
    axins.tick_params(labelsize=7.4, length=2.5, pad=1.5)
    axins.set_title(r"detail: $0.82\leq\alpha\leq1$", fontsize=8.2, pad=3)
    axins.set_facecolor("#FBFBFC")
    for spine in axins.spines.values():
        spine.set_visible(True)
        spine.set_color(MID_GRAY)
        spine.set_linewidth(0.65)

    save(fig, "fig_threshold_ratio")


def c11_coverage() -> None:
    """Fraction of the exact band certified by the scalar C-11 condition."""

    df = pd.read_csv(
        DATA / "F4_C11_sufficient_fraction" / "F4_C11_sufficient_fraction.csv"
    )
    chosen = [
        "no_pair_loops_(1,1,1)",
        "all_antagonistic_(3,3,3)",
        "mixed_(3,0.5,1)",
        "anisotropic_(0.01,1,100)",
    ]
    labels = {
        chosen[0]: r"$(1,1,1)$",
        chosen[1]: r"$(3,3,3)$",
        chosen[2]: r"$(3,0.5,1)$",
        chosen[3]: r"$(0.01,1,100)$",
    }

    fig, ax = plt.subplots(figsize=(6.25, 4.05), layout="constrained")
    style_axes(ax)
    for index, name in enumerate(chosen):
        d = df[df["triple"] == name].sort_values("alpha")
        d = d[d["alpha"] >= 0.70]
        ax.plot(
            d["alpha"],
            d["certified_fraction_(TPhi-T1)/(Talpha-T1)"],
            color=SERIES_COLORS[index],
            linestyle=SERIES_STYLES[index],
            marker=SERIES_MARKERS[index],
            markersize=3.2,
            markevery=max(len(d) // 9, 1),
            markerfacecolor="white",
            markeredgewidth=0.8,
            label=labels[name],
        )

    ax.axhline(1.0, color=MID_GRAY, linewidth=0.8, linestyle=(0, (2, 2)), zorder=0)
    ax.set_xlim(0.70, 1.0)
    ax.set_ylim(0, 1.035)
    ax.set_xlabel(r"fractional order $\alpha$")
    ax.set_ylabel("certified fraction of the exact band")
    ax.set_title("Coverage of the closed-form C-11 certificate", loc="left", pad=8)
    ax.legend(
        title=r"invariants $\beta$",
        loc="lower center",
        bbox_to_anchor=(0.5, 0.025),
        ncol=2,
        frameon=True,
        facecolor="white",
        edgecolor=LIGHT_GRAY,
        framealpha=0.94,
        handlelength=2.6,
        columnspacing=1.4,
    )
    save(fig, "fig_c11_coverage")


def ecological_band() -> None:
    """Loop-space boundaries with the genuinely fractional band encoded as area."""

    df = pd.read_csv(DATA / "F5_L3_alpha_boundaries" / "F5_L3_alpha_boundaries.csv")
    name = "mixed_(3,0.5,1)"
    d = df[df["triple"] == name].sort_values("alpha")
    d = d[d["alpha"] >= 0.82].drop_duplicates(subset="alpha", keep="last")

    alpha = d["alpha"]
    cain = -d["L3_cain_boundary"]
    fractional = -d["L3_fractional_boundary"]

    fig, ax = plt.subplots(figsize=(6.25, 4.0), layout="constrained")
    style_axes(ax)
    ax.fill_between(
        alpha,
        cain,
        fractional,
        color=GREEN,
        alpha=0.16,
        linewidth=0,
        label="fractional-only band",
        zorder=1,
    )
    ax.plot(
        alpha,
        cain,
        color=BLUE,
        linestyle=(0, (5, 2)),
        label="Cain boundary",
        zorder=3,
    )
    ax.plot(
        alpha,
        fractional,
        color=ORANGE,
        linestyle="-",
        label="fractional boundary",
        zorder=4,
    )

    ax.set_yscale("log")
    ax.set_xlim(0.82, 1.0)
    ax.set_xlabel(r"fractional order $\alpha$")
    ax.set_ylabel(r"loop threshold $-L_3$")
    ax.set_title(r"Loop-space stability band, $\beta=(3,0.5,1)$", loc="left", pad=8)
    ax.legend(
        loc="upper right",
        ncol=1,
        frameon=True,
        facecolor="white",
        edgecolor=LIGHT_GRAY,
        framealpha=0.96,
        handlelength=2.6,
        borderpad=0.55,
        labelspacing=0.5,
    )
    save(fig, "fig_ecological_band")


if __name__ == "__main__":
    configure_style()
    spectral_geometry()
    threshold_ratio()
    c11_coverage()
    ecological_band()
