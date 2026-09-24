# Deep novelty audit report — reopened second pass

**Date:** 2026-09-24  
**Status:** `GO-NARROWED — AUDIT STILL OPEN`  
**Scope:** theorem-level novelty audit for `fractional-d-stability-networks`, updated after the Chief reopened the baseline audit at commit `0b3b4df394eceec0dc9951a33fda01560de2f731`.

This report incorporates the mandatory prior art that materially changes the first-pass conclusions:

- Milad Siami, *Stability and Robustness Analysis of Commensurate Fractional-order Networks*, arXiv:2011.04204 / IEEE TCNS.
- Olga Y. Kushel, *Some bounds for determinants of relatively D-stable matrices*, LAA 656 (2023), arXiv:2205.10823.
- Eyad H. Abed, *Strong D-stability*, Systems & Control Letters 7(3) (1986), 207–212.
- Re-reading of Kushel 2019 and Kushel–Pavani 2020/2021.
- Current robust-D-stability work: Casasanta–Simpson-Porco 2026, arXiv:2603.13608.

Detailed derivations are recorded in `research/novelty/REOPENED_AUDIT_2026-09-24.md`.

---

## 1. Central objects

For (0<alpha<1),

[
Sigma_alpha={z
eq0:|arg z|>alphapi/2}.
]

Define

[
mathcal F_alpha^{(n)}
=
{Ainmathbb R^{n	imes n}:
sigma(DA)subsetSigma_alpha
	ext{ for every positive diagonal }D},
]

and let (mathcal D_H^{(n)}) be the classical Hurwitz D-stable class. The genuinely fractional separation class is

[
mathcal P_alpha^{(n)}
=
mathcal F_alpha^{(n)}
setminus
mathcal D_H^{(n)}.
]

The scientific question is no longer whether fractional stabilization or generalized D-stability exists. Both are known. The live question is:

> **What exact structural mathematics governs the genuinely non-Hurwitz portion (mathcal P_alpha^{(n)}), and in what dimension can that portion first have nonempty full-dimensional interior?**

---

# 2. Corrected verdicts on the original candidate contributions

## C-01 — Matignon sector criterion — `KNOWN / IMPORTED`

For a commensurate Caputo system (D^alpha x=Ax), Matignon's criterion gives asymptotic stability iff the spectrum lies outside the excluded wedge:

[
|arglambda|>alphapi/2.
]

Brandibur, Garrappa & Kaslik (2021) provide a corrected modern treatment and explicitly record monotonicity with respect to (alpha). This is standard machinery.

**Verdict:** no novelty.

---

## C-02 — stable for (alpha<1), unstable at (alpha=1) — `KNOWN / MOTIVATION ONLY`

The existence of matrices with eigenvalues in

[
alphapi/2<|arglambda|lepi/2
]

is exactly the geometric difference between the fractional Matignon sector and the Hurwitz half-plane.

Ahmed–El-Sayed–El-Saka (2007) already use this phenomenon explicitly in applied fractional systems. It is also immediate from Matignon plus (alpha)-monotonicity.

**Verdict:** not a contribution.

---

## C-03 — graph-indexed region (S_alpha(G)) — `DEFINITION ONLY`

A graph-indexed stability set is not novel merely because it is defined. Fractional consensus already uses graph spectra with sector conditions, while integer-order ecology/network literature contains many topology-to-spectrum stability theorems.

A publishable theorem must add exact structure that is not a relabeling of Matignon, Laplacian spectral conditions, or classical topology-to-Hurwitz results.

**Verdict:** open only as a theorem program.

---

## C-04 — fractional D-stability under all positive diagonal scalings — `FRAMEWORK KNOWN`

The first-pass report was too optimistic here.

Kushel's ((mathfrak D,mathcal G,circ))-stability framework already includes arbitrary spectral regions and multiplier classes such as positive diagonal matrices. Hence

[
mathcal F_alpha
=
{A:sigma(DA)subsetSigma_alpha orall Dsucc0}
]

is an instance of a known generalized D-stability framework.

More importantly, the previous sentence

> "all existing sufficient conditions use convex regions and are blind to the non-convex purely fractional sliver"

