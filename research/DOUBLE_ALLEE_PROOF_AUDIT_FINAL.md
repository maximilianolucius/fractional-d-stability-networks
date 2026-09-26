# Independent adversarial proof audit — Double-Allee IGP Kolmogorov extension

**Overall compute status: `COMPUTE_AUDIT_PASS_WITH_FIXES`** (every theorem-level item PASSes; two wording-level fixes, no mathematical failure, no counterexample).

**Branch:** `agent/compute-double-allee-proof-audit-20260926` · **Base Chief SHA:** `ba67d678` · **Date:** 2026-09-26  
**Auditor:** compute agent (symbolic + high-precision + adversarial numerics on aureus)  
**Tests:** 39 passed, 0 failed (13 pre-existing + 26 new in `tests/test_double_allee.py`); baseline 13/13 before any edit.

Evidence labels: SYMBOLIC (SymPy re-derivation from the model equations, exact residuals saved), EXACT (rational arithmetic), HP (mpmath, digits stated), CERTIFIED (outward-rounded interval arithmetic), FLOAT, LOGIC (argument written here for Chief review).

## Verdict table

| item | verdict | decisive evidence |
|---|---|---|
| DA-01 Kolmogorov orbit equivalence | **PASS** | SYMBOLIC: J − diag(x)DF = diag(F) (vanishes at F=0); β, κ, L3 invariant under left diagonal scaling (generic 3×3); bijection D ↦ D diag(x*) (LOGIC) |
| DA-02 two-consumer no-go | **PASS** | SYMBOLIC: B, p, m_ij, β, L3 = q1q2(c12e2+c21e1)/(s c11 c22) ≥ 0, κ = Σβ−2−L3, and T1 − κ = 2 + L3 + 2Σ√(β_iβ_j) > 0 on the *whole* positive-β set (strict-P only needed to invoke Cain); EXACT random tests |
| DA-03 IGP reduced matrix & invariants | **PASS** | SYMBOLIC: B, minors, q = −det B, β_ij, κ, L3 = hq1q2(e2−e1e3)/(s c1c2), κ = Σβ−2−L3, oriented cycles ±; sign convention identical to C-13 |
| DA-04 strict-P conditions | **PASS** | SYMBOLIC/LOGIC: s>0 ⇒ all p_i, m_ij > 0; e1e3>e2 ⇒ q>0 — **sufficient, not necessary** (e1=e3=e2=1/2, all other =1: q = 9/4 > 0, EXACT test); sharp condition q>0 ⇔ hq1q2(e2−e1e3) < s(c1c2+e3h²)+c1e2q2²+c2e1q1²; transparent weaker sufficient condition h(e2−e1e3) ≤ 2√(c1c2e1e2) (AM-GM, residual (√(c1e2)q2−√(c2e1)q1)²) |
| DA-05 coexistence geometry | **PASS** | SYMBOLIC: Y(X), Z(X), χ, ν, affine identity, every quadratic coefficient; multiplication by K(X+a) adds no root (polynomial at X=−a is −r(K+a)(a+m) ≠ 0); degeneracies analysed (§DA-05) |
| DA-06 invariant realization | **PASS** | SYMBOLIC: τ−1/τ=ρ, β−1 = (A,B0,C), residual = R exactly, e1e3/e2 = τ² > 1; det of the (q1,q2,h,e2)-Jacobian = −4e1e3h²q1²q2²(e1e3+e2)/(c1c2s)³ ≠ 0 everywhere ⇒ rank 4; image = {β_ij>1, κ>Σβ−2} (open, 4-D) |
| DA-07 double-Allee embedding | **PASS** | SYMBOLIC: g(X)=Q, g'(X)=−QH_A, all three equilibrium equations vanish, H_A(K−X) → 1, r → sX(X+a)/(X−m) (finite); fully quantified feasibility (§DA-07) |
| DA-08 nonempty open biological region | **PASS WITH MINOR FIX** | LOGIC (IFT with det B = −κ s c1c2 ≠ 0 in the full 14-parameter space, all inequalities strict, T_α continuous by C-15) + CERTIFIED full-dimensional box (all 14 parameters, relative half-width 5e−4) + 160k perturbations. Fix: wording "*the* positive coexistence equilibrium" → "*a* / the constructed coexistence branch" (uniqueness is not proved; see §DA-05) |
| DA-09 Allee-threshold sensitivity | **PASS** | SYMBOLIC: ∂_m g = −g/(X−m), dX/dm = −Q/[(X−m)(s+χ)], ∂_X H_A, ∂_m H_A, 1/(X−m)² − 1/(X+a)² = (m+a)(2X+a−m)/(...) > 0; minimal assumptions Q>0, s>0, χ>0, m>−a (§DA-09); FLOAT: ds/dm<0 on the whole feasible branch |
| DA-10 invariant path / unique crossing | **PASS** | SYMBOLIC: path formulas, G1 closed form, G1(0) = −4−4√C0 < 0 for every E0, 2pp''−p'² = −(A0−B0)², G1'' = (A0−B0)²/(2p^{3/2}) + √C0[A0²/(2(1+A0t)^{3/2}) + B0²/(2(1+B0t)^{3/2})] > 0, lim G1/t = E0 − 2√(A0B0); transversality automatic: G1'(t_H) ≥ (4+4√C0)/t_H > 0 |
| DA-11 prescribed-m0 crossing | **PASS** | SYMBOLIC: G1(t0)=0 with the prescribed E0 and E0 − 2√(A0B0) = [2 + 2(√p(t0) − √(A0B0) t0) + 2√C0(…)]/t0 > 0; HP: m0=0.2 on the Cain boundary to 5e−110; CERTIFIED one-sided intervals [0.2+10^−k, 0.2+10^−(k−1)], k=2..7, and [0.2005, 0.45] all fractional-only; m=0.19 classical |
| DA-12 2-D consistency | **PASS** | SYMBOLIC: B2, det = pq, X = d/p, m_c both forms; C-07 classification (LOGIC); admissibility m_c > 0 ⇔ X² + 2aX > Ka |

