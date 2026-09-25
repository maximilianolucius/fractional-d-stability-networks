# Independent proof audit task — C-07 / C-09 / C-11

**Priority:** P0
**Role:** adversarial mathematical verifier
**Rule:** do not improve the proofs until you have first tried to break them.

## Files to audit

1. `research/novelty/REOPENED_AUDIT_2026-09-24.md` — C-07.
2. `research/THEOREM_C09_DIMENSION_THRESHOLD.md` — C-09.
3. `research/THEOREM_C11_FRACTIONAL_CAIN_CERTIFICATE.md` — C-11.
4. `research/novelty/C09_TARGETED_AUDIT.md` — novelty boundaries only.

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

### C-11
- Re-derive the exact infimum of (a_D b_D)/c_D over D>0.
- Verify the optimizer.
- Reconcile notation/sign convention exactly with Cain 1976.
- Verify Phi(A)>1 reproduces Cain in the strict-P/type-2 case.
- Verify the fractional threshold rho_alpha and alpha->1 limit.
- Verify invariance of Phi under positive left-diagonal scaling and the GLV orbit equivalence.

## Computational corroboration

Run the full test suite. Add independent random/property tests if helpful, but label them corroboration only.

## Deliverable

Create `research/PROOF_AUDIT_C07_C09_C11.md`.

For every theorem return exactly one:
- PASS
- PASS WITH MINOR FIX
- FAIL

Any FAIL must contain a smallest counterexample or an exact broken implication.

Do not draft manuscript prose.
