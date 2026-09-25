# Chief review — Compute Wave 1 interim evaluation

**Date:** 2026-09-25
**Compute branch:** `agent/compute-c10-wave1-20260925`
**Reviewed compute HEAD:** `132833a291503a404396660545a9d65a2253c847`
**Decision:** **STRONG PASS SO FAR; MERGE BLOCKED ONLY BY P2 HIGH-PRECISION FINALIZATION**

## What is already accepted

The compute campaign has materially exceeded the requested scope.

Accepted corroboration/results:

- 121 tests passing on aureus;
- 60/60 interval-certified anchor values for the exact C-10 threshold;
- float-vs-high-precision agreement for threshold evaluation at relative error <=7.1e-12 over 4000 random cases;
- exact symmetric-slice agreement with Siami to approximately 1e-107 in high precision;
- 1.28 million Hessian samples with zero failures of logit positive definiteness;
- 2.06 million C-10 adversarial cases plus 120,000 controls in the float stress stage with zero persistent mismatches;
- 8100/8100 independently generated ecological-region classifications agreeing with C-10/C-13;
- C-14 asymptotic convergence confirmed down to 1-alpha=1e-10;
- n=4 reconnaissance completed and correctly labelled exploratory.

## Why the branch is not merged yet

The compute agent deliberately flagged 56,234 numerically delicate P2 cases for independent high-precision re-verification.

The repository does not yet contain:

- `computations/results/C10_STRESS_SUMMARY.json`;
- `computations/results/C10_WORST_CASES.csv`;

and the final report still marks P2 HP as pending.

Therefore the Chief will not call the wave COMPUTE_PASS or merge the branch until those cases are resolved.

The absence of float mismatches is strong evidence, not a substitute for this final gate.

## New mathematics extracted from the campaign

The compute agent supplied proof sketches that were independently re-derived by the Chief and promoted to the new internal theorem:

`research/THEOREM_C15_THRESHOLD_GEOMETRY.md`.

C-15 proves:

1. global strict convexity of the C-10 threshold objective in logit coordinates;
2. uniqueness and nondegeneracy of the simplex optimizer;
3. exact symmetric and two-equal slice reductions;
4. an explicit global parametrization of the entire threshold surface;
5. the universal alpha->2/3+ asymptotic;
6. realizability of every invariant point above the classical Cain threshold.

These are now analytic project results. Their compute evidence is supporting, not foundational.

## Evaluation of n=4 reconnaissance

P5 is scientifically useful but should **not** be folded into the current paper's theorem claims.

Best future direction:

- generic n=4 simplex/orbit reduction is nearly certain and elementary;
- the two-sharing-3-cycles family is the most promising non-Siami structured target;
- the pendant antagonistic-coupling sign effect is worth a later theorem attempt;
- the single 4-cycle is occupied by Siami and should not be pursued;
- the random observation at alpha<=0.75 is hypothesis generation only.

The current paper should remain dimension-3 exact rather than dilute itself with unproved n=4 claims.

## Current gate

To close Compute Wave 1, require exactly:

1. finish P2 high-precision audit of all flagged cases;
2. commit C10_STRESS_SUMMARY.json and C10_WORST_CASES.csv;
3. finalize COMPUTE_WAVE1_FINAL_REPORT.md;
4. return COMPUTE_PASS or COMPUTE_FAIL.

If P2 HP returns zero genuine mismatches, the Chief intends to integrate the compute branch after reconciling the two README-only commits currently ahead on main.
