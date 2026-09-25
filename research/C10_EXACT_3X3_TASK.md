# C-10 research task — exact 3x3 fractional D-stability characterization

**Priority:** P1 after independent proof audit
**Objective:** determine whether the sufficient C-11 certificate can be upgraded to a necessary-and-sufficient criterion for 3x3 matrices, at least on the strict-P(-A) stratum.

## Known structure

For -A a strict P-matrix and D=diag(d1,d2,d3)>0,

[
det(lambda I-DA)=lambda^3+a_D lambda^2+b_D lambda+c_D
]

with positive coefficients.

C-11 gives the exact classical orbit functional

[
Phi(A)=
\frac{
(\sqrt{p_1m_{23}}+\sqrt{p_2m_{13}}+\sqrt{p_3m_{12}})^2
}{q}
=
\inf_{D>0}\frac{a_Db_D}{c_D}.
]

Cain 1976 gives the classical strict-P criterion

[
A in D_H^(3) iff Phi(A)>1
]

under the project's negative-stability sign convention.

For 2/3<alpha<1, the project proves the sufficient fractional criterion

[
Phi(A)>rho_alpha,
\qquad
rho_alpha=(1-2cos(alpha*pi/2))^2.
]

This is not known to be necessary.

## Main questions

1. Is `Phi(A)>rho_alpha` necessary for `A in F_alpha^(3)` on the strict-P stratum?
   - Prove it or produce an explicit analytic counterexample.
2. If not necessary, identify the minimum additional diagonal-orbit invariant(s) needed for an exact criterion.
3. Starting from the optimal fixed-cubic fractional Routh-Hurwitz conditions of Cermak-Nechvatal / Bourafa-Abdelouahab-Moussaoui, eliminate the positive diagonal variables.
4. Determine whether the exact criterion can be expressed only through principal minors.
5. Analyze boundary strata where some signed principal minors vanish (Cain type-1 analogue).
6. State the alpha->1 limit and show it reduces exactly to Cain's theorem.

## Preferred route

For theta=alpha*pi/2, use the exact boundary equation

[
p(re^{i theta})=0
]

for

[
p(lambda)=lambda^3+a_D lambda^2+b_D lambda+c_D.
]

Exploit homogeneity: common scaling of D does not affect eigenvalue arguments, so the orbit has only two independent diagonal ratios.

Possible methods:
- normalized coefficient plane (b/a^2, c/a^3);
- Cardano / optimal fractional Routh-Hurwitz boundary;
- resultant elimination of r and the two independent diagonal ratios;
- geometric programming / log-coordinate convexity where applicable;
- principal-minor invariants and Cain's domination structure.

## Falsification rule

Finite diagonal sampling may be used to find candidate counterexamples to necessity, never as proof.

## Deliverable

Create `research/THEOREM_C10_EXACT_3X3.md`.

Acceptable outcomes:
- EXACT CHARACTERIZATION PROVED;
- NECESSITY OF PHI CERTIFICATE PROVED;
- PHI NOT NECESSARY — explicit counterexample + stronger invariant identified;
- BLOCKED — with a sharply defined residual algebraic problem.

Do not generalize to cactus graphs before this task is closed.
