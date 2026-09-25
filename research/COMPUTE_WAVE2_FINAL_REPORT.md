COMPUTE2_PASS

# Compute Wave 2 — final report (certified atlas, canonical witnesses, robustness, C-15, figure data)

**Branch:** `agent/compute-wave2-20260925`  
**Baseline SHA:** `a8f73dca967e20e90c4dbb7e4aa77d2d6b170497`  
**Final SHA:** HEAD of the branch (commit `wave2: final report`); last artifact commit `33b48f6` (P6).  
**Date:** 2026-09-25  
**Server:** aureus (AMD Ryzen 9 9950X, 32 threads, 186 GB; shared; ≤16 workers, `nice 5–8`, `OMP_NUM_THREADS=1`)

Evidence labels: **CERTIFIED** (outward-rounded interval arithmetic, `fdsn.interval_cert`), **HP** (mpmath, digits
stated), **FLOAT** (float64), **EXACT** (rational arithmetic / closed formula), **PROOF** (elementary argument written
here, for Chief review), **CONJECTURE** / **NUMERICAL OBSERVATION**. Computation corroborates; it does not prove C-10/C-15.

## Executive summary

| item | value |
|---|---|
| tests | **135 passed, 0 failed** (121 baseline + 14 new in `tests/test_wave2.py`); baseline suite 121/121 before any edit |
| certified atlas points | **938 / 938** (0 failures); 903 with the unconditional x-space certificate, all 938 with the logit certificate (conditional on C-15 Thm 1) |
| worst certified relative width | **1.09e−35** (α = 2/3+1e−5, β=1000 symmetric); ordinary region 7.6e−39; median 1.4e−39; targets (1e−12 / 1e−9) met everywhere |
| optimizer enclosure | x* enclosed at every atlas point, radius ≤ 7.4e−34 (median 5e−40) |
| canonical witnesses | **35** (all 10 categories; integers / rationals / short decimals); **10 with CERTIFIED T_α** on the exact rational invariants |
| robustness study | **14 witnesses**, 3 boundaries × 2 norms; **748 constrained/global optimizations + 126,756 directional root-solves** (127,504 total); HP-refined bounds |
| C-15 differential checks | **128,000 float checks** (8,000 points × 16) + **2,500 HP checks** (500 worst points × 5, 40 digits) |
| discrepancies with C-10 / C-15 | **NONE** |
| precision pathologies | 4 identified, all resolved and documented (§8); none is a mathematical discrepancy |
| P6 | **DONE** — exact-looking structure found: two 3-cycles sharing an edge are in F_α iff s+t < R₃(α)³ (necessity PROVED by a cycle-merging lemma, sufficiency CONJECTURE); future-paper only |

Decisive artifacts (all under `computations/results/wave2/`):
`CERTIFIED_THRESHOLD_ATLAS.csv`, `CERTIFIED_THRESHOLD_ATLAS_SUMMARY.json`, `CANONICAL_WITNESSES.{csv,json}`,
`CANONICAL_WITNESSES_README.md`, `ROBUSTNESS_SUMMARY.csv`, `ROBUSTNESS_DETAILS.json`, `C15_SENSITIVITY_VALIDATION.json`,
`C15_SENSITIVITY_WORST.csv`, `FIGURE_DATA/F1..F9/`, `N4_SHARED_EDGE_CONJECTURE.md` (+`_DATA.json`, `_BOUNDARY.csv`,
`_VERIFY.json`), `ENVIRONMENT.json`, `P0_TEST_RESULT.txt`, `FINAL_TEST_RESULT.txt`.
Scripts: `computations/scripts/wave2/w2_p{0..6}_*.py`; reusable infrastructure in `src/fdsn/interval_cert.py`
(new `certify_threshold_logit`, rigorous x*-localisation in `certify_threshold`) and `src/fdsn/c10_threshold.py`
(exact rational inputs). Tests: `tests/test_wave2.py`.

## Most important findings

1. **Certified atlas at 1e−35 or better on 938 points**, including α = 2/3+1e−8 (T ≈ 1e23) and α = 1−1e−10, and
   β spreads of 1e8 (family F). At every point the independent 50-digit Newton value lies inside the bracket, and on
   the symmetric family the closed form 27 h_α(b/3) (C-15 Cor. 1) lies inside the bracket (312/312).
