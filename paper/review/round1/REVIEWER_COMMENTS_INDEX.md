# Reviewer comments — round 1, indexed for the response

Manuscript `mathematics-4633263` (26 pages as submitted). Recommendation of both reviewers: minor revision. Line/page numbers refer to the submitted PDF. "Where" names the section file in `paper/submission/round1-as-submitted/latex-source/sections/`.

## Reviewer 1 (mathematical clarifications; no new analysis or experiments requested)

| # | comment (summary) | where | required change |
|---|---|---|---|
| R1-1 | Lemma 1: display the boundary factorization p(λ) = (λ² − 2urλ + r²)(λ + a + 2ur), u = cos θ, with (1 − 4u²)r² − 2uar − b = 0 and c = r²(a + 2ur), so the boundary roots re^{±iθ} and the third root −a − 2ur < 0 are explicit | 04-exact-dimension-three (Lemma 1) | add the identity and one sentence |
| R1-2 | Interior attainment of the minimum defining T_α: for 2/3 < α < 1 note h_α(0) = (2u/(1−4u²))²(1 + 4u²/(1−4u²)) > 0, hence h_α(B_β(x))/(x₁x₂x₃) → +∞ at ∂Δ²; at α = 1 use B_β(x)/(x₁x₂x₃) = β₂₃/x₁ + β₁₃/x₂ + β₁₂/x₃ → +∞ since h₁(0) = 0; state that T₁ is the endpoint with h₁(b) = b | 04-exact-dimension-three (Eq. 20 area) | add the two limits and the T₁ sentence |
| R1-3 | Theorem 5: justify that minimization preserves strict monotonicity: with x* the minimizer for α₁, T_{α₁} = h_{α₁}(B(x*))/Πx* > h_{α₂}(B(x*))/Πx* ≥ T_{α₂}; same argument gives T_α > T₁ | 05-threshold-geometry (Thm 5) | add the three-term inequality |
| R1-4 | Corollary 1 (low order): show α = 2/3 is included by a strict inequality: μ ∈ spec(−DA), λ = −μ, Kellogg gives \|arg μ\| < 2π/3, so \|arg λ\| = π − \|arg μ\| > π/3 ≥ απ/2 for 0 < α ≤ 2/3 | 04-exact-dimension-three (Cor. 1) | add the two-line argument |
| R1-5 | Distinguish the fractional-only set from its interior: on strict-P(−A), 2/3 < α < 1, A ∈ F_α \ D_H ⇔ T₁(β) ≤ κ < T_α(β), whereas the full-dimensional interior is T₁ < κ < T_α; at κ = T₁ a diagonal scaling gives an imaginary pair (not Hurwitz, but Matignon-stable for α < 1) | 04-exact-dimension-three (band statement) and wherever "fractional-only band" is defined | add a remark |
| R1-6 | Near Eqs. (89)–(90): distinguish J = diag(u*)B from the Jacobian used in the time-domain comparison R*J = D*B, R* = D* diag(u*)⁻¹; failure of classical D-stability means ∃D ≻ 0 with spec(DB) ⊄ {Re z < 0}, not that the unscaled Jacobian is unstable; say the simulation uses a selected positive response-rate configuration | 07-certified-realization (Eqs. 89–90) | add one or two sentences |
| R1-7 | Precision/certification terminology: Table 1 is rounded while Eq. (88) gives many digits and a residual < 10⁻⁵⁹; write m₀ ≈ 0.374451281242515 in the text and state the precision of the high-precision computation; in §7.1 describe the interval software, working precision and the procedure enclosing the minimizer, in particular how a validated lower bound T̲_α with T̲_α − κ > 0 was obtained (uniqueness of the minimizer alone does not give it); define or remove the labels "C-07", "C-09", "C-10" in text and figures | 07-certified-realization (§7.1, Eq. 88, Table 1); figure captions | rewrite the certification paragraph; purge internal claim labels |

## Reviewer 2 (presentation, scope, references)

| # | comment (summary) | where | required change |
|---|---|---|---|
| R2-1 | p. 5 l. 177: "Therefore, the fractional-only" (comma) | 02/03 (line 177) | typo |
| R2-2 | p. 22 l. 683: "consistent with the positive real part" instead of "consistently with" | 07 (line 683) | typo |
| R2-3 | p. 8 l. 245: Theorem 2 assumes −A is a strict P-matrix; explain the implications of this restriction and whether the characterization extends to matrices with zero principal minors | 04-exact-dimension-three (Thm 2) | add a remark (the repository's SCOPE_MATRIX already states that zero-minor strata are not classified; C-07/C-10 boundary cases) |
| R2-4 | The paper proves local spectral stability; discuss whether the positive equilibrium stays biologically feasible under perturbations of parameters and initial conditions | 06-ecological-realization / 07 | add a paragraph: openness of the feasible fractional-only set (C-20), certified m-range [0.394, 0.578], local nature of the statement |
| R2-5 | Figure captions must be self-contained | all figure captions | expand captions (the Wave-2 captions file `research/FIGURE_CAPTIONS_WAVE2.md` is the source) |
| R2-6 | §7: simulations at additional fractional orders, especially near the predicted stability boundary, would strengthen the numerical support (time-step refinement already reported) | 07-certified-realization (Fig. 9) | new computation: runs at several α (e.g. α just above/below the exact boundary order for the chosen diagonal) |
| R2-7 | Many references are old; add a few recent relevant studies on stability of nonlinear fractional-order systems and highlight the novelty of the approach | 01-introduction, references.bib | add recent published references (published-only rule applies; run `computations/reference_audit/reference_audit.py` after) and a sharper novelty paragraph |

## Change classes

- Text-only (no new mathematics): R1-1, R1-2, R1-3, R1-4, R1-5, R1-6, R2-1, R2-2, R2-3, R2-5.
- Text + explicit statement of existing repository results: R1-7 (interval procedure: `computations/scripts/double_allee_interval_box.py`, 50-digit interval Newton with outward rounding, certified lower bound of T_α via the C-15 bracket), R2-4.
- New computation: R2-6 (additional α runs near the boundary).
- Bibliography: R2-7 (must pass the published-only audit).
