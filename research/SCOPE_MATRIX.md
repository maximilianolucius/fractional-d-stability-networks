# Scope matrix

Use this table to prevent a benchmark, a prior-art corollary, or finite computation from being promoted into a general theorem.

**Updated 2026-09-24 — second-pass reopened audit.** The previous statement that existing literature was blind to the non-convex Matignon complement is withdrawn. Siami substantially occupies the single-cycle fractional secant target; Kushel/Kushel–Pavani supply generalized-D-stability and forbidden-boundary machinery; Abed and successors occupy the classical robustness/interior concept.

| Claim ID | Whole matrix/model family | Family under conditions | One-parameter slice | Benchmark only | Certified box only | Numerical observation only |
|---|---:|---:|---:|---:|---:|---|
| C-01 | imported Matignon theorem |  |  |  |  |  |
| C-02 | DERIVABLE BUT NOT NOVEL |  |  | examples only |  |  |
| C-03 | definition only; no theorem yet |  |  |  |  |  |
| C-04 | generalized-D-stability framework already known | exact low-dimensional subclasses may be new |  |  |  | sampler = falsification only |
| C-05 | no general theorem | single cycle substantially occupied by Siami; multi-cycle/cactus still open if non-reducible | possible | possible | possible | exploratory |
| C-06 | classical strong/robust D-stability known | fractional genuinely non-Hurwitz interior is project target | possible | possible | possible | exploratory |
| C-07 | **THEOREM for all real 2×2 matrices and all 0<α<1** |  |  |  |  |  |
| C-08 | **THEOREM: dimension-three open separation for 0<α<=2/3** | explicit strict P-matrix neighborhood | A_γ is witness/center, not the whole theorem |  |  |  |
| C-09 | OPEN for 2/3<α<1 | candidate neighborhoods around structured 3×3 centers | cycle center may guide proof |  | possible | sampler only for counterexample hunting |
| C-10 | OPEN exact 3×3 characterization | target: explicit cubic/principal-minor criterion | boundary-ray parameterizations useful |  | possible | exploratory |

## Current hard boundary

The strongest proved project statement is presently:

```text
min { n : int P_α^(n) != empty } = 3
for every 0 < α <= 2/3.
```

Proof: `research/novelty/REOPENED_AUDIT_2026-09-24.md`.

The range

```text
2/3 < α < 1
```

is **not proved**. No title, abstract, conclusion, or ecological generalization may silently extrapolate C-08 into that range.

## Single-cycle restriction

A theorem whose only mathematical content is a fractional secant condition on a one-cycle network is not an approved novelty target because Siami 2020/2021 already proves the relevant fractional cyclic stability condition, and the key cycle ratio is invariant under positive left-diagonal row scaling.

## Robustness restriction

"Open", "robust", "strong D-stable", or "uniform margin" language must cite and distinguish Hartfiel/Abed/Lee–Edgar and current robust-D-stability work. The project contribution, if any, must be specific to the Matignon angular region and the genuinely non-Hurwitz class P_α.
