# Second independent proof audit — Double-Allee IGP theorem package — FINAL

**Overall status: `PROOF_AUDIT2_PASS_WITH_FIXES`**

**Branch:** `agent/independent-proof-double-allee-20260926` · **Base:** `d2bb43e` (integration SHA `36bf80f`) · **Date:** 2026-09-26  
**Blind verdicts (frozen, commit `01b1c62`):** `research/DOUBLE_ALLEE_PROOF_AUDIT2_BLIND_VERDICTS.md`  
**Checks:** `computations/audit2/double_allee_proof_checks.py` → `computations/audit2/DOUBLE_ALLEE_AUDIT2_RESULTS.json`

## 0. Independence disclosure

The auditor is the same agent/session that produced Audit 1. Phase A was run without opening, importing or copying any Audit-1 file (protocol respected: new code in `computations/audit2/`, exact-rational instead of CAS route, own threshold minimiser, a different witness, time-domain checks), but memory of Audit 1 could not be removed. Verdicts below are therefore **procedurally blind, not epistemically independent**; the sections marked *new in Audit 2* are the parts with genuine additional information.

## 1. Verdict table (final = blind, unchanged after unblinding)

| item | verdict | load-bearing? | one-line reason |
|---|---|---|---|
| DA-01 | PASS | no | J = diag(x*)B at F=0; D ↦ D diag(x*) bijection; invariants left-scaling invariant (exact) |
| DA-02 | PASS | yes (kill of the naive model) | T1 − κ = 2 + L3 + 2Σ√(β_iβ_j) > 0 with L3 ≥ 0, on all of {β>0}; Cain only for the D-stability conclusion |
| DA-03 | PASS | yes | all formulas exact at 400 rational points; C-13 convention |
| DA-04 | PASS (sharpened) | no | exact strict-P ⇔ s>0 ∧ q>0 ⇔ s>0 ∧ s+χ>0 (new identity q = Δ(s+χ)); e1e3>e2 sufficient, not necessary |
| DA-05 | PASS | yes | Cramer, affine identity, quadratic exact; no spurious root; fold ⇔ s+χ=0 ⇔ q=0 (excluded by strict-P) |
| DA-06 | PASS | yes | residual ≡ R exact; e∈(0,1), e1e3/e2=τ²>1; q=κsc1c2>0; regular as R→0⁺; rank 4 |
| DA-07 | PASS (quantified) | yes | K<K_max ⇔ H_A>0; explicit Q₁,Q₂ bounds for μ>0; r finite; "sufficiently close" is parameter-dependent |
| DA-08 | PASS WITH MINOR FIX | yes | IFT in all 14 parameters with state Jacobian B, det B = −κsc1c2 ≠ 0; open, full-dimensional; fix = wording (already applied by the Chief) |
| DA-09 | PASS (sharpened) | yes | dX/dm formula exact; dX/dm<0 needs only strict-P (new); ds/dm<0 needs χ>0 in addition |
| DA-10 | PASS | yes | G1(0)<0 always; G1''>0; crossing ⇔ E0>2√(A0B0); G1'(t_H) ≥ (4+4√C0)/t_H |
| DA-11 | PASS | yes | E0(t0) exact; joint (e2,q2) choice; one-sided fractional-only interval via C-10 §7 (α>2/3) / Kellogg (α≤2/3); C-11 not used |
| DA-12 | PASS | no | C-07 on B2; m_c exact; admissible iff X²+2aX>Ka |

No counterexample; no stop-line event. The load-bearing items DA-06…DA-11 are proved (my own derivations in the blind file, §"Proof audit, item by item").

## 2. Blind findings (summary; full text in the blind file)

Proof-level: all twelve items re-derived from the model equations; dependency graph established (C-07 only in DA-12; C-10/C-15/Cain/Kellogg/IFT only in DA-08, DA-10, DA-11; everything else elementary); no circularity; low-order and high-order cases separated in DA-08 and DA-11; no claim relies on numerics.

Computational corroboration (all new code): 8,000 exact rational identity evaluations (0 failures); own T_α minimiser agreeing with the closed forms to 6e−15; a **new witness at α=0.8** (β=(1.5,2.5,2), κ=70.04 ∈ (17.81, 148.39)) confirmed by a scale-invariant direct spectral search; the Chief design rebuilt from its declared targets (m0=0.2 on the Cain boundary to 5e−60; 0.19 classical; 0.21/0.30/0.45 fractional-only, both routes); 25,000 joint perturbations (16,389 feasible, 0 double roots, 600-case direct-vs-theorem subset with 0 mismatches); 20,000 wide draws (0 double coexistence equilibria); DA-07 bound K_max (0 violations / 6,000); DA-10 root counts (0 violations / 3,000 incl. the no-crossing regime); rank 4 at 200 points.

## 3. New in Audit 2 (not in Audit 1)

