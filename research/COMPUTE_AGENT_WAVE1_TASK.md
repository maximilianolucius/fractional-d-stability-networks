# Compute Agent Wave 1 — C-10/C-13 adversarial validation and frontier exploration

**Date:** 2026-09-25  
**Assigned by:** Chief Researcher  
**Execution class:** HIGH-COMPUTE / LONG-RUN  
**Purpose:** one substantial compute campaign, not piecemeal tasks  
**Target branch:** `agent/compute-c10-wave1-20260925`

## 0. Scientific context

The current theorem package is:

- C-07: exact real 2x2 classification.
- C-09: minimum dimension with nonempty full-dimensional genuinely fractional D-stability is 3 for every 0<alpha<1.
- C-10: exact variational 3x3 characterization on the full-dimensional strict-P(-A) stratum.
- C-11: exact orbit minimum Phi and a simpler sufficient fractional Cain certificate.
- C-12/C-13: GLV abundance invariance and exact loop-coordinate interpretation.

The compute agent is **not** being asked to prove these theorems. Its job is to attack them numerically at scale, validate all formulas independently, produce reproducible theorem-illustration datasets, quantify gaps, and search for the next structural theorem.

Read first:

1. `research/THEOREM_C10_EXACT_3X3.md`
2. `research/THEOREM_C09_DIMENSION_THRESHOLD.md`
3. `research/THEOREM_C11_FRACTIONAL_CAIN_CERTIFICATE.md`
4. `research/THEOREM_C13_ECOLOGICAL_LOOP_COORDINATES.md`
5. `research/CLAIMS.md`
6. `research/Q1_PAPER_ARCHITECTURE.md`
7. `src/fdsn/cubic_certificate.py`
8. `tests/test_cubic_certificate.py`

Do not modify `paper/`.

---

# Phase P0 — reproduce and harden the computational baseline

1. Create a clean environment from `pyproject.toml`.
2. Run the full test suite.
3. Add deterministic high-precision tests (mpmath >= 80 decimal digits) for:
   - C-07 boundary cases;
   - C-09 witness family as alpha approaches 1;
   - C-10 fixed-cubic boundary;
   - C-10 simplex normalization;
   - C-11 exact Phi minimizer;
   - C-12/C-13 invariance under random positive left-diagonal scalings.
4. Add property-based/randomized tests with fixed seeds.

**Required output:** no theorem claim from these tests; label all results numerical corroboration.

---

# Phase P1 — implement the exact C-10 threshold robustly

Implement production-quality numerical utilities for

[
T_alpha(eta)
=
min_{xinDelta_2^circ}
rac{h_alpha(B_eta(x))}{x_1x_2x_3}.
]

Requirements:

- stable parameterization of the open simplex;
- deterministic global search + local refinement;
- high-precision fallback near the boundary;
- gradients/Hessian if useful;
- return optimizer x*, minimum value, stationarity residual, and conditioning diagnostics;
- verify permutation symmetry in beta;
- verify monotonicity in each beta numerically;
- verify (T_alpha	o T_1) as alpha->1;
- verify the low-order transition at alpha=2/3;
- verify the symmetric slice beta=(1,1,1) reproduces the Siami cyclic threshold to high precision.

For each computation, distinguish:
- ordinary floating-point result;
- high-precision corroboration;
- certified bound if you implement interval arithmetic.

If feasible, add an interval/branch-and-bound verifier on the 2D simplex for selected parameter points. This is valuable because it can turn figure anchor points into **CERTIFIED COMPUTATION** rather than ordinary numerics.

---

# Phase P2 — adversarial theorem stress test at scale

Generate a large reproducible population of real 3x3 matrices with -A strict P.

Do not use only one random distribution. Use at least:

1. entry-space generation with rejection;
2. generation in invariant coordinates where feasible;
3. perturbations around the C-09 cyclic witness;
4. samples close to:
   - principal-minor boundaries;
   - classical Cain boundary kappa=T1(beta);
   - fractional boundary kappa=T_alpha(beta);
   - alpha near 2/3;
   - alpha near 1.

Recommended scale on the large server: at least (10^6) matrix/alpha cases total, preferably more if efficient.

Use an alpha grid that is deliberately boundary-heavy, e.g.

[
0.10, 0.30, 0.60, 2/3, 0.70, 0.80, 0.90, 0.95, 0.99, 0.999, 0.9999.
]

For each candidate:

1. classify using C-10;
2. independently minimize the direct spectral margin over positive diagonal ratios:
   [
   min_{Dsucc0 /	ext{ common scale}}
   min_i |arglambda_i(DA)|-alphapi/2;
   ]
3. use multiple global optimizers / starts;
4. rerun all mismatches and near-zero margins at high precision;
5. search aggressively for a counterexample to C-10.

**Stop-the-line rule:** if any genuine mismatch survives high precision, create a smallest explicit counterexample immediately and mark C-10 COMPUTE-FAIL. Do not average it away.

Required summary:
- number of cases;
- distributions;
- minimum observed theorem-vs-direct discrepancy;
- all near-boundary worst cases;
- zero/mismatch count.

---

# Phase P3 — quantify C-11 conservatism and identify closed-form slices

C-11 is sufficient but not necessary. Quantify exactly how conservative it is.

