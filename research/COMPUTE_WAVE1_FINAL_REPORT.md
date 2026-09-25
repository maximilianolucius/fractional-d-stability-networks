# Compute Wave 1 — final report (C-10 / C-09 / C-11 / C-13 / C-14)

**Branch:** `agent/compute-c10-wave1-20260925`  
**Date:** 2026-09-25  
**Final status: COMPUTE_PASS** (C-10, C-09, C-11 soundness, C-14: no counterexample survives high precision)

Evidence labels used throughout: **NUMERICAL** (float64), **HP** (mpmath, digits stated),
**CERTIFIED** (interval arithmetic, outward rounding), **PROOF SKETCH** (analytic argument written
here by the compute agent — must be audited before any promotion; it is *not* a theorem of the
project until the Chief/audit accepts it). No computation here is used as proof of C-07…C-14.

---

## 1. Environment / reproducibility

- Server aureus: AMD Ryzen 9 9950X (16C/32T), 186 GB RAM, shared with other workloads. All jobs ran
  with `nice 5–15`, `OMP_NUM_THREADS=1`, ≤16 worker processes; peak RSS of any process < 1.5 GB.
- Python 3.12.3, numpy 2.5.3, scipy 1.18.1, mpmath 1.3.0, sympy 1.14.0, hypothesis 6.168.1
  (`computations/results/ENVIRONMENT.json`, `pip_freeze.txt`).
- Every randomized block records its seed in its output JSON. P2 master seed `20260925`; job seed
  `= 20260925*1000 + hash(mech)*100000 + job` (generation is replayable).
- Raw P2 arrays (`computations/raw/p2_*.npz`) are not committed; SHA-256 checksums are in
  `C10_STRESS_SUMMARY.json`.

## 2. P0 — baseline

- `pip install -e .[dev]` in a clean venv; `mpmath` added to dependencies, `hypothesis`,
  `pytest-xdist` to dev extras.
- New library code: `src/fdsn/c10_threshold.py` (T_α, analytic gradient/Hessian in logit
  coordinates, mp refinement, invariants, matrix construction from C-13 coordinates),
  `src/fdsn/direct_margin.py` (theorem-independent D-orbit margin minimisation using only
  eigenvalues), `src/fdsn/interval_cert.py` (certified bracket of T_α).
- New tests: `tests/test_high_precision.py` (≥80–110 digits: C-07 boundary cases, C-09 witness as
  α→1⁻ incl. γ_Φ−2 ~ (3π/2)(1−α), C-10 fixed-cubic boundary exactness and homogeneity, simplex
  normalisation from eigenvalues of DA, C-11 Φ minimiser, C-12/C-13 invariance and loop identity,
  C-14 monotonicity/rate, α→2/3 blow-up), `tests/test_c10_numerics.py` (fixed-seed hypothesis
  property tests), `tests/test_p1_structure.py`.
- **Test suite: 121 tests, 121 passed** (`pytest -n 4`, aureus). Label: NUMERICAL/HP corroboration.

## 3. P1 — the exact threshold T_α(β) (`P1_THRESHOLD_VALIDATION.json`)

Implementation: minimise G(y)=log h_α(B_β(x))−Σlog x_i over logits y (x=softmax(y₁,y₂,0)) —
logit grid [−12,12]² + damped Newton with analytic Hessian; HP Newton at any precision.

| check | result | label |
|---|---|---|
| float vs 40-digit HP, 4000 random (β,α) | max rel err 7.1e−12 (worst at α=0.66674: float K=1−4u² input-conditioning), median 8.9e−16 | NUMERICAL vs HP |
| stationarity / conditioning | HP ‖∇G‖ ≤ 3.8e−34; min Hessian eigenvalue ≥ 7.4e−3; cond ≤ 131 | HP |
| permutation symmetry, 20k × 5 perms | max rel diff 3.8e−15 | NUMERICAL |
| monotone in each β_ij, 180k perturbations | 0 violations | NUMERICAL |
| T_α → T_1, α=1−10^{−k}, k=1..10, 300 β | gap>0 always; (T_α/T_1−1)/(1−α) converges | HP 60 |
| symmetric slice vs Siami, 12 α's | |T−(1+R₃³)|/T ≤ 4.0e−107 | HP 105 |
| uniqueness: all grid local minima refined, 4000 cases | 0 cases with >1 distinct minimum | NUMERICAL |
| logit Hessian PD at 1.28 M random points | 0 failures (affine-x Hessian is *not* PSD at 16% of points) | NUMERICAL |
| 60 anchor points (10 β × 6 α) | **all CERTIFIED**, relative bracket width ≈1e−39 | CERTIFIED |