No stop-line event occurred: no certified interval contradicts C-10, no direct spectral computation disagrees with C-10 after HP confirmation, no identity failed.

## Artifacts

- `computations/results/DOUBLE_ALLEE_SYMBOLIC_AUDIT.json` — 71 identities, 0 mismatches (`computations/scripts/double_allee_symbolic_audit.py`)
- `computations/results/DOUBLE_ALLEE_ADVERSARIAL_SUMMARY.json`, `DOUBLE_ALLEE_WORST_CASES.csv` (`computations/scripts/double_allee_adversarial_validation.py`)
- `computations/results/DOUBLE_ALLEE_INTERVAL_BOX.json` (`computations/scripts/double_allee_interval_box.py`, `double_allee_box_meanvalue.py`)
- `src/fdsn/double_allee.py` (model, equilibria, constructions), `src/fdsn/{c10_threshold,direct_margin,interval_cert}.py` (audit infrastructure from the compute waves)
- `tests/test_double_allee.py`; `computations/results/DOUBLE_ALLEE_TEST_RESULT.txt`

## Symbolic verification (task §2)

`double_allee_symbolic_audit.py` derives both reduced matrices as Jacobians of the model per-capita fields, all principal minors and determinants, the β/κ/L3 identities (with the C-13 convention L3 = (a12a23a31 + a13a32a21)/(p1p2p3) applied to the generic matrix), Y(X), Z(X), χ, ν, the quadratic, the realization residual, the embedding identities and limits, dX/dm and the H_A partials, G1, G1', G1'' and the asymptotic slope, the DA-11 identities and the 2-D m_c. 71 entries; every algebraic identity simplifies to residual 0; sign/logic entries are recorded with the argument used. One entry needed exact cancellation of the rational function before substitution (harness detail, not a theorem issue).

## Adversarial numerics (task §3)

**3.1 Witness from scratch.** Only the declared design was used (α=0.9, m0=0.2, β=(2,2,2), κ=18=T1) plus the free scale choices s0=c1=c2=1/20, η=1/2, X0=1, a=1/2, K=11/10, ξ=1/2. The DA-06/DA-07 constructions reproduce the Chief's parameters (q1=h=√2/20, q2=1/(20√e2), e2=1/(4τ²), τ=(14+√200)/2, μ1≈0.033345, μ2≈0.0030098, r≈0.109513). At 100 digits: X(0.2)=1, β=(2,2,2), κ−T1 = −5.3e−110; X(0.21)=0.99985227333769554…, s=0.049282133198657753…, κ−T1 = 0.14571757079398…, T_0.9−κ = 21.5186815310…; T_0.9(β) certified brackets of width 1e−49 at all three m. Classification: m=0.19 classical (κ−T1 = −0.1414), m=0.20 boundary, m=0.21 genuinely fractional; the second quadratic root is negative (≈ −0.35) — one coexistence equilibrium.

