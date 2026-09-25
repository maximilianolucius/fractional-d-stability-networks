# C-11 — Exact diagonal-orbit minimum and fractional Cain certificate

**Date:** 2026-09-24
**Status:** INTERNAL ANALYTIC THEOREM; structural strengthening of C-09
**Novelty status:** do not claim the minimization identity itself as standalone novelty; position it as the fractional extension mechanism of the classical 3x3 Cain criterion.

## Setup

Let A be a real 3x3 matrix such that -A is a strict P-matrix. Define

[
p_i=-a_{ii}>0,
]

[
m_{12}=det A[\{1,2\}],quad
m_{13}=det A[\{1,3\}],quad
m_{23}=det A[\{2,3\}]>0,
]

and

[
q=-det A>0.
]

For a positive diagonal matrix

[
D=operatorname{diag}(d_1,d_2,d_3),
]

write

[
det(lambda I-DA)
=
lambda^3+a_Dlambda^2+b_Dlambda+c_D.
]

Then

[
a_D=p_1d_1+p_2d_2+p_3d_3,
]

[
b_D=m_{12}d_1d_2+m_{13}d_1d_3+m_{23}d_2d_3,
]

[
c_D=q,d_1d_2d_3.
]

## Theorem 1 — exact orbit minimum

Define

[
Phi(A)
=
rac{
left(
sqrt{p_1m_{23}}+
sqrt{p_2m_{13}}+
sqrt{p_3m_{12}}
ight)^2
}{q}.
]

Then

[
oxed{
inf_{Dsucc0}rac{a_Db_D}{c_D}
=
Phi(A).
}
]

Moreover the infimum is attained. Up to common scalar multiplication of D, an optimizer is

[
d_1proptosqrt{rac{m_{23}}{p_1}},
qquad
d_2proptosqrt{rac{m_{13}}{p_2}},
qquad
d_3proptosqrt{rac{m_{12}}{p_3}}.
]

### Proof

Since

[
rac{b_D}{d_1d_2d_3}
=
rac{m_{23}}{d_1}
+
rac{m_{13}}{d_2}
+
rac{m_{12}}{d_3},
]

we have

[
rac{a_Db_D}{c_D}
=
rac1q
left(p_1d_1+p_2d_2+p_3d_3ight)
left(
rac{m_{23}}{d_1}
+rac{m_{13}}{d_2}
+rac{m_{12}}{d_3}
ight).
]

Put

[
x_i=p_id_i,
]

and

[
r_1=p_1m_{23},qquad
r_2=p_2m_{13},qquad
r_3=p_3m_{12}.
]

Then

[
rac{a_Db_D}{c_D}
=
rac1q
left(sum_i x_iight)
left(sum_irac{r_i}{x_i}ight).
]

Cauchy-Schwarz gives

[
left(sum_i x_iight)
left(sum_irac{r_i}{x_i}ight)
ge
left(sum_isqrt{r_i}ight)^2.
]

Equality holds iff

[
x_iproptosqrt{r_i},
]

which is exactly the diagonal scaling stated above. QED.

---

## Corollary 1 — exact recovery of the classical Cain threshold

Let M=-A, so M is a strict P-matrix in Cain's positive-stability convention.

Cain's complete 3x3 D-stability theorem uses

[
Delta
=
sqrt{p_1m_{23}}+
sqrt{p_2m_{13}}+
sqrt{p_3m_{12}}
]

and, in the strict-P/type-2 case, requires

[
q<Delta^2.
]

Equivalently,

[
oxed{
Phi(A)>1.
}
]

Thus the orbit functional (Phi) is exactly the classical 3x3 D-stability domination ratio.

This is not a new classical result; it is the correct bridge to Cain (1976).

---

## Theorem 2 — fractional Cain-type sufficient certificate

Let

[
	heta=rac{alphapi}{2},
qquad
rac23<alpha<1,
]

and define

[
ho_alpha
=
left(1-2cos	hetaight)^2.
]

If -A is a strict P-matrix and

