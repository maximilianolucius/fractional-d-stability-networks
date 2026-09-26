# Figure data registry — Wave 2 (2026-09-26)

Regenerate from a clean clone (heavy steps were run on the compute node; the local steps take ~5 min):

```bash
pip install -e .[dev]
FDSN_WORKERS=16 python computations/figures_wave2/scripts/reembed_search.py   # 4000 designs, ~40 min on 16 cores → data/reembedding_candidates.json
python computations/figures_wave2/scripts/select_design.py                    # selection, 60-digit m0, interval certification (~15 min) → data/design_selected.json, data/branch_wave2.json
python computations/figures_wave2/scripts/run_all.py                          # FIG-01,03,04(+04c),05,06,07,08 → exports/{pdf,svg,png}, metadata/*.json
pytest tests/test_figures_wave2.py
```
Style module `computations/figures_wave2/scripts/figstyle.py` is the Wave-1 module with the output root moved to `figures_wave2/`. FIG-02 is unchanged from Wave 1 and was not re-exported.

| figure | script | source data | evidence classes | claims |
|---|---|---|---|---|
| FIG-01 | `fig01_matignon_hurwitz.py` | analytic | EXACT THEOREM CURVE (rays), SCHEMATIC fills | C-01, C-02, C-04 |
| FIG-03 | `fig03_threshold_geometry.py` | Wave-1 CSV/JSON copied to `data/` | as Wave 1 (frozen; legend only) | C-10, C-15 |
| FIG-04 (+04c) | `fig04_alpha_deformation.py` | `data/fig04_alpha_curves.json` (Wave-1 data) | EXACT THEOREM CURVE + CLOSED-FORM asymptotics | C-14, C-15 Thm 3 |
| FIG-05 | `fig05_ecological_mechanism.py` | none | SCHEMATIC theorem diagram; exact cycle identities | DA-02, DA-03, C-13 |
| FIG-06 | `fig06_double_allee_m_path.py` | `data/design_selected.json`, `data/branch_wave2.json` | EXACT THEOREM CURVE; m₀ CERTIFIED COMPUTATION (60 digits); anchor CERTIFIED INTERVAL | DA-09/10/11, C-10, C-13 |
| FIG-07 | `fig07_certified_anchor.py` | same | (a,b) EXACT THEOREM CURVE; squares/bar CERTIFIED INTERVAL; (c) NUMERICAL CORROBORATION | DA-08, DA-11, C-10, C-11 |
| FIG-08 | `fig08_double_allee_2d_3d.py` | `data/fig08_traced_boundaries.json` (from `design_tools.trace_boundaries`), `data/design_selected.json` | (a) CLOSED-FORM BOUNDARY; (b) NUMERICAL EVALUATION OF EXACT FORMULAS (root tracing, not certified); green segment CERTIFIED INTERVAL; m₀ CERTIFIED COMPUTATION | DA-12, DA-08, C-07, C-10 |

## Design W2-A (canonical biological design of Wave 2; `design_selected.json → design, params`)

Design strings: β12 = 4.79, β13 = 4.506, β23 = 5.607, κ = 62.735, s = 0.8231, c1 = 0.065, c2 = 0.0509, η = 0.773, ξ = 0.393, a = 0.229, m = 0.511, ρK = 0.605 (X = 1). Biological parameters: a = 0.229, K = 1.4913425743, r = 7.8104480113, q1 = 0.5121684678, q2 = 3.2338213736, h = 0.1404219270, e1 = e3 = 0.773, e2 = 0.0140459216, μ1 = 0.3178535346, μ2 = 0.1209173583, c1 = 0.065, c2 = 0.0509; α = 0.9.

Anchor m = 0.511: X = 1, Y = 0.785633, Z = 0.192182; β = (4.79, 4.506, 5.607); κ = 62.735, T₁ = 44.6124, T_{0.9} = 94.5719; certified κ − T₁ ≥ 18.1226, T_{0.9} − κ ≥ 31.8369. Exact crossing m₀ = 0.374451281242514935239080344619043849271764669 (60-digit). Certified m-range [0.394, 0.578] (min certified κ − T₁ ≥ 0.0332, T_{0.9} − κ ≥ 1.342 on the range). Direct spectral corroboration: min_D min|arg λ| = 1.4931 (margin +0.0794 at α = 0.9, −0.0777 at α = 1).

Comparison with the Wave-1 anchor and the full search statistics: `research/FIGURE_WAVE2_REEMBEDDING_REPORT.md`.
