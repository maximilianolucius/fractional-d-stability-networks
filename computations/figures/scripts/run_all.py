"""Regenerate every figure: python computations/figures/scripts/run_all.py  (headless, deterministic)."""
import os, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
FIGS = ["fig01_matignon_hurwitz", "fig02_dimension_contrast", "fig03_threshold_geometry", "fig04_alpha_deformation",
        "fig05_ecological_mechanism", "fig06_double_allee_m_path", "fig07_certified_anchor", "fig08_double_allee_2d_3d"]
only = sys.argv[1:] or FIGS
for f in only:
    p = os.path.join(HERE, f + ".py")
    if os.path.exists(p):
        subprocess.run([sys.executable, p], check=True, cwd=HERE)
