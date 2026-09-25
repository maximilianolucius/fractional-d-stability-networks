# Manuscript

The delivery version is maintained on branch
`q1-submission-tight-20260925`.

Entry points:

- `paper/submission-tight.tex`: journal-neutral tight submission;
- `paper/submission-siam-tight.tex`: SIAM-formatted tight submission;
- `paper/main.tex`: proof-complete technical manuscript.

## Figures

All manuscript figures are generated from the checked-in Wave 2 CSV data. From
the repository root, run:

```bash
python3 paper/figures/generate_figures.py
```

The script writes vector PDFs for LaTeX and high-resolution PNG review copies to
`paper/figures/generated/`. This directory is intentionally ignored because CI
regenerates it from source on every paper build.

The current figure system uses a color-vision-deficiency-safe palette, redundant
line styles and markers, and typography sized for the figures' final manuscript
width. See `paper/figures/FIGURE_REDESIGN_SUMMARY_2026-09-25.md` for the design
and validation record.

## Build

After generating the figures, build from `paper/`:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error submission-tight.tex
latexmk -pdf -interaction=nonstopmode -halt-on-error submission-siam-tight.tex
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The SIAM build additionally needs `siamart251216.cls` and `siamplain.bst` on the
TeX search path. The branch workflow acquires the official macro package before
building.

## Continuous integration

`.github/workflows/tight-paper.yml` regenerates the figures, builds both tight
submission PDFs, reports LaTeX warnings, and uploads the PDFs as a workflow
artifact when this delivery branch changes.

## Status

This is the proof-complete, compressed delivery version. The theorem,
computation, citation, and internal manuscript audits are recorded elsewhere in
the repository; the figure redesign and its visual checks are recorded in the
figure summary linked above.
