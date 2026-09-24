# Scope matrix

Use this table to prevent a benchmark or finite computation from being promoted into a general theorem.

**Updated 2026-09-24** after the novelty audit (`NOVELTY_REPORT.md`): C-02 demoted to standard/derivable; C-06 split into a trivial fixed-D part and an open uniform-over-D part; C-04 restricted to the non-convex purely fractional zone, since convex-region sufficient conditions are prior art (Kushel–Pavani 2021).

| Claim ID | Whole matrix/model family | Family under conditions | One-parameter slice | Benchmark only | Certified box only | Numerical observation only |
|---|---:|---:|---:|---:|---:|---|
| C-01 | ✓ (subject to imported theorem hypotheses: commensurate Caputo, linearization validity, boundary/Jordan case) |  |  |  |  |  |
| C-02 | DERIVABLE BUT NOT NOVEL — corollary of Matignon 1996 + monotonicity (Brandibur et al. 2021, Remark 4); motivation only |  |  | `tests/test_spectral.py` instance |  |  |
| C-03 | definition only; no theorem yet |  |  |  |  |  |
| C-04 | target: structured graph classes only (general case open even at α=1) | target: non-convex sliver zone with uniform margin | possible | possible | possible | current sampler = falsification only |
| C-05 | target: explicit class (cactus/cyclic first), necessary-and-sufficient motif condition | possible | possible | possible | possible | exploratory |
| C-06 | fixed-D openness: derivable (eigenvalue continuity), not a contribution | uniform-over-`𝒟⁺` margin: target, OPEN | possible | possible | possible | exploratory |

`TBD`/target rows must not enter the abstract, title, or conclusions until the corresponding theorem in `CLAIMS.md` is PROVED.
