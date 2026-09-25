# Internal referee pass 2 — proof-complete manuscript

**Date:** 2026-09-25  
**Branch:** \`q1-manuscript-20260925\`  
**Target standard:** Q1 matrix analysis / applied dynamical systems  
**Scientific gates:** novelty PASS WITH REPOSITIONING; proof PASS; compute PASS.

## Recommendation

**SCIENTIFIC CONTENT READY; EDITORIAL REVISION STILL REQUIRED BEFORE EXTERNAL SUBMISSION.**

No new central theorem is needed.

The manuscript is now a complete mathematical paper rather than a scaffold. The remaining work is dominated by presentation, figure integration, witness selection, and journal-length compression.

## Current objective checks

- clean LaTeX build: **PASS**;
- latest completed build: 37 pages including bibliography;
- LaTeX/BibTeX warnings in clean completed build: **0**;
- undefined references: **0**;
- undefined citations: **0**;
- duplicate labels: **0**;
- missing inputs: **0**;
- theorem reconciliation against C-07/C-09/C-10/C-11/C-14/C-15/C-16: **PASS**;
- abstract length: approximately 189 words;
- internal project labels removed from reader-facing validation prose;
- code/data availability statement: present;
- canonical analytic nonsymmetric/general theorem structure: present;
- canonical symmetric cyclic witness: present.

## Scientific spine now complete

1. Matignon/generalized-D-stability definitions and sign convention.
2. Positive-diagonal projective simplex reduction.
3. Exact 2x2 classification.
4. Exact fixed-cubic ray boundary.
5. Exact real-3x3 criterion
   \[
   A\in\mathcal F_\alpha^{(3)}
   \iff
   \kappa<T_\alpha(\beta).
   \]
6. P0 necessity and strict-P interior classification.
7. Exact recovery of Cain at alpha=1.
8. Exact genuinely fractional band.
9. Strict logit convexity and unique optimizer.
10. Symmetry reductions and exact Siami slice.
11. Global threshold-surface parametrization.
12. Exact beta-sensitivity.
13. Strict alpha monotonicity.
14. alpha->1 and alpha->2/3 asymptotics.
15. C-11 closed-form sufficient certificate and asymptotic coverage fraction.
16. Realizability of the entire invariant band.
17. Minimum robust dimension theorem.
18. GLV abundance invariance and feedback-loop coordinates.
19. Independent adversarial/high-precision/interval validation.
20. Explicit comparison with Cain, Bahl--Cain, Kushel--Pavani and Siami.
21. Limitations and higher-dimensional frontier.

## Referee questions

### What is new relative to Kushel--Pavani?

Answered clearly: not generalized D-stability itself, but the explicit exact elimination of every positive diagonal multiplier in the generic real-3x3 Matignon problem to four invariants and a scalar threshold.

**Verdict: PASS.**

### What is new relative to Cain?

Answered clearly: Cain is the exact alpha=1 endpoint; the manuscript gives the full fractional deformation, exact fractional-only band, convex threshold geometry and both fractional-order limiting regimes.

**Verdict: PASS.**

### Why dimension three?

Answered by an exact theorem: n=2 has only a lower-dimensional fractional-only set, while n=3 has nonempty full-dimensional interior for every 0<alpha<1.

**Verdict: PASS.**

### Why is Siami not already the same theorem?

Answered: the single-cycle result is recovered exactly as the beta=(1,1,1) symmetric slice; generic positive beta triples cannot be reduced to that slice by the relevant positive-diagonal orbit action.

**Verdict: PASS.**

### Does computation prove the result?

The manuscript explicitly states no. It describes independent direct-spectral falsification, HP rechecks and interval certification as corroboration/certification only.

**Verdict: PASS.**

### Is the ecological layer consequential?

Yes: positive equilibrium abundance is proven to be an orbit reparametrization, and the exact threshold is converted to reciprocal-pair/directed-cycle invariant coordinates with exact sensitivities.

**Verdict: PASS.**

## Residual bibliography issue — Shao et al. 2017

A final web search on 2026-09-25 located the publisher/ResearchGate metadata but no accessible primary PDF. The available record explicitly says no full text is available through that source. Citation context from later D-region controller-design literature places the article in fractional pole-region / D-region stability, not multiplicative positive-diagonal matrix D-stability.

The article is therefore:

- not used as a load-bearing source;
- not required to establish the novelty boundary, because the stronger relevant multiplicative-D prior art of Kushel--Pavani has been inspected directly;
- retained as a residual access note only.

If a primary PDF becomes available before submission, inspect it and close the note.

## Remaining mandatory work

### Depends on Compute Wave 2

1. certified threshold atlas;
2. 24--40 canonical witnesses;
3. select 3--5 generic nonsymmetric examples for the paper/supplement;
4. robustness margins;
5. final figure-source datasets;
6. C-15 derivative validation summary.

### Editorial, after Wave 2

1. choose final 4--6 main-text figures;
2. integrate one compact canonical witness table;
3. compress 37-page technical draft toward target-journal length;
4. move certification implementation detail and secondary derivations to supplement/appendix;
5. convert to target journal class;
6. add confirmed affiliation/contact;
7. freeze code/data SHA;
8. final title/abstract pass;
9. final external-style referee pass.

## Length diagnosis

The largest section is Section 5 (threshold geometry). It is mathematically justified in the proof-complete technical version but is the main compression reservoir.

Do not compress before Wave 2 fixes the final figure and witness selection.

Likely supplement candidates:
- full threshold-surface parametrization algebra;
- detailed low-order expansion algebra;
- C-11 derivation and coverage proof;
- detailed extreme-scaling pathology;
- interval-certification implementation;
- extended robustness/witness tables.

## Current verdict

- theorem correctness: **PASS**;
- novelty positioning: **PASS**;
- self-containment: **PASS**;
- bibliography core: **PASS**;
- reproducibility: **PASS**;
- exposition: **PASS WITH MINOR EDITING**;
- figures/examples: **WAIT FOR WAVE 2**;
- target-journal length: **NOT YET**;
- scientific readiness for Q1 submission: **YES**;
- external submission readiness today: **NO — WAIT FOR WAVE 2 + COMPRESSION**.

The next manuscript action should be integration of Wave 2 outputs, followed immediately by compression and target-journal formatting.
