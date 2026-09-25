# C-13 — Ecological loop coordinates for exact 3x3 fractional D-stability

**Date:** 2026-09-24  
**Status:** ANALYTIC COROLLARY OF C-10  
**Role in paper:** topology/ecology interpretation layer; loop analysis itself is classical and is not claimed as new.

## 1. Setup

Let

\[
A=(a_{ij})\in\mathbb R^{3\times3}
\]

be an interaction matrix with negative self-effects

\[
a_{ii}=-p_i,\qquad p_i>0.
\]

Assume \(-A\) is a strict P-matrix, the full-dimensional stratum used in C-10.

For each unordered pair \(i<j\), define the normalized reciprocal-loop gain

\[
g_{ij}
=
\frac{a_{ij}a_{ji}}{p_ip_j}.
\]

Then the normalized order-two principal-minor invariants of C-10 are

\[
\boxed{
\beta_{ij}=1-g_{ij}.
}
\]

Indeed,

\[
m_{ij}
=
a_{ii}a_{jj}-a_{ij}a_{ji}
=
p_ip_j-a_{ij}a_{ji}.
\]

Hence

\[
\frac{m_{ij}}{p_ip_j}
=
1-\frac{a_{ij}a_{ji}}{p_ip_j}.
\]

### Ecological sign interpretation

- Predator-prey / antagonistic reciprocal pair:
  \[
  a_{ij}a_{ji}<0
  \quad\Longrightarrow\quad
  \beta_{ij}>1.
  \]

- Mutualistic or competitive reciprocal pair:
  \[
  a_{ij}a_{ji}>0
  \quad\Longrightarrow\quad
  0<\beta_{ij}<1
  \]
  on the strict-P stratum.

- No reciprocal two-cycle:
  \[
  a_{ij}a_{ji}=0
  \quad\Longrightarrow\quad
  \beta_{ij}=1.
  \]

Thus the three beta invariants are exactly normalized pair-feedback coordinates.

---

## 2. Directed three-cycle coordinates

Define the two oriented normalized three-cycle products

\[
\ell_{123}
=
\frac{a_{12}a_{23}a_{31}}{p_1p_2p_3},
\]

and

\[
\ell_{132}
=
\frac{a_{13}a_{32}a_{21}}{p_1p_2p_3}.
\]

Let

\[
L_3=\ell_{123}+\ell_{132}
\]

be the total normalized directed three-cycle feedback.

Expanding the determinant,

\[
\det A
=
a_{11}a_{22}a_{33}
+
a_{12}a_{23}a_{31}
+
a_{13}a_{21}a_{32}
-
a_{13}a_{22}a_{31}
-
a_{12}a_{21}a_{33}
-
a_{11}a_{23}a_{32}.
\]

Substituting \(a_{ii}=-p_i\) and dividing by \(p_1p_2p_3\) gives

\[
\boxed{
\kappa
=
\frac{-\det A}{p_1p_2p_3}
=
1-(g_{12}+g_{13}+g_{23})-L_3.
}
\]

Since \(g_{ij}=1-\beta_{ij}\),

\[
\boxed{
\kappa
=
\beta_{12}+\beta_{13}+\beta_{23}
-2
-L_3.
}
\]

Thus C-10's four diagonal-orbit invariants have a complete motif interpretation:

- three normalized reciprocal two-cycle coordinates;
- one total normalized directed three-cycle coordinate.

No equilibrium-abundance parameter appears.

---

## 3. Exact motif form of the genuinely fractional band

For \(2/3<\alpha<1\), C-10 proves that the full-dimensional genuinely fractional region is

\[
T_1(\beta)
<
\kappa
<
T_\alpha(\beta),
\]

where

\[
T_1(\beta)
=
(\sqrt{\beta_{12}}+\sqrt{\beta_{13}}+\sqrt{\beta_{23}})^2,
\]

and \(T_\alpha(\beta)>T_1(\beta)\) is the exact fractional simplex threshold.

Substituting

\[
\kappa
=
\beta_{12}+\beta_{13}+\beta_{23}-2-L_3
\]

yields the equivalent exact three-cycle interval

\[
\boxed{
\beta_{12}+\beta_{13}+\beta_{23}
-2
-T_\alpha(\beta)
<
L_3
<
\beta_{12}+\beta_{13}+\beta_{23}
-2
-T_1(\beta).
}
\]

Therefore, **conditional on the three normalized pair-feedback loops**, fractional memory creates a nonempty interval of total three-cycle feedback for which the whole positive diagonal orbit is Matignon-stable although the matrix is not classically Hurwitz D-stable.

The width of this interval is exactly

\[
\boxed{
T_\alpha(\beta)-T_1(\beta)>0.
}
\]

This width tends to zero as \(\alpha\to1^-\).

---

## 4. Low-order regime

For

\[
0<\alpha\le2/3,
\]

every strict-P(-A) matrix is fractionally D-stable by the Kellogg P-matrix wedge.

The full-dimensional genuinely fractional condition is then simply failure of the classical Cain condition:

\[
\kappa>T_1(\beta).
\]

In motif coordinates,