Certified method (`fdsn/interval_cert.py`): boundary strip x_i<ε excluded by F>4h(0)/ε>2U;
certified-PD interval Hessian on a box around the HP minimiser (convexity ⇒ G ≥ G(x̂)−‖∇G(x̂)‖₁ρ);
branch-and-bound with monotone and mean-value interval bounds elsewhere.
`computations/results/P1_CERTIFIED_ANCHORS.csv`.

### 3.1 New structural facts (PROOF SKETCH + NUMERICAL/SYMBOLIC corroboration)

**(a) Strict convexity in logit coordinates ⇒ unique minimiser.** With L=log(e^{y₁}+e^{y₂}+1),
Q=log Σ_{i<j}β_ij e^{y_i+y_j} (both convex), φ(s)=log h_α(eˢ):

G = φ(Q − 2L) + 3L − y₁ − y₂,  ∇²G = φ''∇s∇sᵀ + φ'∇²Q + (3−2φ')∇²L.

φ' is the elasticity E = b h'/h; along b = Kr²−2ur (r>2u/K):
E(r) = (Kr−2u)(1+3ur) / ((Kr−u)(1+2ur)), both factors strictly increasing
(derivatives Ku/(Kr−u)² and u/(1+2ur)², sympy), E(2u/K)=0, E→3/2. Hence φ'∈(0,3/2), φ''≥0, and
∇²G ≻ 0 because ∇²L ≻ 0 on ℝ². G is coercive, so **the simplex minimiser is unique and
nondegenerate for every β≻0, 2/3<α<1**; T_α is a smooth convex program. This supplies the
nondegeneracy used by the C-14 envelope argument. (At α=1, φ'≡1 recovers convexity of Cain's
objective.)

**(b) Symmetric slice closed form.** By (a) and permutation symmetry, β₁₂=β₁₃=β₂₃=b ⇒ x*=(1/3,1/3,1/3):

  **T_α(b,b,b) = 27 h_α(b/3).**

For b=1, sympy proves 27h_α(1/3) ≡ 1+R₃(α)³ (using √(u²+K/3)=sinθ/√3), i.e. C-10 reproduces the
Siami cyclic boundary *identically*, not just numerically. Numerically: rel err ≤ 3e−15 on
b∈[1e−6,1e6], x*=1/3 exactly.

**(c) Two-equal slice.** β₁₂=β₁₃ ⇒ x₂*=x₃* (swap symmetry + uniqueness); numerically
|x₂*−x₃*| ≤ 1.5e−13 on 50k cases. The slice reduces to a 1-D problem (see (d)).