For broad beta/alpha grids compute:

[
T_alpha(eta),
qquad
T_1(eta),
qquad
T_{Phi,alpha}(eta)
]

where the last denotes the effective boundary implied by the scalar Phi certificate.

Deliver:

1. ratio/gap statistics;
2. worst and best cases;
3. heatmaps/CSV data in invariant space;
4. symmetric slice beta12=beta13=beta23;
5. two-equal slices beta12=beta13 != beta23;
6. ecologically relevant slices:
   - all antagonistic reciprocal pairs beta>1;
   - mixed antagonistic/mutualistic;
   - weak-pair-loop limits.

Search for simple formulas or optimizer patterns.

In particular test conjectures such as:
- x*= (1/3,1/3,1/3) for fully symmetric beta;
- x1=x2 on two-equal beta slices;
- uniqueness of the simplex optimizer;
- smooth dependence of x* on (alpha,beta).

If a closed form appears, derive it symbolically or numerically to enough precision to hand back a precise conjecture to the Chief.

---

# Phase P4 — ecological motif phase diagrams

Use C-13 coordinates:

[
eta_{ij}=1-rac{a_{ij}a_{ji}}{p_ip_j},
]

[
kappa=
eta_{12}+eta_{13}+eta_{23}-2-L_3.
]

Produce theorem-illustration datasets, not decorative Monte Carlo.

At minimum:

1. phase diagrams in ((L_3,alpha)) for several fixed beta triples;
2. phase diagrams in pair-loop coordinates for fixed alpha;
3. exact classical boundary (T_1) and fractional boundary (T_alpha);
4. width
   [
   W_alpha(eta)=T_alpha(eta)-T_1(eta);
   ]
5. behavior as alpha->1 and alpha->2/3+;
6. compare antagonistic vs mutualistic pair-loop regimes.

Save data separately from figures so the paper can reproduce every plot.

---

# Phase P5 — n=4 reconnaissance (stretch but significant)

Only after P0-P4 are complete.

This phase is **exploratory** and must not be promoted to theorem status.

Goal: determine whether the 3x3 invariant/simplex mechanism suggests a tractable n=4 next theorem.

Tasks:

1. Generate structured 4x4 strict-P(-A) families:
   - single 4-cycle;
   - two coupled 3-cycles;
   - cactus/shared-vertex cycles;
   - block-coupled motifs;
   - random strict-P matrices.
2. Search for fractionally D-stable but non-Hurwitz-D-stable open families using global optimization over diagonal ratios.
3. Record principal-minor / cycle quantities of successful and failed examples.
4. Test whether simple extensions of the 3x3 normalized coefficient picture explain the boundary.
5. Return 3-10 best conjecture families, each with:
   - explicit matrix parameterization;
   - alpha range;
   - numerical margin;
   - candidate invariant/mechanism;
   - whether the family is already structurally covered by Siami or classical cycle theory.

No paper prose. This phase is for the Chief to decide the next theorem programme.

---

# Performance / reproducibility requirements

The server is valuable; use it.

- Parallelize independent parameter cases.
- Use vectorization/JIT/process pools where appropriate.
- Record CPU count, RAM, Python/package versions, wall time, and peak memory where practical.
- Every randomized job must have recorded seeds.
- Use deterministic filenames.
- Do not store gigantic raw arrays in git. Store compact summaries, worst cases, representative samples, and compressed aggregate files only.
- If a raw dataset is too large for git, document its generation command and checksum.
- No external private data are required.

---

# Repository scope

Allowed modifications:

- `src/fdsn/`
- `tests/`
- `scripts/`
- `computations/`
- `research/` for compute reports only

Do not modify:

- `paper/`
- novelty conclusions in `research/CLAIMS.md` unless you find a counterexample; in that case mark the affected claim COMPUTE-FAIL in your report and return it to the Chief rather than silently rewriting the project thesis.

---

# Required deliverables

Create at minimum:

- `research/COMPUTE_WAVE1_FINAL_REPORT.md`
- `computations/scripts/` — reproducible campaign scripts
- `computations/results/C10_STRESS_SUMMARY.json`
- `computations/results/C10_WORST_CASES.csv`
- `computations/results/C11_GAP_SUMMARY.csv`
- `computations/results/C13_PHASE_DATA/` — compact plot-ready data
- `computations/results/N4_RECON_REPORT.md` if P5 is run
- new tests under `tests/`

The final report must contain sections:

1. environment/reproducibility;
2. P0 result;
3. C-10 adversarial validation result;
4. any mismatches/counterexamples;
5. C-11 conservatism;
6. closed-form conjectures found;
7. ecological phase findings;
8. n=4 reconnaissance;
9. exact commands to reproduce;
10. final status:
   - `COMPUTE_PASS`
   - `COMPUTE_FAIL`
   - `PARTIAL/BLOCKED`

If `COMPUTE_FAIL`, put the counterexample at the top of the report.

---

# Commit discipline

Work only on branch:

`agent/compute-c10-wave1-20260925`

Commit by phase (P0, P1, P2, ...). Do not merge to main.

At completion, push the branch and report:
- branch name;
- final SHA;
- test count / pass-fail;
- compute status;
- paths of decisive artifacts.

This is a single substantial compute wave. Do not return after only running the existing tests.