2. **Two certification routes agree.** The Wave-1 unconditional x-space branch-and-bound (upgraded: target = upper
   bound ⇒ rigorous localisation of x*) and a new logit-coordinate certificate that uses only (i) an interval Hessian
   ≥ λ > 0 on a box and (ii) ‖∇G(ŷ)‖ < λR — valid given C-15 Theorem 1. The logit route costs 0.13 s regardless of
   anisotropy; the x-space route exceeded its 240 s budget on 35 extreme-anisotropy points (β ∈ {1e−4, 1e4}),
   which therefore carry only the conditional certificate (listed in the summary JSON, `conditional_only`).
3. **Canonical witness library**: 35 explicit matrices, e.g. `[[-1,-3,0],[0,-1,-2],[-2,0,-1]]` at α=0.8
   (κ=13, T₁=9, T_α=96.72), `[[-1,-3/2,0],[-1/2,-1,-3],[-3,0,-2]]` at α=0.7 (Hurwitz at I, κ=7 > T₁=6.25),
   Siami slice γ ∈ {2.01, 2.1, 2.5, 2.75, 3, 40, 150, 2.005, 2.03}. For every witness the constructed worst diagonal
   D* = diag(x*_i/p_i) gives a positive mp.eig Matignon margin, the independent float global minimisation over D
   is positive at α and negative at α = 1, and the explicit Cain minimiser D_H produces an eigenvalue with
   Re ≥ 0 (35/35 consistent). Band positions range from 2e−5 to 0.991; 27/35 also pass the C-11 scalar certificate,
   8 are genuinely fractional but C-11-uncertified (C-11 not necessary, as in C-10 §8).
4. **Robustness (P3).** Genuinely fractional witnesses are not knife-edge: in the max-entry norm the nearest
   perturbation to the exact fractional boundary is 0.046 (W01, γ=2.5, α=0.9), 0.66 (W10), 0.17 (W02); to the Cain
   boundary 0.125 (W01), 0.25 (W02); the strict-P boundary distance is 0.20–0.56 (exact Eckart–Young σ_min).
   Deliberately near-boundary witnesses (W04, W28 at band position 0.99; W05, W26 at ≈0.01) have distances
   1e−3–3e−3, as designed. Local first-order estimates are within a factor 0.6–1.8 of the optimised bounds
   (the sets are curved). For 4 witnesses at α = 0.7 (T_α ≈ 5e3 ≫ κ) every tried direction leaves the strict-P
   stratum before reaching the fractional boundary: reported as "not reached", not as a distance.
5. **C-15 derivative identity verified**: ∂T/∂β_ij = h'_α(B*)/x_k* to 2.4e−33 (HP, 500 worst points), ∂T/∂α
   envelope formula to 1.75e−28 (limited by h⁴ Richardson truncation, verified to scale as h⁴), implicit-function
   sensitivities of x* to 9.5e−5 (float FD, structurally consistent), logit Hessian PD at all 8,000 points
   (min eigenvalue 4.6e−3, condition number ≤ 141), permutation equivariance to 7e−15.
6. **Two SYMBOLIC IDENTITIES** (follow from the envelope formula + C-15 z_ij formula; verified to 7e−15 / 6e−11):
   Euler-type  Σ_{ij} β_ij ∂T/∂β_ij = E_α(B*)·T with E ∈ (0, 3/2) — the log-elasticities
   ∂log T/∂log β_ij = [1 + (2E−3)(1−2x_k*)]/2 sum to E. Consequence (CONJECTURE-level wording): T_α is
   sub-homogeneous of degree < 3/2 in β; at α=1 (E≡1) this is Cain's degree-1 homogeneity.
7. **Figure layer complete** (F1–F9): 4,190 FLOAT rows per α-sweep family with 402 CERTIFIED anchors,
   129,600-row pair-loop sensitivity surface, HP asymptotics: (T−T₁)/(C(1−α)) → 1 as 1+O(1−α) (F8) and
   (TK³−27)/K → 9Σβ−27 to 6 digits at α = 2/3+1e−10 (F9).
8. **P6 (exploratory, n=4).** Two negative-feedback 3-cycles sharing an edge, invariants (s, t): the numerically
   resolved boundary is **s + t = R₃(α)³ at all 8 orders tested (deviation ≤ 3.6e−14 over 216 points)**, symmetric
   point s = t = R₃³/2 (= 4 at α = 1). Mechanism: for d₃ = d₄ the subspace span{e₁, e₂, e₃+e₄} is DA-invariant and
   DA restricted to it is the single 3-cycle with gain s+t (verified to 1e−48) ⇒ necessity is proved; sufficiency
   (non-merged diagonals never do worse; worst point has x₃* = x₄*) is numerical. Cactus (shared node) does not merge.

## P0 — baseline (`ENVIRONMENT.json`, `P0_TEST_RESULT.txt`)