\[
\boxed{
L_3
<
\beta_{12}+\beta_{13}+\beta_{23}
-2
-T_1(\beta).
}
\]

There is no finite fractional upper threshold in \(\kappa\) on the strict-P stratum in this low-order range.

---

## 5. Cyclic witness as a motif special case

For

\[
A_\gamma
=
\begin{pmatrix}
-1&0&-\gamma\\
\gamma&-1&0\\
0&\gamma&-1
\end{pmatrix},
\]

there are no reciprocal two-cycles, so

\[
\beta_{12}=\beta_{13}=\beta_{23}=1.
\]

Only one oriented three-cycle is present:

\[
\ell_{123}=0,
\qquad
\ell_{132}=-\gamma^3.
\]

Hence

\[
L_3=-\gamma^3,
\]

and

\[
\kappa
=
3-2+\gamma^3
=
1+\gamma^3.
\]

The classical threshold is

\[
T_1(1,1,1)=9,
\]

so the integer-order boundary is

\[
1+\gamma^3=9
\iff
\gamma=2.
\]

For \(2/3<\alpha<1\), C-10 recovers the Siami fractional boundary

\[
\gamma<R_3(\alpha).
\]

Thus the familiar negative-feedback 3-cycle is a one-dimensional slice of the full four-invariant theory, not the theorem itself.

---

## 6. GLV abundance invariance

For a positive generalized Lotka-Volterra equilibrium,

\[
J=\operatorname{diag}(x^*)A,
\qquad
x_i^*>0.
\]

Every row \(i\) is multiplied by \(x_i^*\). Therefore

\[
p_i(J)=x_i^*p_i(A),
\]

\[
m_{ij}(J)=x_i^*x_j^*m_{ij}(A),
\]

and

\[
-\det J
=
x_1^*x_2^*x_3^*(-\det A).
\]

Consequently

\[
\boxed{
\beta_{ij}(J)=\beta_{ij}(A),
\qquad
\kappa(J)=\kappa(A),
}
\]

and the normalized loop products \(g_{ij}\), \(\ell_{123}\), \(\ell_{132}\) are invariant as well.

Hence the C-10 phase classification is independent of the particular positive equilibrium abundance vector.

This gives the ecological interpretation:

> for three-species GLV systems, the classical / genuinely fractional / fractionally unstable D-orbit phase is determined by normalized interaction-loop structure, not by the positive equilibrium abundance scaling.

---

## 7. Strict pair-loop monotonicity and exact sensitivity at fixed kappa

C-15 proves that, for \(2/3<\alpha<1\) and every positive beta triple, the C-10 simplex minimizer

\[
x^*=x^*(\alpha,\beta)
\]

is unique, nondegenerate and smooth.

For fixed simplex point \(x\),

\[
B_\beta(x)
=
\beta_{12}x_1x_2+
\beta_{13}x_1x_3+
\beta_{23}x_2x_3
\]

is strictly increasing in every \(\beta_{ij}\), because every optimizer lies in the open simplex.

Since \(h_\alpha'(b)>0\), increasing one beta coordinate while holding the other two fixed raises the objective strictly at every simplex point. Therefore

\[
\boxed{
\frac{\partial T_\alpha}{\partial\beta_{ij}}>0.
}
\]

More precisely, the envelope theorem applies because the optimizer is unique and nondegenerate. Let

\[
B^*
=
B_\beta(x^*).
\]

Then

\[
\frac{\partial T_\alpha}{\partial\beta_{ij}}
=
\frac{
h_\alpha'(B^*)x_i^*x_j^*
}{
x_1^*x_2^*x_3^*
}.
\]

If \(\{i,j,k\}=\{1,2,3\}\), this simplifies to the exact sensitivity formula

\[
\boxed{
\frac{\partial T_\alpha}{\partial\beta_{ij}}
=
\frac{h_\alpha'(B^*)}{x_k^*}
>0.
}
\]

Thus, **holding the determinant coordinate \(\kappa\) fixed**, making a reciprocal pair more antagonistic (increasing \(\beta_{ij}\)) strictly raises the admissible fractional D-stability threshold.

Equivalently, because

\[
\beta_{ij}=1-g_{ij},
\]

the threshold is strictly decreasing in the normalized reciprocal-loop product \(g_{ij}\) at fixed \(\kappa\).

This is a conditional structural statement. Changing an actual ecological coefficient typically changes both \(\beta\) and \(\kappa\), so it must not be presented as an unconditional causal claim about a biological intervention.

---

## 8. Prior-art boundary

Loop analysis, signed digraphs, community matrices, species-deletion stability, and the ecological interpretation of principal minors are classical topics.

The project should not claim novelty for the statement "loops determine stability" in generic form.

The contribution is narrower and mathematical:

1. C-10 gives an exact fractional positive-diagonal-orbit criterion.
2. C-13 identifies its four invariants with normalized two- and three-species feedback motifs.
3. The exact memory-only stability band has an explicit motif-coordinate form and is invariant under positive GLV abundance scaling.

This is the correct route for reconnecting the matrix theorem to ecological networks.
