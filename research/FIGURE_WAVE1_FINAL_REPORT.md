# Figure Wave 1 — final report

**Status: `FIGURE_WAVE1_PASS`**  
**Branch:** `agent/compute-figures-wave1-20260926` (base `6ba5ddd`) · **Date:** 2026-09-26  
**Tests:** 46 passed, 0 failed (39 pre-existing + 7 new in `tests/test_figures_wave1.py`)  
**No theorem file, claim wording, novelty conclusion or `paper/` content was modified.**

## Inventory

All eight figures exported as vector PDF, SVG and 300-dpi PNG under `computations/figures/exports/{pdf,svg,png}/`, each with a JSON sidecar in `computations/figures/metadata/` (claims, formulas, parameters, evidence class per object, script, data, outputs, git SHA), source scripts in `computations/figures/scripts/`, data in `computations/figures/data/`, captions in `research/FIGURE_CAPTIONS_DRAFT.md`, provenance in `research/FIGURE_DATA_REGISTRY.md`.

| figure | panels | grade | notes |
|---|---|---|---|
| FIG-01 Matignon vs Hurwitz | 2 | theorem-grade (exact sectors) | generic α drawn with α=0.75; α=0.9 |
| FIG-02 2D vs 3D | 2 | theorem-grade (C-07 line; closed-form symmetric band) | (b) reuses the closed forms 9b and 27h_α(b/3) |
| FIG-03 exact C-10 threshold | 2 | theorem-grade + 3 certified anchors | symmetric slice (3 orders) and asymmetric slice (β₁₃=1.5, β₂₃=3) |
| FIG-04 α-deformation | 3 | theorem-grade (HP evaluation) + closed-form asymptotics | C-14 linear law and C-15 low-order law overlaid |
| FIG-05 no-go vs IGP | 2 | theorem diagram | exact signs of DF entries; cycle formulas |
| FIG-06 m-path | 2 | theorem-grade; m₀ certified to 60 digits | flagship ecological figure |
| FIG-07 certified anchor | 4 | certified (a,b) + numerical corroboration (c,d) | anchor m=0.35 |
| FIG-08 2D/3D contrast | 2 | closed-form (a); exact-formula classification + certified interval (b) | (m,K) slice, 15,600 exact classifications |

## Selected robust anchor

**m = 0.35** (Chief design, α=0.9, all other parameters as in the registry): X=0.99773, Y=0.03680, Z=0.001280; s=0.03920; β=(2.27557, 2.27557, 2); κ=22.4091, T₁=19.6356, T_{0.9}=42.8331; κ−T₁ = 2.7734 (14.1% of T₁, certified ≥ 2.773441), T_{0.9}−κ = 20.4240 (47.7% of T_{0.9}, certified ≥ 20.42404); direct scale-invariant spectral check: min|arg λ(DB)| over D = 1.5393 rad (margin +0.1256 at α=0.9, −0.0315 at α=1); Φ=0.876>ρ_{0.9}=0.472 (C-11 also holds); conditioning of the classical margin 80 (vs ≈1000 at the old m=0.21 point). Shortlist, ranked: **0.35**, 0.40, 0.30 (details and rationale in the registry). All candidates are interval-certified points (interval Newton for X, outward rounding, 50 digits; the C-11 certificate is unconditional, the exact C-10 bracket certificate is conditional on C-15 Thm 1 and C-13 §7 monotonicity).

## Classification summary

- **Theorem-grade / exact:** FIG-01, FIG-02, FIG-03 curves, FIG-04 solid curves, FIG-05, FIG-06 curves and path, FIG-07 (a,b) curves, FIG-08 (a).
- **Certified:** FIG-03 squares (3 brackets, width <10⁻³⁰); FIG-06 m₀ (60-digit root, G₁(0.2)=−5·10⁻⁶⁰) and anchor; FIG-07 squares (5 anchors, both margins); FIG-08 green m-interval [0.2005, 0.45] (Audit 1 certificate).
- **Numerical corroboration / illustrative:** FIG-07 (c) worst-diagonal spectrum (scale-invariant search, min|arg λ| over log d∈[−16,16]³ with prescaling), FIG-07 (d) linearised Caputo predictor–corrector run; FIG-08 (b) pointwise classification grid (exact formulas per point; the grid itself is not a proof of openness — the proof is DA-08).

No finite diagonal sampling is used as evidence; every all-D statement in the figures comes from the exact C-10 threshold, and the only diagonal searches (FIG-07c) use the eigenvalue-angle objective.

## QA performed

- Visual review of every PNG at export size; label overlaps fixed (FIG-01, 03, 04, 05, 06, 07); direct labels preferred over legends where two/three curves.
- Grayscale: line style carries the semantics (solid exact / dashed classical / dotted guide, distinct markers), so all figures remain readable without color; the FIG-08(b) class map additionally uses hatching-free flat fills whose luminance differs (orange 0.55, blue 0.32, grey 0.87).
- 50% scale: fonts 7–9.5 pt at 178 mm width remain ≥3.5 pt at half size; FIG-07 is the densest (4 panels) and should be printed at full double-column width.
- Fonts embedded as TrueType (pdf.fonttype 42), SVG text kept as text (`svg.fonttype: none`); white background; no rainbow colormaps; no 3D.

## Unresolved / caveats

1. FIG-07 anchor family: top-predator density Z is O(10⁻³)·X for every m on the branch (Chief design places K close to X). Mathematically irrelevant, biologically a visible feature; if a more "balanced" community is desired for the paper, the Chief should authorise a re-embedding with larger K−X (a different biological parameter set), which is outside this wave's mandate.
2. FIG-08(b) grid classification uses float64 exact-formula evaluation; the certified content is only the green segment. The boundary between classical and fractional-only in the map is the exact Cain surface evaluated pointwise; near the boundary pixels could be misclassified at the 10⁻¹² level only.
3. FIG-01(a) "generic α" is necessarily drawn at a concrete angle (0.75); the caption says so.
4. Optional figures (C-11 vs C-10, simplex optimiser geometry, band-width vs α) were not produced in this wave (not required for PASS).

## Recommended final-paper subset

Core: FIG-03 and FIG-06 (non-negotiable), FIG-01, FIG-02, FIG-05, FIG-07, FIG-08, FIG-04. If page pressure: merge FIG-01+FIG-02 into one two-panel figure (both are schematic/closed-form) and FIG-07+FIG-08(b) (anchor inside the certified region), keeping FIG-04 in the supplement.
