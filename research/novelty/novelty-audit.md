# Novelty audit

Maintained as a living claim-by-claim audit.  
**Last theorem-level update:** 2026-09-24 second-pass reopened audit.  
See `REOPENED_AUDIT_2026-09-24.md` and `../NOVELTY_REPORT.md`.

| Proposed contribution | Closest prior literature | Exact difference after reopened audit | Status |
|---|---|---|---|
| Graph-indexed purely fractional stabilization region `S_α(G)` | Matignon 1996; Brandibur–Garrappa–Kaslik 2021; fractional consensus; Grilli–Rogers–Allesina | Definition alone is not a contribution. A theorem must add exact structure beyond Laplacian-spectrum or generic topology→spectrum statements. | DEFINITION ONLY / NEEDS THEOREM |
| Purely fractional stabilization | Matignon; Ahmed–El-Sayed–El-Saka 2007 | Stable for `α<1` but unstable at `α=1` is standard sector geometry. | KNOWN / MOTIVATION ONLY |
| Fractional D-stability under all positive diagonal scalings | Kushel 2019; Kushel–Pavani 2020/2021; Kushel 2023 | `F_α` is an instance of generalized D-stability. The previous claim that the non-convex Matignon complement was untouched is withdrawn; forbidden-boundary/sector machinery already overlaps it. | FRAMEWORK KNOWN; EXACT SUBCLASS THEOREMS MAY BE NEW |
| Single-cycle fractional D-stability / fractional secant theorem | Siami 2020/2021; Arcak–Sontag 2006 | Siami's cycle ratio is invariant under positive row scaling; diagonal scaling can equalize the diagonal magnitudes. A single-cycle D-orbit theorem is therefore substantially recoverable from prior art. | NOVELTY REJECTED AS CENTRAL TARGET |
| Cactus / multi-cycle topology theorem | Siami 2020/2021 + Arcak 2011 | Potentially new only if the theorem cannot be decomposed into Siami single-cycle conditions plus known α=1 cactus/diagonal-stability results. | OPEN / SECONDARY UNTIL LOW-DIMENSION PROGRAM CLOSED |
| Robust/open fractional D-stability | Hartfiel 1980; Abed 1986; Lee–Edgar 2001; Casasanta–Simpson-Porco 2026 | Robustness/interior/strong D-stability are classical concepts. Novelty requires a genuinely fractional, non-Hurwitz separation result in the Matignon region. | CONCEPT KNOWN; FRACTIONAL NON-HURWITZ VERSION MAY BE NEW |
| Exact `2x2` classification of `F_α` | generalized D-stability background; elementary trace/determinant scaling | Project derivation proves `A∈F_α iff det A>0, a11<=0, a22<=0` for every `0<α<1`; `P_α^(2)` has empty full-dimensional interior. | **THEOREM INTERNALLY PROVED; NOVELTY SECONDARY** |
| Minimal robust dimension for genuinely fractional D-stability, `0<α<=2/3` | Kellogg P-matrix wedge + classical D-stability + Matignon | Project proof gives a full-dimensional open subset of `P_α^(3)`, while `int P_α^(2)=empty`; targeted searches found no identical dimension-threshold theorem. | **STRONG NOVELTY CANDIDATE; THEOREM INTERNALLY PROVED** |
| Same minimal-dimension theorem for all `0<α<1` | Siami supplies structured centers for `α>2/3`; Kushel supplies boundary framework | Need full-dimensional robustness over noncompact diagonal orbit in high-order range. | **HIGHEST-PRIORITY OPEN TARGET** |
| Exact `3x3` characterization for `2/3<α<1` | Cain/classical low-dimensional D-stability; Kushel forbidden-boundary approach | Would require an explicit angular/cubic criterion for the Matignon boundary rays under all `D>0`. | OPEN / POTENTIALLY TITLE-WORTHY |

## Corrected statements that must propagate to any manuscript

1. Do **not** say that all prior fractional D-stability conditions are confined to convex regions or are blind to the Matignon complement.
2. Do **not** claim novelty for a single-cycle fractional secant condition.
3. Do **not** use "strong D-stability" as new terminology.
4. Do **not** extrapolate the proved dimension-three interior result from `α<=2/3` to `α>2/3`.
5. Do distinguish:
   - the known generalized-D-stability framework;
   - the internally proved low-dimensional theorem;
   - the still-open high-order `3x3` characterization.

## Current project thesis

The strongest surviving line is no longer "fractional stabilization on graphs" but:

> determine the smallest dimension in which genuinely non-Hurwitz fractional D-stability has nonempty full-dimensional interior, then characterize the mechanism responsible for the transition.

Current internal theorem:

[
min{n:
operatorname{int}(mathcal F_alpha^{(n)}setminusmathcal D_H^{(n)})
eqarnothing}
=3,
qquad
0<alphale2/3.
]

The extension to every `0<α<1` remains open.

## Rule

A contribution is not marked novel merely because no identical title or keyword was found. The final audit must compare theorem hypotheses, conclusion, matrix dimension, scaling quantifier, spectral region, topology class, and robustness quantifier against the closest literature.
