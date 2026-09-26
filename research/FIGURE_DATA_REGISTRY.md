# Figure data registry — Figure Wave 1 (2026-09-26)

Regenerate everything from a clean clone with

```bash
pip install -e .[dev]
python computations/figures/scripts/branch_data.py        # exact coexistence branch, HP crossing, certified anchors (~3 min)
python computations/figures/scripts/run_all.py            # FIG-01 … FIG-08 → exports/{pdf,svg,png}, metadata/*.json (~4 min)
pytest tests/test_figures_wave1.py
```
Scripts run headlessly (`matplotlib.use("Agg")`), use no randomness except `numpy.default_rng(20260926+2)` in the T_α multi-start (deterministic), and write a JSON sidecar per figure in `computations/figures/metadata/` (claims, formulas, parameters, evidence class of every plotted object, script/data/output paths, git SHA). Palette and conventions: `computations/figures/scripts/figstyle.py` (= `research/FIGURE_STYLE_GUIDE.md`).

| figure | script | source data | evidence classes of plotted objects | claims |
|---|---|---|---|---|
| FIG-01 `fig01_matignon_hurwitz` | `fig01_matignon_hurwitz.py` | none (analytic) | Matignon rays, Hurwitz half-plane: EXACT THEOREM CURVE; shading: SCHEMATIC (exact sectors) | C-01, C-02, C-04 |
| FIG-02 `fig02_dimension_contrast` | `fig02_dimension_contrast.py` | `data/fig02_symmetric_slice.csv` | a₁₁=0 line: EXACT THEOREM CURVE; T₁=9b, T_α=27h_α(b/3): CLOSED-FORM BOUNDARY | C-07, C-09, C-10, C-15 Cor. 1 |
| FIG-03 `fig03_threshold_geometry` | `fig03_threshold_geometry.py` | `data/fig03_symmetric_slice.csv`, `data/fig03_asymmetric_slice.csv`, `data/fig03_certified_anchors.json` | T₁: CLOSED-FORM BOUNDARY; (a) T_α: CLOSED-FORM BOUNDARY; (b) T_α: EXACT THEOREM CURVE (numerical evaluation of the exact variational formula at its unique minimiser); squares: CERTIFIED INTERVAL (width <1e−30; conditional on C-15 Thm 1) | C-10 Thm 1, §6–7; C-15 |
| FIG-04 `fig04_alpha_deformation` | `fig04_alpha_deformation.py` | `data/fig04_alpha_curves.json` | solid: EXACT THEOREM CURVE (float64 in (a); 35-/55-digit in (b)/(c)); dashed: CLOSED-FORM asymptotics | C-14, C-15 Thm 3 |
| FIG-05 `fig05_ecological_mechanism` | `fig05_ecological_mechanism.py` | none | diagrams: SCHEMATIC (theorem diagram: arrows = exact signs of DF entries); formulas: EXACT | DA-02, DA-03, C-13 |
| FIG-06 `fig06_double_allee_m_path` | `fig06_double_allee_m_path.py` (data: `branch_data.py`) | `data/branch_alpha0.9.json` | branch curves, path, T₁/T_{0.9}: EXACT THEOREM CURVE (exact formulas along the exactly solved branch); m₀: CERTIFIED COMPUTATION (60-digit root, G₁(0.2)=−5e−60); anchor: CERTIFIED INTERVAL | DA-09/10/11, C-10, C-13 |
| FIG-07 `fig07_certified_anchor` | `fig07_certified_anchor.py` (data: `branch_data.py`) | `data/branch_alpha0.9.json`, `data/fig07_anchor_candidates.json` | (a),(b) curves: EXACT THEOREM CURVE; squares: CERTIFIED INTERVAL (interval Newton + outward rounding, 50 digits; C-11 bound unconditional, C-10 bound conditional on C-15 Thm 1); (c),(d): NUMERICAL CORROBORATION | DA-08, DA-11, C-10, C-11 |
| FIG-08 `fig08_double_allee_2d_3d` | `fig08_double_allee_2d_3d.py` | `data/fig08_mK_classes.csv` | m_c curve: CLOSED-FORM BOUNDARY; (m,K) classification: NUMERICAL EVALUATION OF EXACT FORMULAS (pointwise exact coexistence + exact C-10 threshold; not diagonal sampling); green segment: CERTIFIED INTERVAL (`computations/results/DOUBLE_ALLEE_INTERVAL_BOX.json`) | DA-12, DA-08, C-07, C-10 |

## Biological parameter set used in FIG-06/07/08 (Chief design; `chief_witness()` in `src/fdsn/double_allee.py`)

a=0.5, K=1.1, r=0.109513274336283, q₁=h=√2/20≈0.0707107, q₂=1/(20√e₂)≈1.40711, e₁=e₃=0.5, e₂=1/(4τ²)≈0.00126266 with τ=(14+√200)/2, μ₁≈0.0333447, μ₂≈0.00300979, c₁=c₂=0.05; α=0.9; m varies (m₀=0.2 is the exact Cain crossing).

## Certified anchor candidates (FIG-07; all interval-certified: X,Y,Z>0, strict-P, κ−T₁>0, κ<T_{0.9}; both C-11 and C-10-bracket certificates)

| m | X, Y, Z | s | β₁₂=β₁₃ | κ | T₁ | T_{0.9} | κ−T₁ (certified ≥) | T_{0.9}−κ (certified ≥) | direct margins (α=0.9 / α=1) | condition (classical / fractional) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.30 | 0.99850, 0.03705, 0.001485 | 0.04281 | 2.16803 | 20.6885 | 19.0014 | 41.5683 | 1.6871 | 20.8798 | +0.1366 / −0.0205 | 112 / 4.6 |
| **0.35 (recommended)** | 0.99773, 0.03680, 0.001280 | 0.03920 | 2.27557 | 22.4091 | 19.6356 | 42.8331 | 2.7734 | 20.4240 | +0.1256 / −0.0315 | 80 / 5.6 |
| 0.40 | 0.99695, 0.03654, 0.001071 | 0.03558 | 2.40524 | 24.4839 | 20.3941 | 44.3502 | 4.0898 | 19.8663 | +0.1140 / −0.0430 | 65 / 6.9 |

(0.33 and 0.38 were also certified; full records in `data/branch_alpha0.9.json`.) "Condition" = Σᵢ|∂(margin)/∂log pᵢ|/margin over the 14 biological parameters (float finite differences). Ranking rationale: m=0.40 has the largest classical margin and best conditioning but the smallest top-predator density (Z/X=0.107%) and lies closer to the feasibility loss at m≈0.643; m=0.30 has the largest Z but a classical margin of only 8.9% of T₁; m=0.35 balances both (classical margin 14% of T₁, fractional margin 48% of T_{0.9}, Z/X=0.128%). Caveat common to the whole family: Z is O(10⁻³)X because the construction places K close to X (Q small); this is a property of the Chief design, not of the theorem.