1. **Exact Schur identity q = −det B = Δ·(s + χ)**, Δ = c1c2 + e3h² (500 exact rational points, 0 failures; it is also immediate from the definitions of χ and q). Consequences: (a) the strict-P determinant condition is exactly **s + χ > 0**, a transparent one-line criterion; (b) the scalar prey-equation derivative is Φ_X = −(s+χ) = −q/Δ, so the reduced IFT of DA-09 and the full-system IFT of DA-08 are the *same* nondegeneracy condition (a fold of the coexistence branch is exactly q = 0); (c) **dX/dm < 0 holds on the entire strict-P stratum** (only Q>0 and q>0 are needed), whereas ds/dm < 0 still needs χ > 0 (the term χX'H_A). Audit 1 and the Chief text list χ>0 among the assumptions for both signs; for dX/dm it can be dropped. This is a sharpening, not a correction.
2. **Order-independence of the worst orbit point.** min_D min_i |arg λ_i(DB)| does not depend on α; the same d* is the classical-instability witness (Re>0) and the fractional worst case. Time-domain corroboration at d* with the correct state scaling D_sim = d*/x*: α=1 (nonlinear RK45) exponential growth of a 10⁻³ perturbation to 30×; linearised Caputo (own PECE) α=0.8 decays 10⁻³ → 1.7·10⁻⁴, α=0.9 grows → 1.9·10⁻², matching |arg| = 1.333 ∈ (0.8π/2, 0.9π/2). This is a physically independent confirmation route (no invariants, no thresholds).
3. **DA-07 quantifier caveat.** A fixed relative closeness K = X + 10⁻³(K_max − X) left μ1 or μ2 ≤ 0 in 33/4000 random embeddings: "K sufficiently close to X" is genuinely parameter-dependent; the explicit bounds Q < Q₁ = e1q1X/[ξc1/q1+(1−ξ)h/q2] and Q < Q₂ (μ2) should accompany the theorem or its proof.
4. **DA-05 regime remark.** When χ<0 (only possible with e2 ≫ e1e3, outside the theorem's regime) the leading coefficient r+Kχ can vanish or turn negative (40/20,000 wide draws): the "explicit quadratic" statement implicitly assumes r + Kχ ≠ 0 (automatic under e1e3 ≥ e2).

## 4. Post-unblinding reconciliation with Audit 1 and Chief Review 1

| item | verdict A1 / A2 | proof route | assumptions A1 found that A2 missed | assumptions A2 found that A1 missed |
|---|---|---|---|---|
| DA-01 | PASS / PASS | same idea (elementary) | — | — |
| DA-02 | PASS / PASS | same identity T1−κ = 2+L3+2Σ√(β_iβ_j); A2 exact-rational instead of SymPy | — | — |
| DA-03 | PASS / PASS | A1 SymPy, A2 exact rational | — | — |
| DA-04 | PASS / PASS | same sharp condition; A2 adds q = Δ(s+χ) ⇒ "s+χ>0" | A1's AM-GM weaker sufficient condition (A2 did not restate it) | Schur form of the condition |
| DA-05 | PASS / PASS | same; A2 adds fold ⇔ q=0 and the r+Kχ ≠ 0 remark | — | r+Kχ ≠ 0 implicit; fold identification |
| DA-06 | PASS / PASS | A1 symbolic det of the Jacobian (rank 4 everywhere); A2 FD rank at 200 points (weaker) | A1's closed-form determinant is stronger | — |
| DA-07 | PASS / PASS | same quantified bounds | — | empirical evidence that a fixed closeness fraction is insufficient |
| DA-08 | PASS WITH MINOR FIX / PASS WITH MINOR FIX | same (IFT); A1 added a certified 14-D box (not replicated in A2, not needed for the proof) | — | — (A2 stresses the fix is already applied in the current file) |
| DA-09 | PASS / PASS | same signs | — | χ>0 not needed for dX/dm<0 (strict-P suffices) |
| DA-10 | PASS / PASS | same, incl. transversality bound | — | explicit no-crossing argument when E0 ≤ 2√(A0B0) and numeric root counts in both regimes |
| DA-11 | PASS / PASS | same; A2 notes the joint (e2,q2) choice explicitly | A1's certified one-sided intervals (A2 used direct spectral checks instead) | wording: "choose the efficiency ratio" must be read as the joint DA-06 choice |
| DA-12 | PASS / PASS | same | — | — |

**Disagreements: none.** Every verdict coincides; all fixes requested by Audit 1 and integrated by the Chief (`1560210`) are consistent with my blind reading of the current theorem file (they were already present in the version I audited). Chief Review 1's dispositions (ACCEPT / ACCEPT WITH SHARPENING / ACCEPT FIX) are compatible with these verdicts.

Unexplained discrepancies: none. Numerical values agree where they overlap (m=0.21: κ=18.2331, T1=18.0873, T_0.9=39.7517, direct margins 0.15512 / −0.00196; crossing m_H = 0.2000; feasibility loss at m≈0.643 by Z→0).

## 5. Recommended (non-blocking) edits for the Chief

1. §5/§7 (strict-P): add the identity q = (c1c2 + e3h²)(s + χ) and state strict-P as s>0, s+χ>0.
2. §9: state that dX/dm<0 needs only Q>0 and q>0 (strict-P); keep χ>0 for ds/dm<0.
3. §7 (embedding): display the explicit bounds Q < Q₁, Q < Q₂ (and K_max) so that "K sufficiently close to X" is quantified in the theorem, not only in the proof.
4. §4: note that the quadratic form presumes r + Kχ ≠ 0 (automatic when e1e3 ≥ e2).
5. §11: phrase the E0 realization as the joint choice of (e2, q2) in the DA-06 construction.
6. Validation section (future): the worst orbit diagonal is order-independent; a single d* serves for all α, and time-domain simulations must scale the state by d*/x*.

## 6. Checks run

- `python computations/audit2/double_allee_proof_checks.py` (819 s, aureus): exact identity tests, T_α self-check, witnesses, time-domain simulations, 25k perturbations, degeneracy hunt, m-branch, path/rank checks, DA-07 bounds; `... sim path` reruns; `addendum` for the Schur identity.
- Pre-existing test suite untouched (no test files modified on this branch; Audit-1 tests not run or relied upon in Phase A).
- No Audit-1 artifact modified; no Chief file modified; `paper/` untouched.
