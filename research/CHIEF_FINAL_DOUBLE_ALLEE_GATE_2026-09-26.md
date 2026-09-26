# Chief final gate — Double-Allee extension

**Date:** 2026-09-26  
**Canonical Chief branch:** `chief/double-allee-submission-gate-20260926`  
**External audit:** `agent/external-proof-double-allee-20260926` @ `5066fa067dbff1c9b79c053195dbc992b28dc5a4`

## Final proof decision

The Double-Allee Kolmogorov / IGP theorem package has passed:

1. the first symbolic/computational adversarial audit;
2. the blind same-session replication;
3. a genuinely different-session external proof audit.

No load-bearing implication failed.

The external audit returned:

~~~text
EXT-01 PASS
EXT-02 PASS
EXT-03 PASS
EXT-04 PASS
EXT-05 PASS WITH FIX
EXT-06 PASS
EXT-07 PASS
EXT-08 PASS
~~~

Overall:

`EXTERNAL_AUDIT_PASS_WITH_FIXES`

## Final integrated strengthening

The positive strict-P coexistence stratum satisfies

~~~text
q=-det B=Delta(s+chi)>0,
~~~

hence

~~~text
s>0,
s+chi>0.
~~~

On that stratum, with Q>0, m>-a and 0<m<X<K,

~~~text
dX/dm<0
and
ds/dm<0
~~~

hold without any extra sign assumption on chi.

Thus

~~~text
t=1/s
~~~

is strictly increasing with m throughout the positive strict-P branch.

This strengthens the Allee-threshold mechanism: the monotone invariant-space motion is intrinsic to the strict-P coexistence branch, not only to the special constructive subfamily with chi>0.

## What is now frozen mathematically

The following statements are approved for manuscript integration:

1. **Kolmogorov orbit equivalence:** positive-equilibrium Jacobians inherit exactly the same positive-diagonal orbit as the per-capita derivative matrix.
2. **Competitive two-consumer no-go:** the naive extension cannot realize the open fractional-only band on the strict-P stratum.
3. **Exact IGP invariant coordinates:** beta_12,beta_13,beta_23,kappa and L3 have closed forms.
4. **Invariant realization theorem:** the IGP architecture realizes an open four-dimensional invariant set and in particular the C-10 fractional-only band with beta_ij>1.
5. **Quantified Double-Allee embedding:** every required positive reduced slope can be embedded at a positive coexistence equilibrium with explicit feasibility bounds.
6. **Open biological fractional-only theorem:** for every fixed 0<alpha<1 there is a nonempty open set in the full biological parameter space with
   `J in F_alpha^(3) \ D_H^(3)`.
7. **Allee monotonicity theorem:** increasing m decreases X and s and therefore increases t=1/s along the positive strict-P branch.
8. **Unique/transverse Cain crossing:** the invariant path crosses the classical D-stability boundary at most once and does so transversally when the crossing condition holds.
9. **Prescribed-m0 transition:** parameters can be chosen so that varying only m moves the fixed biological model from classical D-stability into fractional-only D-stability.
10. **2D/3D contrast:** the corresponding 2D Double-Allee model has only a codimension-one fractional-only D-stability mechanism.

## Important scope restrictions

The manuscript must NOT claim:

- global uniqueness of the coexistence equilibrium;
- novelty of fractional intraguild predation;
- novelty of the double-Allee law;
- novelty of generic Kolmogorov factorization;
- novelty of Matignon stability;
- novelty of generalized D-stability itself;
- that C-11 is exact or necessary;
- that the ecological theorem proves global nonlinear stability.

The ecological theorems are local-equilibrium / positive-diagonal spectral theorems.

## Manuscript architecture decision

**Approved:** integrate the Double-Allee extension into the current C-10/C-15 paper rather than treat it as a separate model paper.

The recommended theorem spine is:

~~~text
C-07  exact 2x2 obstruction
  ->
C-10  exact real 3x3 Matignon D-stability threshold
  ->
C-15  threshold geometry
  ->
Cain limit + C-09 minimum robust dimension
  ->
Kolmogorov orbit bridge
  ->
competitive architecture no-go
  ->
IGP invariant realization
  ->
open Double-Allee fractional-only biological region
  ->
Allee m-crossing
  ->
exact 2D/3D ecological contrast.
~~~

The old ecological motif discussion should be compressed into the setup for this realization theorem.

## Manuscript status

~~~text
PROOF GATE:                 PASS
TRUE EXTERNAL AUDIT:        PASS WITH FIX
THEOREM PACKAGE:            FROZEN FOR DRAFTING
NOVELTY:                    GO-NARROWED
MANUSCRIPT ARCHITECTURE:    UNLOCKED
SUBMISSION-READY:           NO
MERGE TO MAIN:              NOT YET
~~~

## Remaining gates before submission

### 1. Published-source-only bibliography

Per `agent_directives_publishable_first_submission.md`:

- no unpublished reference may appear in the paper;
- this includes arXiv/preprints, working papers, submitted or unpublished manuscripts, technical drafts, and personal communications;
- every cited result must use a formally published journal/conference/book version;
- DOI/publisher metadata must be verified where available;
- a manuscript claim may not depend on an unpublished-only source.

Internal novelty audits may retain unpublished material for research provenance, but the submitted bibliography may not.

### 2. Final frozen-claim novelty audit

Repeat the closest-work comparison using the exact final theorem wording, especially:
- C-10 explicit elimination;
- C-15 threshold geometry;
- open ecological realization;
- Allee-threshold crossing.

### 3. Manuscript construction

Write the paper theorem-first under the 25-page limit.

### 4. Final referee simulation

Independent passes for:
- proof rigor;
- novelty;
- bibliography/reference compliance;
- numerical evidence boundaries;
- page economy;
- visual quality.

Only after those steps may the manuscript be labeled submission-ready.
