# Figure Wave 2 — final report

**Status: `FIGURE_WAVE2_PASS`**
**Branch** `agent/compute-figures-wave2-20260926` (base `85cf354`) · **Date** 2026-09-26
**Tests:** 52 passed, 0 failed (46 pre-existing incl. Wave-1 tests + 6 new in `tests/test_figures_wave2.py`; run with `PYTHONPATH=src python -m pytest -q`)
**No theorem file, claim wording, novelty conclusion, `paper/` content or Wave-1 output was modified.** All Wave-2 outputs live in `computations/figures_wave2/` (scripts, data, exports/{pdf,svg,png}, metadata).

## Part A — re-embedding (details: `research/FIGURE_WAVE2_REEMBEDDING_REPORT.md`)

A materially better witness exists and was adopted: **design W2-A, anchor m = 0.511** (max/min density ratio 5.2 vs 780 for Wave-1 m = 0.35; classical margin 40.6 % of T₁ vs 14.1 %; fractional margin 33.7 % of T_{0.9} vs 47.7 %; conditioning of the classical margin 83 vs 80). Exact crossing m₀ = 0.374451… (60 digits); certified points m = 0.481/0.511/0.541 and a fully certified m-range [0.394, 0.578]. 4000 designs sampled, 1527 accepted, 365 robust; ≥ 10 candidates with metrics in `data/reembedding_candidates.json` and `design_selected.json → shortlist`. Wave-1 m = 0.35 is retained as documented backup; both are constructive witnesses, not calibrated ecosystems.

## Part B — figure-by-figure changes

| figure | Wave-2 change | panels |
|---|---|---|
| FIG-01 | panel (a) titled "representative order, α = 0.75"; background fills lightened (0.12/0.08) so the Matignon wedge dominates | 2 |
| FIG-02 | unchanged (Wave-1 export accepted) | 2 |
| FIG-03 | scientific content frozen; panel (b) legend reduced (three short entries) | 2 |
| FIG-04 | two-panel main candidate (global ratio; classical-limit C-14 asymptotic); low-order C-15 panel exported separately as `fig04c_low_order_asymptotic`; long orange annotations replaced by a short "dashed: …" label | 2 (+1 separate) |
| FIG-05 | symmetric node geometry (x bottom-centre, y/z top), role labels beside nodes, one-line decisive identities per box, smaller headings; red no-go / green realized kept | 2 |
| FIG-06 | regenerated for design W2-A; panel (a) annotations reduced to: classical point, m₀, anchor, feasibility endpoint (arrow "s → 0⁺ at m = 0.613"; the gap curve is plotted up to 4× its anchor value because κ − T₁ diverges at the end of the branch); panel (b) geometry as in Wave 1 (path, T₁, T_{0.9}, three markers) | 2 |
| FIG-07 | rebuilt with 3 panels: (a) densities (now balanced: X = 1, Y = 0.79, Z = 0.19), (b) certified margins with three certified squares and the certified m-range bar, (c) spectral-angle corroboration at the worst diagonal; time-domain panel dropped; caption and metadata state that (c) is corroboration only and the all-D statement is the theorem | 3 |
| FIG-08 | (a) unchanged; (b) redesigned: boundaries κ = T₁, κ = T_{0.9} and feasibility edge traced by scan + 80-step bisection on the exact functions for 61 values of K (`design_tools.trace_boundaries`), light fills between the traced curves, certified segment and anchor overlaid, title states "traced boundaries: exact formulas pointwise, not certified" | 2 |

## Part C — final set

`research/FIGURE_FINAL_SET_RECOMMENDATION.md`: **6 environments, 14 panels** — Fig. 1 = FIG-01(b) + FIG-02 (3 panels); Fig. 2 = FIG-03 (2); Fig. 3 = FIG-04 two-panel (2); Fig. 4 = FIG-05 (2); Fig. 5 = FIG-06 (2); Fig. 6 = FIG-08(a,b) + FIG-07(b,c) (4). Optional 7th: FIG-04c (1 panel) if space remains. No supplement; omitted panels (FIG-01a, FIG-07a, FIG-04c, time-domain) each replaced by one sentence in the text.

