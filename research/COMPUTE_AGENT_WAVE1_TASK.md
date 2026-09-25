# Compute Agent Wave 1 — C-10/C-14 adversarial validation and frontier exploration

**Date:** 2026-09-25  
**Assigned by:** Chief Researcher  
**Execution class:** HIGH-COMPUTE / LONG-RUN  
**Purpose:** one substantial compute campaign, not piecemeal tasks  
**Target branch:** \`agent/compute-c10-wave1-20260925\`

## 0. Scientific context

The current theorem package is:

- C-07: exact real 2x2 classification.
- C-09: minimum dimension with nonempty full-dimensional genuinely fractional D-stability is 3 for every \(0<\alpha<1\).
- C-10: exact variational 3x3 characterization on the full-dimensional strict-P(-A) stratum.
- C-11: exact orbit minimum \(\Phi\) and a simpler sufficient fractional Cain certificate.
- C-12/C-13: GLV abundance invariance and exact loop-coordinate interpretation.
- C-14: strict monotonicity of \(T_\alpha\) and its sharp \(\alpha\to1^-\) asymptotic rate.

The compute agent is **not** being asked to prove these theorems. Its job is to attack them numerically at scale, validate formulas independently, produce reproducible theorem-illustration datasets, quantify gaps, and search for the next structural theorem.

Read first:

1. \`research/THEOREM_C10_EXACT_3X3.md\`
2. \`research/THEOREM_C09_DIMENSION_THRESHOLD.md\`
3. \`research/THEOREM_C11_FRACTIONAL_CAIN_CERTIFICATE.md\`
4. \`research/THEOREM_C13_ECOLOGICAL_LOOP_COORDINATES.md\`
5. \`research/THEOREM_C14_CLASSICAL_LIMIT_RATE.md\`
6. \`research/CLAIMS.md\`
7. \`research/Q1_PAPER_ARCHITECTURE.md\`
8. \`src/fdsn/cubic_certificate.py\`
9. \`tests/test_cubic_certificate.py\`

Do not modify \`paper/\`.

---

# Phase P0 — reproduce and harden the computational baseline

1. Create a clean environment from \`pyproject.toml\`.
2. Run the full test suite.
3. Add deterministic high-precision tests (mpmath >= 80 decimal digits) for:
   - C-07 boundary cases;
   - C-09 witness family as \(\alpha\to1^-\);
   - C-10 fixed-cubic boundary;
   - C-10 simplex normalization;
   - C-11 exact \(\Phi\) minimizer;
   - C-12/C-13 invariance under random positive left-diagonal scalings;
   - C-14 monotonicity and asymptotic rate.
4. Add property-based/randomized tests with fixed seeds.

**Required output:** no theorem claim from these tests; label all results numerical corroboration.

---

# Phase P1 — implement the exact C-10 threshold robustly

Implement production-quality numerical utilities for

\[
T_\alpha(\beta)
=
\min_{x\in\Delta_2^\circ}
\frac{h_\alpha(B_\beta(x))}{x_1x_2x_3}.
\]

Requirements:

- stable parameterization of the open simplex;
- deterministic global search plus local refinement;
- high-precision fallback near the boundary;
- gradients/Hessian if useful;
- return optimizer \(x^*\), minimum value, stationarity residual, and conditioning diagnostics;
- verify permutation symmetry in \(\beta\);
- verify monotonicity in each \(\beta_{ij}\) numerically;
- verify \(T_\alpha\to T_1\) as \(\alpha\to1^-\);
- verify the low-order transition at \(\alpha=2/3\);
- verify the symmetric slice \(\beta=(1,1,1)\) reproduces the Siami cyclic threshold to high precision.

For each computation, distinguish:
- ordinary floating-point result;
- high-precision corroboration;
- certified bound if interval arithmetic is implemented.

If feasible, add an interval/branch-and-bound verifier on the 2D simplex for selected parameter points. This can turn figure anchor points into **CERTIFIED COMPUTATION** rather than ordinary numerics.

---

# Phase P2 — adversarial theorem stress test at scale

Generate a large reproducible population of real 3x3 matrices with \(-A\) strict P.

Use at least four distinct generation mechanisms:

1. entry-space generation with rejection;
2. generation in invariant coordinates where feasible;
3. perturbations around the C-09 cyclic witness;
4. samples close to:
   - principal-minor boundaries;
   - classical Cain boundary \(\kappa=T_1(\beta)\);
   - fractional boundary \(\kappa=T_\alpha(\beta)\);
   - \(\alpha\) near \(2/3\);
   - \(\alpha\) near \(1\).

Recommended scale: at least \(10^6\) matrix/alpha cases total, preferably more if efficient.

Use a boundary-heavy alpha grid such as:

\[
0.10,\ 0.30,\ 0.60,\ 2/3,\ 0.70,\ 0.80,\ 0.90,\ 0.95,\ 0.99,\ 0.999,\ 0.9999.
\]

For each candidate:

1. classify using C-10;
2. independently minimize the direct spectral margin over positive diagonal ratios:
   \[
   \min_{D\succ0\ /\ \text{common scale}}
   \min_i |\arg\lambda_i(DA)|-\alpha\pi/2;
   \]
3. use multiple global optimizers / starts;
4. rerun all mismatches and near-zero margins at high precision;
5. search aggressively for a counterexample to C-10.

**Stop-the-line rule:** if any genuine mismatch survives high precision, create a smallest explicit counterexample immediately and mark C-10 COMPUTE-FAIL.

Required summary:
- number of cases;
- distributions;
- minimum observed theorem-vs-direct discrepancy;
- all near-boundary worst cases;
- zero/mismatch count.

---

# Phase P3 — quantify C-11 conservatism and closed-form slices

C-11 is sufficient but not necessary. Quantify how conservative it is.

For broad \(\beta/\alpha\) grids compute:

\[
T_\alpha(\beta),\qquad
T_1(\beta),\qquad
T_{\Phi,\alpha}(\beta),
\]

where the last denotes the effective boundary implied by the scalar \(\Phi\) certificate.

Deliver:

1. ratio/gap statistics;
2. worst and best cases;
3. heatmaps/CSV data in invariant space;
4. symmetric slice \(\beta_{12}=\beta_{13}=\beta_{23}\);
5. two-equal slices \(\beta_{12}=\beta_{13}\ne\beta_{23}\);
6. ecologically relevant slices:
   - all antagonistic reciprocal pairs \(\beta>1\);
   - mixed antagonistic/mutualistic;
   - weak-pair-loop limits.

Test:
- \(x^*=(1/3,1/3,1/3)\) for fully symmetric beta;
- \(x_1=x_2\) on appropriate two-equal slices;
- uniqueness of the simplex optimizer;
- smooth dependence of \(x^*\) on \((\alpha,\beta)\).

If a closed form appears, return a precise conjecture with numerical evidence and symbolic simplification where possible.

---

# Phase P3B — validate C-14 quantitatively

Independently test the theorem

\[
T_{\alpha_1}(\beta)>T_{\alpha_2}(\beta)
\quad
\text{for }2/3<\alpha_1<\alpha_2\le1,
\]

and the asymptotic expansion

\[
T_\alpha(\beta)
=
T_1(\beta)
+
C(\beta)(1-\alpha)
+
O((1-\alpha)^2),
\]

with

\[
C(\beta)
=
\pi
\left(
\frac{S^{5/2}}{\sqrt G}
+
S^{3/2}\sqrt G
\right),
\]

\[
S=\sqrt{\beta_{12}}+\sqrt{\beta_{13}}+\sqrt{\beta_{23}},
\qquad
G=\sqrt{\beta_{12}\beta_{13}\beta_{23}}.
\]

Use high precision for \(\alpha=1-10^{-k}\), \(k=2,\ldots,10\), over diverse beta triples.

For each beta triple estimate

\[
\frac{T_\alpha-T_1}{1-\alpha}
\]

and compare it with \(C(\beta)\). Report convergence order and worst relative error.

For \(\beta=(1,1,1)\), cross-check both

\[
T_\alpha(1,1,1)=1+R_3(\alpha)^3
\]

and

\[
C(1,1,1)=12\pi\sqrt3.
\]

---

# Phase P4 — ecological motif phase diagrams

Use C-13 coordinates:

\[
\beta_{ij}=1-\frac{a_{ij}a_{ji}}{p_ip_j},
\]

\[
\kappa=
\beta_{12}+\beta_{13}+\beta_{23}-2-L_3.
\]

Produce theorem-illustration datasets, not decorative Monte Carlo.

At minimum:

1. phase diagrams in \((L_3,\alpha)\) for several fixed beta triples;
2. phase diagrams in pair-loop coordinates for fixed alpha;
3. exact classical boundary \(T_1\) and fractional boundary \(T_\alpha\);
4. width
   \[
   W_\alpha(\beta)=T_\alpha(\beta)-T_1(\beta);
   \]
5. behavior as \(\alpha\to1^-\) and \(\alpha\to2/3^+\);
6. compare antagonistic vs mutualistic pair-loop regimes.

Save plot-ready data separately from figures.

---

# Phase P5 — n=4 reconnaissance

Only after P0-P4 are complete. This phase is exploratory and must not be promoted to theorem status.

Study:

1. single 4-cycle;
2. two coupled 3-cycles;
3. cactus/shared-vertex cycles;
4. block-coupled motifs;
5. random strict-P 4x4 matrices.

Search for fractionally D-stable but non-Hurwitz-D-stable open families using global optimization over diagonal ratios.

Return 3-10 best conjecture families, each with:
- explicit parameterization;
- alpha range;
- numerical margin;
- candidate invariant/mechanism;
- whether structurally covered by Siami or classical cycle theory.

---

# Performance / reproducibility requirements

Use the server aggressively but reproducibly.

- Parallelize independent parameter cases.
- Use vectorization/JIT/process pools where appropriate.
- Record CPU count, RAM, Python/package versions, wall time, and peak memory where practical.
- Every randomized job must record seeds.
- Do not commit gigantic raw arrays.
- Commit compact summaries, worst cases, representative samples, scripts, seeds, and checksums.
- If a raw dataset is too large for git, document generation command and checksum.

---

# Repository scope

Allowed modifications:

- \`src/fdsn/\`
- \`tests/\`
- \`scripts/\`
- \`computations/\`
- \`research/\` for compute reports only

Do not modify:
- \`paper/\`
- canonical novelty conclusions unless a real counterexample is found.

---

# Required deliverables

Create at minimum:

- \`research/COMPUTE_WAVE1_FINAL_REPORT.md\`
- \`computations/scripts/\`
- \`computations/results/C10_STRESS_SUMMARY.json\`
- \`computations/results/C10_WORST_CASES.csv\`
- \`computations/results/C11_GAP_SUMMARY.csv\`
- \`computations/results/C14_LIMIT_RATE.csv\`
- \`computations/results/C13_PHASE_DATA/\`
- \`computations/results/N4_RECON_REPORT.md\` if P5 is run
- new tests under \`tests/\`

The final report must contain:

1. environment/reproducibility;
2. P0 result;
3. C-10 adversarial validation;
4. mismatches/counterexamples;
5. C-11 conservatism;
6. closed-form conjectures;
7. C-14 validation;
8. ecological phase findings;
9. n=4 reconnaissance;
10. exact reproduction commands;
11. final status:
   - \`COMPUTE_PASS\`
   - \`COMPUTE_FAIL\`
   - \`PARTIAL/BLOCKED\`

If COMPUTE_FAIL, put the counterexample at the top.

---

# Commit discipline

Work only on branch:

\`agent/compute-c10-wave1-20260925\`

Commit by phase. Do not merge to main.

At completion, push the branch and report:
- branch;
- final SHA;
- test count / pass-fail;
- compute status;
- decisive artifact paths.

This is one substantial compute wave. Do not return after only running existing tests.
