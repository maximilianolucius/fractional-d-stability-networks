# Wave 2 integration notes for the manuscript

**Date:** 2026-09-25  
**Source branch:** \`agent/compute-wave2-20260925\`  
**Status:** update as P3--P5 and final report arrive.

## P1 certified atlas — wording lock

Current P1 summary:

- total atlas points: 938;
- all 938 have interval enclosures and HP values inside the reported brackets;
- 903 points were certified by the unconditional interval/global branch-and-bound route;
- 35 highly anisotropic points exhausted the unconditional box/time budget and were closed using the already-proved C-15 strict-convexity/unique-minimizer structure;
- failures: 0;
- worst relative width over all reported brackets: approximately \(1.1\times10^{-35}\);
- median relative width: approximately \(1.37\times10^{-39}\).

### Main-paper wording

Do **not** simply write:

> 938 independent interval-certified global minima.

That would overstate independence from C-15.

Preferred wording:

> The Wave 2 atlas enclosed 938 threshold values by interval arithmetic. Of these, 903 were certified by a global branch-and-bound route that does not use the strict-convexity theorem; 35 extreme-anisotropy cases used the proved C-15 convexity/uniqueness result to complete localization. All high-precision optimizers lay inside the reported enclosures.

If the section is compressed, report the independent number 903 in the main text and move the 35 theorem-assisted cases to supplementary material.

## P2 witness library

Current P2:

- 35 exact real \(3\times3\) matrices;
- all satisfy strict-P(-A);
- all satisfy \(T_1<\kappa<T_\alpha\);
- all pass independent direct spectral checks;
- 10 have interval-certified \(T_\alpha\);
- categories include symmetric cyclic, generic nonsymmetric, strong antagonistic loops, mixed ecological signs, near-Cain, near-fractional-boundary, near both alpha transitions, Hurwitz-at-identity but not Hurwitz D-stable, and non-Hurwitz-at-identity.

Provisional main-paper selection is recorded in:

\`research/MANUSCRIPT_WITNESS_SELECTION.md\`.

## Integration rule

Do not modify the reader-facing numerical section with P1/P2 numbers until:

1. P3 robustness is complete;
2. P4 sensitivity checks are complete;
3. P5 figure datasets are complete;
4. \`research/COMPUTE_WAVE2_FINAL_REPORT.md\` returns \`COMPUTE2_PASS\`.

This prevents intermediate results from being frozen into the manuscript before the final evidence labels are known.
