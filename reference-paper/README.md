# Previous accepted paper — format reference

This directory contains the publication-format reference extracted from the previously accepted paper package:

**Exact Stability Atlases and a Memoryless-Surrogate Failure Theorem for a Caputo Allee Predator-Prey Model**

The directory is retained as the **format and editorial-style reference** for the new `fractional-d-stability-networks` research project. GitHub contains the accepted MDPI *Mathematics* LaTeX source, the class/bibliography definitions needed for reuse, publication figures, required converted logo assets, and the compiled PDF. The original uploaded ZIP is intentionally not duplicated in GitHub; its SHA-256 checksum is retained for provenance.

## Purpose in this repository

Use this paper to reproduce:

- the MDPI *Mathematics* document class and accepted-paper layout;
- title/author/abstract/keywords/MSC placement;
- theorem/proposition/corollary formatting;
- figure and multi-panel figure conventions;
- table formatting;
- bibliography/citation style;
- declarations and end-matter structure;
- the overall level of mathematical exposition and visual density.

Do **not** treat the mathematical claims in this paper as automatically novel for the new project. The new project must establish its own novelty independently, as specified in `research/NOVELTY_AGENT_TASK.md` and `agent_directives_publishable_first_submission.md`.

## Key files

- `mathematics-4528508.tex` — accepted manuscript source and primary format reference.
- `mathematics-4528508.pdf` — compiled accepted paper.
- `Definitions/` — MDPI class, bibliography styles, and template assets used by the accepted source.
- `fig*.pdf` — publication figures used by the paper.

## Recommended reuse strategy

Do not edit this directory in place. Keep it immutable as a reference snapshot. Build the new paper in `paper/`, copying only the formatting components that are needed after the novelty audit has identified the principal theorem and final manuscript architecture.
