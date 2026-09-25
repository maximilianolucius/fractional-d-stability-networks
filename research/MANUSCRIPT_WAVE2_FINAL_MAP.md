# Wave 2 manuscript integration — final evidence map

**Wave 2 status:** COMPUTE2_PASS  
**Final compute branch SHA:** bde75795c7ff1237220085df0b6ce3b44384c6d9  
**Integrated to main:** yes  
**Manuscript branch synchronized:** yes

## Main-text evidence

Keep in the refereed article:

1. two independent computational routes, invariant-space and direct spectral;
2. Wave 1 adversarial summary:
   - 2,180,000 cases;
   - 56,234 HP rechecks;
   - zero unresolved discrepancies;
3. Wave 2 atlas:
   - 938 total interval-enclosed points;
   - 903 unconditional global interval certificates;
   - 35 extreme-anisotropy points completed using the proved C-15 global convexity theorem;
   - worst relative width about 1.1e-35;
4. four canonical witnesses:
   - W03 symmetric/cyclic reference;
   - W22 Hurwitz at identity but not Hurwitz D-stable;
   - W18 mixed ecological loop signs;
   - W28 near exact fractional boundary;
5. compact robustness statement from 14 witnesses;
6. C-15 differential validation:
   - 128,000 float checks;
   - 2,500 HP checks;
   - primary derivative identity worst HP relative error about 2.4e-33;
   - Hessian positive definite at all 8,000 tested points;
7. four theorem-driven figures:
   - Matignon vs Hurwitz geometry;
   - T_alpha/T1 versus alpha;
   - C-11 band coverage;
   - ecological L3 band.

## Supplement / repository only

Move or keep outside the main text:

- full 938-row atlas;
- list of 35 conditional-only/unconditional certification classifications;
- full 35-witness library;
- all 84 robustness boundary/norm rows and detailed perturbation matrices;
- all 500 worst C-15 rows;
- F1--F9 full CSV data;
- detailed numerical pathology cases;
- reproduction logs/environment JSON;
- preview PNGs.

## Future-paper only — exclude from current manuscript claims

All P6 n=4 shared-edge material, including:

- cycle-merging invariant subspace lemma;
- numerical boundary s+t=R3(alpha)^3;
- sufficiency conjecture;
- k-shared-cycle generalization idea.

The current Discussion may mention n=4 only as an open direction, without stating the P6 conjecture unless clearly labelled exploratory. Prefer omitting the exact conjectured boundary from the submitted paper to keep the story dimension-three exact.

## Evidence semantics

Use these labels consistently:

- PROVED / theorem: analytic result in the manuscript;
- CERTIFIED: outward-rounded interval or exact symbolic certificate;
- HP: arbitrary-precision numerical evaluation;
- FLOAT: standard floating-point evaluation;
- NUMERICAL ROBUSTNESS UPPER BOUND: optimization result without rigorous lower bound.

Never call the 35 C-15-assisted atlas enclosures an independent validation of C-15.
