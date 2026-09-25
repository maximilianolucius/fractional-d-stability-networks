# Independent proof audit task — C-07 / C-09 / C-10 / C-11 / C-14 / C-15

**Priority:** P0
**Role:** adversarial mathematical verifier
**Rule:** do not improve the proofs until you have first tried to break them.

## Files to audit

1. `research/novelty/REOPENED_AUDIT_2026-09-24.md` — C-07.
2. `research/THEOREM_C09_DIMENSION_THRESHOLD.md` — C-09.
3. `research/THEOREM_C10_EXACT_3X3.md` — C-10.
4. `research/THEOREM_C11_FRACTIONAL_CAIN_CERTIFICATE.md` — C-11.
5. `research/THEOREM_C14_CLASSICAL_LIMIT_RATE.md` — C-14.
6. `research/THEOREM_C15_THRESHOLD_GEOMETRY.md` — C-15.
7. `research/novelty/C09_TARGETED_AUDIT.md` and `research/novelty/C10_TARGETED_AUDIT.md` — novelty boundaries only.

## Mandatory checks

### C-07
- Verify necessity/sufficiency of the real 2x2 classification for every 0<alpha<1.
- Check all boundary cases: zero diagonal entries, repeated roots, zero determinant, alpha approaching 1.
- Verify the exact description of P_alpha^(2) and empty full-dimensional interior.

### C-09
- Verify the Kellogg rotation argument for alpha<=2/3.
- Verify the cubic angular lemma for 2/3<alpha<1, including coefficient matching and all inequality directions.
- Verify the A_gamma spectrum and strict-P property.
- Verify the gamma interval is nonempty for every alpha<1.
- Verify the open-ball argument is genuinely full-dimensional and uniform over every D>0.
- Check that no step silently assumes compactness of the positive diagonal orbit.

### C-10
- Re-derive the fixed-cubic boundary function H_theta(a,b) from p(r exp(i theta))=0.
- Verify the unique-boundary and stability-side argument for positive cubic coefficients.
- Verify the homogeneity of H_theta.
- Verify the bijection between the positive diagonal orbit modulo common scaling and the open simplex x_i=p_i d_i/a_D.
- Verify the four orbit invariants beta_ij and kappa.
- Verify the exact equivalence A in F_alpha iff kappa<T_alpha(beta) on the strict-P stratum.
- Verify the P0 necessity lemma and the claim that every interior point must be strict P.
- Verify the complete interior formulas for alpha<=2/3 and alpha>2/3.
- Verify T_alpha(beta)>T_1(beta) and the exact fractional-only band.
- Verify the alpha->1 limit reproduces Cain with the correct strict/equality cases.
- Verify the analytic Siami counterfamily proving that C-11's Phi threshold is not necessary.

### C-11
- Re-derive the exact infimum of (a_D b_D)/c_D over D>0.
- Verify the optimizer.
- Reconcile notation/sign convention exactly with Cain 1976.
- Verify Phi(A)>1 reproduces Cain in the strict-P/type-2 case.
- Verify the fractional threshold rho_alpha and alpha->1 limit.
- Verify invariance of Phi under positive left-diagonal scaling and the GLV orbit equivalence.

### C-14
- Verify strict monotonicity of T_alpha(beta) in alpha.
- Re-derive the expansion of h_alpha(b) at alpha=1.
- Verify uniqueness/nondegeneracy of the classical simplex minimizer.
- Verify the envelope-theorem step and the coefficient C(beta).
- Check the symmetric beta=(1,1,1) coefficient 12*pi*sqrt(3) against the Siami slice.

### C-15
- Verify the elasticity formula E=b h'/h and the bounds 0<E<3/2.
- Verify phi''>0 and the positive-definite Hessian decomposition in logit coordinates.
- Verify coercivity and uniqueness/nondegeneracy of the threshold optimizer.
- Verify the symmetric and two-equal slice reductions.
- Re-derive the explicit beta_ij(x,r) parametrization and prove its bijectivity.
- Verify the alpha->2/3+ expansion through the K^-2 coefficient.
- Verify the realizability theorem for every beta>0 and kappa>=T1(beta), including G<=0, G>0 and G=0 cases.

## Computational corroboration

Run the full test suite. Add independent random/property tests if helpful, but label them corroboration only.

## Deliverable

Create `research/PROOF_AUDIT_C07_C09_C10_C11.md`.

For every theorem C-07, C-09, C-10, C-11, C-14 and C-15 return exactly one:
- PASS
- PASS WITH MINOR FIX
- FAIL

Any FAIL must contain a smallest counterexample or an exact broken implication.

Do not draft manuscript prose.
