# Submission package as sent to the journal — round 1

**Manuscript:** *From Cain to Matignon: Exact Positive-Diagonal Stability in Dimension Three and a Nonlinear Caputo Ecological Realization*
**Journal / ID:** Mathematics (MDPI), manuscript `mathematics-4633263` · package dated 2026-10-01 · 26 pages.
**Archived here on 2026-10-16** from the author's copy of the submitted zip (unmodified; SHA-256 in `SHA256SUMS.txt`).

| item | content |
|---|---|
| `mathematics-4633263-submission-package.zip` | the exact zip that was uploaded (26 files) |
| `latex-source/` | the same zip unpacked for diffs: `main.tex`, `sections/01…08`, `references.bib`, `figures/` (7 PDFs), `Definitions/` (MDPI class files) |
| `from-cain-to-matignon-as-submitted.pdf` | the compiled manuscript included in the zip (it sat under `latex-source/sections/` in the zip; moved here) |
| `README_SUBMISSION.txt` | the recompile note shipped with the zip |

Relation to the repository sources (`paper/` on branch `chief/applied-simulation-20260927`, commit `fa63ecf`): the eight section files and `references.bib` are byte-identical to the repository versions; `main.tex` differs only in (i) local paths (`Definitions/mdpi` and `figures/` instead of the repository paths), (ii) the author block (the submitted version lists a single author/affiliation; the repository version lists two), (iii) the data-availability statement (the repository version links the `paper-v1.1.0` release) and (iv) the acknowledgment.

Recompile: `cd latex-source && latexmk -pdf -file-line-error -interaction=nonstopmode main.tex`.