**(d) Explicit parametrisation of the whole threshold surface.** The Lagrange conditions
μ x_i ∂_iB = 1+λx_i (μ=h'/h, λ=2μB−3) are *linear* in β. Solving:

  β_ij = B·[1 + (2E−3)(1−2x_k)] / (2E x_i x_j),  T_α = r²(1+2ur)/(x₁x₂x₃),

with B=Kr²−2ur, E=E(r), {i,j,k}={1,2,3}. By (a), the map (x,r)↦β is a bijection from the admissible
set {all three brackets >0} onto ℝ³₊, so **{(β, T_α(β))} is the image of an explicit
algebraic map of (x₁,x₂,r)**. Verified on 101,618 admissible random (x,r): max rel err in T
6.9e−15, max |x−x*| 2e−9 (NUMERICAL), HP spot checks 5e−14 (limited by float β). At α=1 (E≡1)
it collapses to β_ij ∝ x_k², i.e. Cain's minimiser.

**(e) Low-order transition α→2/3⁺.** With K=1−4cos²(απ/2)→0⁺:

  **T_α(β) = 27/K³ + (9(β₁₂+β₁₃+β₂₃) − 27)/K² + O(1/K).**

HP (80 digits, α=2/3+10^{−k}, k up to 15, 20 β): leading term error 1.8e−7, second-order 6.3e−8 at
k≥9; sympy series of the centre evaluation confirms both orders. The blow-up rate is universal
(independent of β); the first β-dependence is through Σβ only.

**(f) Realizability.** For real A, ℓ₁₂₃ℓ₁₃₂ = g₁₂g₁₃g₂₃ =: G, so L₃ = ℓ+G/ℓ needs L₃² ≥ 4G when
G>0. At κ=T₁, |L₃| = 2+2Σ√(β_iβ_j) ≥ 2√G in every sign pattern, and |L₃| grows with κ; hence
**every (β,κ) with κ ≥ T₁(β) is realised by a real matrix**, so the band T₁<κ<T_α is nonempty in
matrix space for *every* β (not just for one witness). Invariant points with κ<T₁ can be
non-realizable when G>0.

## 4. P2 — adversarial validation of C-10

Scripts: `p2_stress.py` (float), `p2_hp_verify.py`, `p2_hp_controls.py`, `p2_hp_recheck.py`,
`p2_c5_lemma2_witness.py`, `p2_finalize_summary.py`. Summary: `C10_STRESS_SUMMARY.json`;
closest-to-boundary cases: `C10_WORST_CASES.csv` (5000 HP cases, full matrices).

**Scale:** 2,060,000 C-10 matrix/α cases + 120,000 control cases = 2,180,000 (float stage 6,143 s wall,
16 workers); HP stage 56,234 flagged cases (5,425 s wall, 82,442 CPU-s).
α grid: 0.1, 0.3, 0.6, 2/3, 2/3+1e−7, 2/3+1e−4, 0.7, 0.8, 0.9, 0.95, 0.99, 0.999, 0.9999, plus continuous α
in M4a/M4d/M4e (α=2/3+10^{−U[1,8]}, 1−10^{−U[1,6]}).

**Direct side (independent of the proof):** min over D of min|arg λ(DA)|−απ/2 with LAPACK eigenvalues
of the full matrix only — O1 log-grid [−16,16]² step 0.5 + pattern search from 3 separated starts
(all cases); O2 Nelder–Mead from O1 + 2 random starts (799,898 runs); O3 differential evolution
(45,460 runs). Random positive-diagonal similarity, permutation and row scaling applied to every
generated matrix. Float decision tolerance = max(1e−12, 10× a-posteriori eigen-angle error).

| mechanism | cases | theorem: member | float mismatches | near-zero → HP | min |κ/T−1| |
|---|---|---|---|---|---|
| M1 entry space (normal / t₁.₅ / sparse) × 13 α | 520,000 | 516,371 | 0 | 0 | 2.3e−5 |
| M2 invariant coords, κ=T·10^{U[−1,1]} | 300,000 | 192,915 | 0 | 0 | 2.2e−6 |
| M3 perturbed cyclic witness A_γ | 150,000 | 117,920 | 0 | 0 | 1.3e−5 |
| M4a κ=T_α(1±10^{−U[1,9]}) | 450,000 | 224,938 | 0 | 24,386 | 1.0e−11 |
| M4b κ=T₁(1±δ) (Cain boundary) | 100,000 | 98,442 | 0 | 0 | 3.3e−6 |
| M4c tiny β_ij / tiny κ (minor boundary) | 120,000 | 101,230 | 0 | 1,714 | 1.5e−10 |
| M4d α=2/3+10^{−U[1,8]} at the boundary | 120,000 | 60,261 | 0 | 22,593 | 7.6e−10 |
| M4e α=1−10^{−U[1,6]}, inside/at thin band | 180,000 | 119,969 | 0 | 2,474 | 6.8e−12 |
| M4f extreme β (1e−6…1e6) at the boundary | 120,000 | 59,737 | 0 | 5,079 | 3.2e−8 |
| C5 control: −A not P₀ or det(−A)≤0 | 60,000 | 0 (Lemma 2) | 0 | 0 | — |
| C6 control: α=1, κ=T₁(1±δ) (Cain) | 60,000 | 29,747 | 0 | 0 | 1.0e−9 |

- **Float stage: 0 mismatches** in all 2,180,000 cases.
- **HP stage:** all 56,234 flagged cases (near-zero direct margin or |κ/T−1|<1e−10) recomputed from
  the exact binary entries: invariants and T_α at 60 digits, mp.eig margins at 40 digits, local mp
  search from the float direct optimizer and separately from the theorem minimiser.
  **56,234/56,234 consistent**, and 56,234/56,234 consistent using *only* the independent start.
  0 escalations to 110 digits were needed. Example extremes (`C10_WORST_CASES.csv`): α=2/3+1.1e−8,
  κ/T−1=+4.9e−11 → HP min margin −2.9e−19 (unstable, as predicted); κ/T−1=−7.4e−10 → +4.9e−18 (stable).
- **Theorem minimiser vs direct worst D:** near the boundary (|κ/T−1|<1e−4, 530k cases) the orbit
  coordinates of the direct optimum agree with the C-10 simplex minimiser x*: median max-abs
  difference 4e−8…8e−7, p99 ≤ 5.4e−5, max 1.2e−4 (M4d, α→2/3 where the margin is ~K-flat).
- **Optimizer disagreement** (O2/O3 below O1 by >1e−9): 134 cases (M1 51, M2 2, M4c 81), all far from
  the boundary; the final margin is the minimum over optimizers, and none changed a classification.
- Direct-margin distributions per mechanism: `C10_STRESS_SUMMARY.json → mechanisms.*.margin_quantiles_*`.

## 5. Mismatches / counterexamples

**None.** GENUINE_C10_COUNTEREXAMPLES = 0. What had to be ruled out (every item recorded in the JSONs):

1. *Pilot run (before the float reliability filter):* float margin exactly −θ at extreme diagonal
   ratios (~e^32) — an eigenvalue of size ~1e−14‖DA‖ acquired a spurious positive sign. Fixed by
   excluding |λ|<1e−10·max|λ| from the float minimum; the excluded region was then audited in mp
   (item 4).
2. *HP control sample v1* (1,650 random non-flagged cases): 95 reported inconsistent. Cause: the
   control protocol started the local mp search at D=I; the C5 controls (outside C-10's hypothesis)
   need extreme D. Superseded.
3. *HP control sample v2* (float global start): 117 inconsistent = 31 C5 + 86 strict-P. Recheck
   (`P2_HP_RECHECK.json`): in all 86 strict-P cases the unbounded mp pattern search had run away to
   |w|∈[50, 205] (ratios up to e^205) where 40 digits cannot resolve the smallest eigenvalue;
   re-evaluated at 60+2|w|/ln10 digits (≤240) the margin is positive in 86/86, and a bounded search
   (|w|≤16, 60 digits) finds 0 negative margins. Several of these were at α=0.1/0.3 where the Kellogg
   wedge already guarantees membership — consistent with an artefact.
   The 31 C5 controls: analytic Lemma-2 witnesses (dominant row with a_ii>0; 2×2 block with negative
   minor; D=I when det A≥0) verified at 150 digits for **150/150** C5 controls in the sample
   (`P2_C5_LEMMA2_WITNESSES.json`) — Lemma 2 corroborated.
4. *Extreme-scaling audit:* v1 (60 digits for ratios up to 1e60) gave 127 spurious negatives;
   v2 at 250 digits with ratios 1e30 and 1e60 in 12 corner patterns: **0 negatives in 1,350
   strict-P cases**, minimum margin 1.6e−4 (so the orbit boundary region does not hide instabilities).

Lessons: the mp re-verifier must bound the search box or scale precision with |log d|; float eigenvalue
angles are meaningless below ~1e−10 of the spectral radius.

## 6. P3 — C-11 conservatism (`C11_GAP_SUMMARY.csv`, `C11_GAP_GRID.csv`, `P3_SLICES.json`)

In κ-space the C-11 certificate reads Φ(A)=T₁/κ > ρ_α ⇔ κ < T_Φ := T₁/ρ_α.
Certified fraction of the genuinely fractional band: f = (T_Φ−T₁)/(T_α−T₁) ∈ (0,1].

- **Soundness:** T_Φ ≤ T_α in all 10,659 grid points + 200,000 random (β,α): 0 violations.
- Grid β_ij ∈ logspace(−2,2,21) (1,771 unordered triples) × 11 α:

| α | f min | f median | f max | T_Φ/T_α min |
|---|---|---|---|---|
| 0.6667 | 0.000 | 0.0009 | 0.024 | 0.000 |
| 0.70 | 0.0026 | 0.449 | 1.000 | 0.0026 |
| 0.80 | 0.012 | 0.744 | 1.000 | 0.014 |
| 0.90 | 0.027 | 0.787 | 1.000 | 0.050 |
| 0.95 | 0.045 | 0.774 | 1.000 | 0.141 |
| 0.99 | 0.092 | 0.716 | 1.000 | 0.620 |
| 0.9999 | 0.115 | 0.682 | 1.000 | 0.995 |

- Worst case everywhere: small pair invariants β=(0.01,0.01,0.01) (strongly mutualistic/competitive
  pairs). Best: large/anisotropic antagonistic triples (f→1).
- **C-11 conservatism does not vanish as α→1.** Exact limit (sympy):
  **f → 2π T₁/C(β) = 2√(SG)/(S+G) ≤ 1**, equality iff S=G (AM-GM). Symmetric slice:
  f→2√3·√b/(3+b) (0.115 at b=0.01, 0.866 at b=1, exactly 1 at b=3); matches the α=0.9999 grid.
  In relative κ-terms T_Φ/T_α→1 (because W→0), but as a fraction of the band C-11 can miss up to
  ~100% of it for small β, uniformly as α→1.
- At α→2/3⁺: ρ_α→0 like (2u−1)² ~ K²/4 so T_Φ ~ 4T₁/K², while T_α ~ 27/K³: f→0.
- Symmetric b=1 (Siami slice): T_Φ/T_α = 0.092 (α=.68), 0.46 (.75), 0.87 (.9), 0.99 (.99).

## 7. Closed-form conjectures / results

1. T_α(b,b,b) = 27h_α(b/3) — PROOF SKETCH via §3.1(a,b).
2. Explicit parametric closed form of T_α on all of ℝ³₊ — §3.1(d), PROOF SKETCH.
3. T_α = 27/K³ + (9Σβ−27)/K² + O(1/K) as α→2/3⁺ — CONJECTURE with HP + symbolic support.
4. T_α(1,1,1) = 9 + 12√3π ε + 36π² ε² + 31√3π³ ε³ + O(ε⁴), ε=1−α (exact series of 1+R₃³, sympy;
   numeric second-order coefficient from C-10 agrees to 5e−10).
5. C-11 band fraction limit 2√(SG)/(S+G) — PROOF SKETCH (from C-14 and ρ_α = 1−2πε+O(ε²)).

## 8. P3B — C-14 (`C14_LIMIT_RATE.csv`, `P3B_C14_SUMMARY.json`)

100 β triples (11 structured incl. extreme 1e−4…1e4, 89 lognormal), α=1−10^{−k}, k=2..10, HP 70 digits.

- rate (T_α−T₁)/(1−α) → C(β): worst relative error 0.52 (k=2), 7.9e−3 (k=5), 9.2e−7 (k=9),
  **9.2e−8 (k=10)**; median convergence order 1.000000002 (last step), min 0.99999 — residual is
  O((1−α)²) as claimed.
- Second-order coefficient D(β)=lim (T−T₁−Cε)/ε²: stabilised to 1.5e−5 between k=9 and 10;
  D/C ranges from −920 to +9.3 — **D can be negative and large for extreme β**, so the linear
  asymptotic is accurate only for 1−α ≪ C/|D| (≈1e−3 for the worst triple). Not a contradiction.
- Monotonicity: T strictly decreasing on 40 α's in (2/3,1) for all 100 β; plus 0 violations in P3.
- β=(1,1,1): C = 12π√3 to 1e−59; D = 36π² (exact) vs numeric 355.30575861 (k=10).
- **C-14: no disagreement found (COMPUTE-PASS for C-14).**

## 9. P4 — ecological phase data (`computations/results/C13_PHASE_DATA/`)

- (L₃,α) boundaries for 9 motif triples (no pair loops; all antagonistic; mixed; mutualistic/
  competitive; weak-pair-loop limit; strong antagonism): 500 α-points each, T₁, T_α, W_α, L₃ cuts,
  realizability column. Pair-loop (g₁₂,g₁₃) grids 140² at α∈{0.75,0.9,0.99}, g₂₃∈{0,−2,0.5}.
- **Independent validation:** 8,100 matrices sampled inside CLASSICAL / FRACTIONAL / UNSTABLE regions
  (9 triples × 3 α) classified by direct eigenvalue minimisation over D, for α and for α=1:
  **8,100/8,100 agree** with the C-10/C-13 regions (NUMERICAL).
- W/(C(1−α)) = 1+O(1e−6) at 1−α=1e−7 and W·K³/27 = 1+O(1e−5) at α=2/3+1e−7 for every triple.
- Antagonistic vs mutualistic (symmetric slice, exact closed form): W_α increases strictly with b
  (antagonism) at every α tested; e.g. α=0.9: W=8.63 (b=0.5), 12.93 (b=1), 30.67 (b=3).
  The *relative* width W/T₁ is not monotone in b.
- Figures (illustrative only) in `C13_PHASE_DATA/figures/`; plot-ready CSVs separate.

## 10. P5 — n=4 reconnaissance (EXPLORATORY)

Full write-up: `computations/results/N4_RECON_REPORT.md` (data `N4_RECON.json`). Highlights:
- single 4-cycle reproduces Siami R₄(α)=sin(απ/2)/sin(απ/2−π/4) and Hurwitz γ=√2 (covered);
- the C-10 orbit reduction extends verbatim: quartic built from 11 normalised principal-minor
  invariants on the 3-simplex agrees with eigenvalue margins to 1.5e−13;
- open genuinely-fractional families beyond single cycles (two 3-cycles sharing an edge; 3-cycle +
  pendant pair); pendant-coupling sign rule (antagonistic coupling preserved F at all scanned points,
  mutualistic removed 37%);
- random strict-P 4×4 (8,000): no non-member for α≤0.75, GF fraction 2.1% → 0.34% as α: 0.75 → 0.99;
- the DE objective min(m_α,−m₁) turned out to be trivially bounded by (1−α)π/4 for every n and was
  saturated by both n=3 and n=4 — **uninformative, reported as a negative result**.

## 11. Final status

| claim | verdict | evidence |
|---|---|---|
| C-10 (exact 3×3 criterion) | **COMPUTE_PASS** | 2.06M cases, 0 float mismatches, 56,234/56,234 HP-consistent, 0 after recheck |
| C-09 (dimension threshold) | COMPUTE_PASS | witness family at 80–110 digits; band nonempty for every β (realizability §3.1f) |
| C-11 (sufficiency of Φ>ρ) | COMPUTE_PASS (sound); conservative | 0 violations of T_Φ≤T_α in 210k (β,α); band fraction limit 2√(SG)/(S+G) |
| C-12/C-13 | COMPUTE_PASS | 80-digit invariance tests; 8,100/8,100 phase-region validations |
| C-14 | COMPUTE_PASS | order-1 convergence, worst rel err 9.2e−8 at 1−α=1e−10; monotone everywhere tested |
| Lemma 2 (P₀ necessity) | corroborated | 150/150 analytic witnesses at 150 digits |

**Overall: COMPUTE_PASS.** Computations corroborate; they do not replace the proofs.

## 12. Reproduction commands

```bash
python3 -m venv venv && venv/bin/pip install -e .[dev] numba sympy
venv/bin/python -m pytest -n 8                                   # P0
venv/bin/python computations/scripts/env_info.py
venv/bin/python computations/scripts/p1_threshold_validation.py  # P1 (~4 min, 16 workers)
venv/bin/python computations/scripts/symbolic_checks.py
venv/bin/python computations/scripts/p2_stress.py                # P2 float stage
venv/bin/python computations/scripts/p2_hp_verify.py             # P2 HP stage (flagged cases)
venv/bin/python computations/scripts/p2_hp_controls.py           # corrected controls + 250-digit audit
venv/bin/python computations/scripts/p2_hp_recheck.py            # recheck of reported control failures
venv/bin/python computations/scripts/p2_c5_lemma2_witness.py     # Lemma-2 witnesses for C5 controls
venv/bin/python computations/scripts/p2_finalize_summary.py      # final accounting
venv/bin/python computations/scripts/p3_gaps_slices.py           # P3
venv/bin/python computations/scripts/p3b_c14.py                  # P3B
venv/bin/python computations/scripts/p4_phase.py                 # P4
venv/bin/python computations/scripts/p5_n4_recon.py              # P5
```
Worker count: `FDSN_WORKERS` (default 16).
