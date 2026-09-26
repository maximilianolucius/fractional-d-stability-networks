# Final figure-set recommendation (after Figure Wave 2)

**Date** 2026-09-26 · constraints: 25-page ceiling, no supplementary material, one figure environment per numbered figure.
**Recommendation: 6 figure environments, 14 panels in total** (a 7th, FIG-04c, is the only optional addition).

Priority order used: theorem communication > visual clarity > ecological mechanism > page economy. Every mathematical statement of an omitted panel must be covered in the text; the omitted panels are listed with the sentence that replaces them.

| env. | content (Wave-2 export) | panels | width | role |
|---|---|---|---|---|
| **Fig. 1** | **merge FIG-01 (b) + FIG-02** — Matignon sector at α = 0.9 (FIG-01b); the 2D codimension-one line (FIG-02a); the 3D open symmetric band (FIG-02b) | 3 | 2-col | conceptual: sector vs half-plane; why n = 3 is the first robust dimension (C-01, C-07, C-09) |
| **Fig. 2** | **FIG-03** exact C-10 threshold geometry (frozen) | 2 | 2-col | flagship theorem figure (C-10, C-15) |
| **Fig. 3** | **FIG-04** two-panel α-deformation: global ratio T_α/T₁ and classical-limit C-14 asymptotic | 2 | 2-col | theorem (C-14); the low-order C-15 law is stated in the text |
| **Fig. 4** | **FIG-05** ecological no-go vs IGP mechanism (polished) | 2 | 2-col | mechanism (DA-02/03, C-13) |
| **Fig. 5** | **FIG-06** Double-Allee m-path for design W2-A (flagship) | 2 | 2-col | narrative: one control parameter crosses the exact Cain boundary once (DA-09/10/11) |
| **Fig. 6** | **merge FIG-07 (b,c) + FIG-08** — 2D m_c curve (FIG-08a), traced (m,K) classification with certified segment (FIG-08b), certified margins along m (FIG-07b), spectral-angle corroboration at the worst diagonal (FIG-07c) | 4 (2×2) | 2-col, full height | certified witness + 2D/3D contrast (DA-08, DA-11, DA-12) |
| (opt.) Fig. 7 | FIG-04c low-order asymptotic T_αK³/27 vs K | 1 | 1-col | include only if the page budget allows after typesetting; otherwise text only |

Total panels: 3 + 2 + 2 + 2 + 2 + 4 = **14** (15 with the optional single-panel Fig. 7).

## Merges and what is dropped

1. **FIG-01 (a) dropped, FIG-01 (b) + FIG-02 merged.** The "representative order α = 0.75" panel carries no information beyond FIG-01(b) once the caption states that the sliver widens as α decreases. Merging the sector picture with the dimension contrast gives one three-panel conceptual opener (all objects exact/closed-form), saving one environment.
2. **FIG-07 (a) dropped; FIG-07 (b,c) merged with FIG-08.** The density panel (a) exists to show the balanced coexistence of the new design; its content is three numbers (X, Y, Z at the anchor) and belongs in the caption/text. The certified-margin panel and the spectral-angle panel then sit next to the (m,K) classification whose green segment is the same certificate, which is the natural place for them. The 2×2 layout is: (a) 2D curve, (b) 3D (m,K) slice, (c) certified margins, (d) worst-diagonal spectrum.
3. **FIG-04 (c) not included by default.** Its statement (T_α ≈ 27/K³ (1 + K(9Σβ − 27)/27) as α ↓ 2/3, C-15 Thm 3) is one displayed formula in the text; the exported `fig04c_low_order_asymptotic` is ready if space remains.
4. **Nothing moves to a supplement** (none exists). The omitted panels FIG-01(a), FIG-07(a), FIG-04(c) and FIG-07's former time-domain panel are all covered by one sentence each in the text.

## Figures that must not be cut

FIG-03 (Fig. 2) and FIG-06 (Fig. 5) are the two non-negotiable figures (Chief review). If the page count still overflows after this set, cut in this order: optional Fig. 7 → Fig. 3 reduced to its panel (a) only (C-14 law stated in text) → Fig. 1 reduced to panels (a),(c) (2D line described in text). Do not touch Figs. 2, 4, 5, 6.

## Width and placement

All six environments are double-column (178 mm); Fig. 6 is the tallest (≈ 150 mm). Figures 1–3 belong with the theory sections (C-01–C-15), Figs. 4–6 with the ecological section (DA-02–DA-12). Vector PDFs with embedded TrueType fonts are in `computations/figures_wave2/exports/pdf/` (FIG-02 is only in Wave 1, `computations/figures/exports/pdf/fig02_dimension_contrast.pdf`, unchanged and accepted). The merged environments (Figs. 1 and 6) are assembled from the individual panel PDFs at typesetting time (subfigure / minipage), which keeps every panel reproducible from its own script and metadata.