is **withdrawn**.

Kushel–Pavani explicitly discuss the fractional-order stability set as the complement of a cone and note that this complement is not an LMI region. Their forbidden-boundary machinery treats the relevant angular boundaries under diagonal scaling. Kushel 2023 further studies relatively D-stable matrices and sector gaps.

These works do **not** supply the exact low-dimensional characterization sought here, but they occupy the ambient framework and much of the boundary/sector language.

**Verdict:** the concept is known. Only exact subclass characterization, dimension thresholds, or genuinely new structural separation remain viable.

---

## C-05 — single-cycle / motif fractional D-stability — `SINGLE-CYCLE NOVELTY REJECTED`

This is the most important correction.

Siami studies a cyclic commensurate fractional network with ratio

[
gamma=
left(
rac{prod_i c_i}
     {prod_i a_i}
ight)^{1/n},
]

and derives a generalized fractional secant condition. The condition is sufficient for the general single-circuit family and becomes necessary in a special equalized/uniform case.

Under a positive diagonal left scaling (D=operatorname{diag}(d_i)), both the relevant diagonal coefficient and cycle coefficient in row (i) are multiplied by (d_i). Hence

[
gamma(DA)=gamma(A).
]

Moreover, choosing

[
d_i=k/a_i
]

equalizes all diagonal magnitudes inside the same orbit.

Therefore a theorem of the form

> "a single-cycle matrix is fractionally D-stable iff a fractional secant condition holds"

is substantially recoverable from Siami by invariance plus diagonal equalization.

**Verdict:** a single-cycle secant theorem cannot be the paper's central novelty. Cactus or multi-cycle results survive only if they are strictly non-reducible to Siami plus known Arcak/Sontag-style results.

---

## C-06 — openness / robustness / uniform angular margin — `CONCEPT KNOWN; FRACTIONAL NON-HURWITZ VERSION MAY BE NEW`

Abed (1986) introduced **strong D-stability** precisely to mean D-stability that persists under all sufficiently small perturbations.

The classical literature also includes Hartfiel on the interior of the D-stable set, later structured-singular-value characterizations, and a 2026 Lyapunov characterization of robust D-stability by Casasanta & Simpson-Porco.

Therefore:

- "robust D-stability",
- "strong D-stability",
- "interior of D-stable matrices",
- or generic "uniform margin"

cannot be claimed as new concepts.

What may be new is a theorem showing a full-dimensional open subset of matrices that are robustly stable in the **fractional Matignon region** while remaining outside classical Hurwitz D-stability.

**Verdict:** viable only in genuinely fractional non-Hurwitz form.

---

# 3. Exact low-dimensional result: the (2	imes2) problem is closed

Let

[
A=
egin{pmatrix}
a&b\
c&d
end{pmatrix},
qquad
D=
operatorname{diag}(x,y),
quad x,y>0.
]

Then

[
operatorname{tr}(DA)=xa+yd,
qquad
det(DA)=xydet A.
]

For every (0<alpha<1),

[
oxed{
Ainmathcal F_alpha^{(2)}
iff
det A>0,quad ale0,quad dle0.
}
]

### Sufficiency

If (det A>0) and (a,dle0), then for every positive (D),

[
det(DA)>0,
qquad
operatorname{tr}(DA)le0.
]

The eigenvalues are therefore either both negative real numbers or a conjugate pair with nonpositive real part. Hence

[
|arglambda|gepi/2>alphapi/2.
]

### Necessity

- If (det Ale0), then (DA) has a zero or nonnegative real eigenvalue.
- If (a>0), taking (x/y	oinfty) forces a positive real eigenvalue asymptotically.
- If (d>0), taking (y/x	oinfty) does the same.

Therefore the characterization is exact.

The classical Hurwitz D-stable subset additionally requires

[
(a,d)
eq(0,0).
]

Thus

[
oxed{
mathcal P_alpha^{(2)}
=
left{
egin{pmatrix}
0&b\
c&0
end{pmatrix}
:
bc<0
ight},
}
]

and so

[
oxed{
operatorname{int}_{mathbb R^4}
mathcal P_alpha^{(2)}
=
arnothing.
}
]