Branch and baseline SHA verified; Wave-1 `COMPUTE_PASS`, `GENUINE_C10_COUNTEREXAMPLES = 0`, 2,060,000 cases
confirmed readable; full suite 121/121 before any edit. Python 3.12.3, numpy 2.5.3, scipy 1.18.1, mpmath 1.3.0,
sympy 1.14.0, OpenBLAS single-threaded per worker. Note: the Wave-1 file `computations/results/P0_TEST_RESULT.txt`
reads "100 passed" (a stale copy overwritten by an rsync during Wave 1); the Wave-1 final report and both Wave-2 runs
give 121 — recorded in `ENVIRONMENT.json`, not a reproducibility problem.

## P1 — certified atlas (`CERTIFIED_THRESHOLD_ATLAS.csv`, `..._SUMMARY.json`)

Families: A symmetric (13 b ∈ [1e−3, 1e3]) × 24 α = 312; B two-equal (37 ratios, 6/decade over 6 decades) 316;
C all-antagonistic 70; D all-below-one 60; E Wave-1 C-13 ecological triples 90; F anisotropic (1e−4..1e4) 90.
α grid: 2/3+10^−k (k=1..8), {0.7, 0.75, 0.8, 0.85, 0.9, 0.95}, 1−10^−k (k=1..10). Precision dps 40 (50 for
α−2/3 ≤ 1e−6). Per point the CSV records β, α (exact decimal strings), status, method, L, U, mid, relative width,
x̂ and the rigorous enclosure radius, core radius, T₁, the 50-digit HP value and its bracket membership, the closed
form for family A, dps, boxes, runtime. Wall time 818 s on 16 workers.

Certificate semantics. *Unconditional*: strip exclusion + interval-certified convex core + branch-and-bound with
target U (so F > U outside the core ⇒ x* in the core; strong convexity on the core gives |x*−x̂| ≤ 2‖∇G‖/λ).
*Conditional (logit)*: G convex on ℝ² (C-15 Thm 1, proof-audited) + interval Hessian ≥ λ on ŷ+[−R,R]² + ‖∇G(ŷ)‖ < λR
⇒ y* in the box, |y*−ŷ| ≤ ‖∇G(ŷ)‖/λ, G(y*) ≥ G(ŷ) − ‖∇G‖²/λ; |x*−x̂| ≤ |y*−ŷ|/2. Where both exist the
intersection is reported and the two always overlap (assertion in the script).

## P2 — canonical witnesses (`CANONICAL_WITNESSES.{csv,json}`, README)

Exhaustive search over diag ∈ {−1,−2}³, off-diagonals ∈ {−3,−2,−3/2,−1,−1/2,0,1/2,1,3/2,2,3}⁶ (11.6 M matrices) gave
53,172 band cases on the α grid; representatives chosen by fewest / smallest entries, plus hand-built Siami-slice and
decimal-tuned boundary witnesses (a 3-cycle entry whose reciprocal partner is 0 moves κ linearly at fixed β).
Coverage: 1 Siami ×9, 2 generic ×12, 3 strong antagonistic ×4, 4 mixed signs ×4, 5 near Cain ×5, 6 near fractional
×6, 7 near α=2/3 ×2 (γ=150 at α=0.67, γ=40 at α=0.68), 8 near α=1 ×4, 9 Hurwitz-at-I ×6, 10 non-Hurwitz ×19
(multi-tagged). All invariants exact rationals; T_α HP 40 digits; 10 witnesses CERTIFIED (widths ≤ 3.3e−38).

## P3 — robustness (`ROBUSTNESS_SUMMARY.csv`, `ROBUSTNESS_DETAILS.json`)

P3A (HP 40): m_frac, m_Cain, normalised versions, band position, ∂T/∂β_ij, ∂T/∂α, ∂T₁/∂β, E(B*), Euler check,
first-order α-distance to the fractional boundary. P3B (per witness × {fractional, Cain, strict-P} × {Frobenius,
max}): local first-order |g|/‖∇g‖; SLSQP (8 starts); differential evolution; 3,018 directional root-solves;
HP secant refinement along the best direction (residuals ≤ 1e−30 where reached). Strict-P: Frobenius distance is
EXACT (min over |a_ii|, σ_min of 2×2 blocks, σ_min(A)); max-norm has a rigorous lower bound (Frobenius/3) and the
single-entry upper bound; SLSQP reproduced the exact values to 1e−9. No rigorous lower bound is claimed for the
fractional/Cain boundaries (upper bounds only, labelled).

## P4 — C-15 differential structure (`C15_SENSITIVITY_VALIDATION.json`, `C15_SENSITIVITY_WORST.csv`)