**3.2 Direct all-D attack (m=0.21, log d_i ∈ [−20,20]).** Pattern search (4 starts), 12 Nelder–Mead seeds and 3 differential-evolution seeds all return min|arg λ(DB)| − 0.9π/2 = 0.15511761312653 rad at w ≈ (−0.00362, 0); 50-digit recheck 0.1551176131265285…; eigenvalues at the worst diagonal 0.004823356 ± 2.4583597i, −3.0060292: the same diagonal is the classical-instability witness (Re λ > 0), with max cos(min|arg|) = 0.0019620 and α=1 margin −0.0019620. All agree with C-10 (T1 = 18.087 < κ = 18.233 < T_0.9 = 39.752) and C-11 (Φ = 0.99201 > ρ = 0.47215). At the boundary point m=0.20 the α=1 margin is 4e−16 and the normalized abscissa 9e−16 (exactly on the boundary), the 0.9-margin 0.15707963 = π/20. A methodological note: the *raw* spectral abscissa is not scale-invariant (outside the unstable sliver it tends to 0⁻ as d → 0) and a global optimizer drifts to the box corner; the scale-invariant objective Re λ/|λ| must be used — recorded so that future scripts do not report a false negative.

**3.3 Random falsification (160,000 joint perturbations of all 14 parameters; seeds in the JSON).** Log-normal noise σ ∈ {0.02, 0.1, 0.3} (40k each), an m-sweep on [0.15, 0.25] (20k) and boundary-pushed samples (K→X, e2 ↔ e1e3, mortalities up, m→X, a extreme; 20k). Feasible 108,449 (infeasible rejected explicitly, 51,551); **0 cases with two coexistence equilibria**; strict-P 104,454; classes: classical 41,038, genuinely fractional 59,626, unstable 3,790 (unstable only at σ ≥ 0.1 and in the boundary mode). Of the 3,995 feasible non-strict-P points, the 3,984 produced by the σ=0.3 and boundary modes were re-examined: every one violates s > 0 and none has q ≤ 0 (no feasible point with e2 ≥ e1e3 was found either — the e2 ↔ e1e3 pushes destroy feasibility of the witness branch before they reach the strict-P question; the DA-04 non-necessity is therefore established at the matrix level). Direct spectral optimisation on 4,500 adversarial cases (2,500 nearest to a boundary with |κ/T−1| down to 6e−7, 1,500 random, 500 non-strict-P): **0 mismatches**, 0 undecided. 59,584 of the 59,626 fractional-only points also pass C-11; 42 are fractional-only but C-11-uncertified (C-11 sufficient, not necessary, as expected).

**m-branch.** With the 13 other parameters fixed at the witness values, the coexistence branch exists for m ∈ [0.005, 0.6438] (feasibility lost at 0.6438), ds/dm < 0 everywhere (s from 0.0639 to 0.0178), exactly one classical crossing at m_H = 0.2000000 (bisection), and no fractional crossing before feasibility loss (min T_0.9 − κ = 13.4): consistent with the Chief's explicit non-claim of a second threshold m2.

**3.4 Certification.** (A) With all other parameters fixed, **m ∈ [0.2005, 0.45] is CERTIFIED genuinely fractional** (41 adaptive sub-intervals, X by interval Newton, κ−T1 ≥ 8.98e−4 on the left end, T_0.9 − κ ≥ 16.9 via the certified bracket at the lower β corner with C-13 §7 monotonicity, Φ−ρ > 0 unconditional); one-sided intervals [0.2+10^−k, 0.2+10^−(k−1)] for k=2..7 certified with κ−T1 lower bounds 1.2e−2 … 1.5e−7 (scaling linearly in m−m0, i.e. transversality seen in certified data). (B) A **full 14-parameter box** p_i ∈ [p_i(1−5e−4), p_i(1+5e−4)] around m=0.21 is CERTIFIED (mean-value interval form with implicit-function derivatives generated by SymPy: κ−T1 ∈ [0.0574, 0.2340], Y ∈ [0.03746, 0.03753], Z ∈ [0.001756, 0.001939], both C-11 and C-10-bracket certificates), plus an anisotropic box with half-widths up to 5e−3 in the insensitive directions (e2, μ2, m). δ = 1e−3 is *not* certifiable for a genuine reason: Σ_i |∂(κ−T1)/∂log p_i| ≈ 147 so a 1e−3 relative move can consume the 0.146 margin. Naive interval evaluation through the aggregated quadratic coefficients overestimates by ~26× and fails even at 5e−5; this is documented as a numerical pathology, not a mathematical one.

## Independent logic checks (task §4)