**Proof status:** analytic theorem.  
**Novelty status:** structurally useful, but likely too elementary to carry a Q1 paper by itself.

---

# 4. The P-matrix bridge

A classical theorem of Kellogg gives the eigenvalue wedge for a (P)-matrix (Pinmathbb R^{n	imes n}):

[
|argmu|<pi-rac{pi}{n}
qquad
(muinsigma(P)).
]

If (-A) is a (P)-matrix and (Dsucc0), then (D(-A)) remains a (P)-matrix because every principal minor is multiplied by a positive product of entries of (D).

Therefore the eigenvalues of

[
DA=-D(-A)
]

satisfy

[
|arglambda(DA)|>rac{pi}{n}.
]

Hence:

> **Kellogg-to-Matignon lemma.**  
> If (-A) is a (P)-matrix, then
> [
> Ainmathcal F_alpha^{(n)}
> qquad
> orall,0<alphale2/n.
> ]

This bridge is imported/classical in ingredients and must not be presented as the paper's main novelty. Its role is to produce a full-dimensional separation theorem in dimension three.

---

# 5. Dimension three supports an open genuinely fractional class for (0<alphale2/3)

Consider

[
A_gamma=
egin{pmatrix}
-1&0&-gamma\
gamma&-1&0\
0&gamma&-1
end{pmatrix},
qquad gamma>2.
]

The matrix (-A_gamma) is a strict (P)-matrix:

- its three order-one principal minors equal (1);
- its three order-two principal minors equal (1);
- its determinant is (1+gamma^3>0).

Therefore, by the bridge above,

[
A_gammainmathcal F_alpha^{(3)}
qquad
orall,0<alphale2/3.
]

But

[
sigma(A_gamma)
=
left{
-1-gamma,,
-1+rac{gamma}{2}
pm irac{sqrt3,gamma}{2}
ight}.
]

If (gamma>2), the complex pair has positive real part. Thus (A_gamma) is not even Hurwitz at (D=I), and therefore

[
A_gamma
otinmathcal D_H^{(3)}.
]

Hence

[
A_gammainmathcal P_alpha^{(3)}.
]

### Full-dimensional openness

The strict (P)-matrix inequalities for (-A_gamma) are strict polynomial inequalities in the entries. They therefore persist on a sufficiently small full-dimensional ball around (A_gamma).

Likewise, the positive spectral abscissa of (A_gamma) at (D=I) persists under sufficiently small perturbations.

Consequently there exists (arepsilon>0) such that

[
oxed{
B_arepsilon(A_gamma)
subset
mathcal F_alpha^{(3)}
setminus
mathcal D_H^{(3)}
}
]

for every (0<alphale2/3).

Therefore

[
oxed{
operatorname{int}
mathcal P_alpha^{(3)}

eqarnothing
qquad
(0<alphale2/3).
}
]

Combining dimensions 1, 2 and 3:

[
oxed{
minleft{
n:
operatorname{int}mathcal P_alpha^{(n)}

eqarnothing
ight}
=
3,
qquad
0<alphale2/3.
}
]

### Status

- **Mathematical proof:** complete at the level recorded above, modulo the imported Kellogg theorem.
- **Novelty:** strong candidate, but not yet frozen. Targeted searches found all ingredients separately but did not locate this minimal-dimension robust genuinely-fractional separation theorem as a published result.

This is presently the strongest surviving result in the project.

---

# 6. Why (alpha=2/3) is a genuine cubic transition

For a cubic

[
p(lambda)
=
lambda^3+alambda^2+blambda+c
]

with positive coefficients, suppose a conjugate pair lies on the angular boundary

[
lambda=re^{pm i	heta}
]

and the third root is (-s), (s>0). Writing

[
t=s/r,
qquad h=cos	heta,
]

gives

[
a=r(t-2h),
]

[
b=r^2(1-2ht),
]

[
c=tr^3.
]

To keep (a,b>0), one needs

[
2cos	heta
<
t
<
rac{1}{2cos	heta}.
]

That interval exists exactly when

[
	heta>pi/3.
]