[
oxed{
Phi(A)>ho_alpha,
}
]

then

[
oxed{
Ainmathcal F_alpha^{(3)}.
}
]

### Proof

For every D>0, Theorem 1 gives

[
rac{a_Db_D}{c_D}
ge
Phi(A)
>
ho_alpha.
]

The cubic angular certificate proved in
`research/THEOREM_C09_DIMENSION_THRESHOLD.md`
then implies

[
sigma(DA)subsetSigma_alpha.
]

Since this holds for every positive diagonal D, A belongs to
(mathcal F_alpha^{(3)}). QED.

---

## Corollary 2 — classical limit

As

[
alpha	o1^-,
]

we have

[
ho_alpha	o1.
]

Hence the fractional sufficient certificate

[
Phi(A)>ho_alpha
]

converges exactly to the strict-P classical Cain condition

[
Phi(A)>1.
]

This provides a continuous bridge between genuinely fractional D-stability and classical Hurwitz D-stability.

---

## Corollary 3 — explicit purely fractional band

For every

[
rac23<alpha<1,
]

the interval

[
oxed{
ho_alpha<Phi(A)le1
}
]

is a natural genuinely fractional band:

- (Phi(A)>ho_alpha) certifies fractional D-stability;
- (Phi(A)le1) fails the strict classical Cain D-stability threshold within the strict-P class.

Therefore, whenever the remaining Cain hypotheses are strict and (Phi(A)le1), matrices in this band are explicit candidates for

[
mathcal P_alpha^{(3)}
=
mathcal F_alpha^{(3)}
setminus
mathcal D_H^{(3)}.
]

For the C-09 witness family A_gamma, this band is nonempty for every alpha<1.

---

## Theorem 3 — invariance of Phi under positive left diagonal scaling

For every positive diagonal E,

[
oxed{
Phi(EA)=Phi(A).
}
]

### Proof

If E=diag(e_1,e_2,e_3), then

[
p_i(EA)=e_i p_i(A),
]

[
m_{jk}(EA)=e_je_km_{jk}(A),
]

and

[
q(EA)=e_1e_2e_3q(A).
]

Thus every product (p_i m_{jk}), with {i,j,k}={1,2,3}, acquires the common factor (e_1e_2e_3). The squared sum of square roots acquires the same factor as q, so the ratio is unchanged. QED.

Phi is also invariant under simultaneous permutation of rows/columns and under positive diagonal similarity, because the relevant principal minors are correspondingly permuted or unchanged.

---

## Ecological consequence for GLV Jacobians

For a generalized Lotka-Volterra equilibrium with positive abundance vector x*,

[
J
=
operatorname{diag}(x^*)A.
]

Therefore

[
oxed{
Phi(J)=Phi(A).
}
]

More fundamentally, because multiplication by diag(x*) simply reparametrizes the full positive left-diagonal orbit,

[
Jinmathcal F_alpha
iff
Ainmathcal F_alpha,
]

and

[
Jinmathcal D_H
iff
Ainmathcal D_H.
]

Hence

[
oxed{
Jinmathcal P_alpha
iff
Ainmathcal P_alpha.
}
]

The genuinely fractional D-stability classification is therefore independent of the particular positive equilibrium abundances in a GLV model; it is an interaction-matrix property.

This is the correct ecological application layer for the matrix theorem.

---

## Research status

The exact orbit-minimum identity is elementary and mirrors Cain's classical proof structure. Do not sell it alone as novelty.

Its value to the project is that it:

1. replaces the previous non-sharp AM-GM bound by the exact orbit minimum;
2. exposes the direct relationship with Cain's complete 3x3 classical criterion;
3. gives a transparent fractional threshold (ho_alpha<1);
4. makes the alpha -> 1 classical limit exact;
5. supplies an abundance-invariant certificate for 3-species GLV systems.

The next open mathematical question is whether (Phi(A)>ho_alpha) is merely sufficient or can be upgraded, with additional invariants, to a necessary-and-sufficient characterization of (mathcal F_alpha^{(3)}).