8,000 points (symmetric / two-equal / generic / anisotropic 1e−4..1e4 / α = 2/3+10^−U[1,7] / α = 1−10^−U[1,8]) × 16
checks. Float failures: 532, all in the c1–c3 group and all in the near-2/3 regime (T ≈ 27/K³ up to 1e20 dominates the
β-dependence; the FD quotient loses ~7 digits) — every one of them is among the 500 HP-rechecked points (max HP
relative error 2.4e−33). No failure in c4–c16. The logit Hessian is PD at all points (min eig 4.6e−3; median
condition number 3.0, max 141 for strongly anisotropic β).

## P5 — figure-source datasets (`FIGURE_DATA/`)

F1 T_α/T₁ vs α (+402 CERTIFIED anchors with brackets and x-enclosures); F2 W_α; F3 W_α/T₁; F4 C-11 certified fraction
with the exact α→1 limit 2√(SG)/(S+G); F5 (L₃, α) boundaries with realizability column; F6 pair-loop sensitivity and
log-elasticity surfaces (α ∈ {0.75, 0.9, 0.99}, g₂₃ ∈ {0, −2, 0.5}, 120² grid); F7 x*(α, β) sweeps and a β-path with
the Cain minimiser; F8 classical asymptotic (HP 45, k=1..10, incl. D estimate); F9 low-order blow-up (HP 55).
Each family: CSV with `evidence` column, README (purpose, columns, script, SHA). Preview PNGs are QA only.

## P6 — see `N4_SHARED_EDGE_CONJECTURE.md` (future-paper material, not a manuscript claim)

## Precision pathologies and how they were handled

1. Float FD near α = 2/3 (P4): 532 checks fail float tolerance; HP recheck resolves all (≤ 2.4e−33).
2. x-space branch-and-bound budget (P1): 35 anisotropic points not finished in 240 s / 300k boxes; certified by the
   logit route (conditional on C-15), explicitly flagged; the 55 other family-F points carry both certificates.
3. ∂T/∂α HP error 1.75e−28 constant across points: verified to be Richardson truncation (scales as h⁴: 1e−21, 1e−29,
   1e−37 for h = 1e−6, 1e−8, 1e−10; dps-independent). Not a discrepancy.
4. Two witness-selection slips during development, both caught by the two-route consistency check and fixed before
   the committed library: γ = 2.8 at α = 0.9 lies *outside* the band (R₃(0.9) = 2.7563, not 2.80) — replaced by
   γ = 2.75; two integer matrices with κ = T₁ *exactly* (float filter accepted κ/T₁−1 ≈ 1e−16) — exact-arithmetic
   filter added. In both cases C-10 and the direct eigenvalue route agreed, i.e. these were errors in my choice of
   witnesses, not in the theorem.
5. Not a pathology but a limitation: for 4 witnesses at α = 0.7 the fractional boundary is not the nearest boundary
   of the class (strict-P is crossed first along every tried direction); recorded as NOT REACHED.

## Stop-line audit

No certified interval contradicts C-10 (938/938 brackets contain the independent HP value and, where available,
the closed form); no direct spectral computation disagrees with C-10 after HP confirmation (35 witnesses, 216 P6
boundary points × 2 routes); no C-15 identity fails after HP recheck; the test suite did not regress (121 → 135);
Wave-1 artifacts validated. **COMPUTE2_PASS.**

## Reproduction

```bash
python3 -m venv venv && venv/bin/pip install -e .[dev] sympy threadpoolctl
OMP_NUM_THREADS=1 venv/bin/python -m pytest -n 8                       # 135 passed
cd computations/scripts/wave2
OMP_NUM_THREADS=1 FDSN_WORKERS=16 python w2_p0_baseline.py
OMP_NUM_THREADS=1 FDSN_WORKERS=16 python w2_p1_atlas.py               # ~14 min
OMP_NUM_THREADS=1 FDSN_WORKERS=8  python w2_p2_witnesses.py           # ~1 min
OMP_NUM_THREADS=1 FDSN_WORKERS=14 python w2_p3_robustness.py          # ~4 min
OMP_NUM_THREADS=1 FDSN_WORKERS=12 python w2_p4_c15.py                 # ~6 min
OMP_NUM_THREADS=1 python w2_p5_figure_data.py                         # ~2 min
OMP_NUM_THREADS=1 python w2_p6_n4_shared_edge.py && python w2_p6_verify.py   # ~3 min
```
All randomised blocks use fixed seeds recorded in the outputs (2026, 415, 6, 9). Wave-1 raw arrays are not needed.
