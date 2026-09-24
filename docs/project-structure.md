# Project structure

The repository separates theory, manuscript text, code, and generated evidence so that a paper claim can be traced to either a proof or a reproducible computational artifact.

- `paper/` contains submission-facing manuscript source and final publication figures.
- `supplement/` is an **internal research-support area only**. Under the current publication directives, the submitted article cannot rely on a supplementary PDF or external appendix for any load-bearing claim.
- `research/` contains novelty audits, claim/scope registries, theorem notes, literature comparisons, and research logs.
- `src/fdsn/` contains reusable algorithms and mathematical diagnostics.
- `scripts/` and `experiments/` contain orchestration, reproducibility runs, and generated evidence.
- `tests/` contains regression and mathematical sanity checks.

The manuscript must remain logically self-contained even if every internal research-support file is hidden from the reader.