Since the Matignon boundary is

[
	heta=alphapi/2,
]

the critical point is

[
oxed{alpha=2/3}.
]

Thus (2/3) is not an artifact of the chosen example. It is the natural angular threshold at which a positive-coefficient cubic can first meet the Matignon boundary.

---

# 7. Highest-value open problem: (n=3,;2/3<alpha<1)

For (2/3<alpha<1), the (P)-matrix wedge alone is too weak.

Siami nevertheless supplies structured cyclic centers satisfying a fractional secant condition and allows a range in which the cycle is fractionally stable while classically unstable.

The central unresolved question is:

[
oxed{
operatorname{int}
mathcal P_alpha^{(3)}

eqarnothing
quad ?
}
]

for every

[
2/3<alpha<1.
]

Equivalently, can one produce a full-dimensional open ball around a (3	imes3) genuinely fractional D-stable matrix?

### Why ordinary continuity is insufficient

The quantifier

[
orall Dsucc0
]

ranges over a noncompact cone. After scalar normalization, the diagonal orbit approaches degenerate faces where one or more diagonal coordinates tend to zero.

Therefore a proof must control:

- interior normalized diagonal directions;
- all boundary faces;
- principal-submatrix limits;
- contact with the two Matignon rays.

This is exactly where a genuine new theorem could live.

---

# 8. Candidate exact (3	imes3) program

The strongest possible next theorem would be an explicit characterization of

[
mathcal F_alpha^{(3)}
qquad
(2/3<alpha<1)
]

analogous in role to classical low-dimensional D-stability criteria, but replacing exclusion of the imaginary axis with exclusion of the rays

[
arglambda
=
pmalphapi/2.
]

A viable route is:

1. normalize (D) to a simplex;
2. write the cubic coefficients of (det(lambda I-DA)) in terms of diagonal entries and principal minors;
3. parameterize boundary contact by (lambda=re^{pm ialphapi/2});
4. eliminate (r) and diagonal ratios;
5. derive an explicit inequality or finite family of inequalities;
6. analyze all simplex faces;
7. compare the resulting criterion theorem-by-theorem with Kushel's forbidden-boundary framework and classical (3	imes3) D-stability.

If this exact criterion is obtained, it is likely stronger and cleaner than a graph-specific theorem.

---

# 9. Reopened mandatory questions — answers

### 1. Does Siami quantify over the same positive diagonal orbit (DA)?

Not explicitly in the theorem statement. However, his key cycle ratio is invariant under all positive diagonal left row scalings, and the orbit can equalize the diagonal coefficients. Therefore the single-cycle D-orbit theorem is substantially subsumed.

### 2. Can the proposed single-cycle theorem be recovered from Siami?

Yes, to a degree that makes it unsafe as a novelty claim.

### 3. Does Siami reach the right-half-plane Matignon sliver?

Yes. The fractional cyclic criterion permits stability beyond the integer-order Hurwitz range for suitable (alpha<1).

### 4. What is the relation between Kushel's sector work and (Sigma_alpha)?

Kushel supplies the generalized-D-stability setting and sector/boundary machinery. Kushel–Pavani explicitly discuss fractional stability via the complement of a cone. Their work does not give the present low-dimensional (mathcal P_alpha) characterization, but the nonconvex/boundary geometry is not untouched.

### 5. Does Kushel already imply a generic proposed uniform angular margin?

Sector-gap results exist for important D-stable subclasses, so "uniform angular margin" is not itself novel. A new theorem must concern the genuinely non-Hurwitz Matignon class and exact quantifiers.

### 6. Which topology claims survive Siami?

Not a single-cycle secant theorem. Multi-cycle/cactus claims survive only if they cannot be reduced to Siami cycle conditions plus classical topology results.

### 7. Is the (2	imes2) classification known or immediate?

It is elementary enough to derive exactly from trace/determinant scaling, and the project now has a complete analytic proof. It is unlikely to be enough for a paper by itself.

### 8. Is (operatorname{int}mathcal P_alpha^{(3)}
eqarnothing)?

Yes, analytically for

[
0<alphale2/3.
]

