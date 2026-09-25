# Independent adversarial proof audit — C-07 / C-09 / C-10 / C-11 / C-14 / C-15 / C-16

**Date:** 2026-09-25  
**Branch:** agent/proof-audit-c07-c10-20260925  
**Audited base:** b863b44ce8a3105424eb3fd50f9983acdb4fffc3  
**Role:** independent mathematical verifier  
**Scope:** proof validity, equality cases, positive-diagonal quantifiers and the explicitly imported classical results. This is not a novelty audit.

## Final verdicts

| Claim | Verdict | Reason for any qualification |
|---|---|---|
| C-07 | **PASS** | The \(2\times2\) equivalence, the classical subset and the empty-interior conclusion are correct, including all equality cases. |
| C-09 | **PASS** | The Kellogg bridge, cubic certificate, witness interval and full-dimensional open-ball argument are valid and uniform over every \(D\succ0\). |
| C-10 | **PASS WITH MINOR FIX** | The theorem is correct. Replace the reference to “compactness of the normalized simplex” by the coercive compact-sublevel argument below; the open simplex itself is not compact. |
| C-11 | **PASS WITH MINOR FIX** | The mathematics is correct. The source contains literal control characters that corrupt much of its TeX, and Corollary 3 can state membership rather than merely call the matrices “candidates.” |
| C-14 | **PASS** | Monotonicity, the endpoint expansion, the envelope step and the symmetric coefficient all check exactly. |
| C-15 | **PASS WITH MINOR FIX** | The results are correct. The parametrization proof should explicitly verify two short identities, and the realizability proof should give the promised off-diagonal construction. |
| C-16 | **PASS** | The coefficient formula, invariants, simplex bijection, normalized polynomial and invariant counts are correct for arbitrary \(n\). |

There is no FAIL verdict and therefore no counterexample to report.

## 1. Conventions and imported results

For \(D\succ0\), left and right diagonal multiplication have the same spectrum because

\[
DA=D(AD)D^{-1}.
\]

Thus Cain's right-multiplier convention for \(M=-A\) and this repository's left-multiplier convention for \(A\) agree after the sign change. If

\[
\det(\lambda I-DA)=\lambda^3+a_D\lambda^2+b_D\lambda+c_D,
\]

then on the strict-\(P(-A)\) stratum

\[
a_D=\sum_i p_i d_i,\qquad
b_D=\sum_{i<j}m_{ij}d_id_j,\qquad
c_D=q d_1d_2d_3
\]

are all positive.

The strict inequalities used throughout are necessary: the Matignon rays, zero, and the imaginary axis at \(\alpha=1\) are not part of the relevant open stability regions.

The imported Kellogg statement was checked against the original result: if \(P\) is an \(n\times n\) strict P-matrix, every eigenvalue \(\mu\) satisfies

\[
|\arg\mu|<\pi-\frac\pi n.
\]

The imported Cain statement was checked against the original 1976 paper. On the strict-P/type-2 stratum, Cain's determinant condition is strict. Here it is \(q<\Delta^2\), equivalently \(\Phi>1\).

Primary sources:

- R. B. Kellogg, [On complex eigenvalues of M and P matrices](https://doi.org/10.1007/BF01402527), *Numerische Mathematik* 19 (1972), 170–175.
- B. E. Cain, [Real, 3 x 3, D-stable matrices](https://doi.org/10.6028/JRES.080B.013), *Journal of Research of the National Bureau of Standards* 80B (1976), 75–77.

## 2. C-07 — exact real \(2\times2\) classification

Let

\[
A=\begin{pmatrix}a&b\\c&d\end{pmatrix},
\qquad
D=\operatorname{diag}(x,y).
\]

Then

\[
\operatorname{tr}(DA)=xa+yd,\qquad
\det(DA)=xy\det A.
\]

Necessity:

- If \(\det A=0\), every \(DA\) has a zero eigenvalue.
- If \(\det A<0\), every \(DA\) has two real eigenvalues of opposite signs.
- If \(a>0\), fix \(x>0\) and let \(y\downarrow0\). The limiting matrix has the simple positive eigenvalue \(xa\), which persists for small \(y>0\). Exchanging the indices excludes \(d>0\).

Hence membership requires

\[
\det A>0,\qquad a\le0,\qquad d\le0.
\]

These inequalities are also sufficient: every \(DA\) has positive determinant and nonpositive trace. Real roots are negative; a nonreal conjugate pair has nonpositive real part and arguments of magnitude at least \(\pi/2>\alpha\pi/2\).

The boundary \(a=d=0\) gives purely imaginary roots. It is stable for every \(\alpha<1\), but not at \(\alpha=1\). Repeated negative roots cause no exception. Classical Hurwitz D-stability requires at least one of \(a,d\) to be strictly negative. Therefore

\[
\mathcal P_\alpha^{(2)}
=
\left\{
\begin{pmatrix}0&b\\c&0\end{pmatrix}:bc<0
\right\},
\]

a codimension-two subset of \(\mathbb R^4\).

**C-07 verdict: PASS.**

## 3. C-09 — minimum robust dimension

### Kellogg rotation

For \(D\succ0\), \(D(-A)=-DA\) remains a strict P-matrix. Kellogg gives

\[
|\arg\mu|<\pi-\frac\pi n
\quad (\mu\in\sigma(-DA)).
\]

Rotation by \(\pi\) therefore gives

\[
|\arg\lambda|>\frac\pi n
\quad (\lambda\in\sigma(DA)).
\]

Thus \(-A\) strict P implies \(A\in\mathcal F_\alpha^{(n)}\) for \(0<\alpha\le2/n\). Strictness at \(\alpha=2/n\) is preserved.

### Cubic angular lemma

If a violating conjugate pair is \(re^{\pm i\phi}\), \(0<\phi\le\theta<\pi/2\), positivity of the constant coefficient forces the third root to be \(-s\), \(s>0\). With \(t=s/r\) and \(u=\cos\phi\), coefficient matching gives

\[
a=r(t-2u),\qquad
b=r^2(1-2tu),\qquad
c=tr^3.
\]

The conditions \(a,b>0\) give \(2u<t<(2u)^{-1}\), hence \(0<u<1/2\), and

\[
\frac{ab}{c}
=1+4u^2-2u(t+t^{-1})
\le(1-2u)^2
\le(1-2\cos\theta)^2.
\]

Every inequality direction in the contrapositive is correct. Equality in the final certificate is intentionally not certified.

### Uniform orbit and open ball

For strict \(P(-A)\), AM-GM yields, simultaneously for every \(D\succ0\),

\[
\frac{a_Db_D}{c_D}
\ge
\frac{9(p_1p_2p_3m_{12}m_{13}m_{23})^{1/3}}q.
\]

This controls the noncompact diagonal orbit directly; no compactness of diagonal ratios is assumed.

For the witness \(A_\gamma\),

\[
p_i=m_{ij}=1,\qquad
q=1+\gamma^3,\qquad
L(A_\gamma)=\frac9{1+\gamma^3},
\]

and

\[
\sigma(A_\gamma)
=\{-1-\gamma,-1+\gamma/2\pm i\sqrt3\gamma/2\}.
\]

For \(2/3<\alpha<1\), the interval

\[
2<\gamma<\left(\frac9{\rho_\alpha}-1\right)^{1/3}
\]

is nonempty because \(0<\rho_\alpha<1\). Strict P-minors, \(L>\rho_\alpha\), and positive spectral abscissa at \(D=I\) are open full-matrix conditions. Their intersection contains a full-dimensional ball. Combined with C-07 and the Kellogg range, this proves the minimum dimension for every \(0<\alpha<1\).

**C-09 verdict: PASS.**

## 4. C-10 — exact strict-P \(3\times3\) characterization

### Fixed cubic boundary

For \(\lambda=re^{i\theta}\), separation of the imaginary part of

\[
\lambda^3+a\lambda^2+b\lambda+c=0
\]

gives

\[
(1-4u^2)r^2-2uar-b=0,\qquad u=\cos\theta.
\]

When \(\pi/3<\theta<\pi/2\), \(K=1-4u^2>0\), so this equation has exactly one positive root

\[
r_\theta(a,b)=\frac{ua+\sqrt{u^2a^2+Kb}}K.
\]

The real part gives

\[
c=H_\theta(a,b)=r^2(a+2ur).
\]

For small positive \(c\), the roots are a small negative root and a perturbation of the Hurwitz quadratic \(\lambda^2+a\lambda+b\). For large \(c\), two roots approach angles \(\pm\pi/3\). Since the only possible ray contact occurs at the unique value \(H_\theta\), the stable side is exactly \(c<H_\theta\). At equality the pair lies on the excluded boundary. Direct substitution verifies

\[
H_\theta(sa,s^2b)=s^3H_\theta(a,b).
\]

### Orbit-simplex bijection

With \(s=a_D\) and \(x_i=p_id_i/s\), \(x\in\Delta_2^\circ\). Conversely,

\[
d_i=sx_i/p_i
\]

recovers every simplex point. Two diagonals give the same \(x\) exactly when they differ by a common positive scalar. The normalized coefficients are

\[
\frac{b_D}{s^2}=B_\beta(x),\qquad
\frac{c_D}{s^3}=\kappa x_1x_2x_3.
\]

The fixed-cubic result therefore gives, without loss in either direction,

\[
A\in\mathcal F_\alpha^{(3)}
\iff
\kappa<T_\alpha(\beta).
\]

The minimum is attained in the interior. The function \(h_\alpha\) has the positive continuous extension

\[
h_\alpha(0)=\left(\frac{2u}{K}\right)^2
\left(1+\frac{4u^2}{K}\right)>0,
\]

whereas \(x_1x_2x_3\to0\) on the simplex boundary.

### P0 necessity, interior and equality cases

- A positive diagonal entry produces a persistent positive eigenvalue when the other row scalings tend to zero.
- A negative order-two principal minor produces a positive eigenvalue in the corresponding limiting \(2\times2\) block.
- A real Matignon-stable cubic has one negative real root; the other roots are either both negative or a conjugate pair. Its determinant is strictly negative.

Thus \(-A\) is P0 with positive determinant. Any zero order-one or order-two principal minor can be perturbed arbitrarily slightly to the forbidden sign, so every interior point is strict P.

The Cain endpoint is

\[
T_1(\beta)
=\min_x\frac{B_\beta(x)}{x_1x_2x_3}
=\left(\sqrt{\beta_{12}}+\sqrt{\beta_{13}}+\sqrt{\beta_{23}}\right)^2.
\]

The minimum is attained, so \(\kappa=T_1\) is not classically D-stable. It is also not an interior point of the fractional-only difference. For \(2/3<\alpha<1\), \(h_\alpha(b)>b\) pointwise. Evaluation at the fractional minimizer proves the strict inequality \(T_\alpha>T_1\).

The analytic Siami family also checks: \(\gamma_\Phi<R_3\) follows from the displayed factorization because \(0<t<2-\sqrt3\); \(\gamma_\Phi>2\) follows from \(\rho_\alpha<1\). Hence C-11's scalar certificate is not necessary.

### Required minor correction

The sentence in Theorem 2 saying that “compactness of the normalized simplex supplies a positive margin” is literally false because \(\Delta_2^\circ\) is open. Replace it by:

> The objective extends continuously to \(+\infty\) at the closed-simplex boundary. For parameters in a sufficiently small neighborhood of a fixed strict-P matrix, \(h_\alpha(B_\beta(x))\) has a uniform positive lower bound and the sublevel sets containing all minimizers lie in one compact subset of \(\Delta_2^\circ\). The minimum therefore varies continuously, and the strict inequality \(\kappa<T_\alpha(\beta)\) persists.

This is a local compact-sublevel/coercivity correction, not a change to the theorem.

**C-10 verdict: PASS WITH MINOR FIX.**

## 5. C-11 — exact orbit minimum and sufficient certificate

The identity

\[
\frac{a_Db_D}{c_D}
=\frac1q
\left(\sum_i x_i\right)
\left(\sum_i\frac{r_i}{x_i}\right),
\quad
x_i=p_id_i,
\]

with

\[
(r_1,r_2,r_3)=(p_1m_{23},p_2m_{13},p_3m_{12})
\]

is exact. Cauchy-Schwarz gives the claimed minimum, and its equality condition gives

\[
d_1\propto\sqrt{m_{23}/p_1},\qquad
d_2\propto\sqrt{m_{13}/p_2},\qquad
d_3\propto\sqrt{m_{12}/p_3}.
\]

The infimum is attained at a finite positive diagonal. Consequently \(\Phi>1\), not \(\Phi\ge1\), is the classical strict-P Cain condition.

The implication

\[
\Phi>\rho_\alpha
\Longrightarrow
\frac{a_Db_D}{c_D}>\rho_\alpha
\quad\forall D\succ0
\]

feeds directly into the C-09 cubic angular lemma. Positive left multiplication scales every \(p_i m_{jk}\) and \(q\) by the same product \(e_1e_2e_3\), proving \(\Phi(EA)=\Phi(A)\). In the GLV application, multiplication by \(\operatorname{diag}(x^*)\) bijectively reparametrizes the full positive diagonal orbit.

### Required minor corrections

1. *research/THEOREM_C11_FRACTIONAL_CAIN_CERTIFICATE.md* contains literal form-feed, backspace, carriage-return and tab characters where TeX backslashes should appear. Sanitize the file before manuscript reuse.
2. On the strict-P stratum, \(\rho_\alpha<\Phi\le1\) proves membership in \(\mathcal P_\alpha^{(3)}\); these are not merely “candidates.” Equality \(\Phi=1\) fails classical D-stability because the orbit minimum is attained.

**C-11 verdict: PASS WITH MINOR FIX.**

## 6. C-14 — monotonicity and classical-limit rate

For fixed \(a,b>0\), the cubic at \(c=H_{\theta_2}(a,b)\) has its conjugate pair at angle \(\theta_2\). If \(\theta_1<\theta_2\), it is strictly stable for the wider \(\theta_1\) condition. Uniqueness of the boundary value gives

\[
H_{\theta_1}(a,b)>H_{\theta_2}(a,b).
\]

Pointwise strictness remains strict after minimization: at a minimizer \(x_1^*\) of the first objective,

\[
T_{\alpha_1}=f_{\alpha_1}(x_1^*)
>f_{\alpha_2}(x_1^*)
\ge T_{\alpha_2}.
\]

At \(u=0\), implicit differentiation of

\[
(1-4u^2)r^2-2ur-b=0
\]

gives \(r=\sqrt b\) and \(r_u=1\). Hence

\[
h_u(0,b)=2\sqrt b(1+b),
\]

and, because \(u=(\pi/2)(1-\alpha)+O((1-\alpha)^3)\),

\[
h_\alpha(b)=b+\pi(1-\alpha)\sqrt b(1+b)+O((1-\alpha)^2).
\]

The classical objective has the unique nondegenerate minimizer stated in C-14. The envelope theorem therefore applies and gives

\[
C(\beta)=\pi S^{3/2}
\left(\frac S{\sqrt G}+\sqrt G\right).
\]

At \(\beta=(1,1,1)\), this is \(12\pi\sqrt3\), agreeing with the direct expansion of \(1+R_3(\alpha)^3\).

**C-14 verdict: PASS.**

## 7. C-15 — convexity, parametrization, transition and realizability

### Elasticity and Hessian

With \(b=r(Kr-2u)\) and \(h=r^2(1+2ur)\), differentiation gives

\[
E=\frac{b h'}h
=
\frac{(Kr-2u)(1+3ur)}{(Kr-u)(1+2ur)}.
\]

Both factors in C-15 increase strictly, with limiting product from \(0\) to \(3/2\). Thus \(0<E<3/2\) and \(dE/db>0\).

For \(s=Q-2L\), the Hessian identity

\[
\nabla^2G
=\phi''\nabla s\nabla s^\top
+\phi'\nabla^2Q
+(3-2\phi')\nabla^2L
\]

is correct. The first two terms are positive semidefinite, while \(\nabla^2L\) is positive definite and \(3-2\phi'>0\). Hence the Hessian is positive definite. Since \(h_\alpha\) has a positive limit at \(b=0\), the objective diverges at the simplex boundary, giving coercivity, uniqueness, nondegeneracy and smooth dependence.

### Parametrization

The stationarity equations are correct. For the inverse construction, let \(c=2E-3\) and

\[
z_{ij}=\frac{1+c(1-2x_k)}{2E}.
\]

Then

\[
z_{12}+z_{13}+z_{23}
=\frac{3+c}{2E}=1,
\]

and

\[
E(z_{ij}+z_{ik})=1+cx_i.
\]

Consequently the displayed \(\beta_{ij}=Bz_{ij}/(x_ix_j)\) reproduces \(B_\beta(x)=B\) and makes \(x\) stationary. Strict convexity then makes it the unique global minimizer. These identities close the omitted algebraic step in the bijectivity proof.

### Low-order asymptotic

Writing \(2u=\sqrt{1-K}\) and expanding the positive boundary root gives

\[
K^3h_\alpha(b)=1+K(3b-1)+O(K^2)
\]

uniformly for bounded \(b\ge0\). Since \(B_\beta\) is bounded on the closed simplex, this supplies the uniform lower bound that keeps minimizers in a fixed compact subset. Perturbation around the unique maximum of \(x_1x_2x_3\) gives

\[
T_\alpha(\beta)
=\frac{27}{K^3}
+\frac{9\sum\beta_{ij}-27}{K^2}
+O(K^{-1}),
\qquad
x^*=\left(\frac13,\frac13,\frac13\right)+O(K).
\]

### Realizability

The discriminant argument for

\[
\ell^2-L_3\ell+G=0
\]

is correct in every sign case. The construction can be made explicit. For a nonzero real root \(\ell\), set

\[
a_{12}=a_{23}=1,\quad
a_{31}=\ell,\quad
a_{21}=g_{12},\quad
a_{32}=g_{23},\quad
a_{13}=g_{13}/\ell,
\]

and \(a_{ii}=-1\). The pair products are \(g_{ij}\), the forward loop is \(\ell\), and the reverse loop is \(G/\ell\). When \(G=0\), \(L_3<0\) for \(\kappa\ge T_1\), so the quadratic has the nonzero root \(\ell=L_3\) and the same construction works. This proves realizability including zero pair products.

### Required minor correction

Add the two \(z\)-identities to Theorem 2 and the explicit six-entry construction to Theorem 4. The theorem statements do not change.

**C-15 verdict: PASS WITH MINOR FIX.**

## 8. C-16 — general orbit-simplex reduction

For every index set \(I\),

\[
\det(DA[I])=\left(\prod_{i\in I}d_i\right)\det A[I].
\]

The principal-minor expansion of the characteristic polynomial gives

\[
c_k(D)=\sum_{|I|=k}m_I\prod_{i\in I}d_i.
\]

Under \(A\mapsto EA\), both \(m_I\) and \(\prod_{i\in I}p_i\) acquire the factor \(\prod_{i\in I}e_i\), proving invariance of every \(\beta_I\).

The map \(D\mapsto x\), \(x_i=p_id_i/\sum_jp_jd_j\), is a bijection modulo common positive scale, with inverse \(d_i=sx_i/p_i\). Substitution gives

\[
\frac{c_k(D)}{s^k}=B_k(x)
\]

and the normalized polynomial in C-16. The number of non-singleton subsets is

\[
\sum_{k=2}^n\binom nk=2^n-n-1.
\]

For \(n=3\), this gives the three \(\beta_{ij}\) plus \(\kappa\). For \(n=4\), it gives \(6+4+1=11\) invariants. All signs and powers of \(s\) agree.

**C-16 verdict: PASS.**

## 9. Computational corroboration

All computation ran on r39 under nice -n 10, restricted to CPUs 0–7, with a 3 GiB virtual-memory cap and BLAS thread caps. It is corroboration only; no verdict treats sampling as proof.

The full repository suite at the audited commit passed:

    13 passed

An independent deterministic property campaign used seed 20260925:

    fixed_cubic_cases=10000 boundary_angle_error=8.882e-16
    orbit_min_cases=12000 worst_relative_error=7.772e-16
    parametrization_cases=300 worst_x_error=3.458e-08 worst_T_relative_error=1.266e-14
    classical_limit_cases=30 worst_ratio_error=1.269e-04
    low_order_checks=40 max_scaled_remainder=2.013e+01
    realizability_cases=1004 worst_invariant_abs_error=9.948e-14
    general_simplex_cases=500 worst_coefficient_abs_error=2.665e-15
    INDEPENDENT_PROPERTY_CHECKS=PASS

The fixed-cubic campaign tested both sides of the exact boundary. The parametrization campaign generated admissible \((x,r)\), reconstructed \(\beta\), and independently minimized the log-objective. The realizability campaign covered \(G<0\), \(G>0\), and exact \(G=0\) examples. The C-16 campaign compared characteristic coefficients directly for dimensions \(2\) through \(6\).

## 10. Audit gate

The C-07/C-09/C-10/C-11/C-14/C-15/C-16 proof package survives adversarial verification. The three PASS WITH MINOR FIX items are local, explicitly repairable, and do not narrow any theorem statement. They should be applied before the package is labeled submission-certified; bibliographic novelty remains governed by the separate specialist novelty lane.
