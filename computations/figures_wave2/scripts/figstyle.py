"""Shared style, palette and export helpers for the manuscript figures (Figure Wave 1).

Palette and conventions follow research/FIGURE_STYLE_GUIDE.md exactly.
Every figure script imports this module and calls `export(fig, name, metadata)`,
which writes PDF + SVG + PNG (300 dpi) and a JSON metadata sidecar.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
import time

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
FIGROOT = os.path.abspath(os.path.join(HERE, ".."))
ROOT = os.path.abspath(os.path.join(FIGROOT, "..", ".."))
DATA = os.path.join(FIGROOT, "data")
META = os.path.join(FIGROOT, "metadata")
EXPORTS = {ext: os.path.join(FIGROOT, "exports", ext) for ext in ("pdf", "svg", "png")}
for d in (DATA, META, *EXPORTS.values()):
    os.makedirs(d, exist_ok=True)

# canonical semantic palette (do not change)
FRAC = "#1F4E79"     # fractional / Matignon / memory
CLAS = "#D97A00"     # classical / Cain / Hurwitz
BIO = "#2A7F62"      # biologically admissible / realized
NOGO = "#B14E3A"     # no-go / excluded / unstable
NDARK = "#5C6770"    # neutral dark
NLIGHT = "#D9DDE3"   # neutral light
PALETTE = {"fractional": FRAC, "classical": CLAS, "biological": BIO, "nogo": NOGO, "neutral_dark": NDARK, "neutral_light": NLIGHT}

# widths in inches (88 mm single column, 178 mm double column)
W1, W2 = 88 / 25.4, 178 / 25.4
LW_THM, LW_CMP, LW_AUX = 2.2, 1.6, 0.9      # theorem boundary / comparison boundary / auxiliary guide


def setup():
    plt.rcParams.update({
        "figure.facecolor": "white", "savefig.facecolor": "white", "axes.facecolor": "white",
        "font.family": "sans-serif", "font.sans-serif": ["DejaVu Sans", "Liberation Sans", "Arial"],
        "mathtext.fontset": "stix", "font.size": 8, "axes.labelsize": 8.5, "axes.titlesize": 8.5,
        "xtick.labelsize": 7.5, "ytick.labelsize": 7.5, "legend.fontsize": 7, "legend.frameon": False,
        "axes.spines.top": False, "axes.spines.right": False, "axes.linewidth": 0.7,
        "xtick.major.width": 0.7, "ytick.major.width": 0.7, "xtick.direction": "out", "ytick.direction": "out",
        "axes.grid": False, "lines.linewidth": LW_CMP, "savefig.dpi": 300, "pdf.fonttype": 42, "svg.fonttype": "none",
        "axes.unicode_minus": True,
    })


def panel_label(ax, s, x=-0.14, y=1.04):
    ax.text(x, y, s, transform=ax.transAxes, fontsize=9.5, fontweight="bold", va="bottom", ha="left")


def git_sha():
    try:
        return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
    except Exception:
        return "n/a"


def export(fig, name, metadata: dict):
    """Write exports/{pdf,svg,png}/name.* and metadata/name.json."""
    paths = {}
    for ext in ("pdf", "svg", "png"):
        p = os.path.join(EXPORTS[ext], f"{name}.{ext}")
        fig.savefig(p, format=ext, bbox_inches="tight", pad_inches=0.02, dpi=300 if ext == "png" else None)
        paths[ext] = os.path.relpath(p, ROOT)
    meta = {"figure": name, "generated_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "git_sha": git_sha(),
            "script": os.path.relpath(sys.argv[0], ROOT) if sys.argv and sys.argv[0] else "", "outputs": paths,
            "palette": PALETTE, **metadata}
    with open(os.path.join(META, f"{name}.json"), "w") as f:
        json.dump(meta, f, indent=2, default=str)
    plt.close(fig)
    print("exported", name, file=sys.stderr)
    return meta


def save_data(name, obj):
    p = os.path.join(DATA, name)
    if name.endswith(".json"):
        with open(p, "w") as f:
            json.dump(obj, f, indent=1, default=str)
    else:
        import numpy as np
        np.savetxt(p, obj["array"], delimiter=",", header=obj["header"], comments="", fmt="%.15g")
    return os.path.relpath(p, ROOT)