The range (2/3<alpha<1) remains open.

### 9. How must "strong fractional D-stability" differ from Abed?

It must describe persistence inside the Matignon sector for matrices that are outside classical Hurwitz D-stability, and it must yield a theorem not inherited from classical robust D-stability.

### 10. What is the smallest Q1-level theorem package now visible?

The current package should be:

1. exact (2	imes2) characterization;
2. proof that the first dimension with a full-dimensional genuinely fractional D-stable region is (3);
3. extension of that dimension threshold to all (0<alpha<1), or an exact (3	imes3) characterization in the high-order range;
4. only then a motif/network interpretation.

---

# 10. Strongest novelty surviving the reopened audit — ≤3 sentences

For (0<alphale2/3), the project now has an analytic proof that dimension three is the first dimension in which the genuinely non-Hurwitz fractional D-stable class can have nonempty full-dimensional interior: the class is empty in dimension one, has empty interior in dimension two, and contains an explicit open ball in dimension three. The individual ingredients — Matignon stability, P-matrix wedges, generalized D-stability, cyclic fractional secant conditions, and strong D-stability — are known, but the combined minimal-dimension separation theorem was not located in the targeted literature audit. The high-value unresolved extension is to prove the same dimension threshold for every (0<alpha<1) or derive an exact (3	imes3) characterization for (2/3<alpha<1).

# 11. Exact theorem target

> **Target theorem.** For every (0<alpha<1),
> [
> min{n:
> operatorname{int}
> (mathcal F_alpha^{(n)}
> setminus
> mathcal D_H^{(n)})
> 
eqarnothing}
> =3.
> ]
> Equivalently: (nle2) cannot support a full-dimensional robust genuinely fractional D-stable class, while (n=3) can. For (0<alphale2/3) this is already proved internally; the remaining proof burden is (2/3<alpha<1).

A stronger alternative target is an exact characterization of (mathcal F_alpha^{(3)}) in the high-order regime.

# 12. Prior-art result most likely to kill the current target

No single located paper presently kills the dimension-threshold theorem. The **closest structural threats** are:

1. Kushel/Kushel–Pavani generalized-D-stability and forbidden-boundary theory, if a low-dimensional specialization already implies the same result;
2. classical low-dimensional D-stability/interior results (Cain, Hartfiel, Abed), if a direct region substitution yields the fractional statement;
3. Siami, for any proof that remains confined to a single-cycle submanifold instead of producing a full-dimensional open class.

# 13. Final verdict

[
oxed{	exttt{GO-NARROWED}}
]

Proceed with the low-dimensional theorem program. Do **not** draft the central manuscript around a single-cycle/cactus novelty claim. The immediate research priority is:

[
oxed{
n=3,qquad 2/3<alpha<1.
}
]

Numerical diagonal sampling remains counterexample hunting only.

---

# 14. Key sources

- Brandibur, Garrappa & Kaslik 2021, *Mathematics* 9:914: https://www.mdpi.com/2227-7390/9/8/914
- Kushel 2019, *SIAM Review* 61(3):643–729: https://arxiv.org/abs/1907.07089
- Kushel & Pavani 2020: https://arxiv.org/abs/2004.11172
- Kushel & Pavani 2021: https://arxiv.org/abs/2103.04127
- Kushel 2023 / arXiv preprint: https://arxiv.org/abs/2205.10823
- Siami 2020/2021: https://arxiv.org/abs/2011.04204
- Abed 1986, DOI: https://doi.org/10.1016/0167-6911(86)90116-7
- Casasanta & Simpson-Porco 2026: https://arxiv.org/abs/2603.13608
- Sabatier, Moze & Farges 2010, *Comput. Math. Appl.* 59:1594–1609.
- Ahmed, El-Sayed & El-Saka 2007, *J. Math. Anal. Appl.* 325:542–553.
- Arcak & Sontag 2006, *Automatica* 42(9).
- Arcak 2011, *IEEE TAC* 56(12):2766–2777.
- Hartfiel 1980, *Linear Algebra and its Applications*, interior of D-stable matrices.
- Lee & Edgar 2001, *Systems & Control Letters* 44:273–277.