1. *No-go structural or sign artefact?* Structural. The identity T1 − κ = 2 + L3 + 2Σ√(β_iβ_j) uses the C-13 convention verified symbolically on the generic matrix; L3 ≥ 0 for the two-consumer architecture holds for all positive parameters (both oriented 3-cycles have the same sign). Under the opposite convention the same inequality appears with the sign of L3 flipped and L3 ≤ 0 — the conclusion κ < T1 is convention-independent.
2. *Four-dimensional?* Yes: the Jacobian determinant of (β12, β13, β23, κ) w.r.t. (q1, q2, h, e2) is −4e1e3h²q1²q2²(e1e3+e2)/(c1c2s)³, nonzero on the whole positive domain; the image is exactly {β_ij > 1, κ > Σβ − 2}.
3. *Genuinely open full-dimensional set?* Yes. The equilibrium equations are three equations in (X,Y,Z) with Jacobian B (det B = −κ s c1c2 ≠ 0) depending smoothly on all 14 parameters; the equilibrium continues as a smooth function of all of them, and every defining inequality is strict. The certified 5e−4 box is an explicit full-dimensional instance.
4. *K → X⁺ pathology?* None mathematically: H_A(K−X) → 1, Q → 0, r → sX(X+a)/(X−m) (finite), μ1 → e1q1X, μ2 → e2q2X. Practically, Y, Z = O(Q) → 0: the consumers become rare (witness: Z = 0.18% of X), and the equilibrium is a near-cancellation (χX ≈ ν), which is why the witness is sensitive (condition ~10³ in log-parameters). Recommendation: for the paper choose K farther from X or m deeper in the band (m ≈ 0.3–0.45, all certified) to obtain a less fragile example.
5. *e1e3 > e2 plausible with efficiencies in (0,1)?* Yes (any e1=e3=η, e2 < η²); the witness uses e2 = 0.00126 (τ = 14 needed for κ = 18 = T1 at β=(2,2,2)); milder ratios realize smaller R.
6. *Same model with m only?* Yes: the m-branch is computed with the exact fixed 13-parameter vector; no hidden retuning (the construction tunes parameters once, at m0).
7. *Feasibility loss before the crossing?* No: feasible on [0.005, 0.644] ⊃ m0 = 0.2; the classical crossing is at 0.2000000 and the branch stays feasible for another 0.44 of m.
8. *Transverse?* Yes, with the explicit bound G1'(t_H) ≥ (4 + 4√C0)/t_H; the certified one-sided data show κ − T1 ∝ (m − m0) down to 10⁻⁷.
9. *2-D/3-D contrast exact?* Yes: both use F_α (all D) and Hurwitz D-stability; C-07 gives the codimension-one set g'(X)=0 in 2-D, C-10 the open band in 3-D.
10. *C-11 used where C-10 is required?* No. The theorems use C-10; C-11 appears only in the Chief's interval certificate (a sufficient certificate, legitimately used). This audit adds the exact-threshold certificate κ_hi < L(β_lo) in every certified box.

## Minor fixes / remarks for the Chief (no theorem is false)

1. DA-08 / §8 wording: "its positive coexistence equilibrium" → "a positive coexistence equilibrium (the constructed branch)"; uniqueness of the coexistence equilibrium is not proved (the quadratic can in principle have two admissible roots; none seen in 108k feasible samples, and the witness has one).
2. DA-06 / §6: the clause "if in addition κ > T1 the construction can be chosen with e_i ∈ (0,1) and e1e3 > e2" is redundant — every target with R > 0 already admits it (the construction always has e1e3/e2 = τ² > 1 and e_i < 1).
3. DA-04: state explicitly that e1e3 > e2 is sufficient and not necessary; the sharp strict-P condition is q > 0 (§DA-04 above), and the weaker transparent sufficient condition h(e2 − e1e3) ≤ 2√(c1c2e1e2) may be worth recording.
4. DA-09: list the minimal assumptions (Q > 0, s > 0, χ > 0, m > −a) — χ > 0 is genuinely used for the sign of dX/dm and of the first term of ds/dm.
5. Numerical-methods note for the manuscript's validation section: maximise Re λ/|λ| (or minimise the angle), never the raw spectral abscissa, over positive diagonals; and use interval Newton / mean-value forms for any interval certificate in parameter space.

## Reproduction

```bash
pip install -e .[dev]          # numpy, scipy, mpmath, sympy, pytest-xdist
pytest -n 6                     # 39 passed
python computations/scripts/double_allee_symbolic_audit.py            # ~2 min
FDSN_WORKERS=16 OMP_NUM_THREADS=1 python computations/scripts/double_allee_adversarial_validation.py   # ~30 s wall on 16 workers
python computations/scripts/double_allee_interval_box.py              # ~1 min
python computations/scripts/double_allee_box_meanvalue.py             # ~1 min
```
