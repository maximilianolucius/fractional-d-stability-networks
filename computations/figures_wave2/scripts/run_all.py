"""Render every Wave-2 figure (requires data/design_selected.json and data/branch_wave2.json from select_design.py,
and data/reembedding_candidates.json from reembed_search.py; both were produced on the compute node)."""
import runpy, os
HERE = os.path.dirname(os.path.abspath(__file__))
for name in ("fig01_matignon_hurwitz", "fig03_threshold_geometry", "fig04_alpha_deformation", "fig05_ecological_mechanism",
             "fig06_double_allee_m_path", "fig07_certified_anchor", "fig08_double_allee_2d_3d"):
    runpy.run_path(os.path.join(HERE, name + ".py"), run_name="__main__")
