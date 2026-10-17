# Mathematics 4633263 — round-1 revised manuscript

The new source in `revised-source/` was copied directly from the submitted ZIP archived in `paper/submission/round1-as-submitted/`. No working-branch `main.tex`, author block, or references were substituted silently. The original archive remains immutable.

**Submission metadata:** *From Cain to Matignon: Exact Positive-Diagonal Stability in Dimension Three and a Nonlinear Caputo Ecological Realization*; journal *Mathematics (MDPI)*; manuscript `mathematics-4633263`. The submitted manuscript lists **Ibrahim Alraddadi as sole author**. This revision preserves that submitted author/affiliation block, pending author approval of any editorial changes.

**Comments addressed:** R1-1…R1-7, R2-1…R2-7. See `RESPONSE_TO_REVIEWERS.md`, which provides a point-by-point map. New mathematical text makes cubic factorization, optimizer attainment, strict monotonicity and the low-order endpoint explicit. The exact fractional-only set is distinguished from its interior. The interval certificate is described from the actual `src/fdsn/interval_cert.py` implementation, with precision and validated lower threshold bounds. Six additional full nonlinear Caputo-order simulations bracket the selected row-scaled spectral threshold. Two published 2025–2026 references are added.

**Rebuild:** run `bash paper/review/round1/build-round1-revision.sh` from a checkout with `latexmk` and the TeX packages for the archived MDPI template. The script unpacks the **exact submitted ZIP**, overlays the updated `main.tex`, section sources and `references.bib`, then creates a compiled PDF, a standalone submission ZIP and SHA256SUMS in `paper/review/round1/_build/out/`. The archive retains the original seven figure PDFs. Run `bash .../build-round1-revision.sh --assemble-only` to inspect the assembled sources without compiling.

**Numerics:** supplemental script `order_sweep_round1.py` documents the independent PECE time integrations for alpha 0.900, 0.930, 0.945, 0.950, 0.955 and 0.965, at time steps 0.04 and 0.02; results reported in new Table (order scan). Results are finite-time checks, distinct from a theorem.

**Limitations:** the original PDFs of referee reports remain private and excluded from GitHub. Review of LaTeX source does not by itself establish acceptance by the journal. The figure PDFs inherited from the exact submission must still be checked for any internal lettering embedded within their vector graphics, independently of the captions rewritten in LaTeX.
