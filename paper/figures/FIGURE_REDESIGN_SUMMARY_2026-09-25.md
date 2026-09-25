# Figure redesign and QA summary — 2026-09-25

## Scope

The delivery branch is `q1-submission-tight-20260925`. Its neutral and SIAM
submission variants include the threshold-ratio and ecological-band figures.
The proof-complete technical manuscript additionally includes the spectral
geometry and C-11 coverage figures. All four are produced by
`paper/figures/generate_figures.py` from the checked-in Wave 2 CSV data.

## Design changes

- Established one publication style across all figures: serif typography,
  consistent line weights, restrained horizontal grids, and larger labels sized
  for the actual manuscript placement.
- Adopted the color-vision-deficiency-safe Okabe–Ito palette. Curves also differ
  by dash pattern and marker, so interpretation does not depend on color alone.
- Kept PDF as the vector manuscript format and raised PNG review output to
  320 dpi. Embedded PDF fonts use TrueType outlines for reliable rendering.
- Removed overlapping fills, labels, and legends; legends now occupy deliberate
  empty regions or sit outside the data geometry.

### Spectral geometry

- Replaced overlapping hatched wedges with three disjoint visual classes:
  Hurwitz stable, fractional-only, and excluded.
- Added an explicit boundary-angle arc and direct region labels.
- Moved the legend below the axes and kept annotations clear of axes and rays.

### Threshold enlargement

- Preserved the logarithmic main view needed to show the low-order blow-up.
- Added a linear inset on `0.82 <= alpha <= 1` so convergence near integer order
  can be read without compressing the main result.
- Used four redundant color/style/marker encodings and placed the legend in the
  otherwise empty upper-left region.

### C-11 certificate coverage

- Enlarged labels and separated all four series by color, dashes, and markers.
- Added the full-coverage reference at 1 and placed the compact two-column
  legend in the data-free lower portion of the panel.

### Ecological loop-space band

- Encoded the genuinely fractional interval as a translucent filled band rather
  than leaving readers to infer the area between two curves.
- Distinguished the Cain and fractional boundaries with both color and line
  style, while retaining the logarithmic ordinate.

## Manuscript integration

- Increased figure widths in both submission sections from `0.68` to
  `0.82\linewidth`.
- Increased widths in the technical manuscript to `0.72\linewidth` for the
  spectral diagram and `0.78\linewidth` for the three data figures.
- Revised captions to explain the inset, shaded band, redundant encodings, and
  visual meaning of each region.

## Reproduction

From the repository root:

```bash
python3 paper/figures/generate_figures.py
cd paper
latexmk -pdf -interaction=nonstopmode -halt-on-error submission-tight.tex
latexmk -pdf -interaction=nonstopmode -halt-on-error submission-siam-tight.tex
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The SIAM commands require `siamart251216.cls` and `siamplain.bst` on the TeX
search path; CI obtains the December 2025 SIAM package automatically.

## Validation record

- `python3 -m py_compile paper/figures/generate_figures.py`: passed.
- Headless regeneration of all four PDF and PNG pairs: passed.
- Neutral tight submission: passed, 15 A4 pages, no LaTeX warnings.
- SIAM tight submission: passed, 15 pages; both figure pages were visually
  inspected at 144 dpi.
- Technical manuscript: passed, 39 pages; all four figure pages were visually
  inspected at 144 dpi.
- Visual checks covered label and legend collisions, axis readability, final
  placement size, grayscale-redundant encodings, and caption consistency.

The SIAM log still reports the pre-existing missing bibliography entry
`AlraddadiAlharthi2026` and two small text overfull boxes outside the figures.
The redesigned figures introduce no overfull boxes or unresolved references.