## Part D — visual QA (Wave-2 exports)

- **100 % inspection** of every PNG (300 dpi) after each edit; collisions found and fixed: FIG-06 (gap curve dominated by the divergence near feasibility loss → windowed; "κ − T₁" label over m₀; "anchor" label in (b)), FIG-07 ("m₀" over the dotted line; legend over certified squares; "min min" text rendering; "anchor" over the X label), FIG-08 (region labels over the anchor/legend; legend over the traced boundary; long legend entries), FIG-05 (box text at the canvas edge → 6.6 pt), FIG-01 (mathtext title).
- **50 % and grayscale** (converted copies of FIG-06/07/08 at half size): line style and markers carry the semantics (dashed classical, solid fractional, square/circle/diamond), fills differ in luminance; all labels legible at half size (≥ 3 pt equivalent).
- **Colourblind-safe semantics:** every colour pairing is doubled by line style or marker; the only colour-only element is the region fill in FIG-08(b), which is also separated by drawn boundary curves.
- **Column suitability:** all Wave-2 figures are 178 mm double-column; FIG-04c is 88 mm single-column.
- **Vector/text checks:** `pdffonts` shows embedded TrueType subsets (DejaVu Sans, STIX) in all 8 PDFs; SVGs contain text elements and no `<image>` (no rasterised equations); PNGs are 300 dpi.
- **Consistency:** fonts 6–9.5 pt from the shared `figstyle` module; panel labels bold; palette unchanged from Wave 1.
- **Evidence wording:** FIG-07(c) and FIG-08(b) captions/metadata/titles state explicitly what is certified (squares, green segment, m₀) and what is pointwise or corroborative; no finite diagonal sampling is presented as proof anywhere.

## Tests (`tests/test_figures_wave2.py`)

1. selected design: all parameters positive, efficiencies in (0,1), unique positive coexistence, strict-P, Y/X and Z/X ≥ 10⁻², ratio < 30, relative margins ≥ 0.10 / 0.20, invariants match the stored record;
2. local m-crossing with correct signs (classical point and m₀ − 0.01 negative, m₀ + 0.01 and anchor positive) and a unique sign change on the branch;
3. FIG-06: the stored m₀ satisfies κ = T₁ to 48 digits and is reproduced by a fresh 60-digit bisection to 40 digits;
4. certified records: interval fully certified and containing the anchor; exact float evaluation respects every certified lower bound;
5. FIG-08: the traced boundaries separate the classes on both sides (±2·10⁻³ in m) for κ = T₁, κ = T_{0.9} and the feasibility edge, and the traced κ = T₁ curve passes through m₀ at K = K₀;
6. all Wave-2 exports and metadata exist.

## Remaining caveats

1. The merged environments of Part C (Figs. 1 and 6) are recommendations; the merged PDFs are not pre-assembled — each panel is exported individually and the merge is a typesetting operation (subfigure). If the Chief wants single-file merged exports, that is one short script per merge.
2. FIG-06(a) shows the gap curve only up to 4× its anchor value; the divergence of κ − T₁ at the end of the branch is indicated by the arrow and stated in the caption. Readers should not infer from the plot that the classical margin stays bounded.
3. The Wave-2 certified m-range [0.394, 0.578] is shorter than the Wave-1 range [0.2005, 0.45] because the W2-A branch leaves 𝔽_{0.9} at m ≈ 0.59; certification of the whole feasible fractional-only segment is not attempted.
4. FIG-08(b) fills are bounded by traced curves (float64 root-finding on exact formulas); the classification is exact pointwise but not interval-certified; this is stated in the title, legend wording and caption.
5. FIG-04c's (1,1,1) curve dips below 1 for K ≳ 0.2 (far from the K → 0 regime of the asymptotic); unchanged from Wave 1 and correctly outside the asymptotic's domain.
