# Reopened novelty audit — 2026-09-24

**Role:** independent web-search / theorem-level prior-art audit  
**Status:** ACTIVE RESEARCH RECORD  
**Controlling direction:** `research/CHIEF_RESEARCH_DIRECTION_2026-09-24.md`

This note supersedes the over-broad conclusions of the baseline audit at commit `0b3b4df394eceec0dc9951a33fda01560de2f731` wherever they conflict with the findings below.

## 1. Central objects

For (0<alpha<1),

[
Sigma_alpha={z
eq 0:|arg z|>alphapi/2},
]

[
mathcal F_alpha^{(n)}
=
{Ainmathbb R^{n	imes n}:
sigma(DA)subsetSigma_alpha 	ext{for every }Dsucc0},
]

and, with (mathcal D_H^{(n)}) denoting classical Hurwitz D-stability,

[
mathcal P_alpha^{(n)}
=
mathcal F_alpha^{(n)}setminusmathcal D_H^{(n)}.
]

Definitions alone are not contributions. The novelty target is exact structural mathematics for the genuinely non-Hurwitz part (mathcal P_alpha^{(n)}).

---

## 2. Siami 2020/2021: the single-cycle target is substantially occupied

**Reference:** Milad Siami, *Stability and Robustness Analysis of Commensurate Fractional-order Networks*, arXiv:2011.04204; later IEEE TCNS.  
URL: https://arxiv.org/abs/2011.04204

Siami studies a single-circuit interconnection with negative diagonal terms (a_i>0), coupling magnitudes (c_i>0), and the geometric ratio

[
gamma=
left(rac{prod_i c_i}{prod_i a_i}ight)^{1/n}.
]

His generalized fractional secant result gives a sufficient stability condition for the cyclic system and becomes necessary in a special uniform-coupling/equalized case. In the notation relevant to our project, the threshold is of the form

[
gamma<R_n(alpha)
=
rac{sin(alphapi/2)}
{sin(alphapi/2-pi/n)}
]

in the nontrivial regime (alpha>2/n), while the small-order regime is automatically stable for that structured family.

### Consequence for our diagonal orbit

For any positive diagonal left scaling (D=operatorname{diag}(d_i)), row (i) multiplies both the associated diagonal coefficient and outgoing cycle coefficient by (d_i). Therefore

[
gamma(DA)
=
left(
rac{(prod_i d_i)(prod_i c_i)}
     {(prod_i d_i)(prod_i a_i)}
ight)^{1/n}
=
gamma(A).
]

Thus Siami's sufficient condition is invariant over the full positive diagonal orbit.

Conversely, by choosing (d_i=k/a_i), one equalizes all diagonal magnitudes of (DA). Hence the special case in which Siami's criterion is necessary can be reached inside the same diagonal orbit. Subject to matching the precise sign convention of the cyclic family, this means that an exact theorem of the form

> "single-cycle fractional D-stability iff a fractional secant inequality holds"

is **corollary-level or near-corollary-level prior art**, not an acceptable central novelty claim.

### Decision

- "fractional secant criterion": **NOT NOVEL** as a title-level claim.
- "single-cycle characterization": **NOT APPROVED as novelty** without a theorem strictly beyond Siami.
- cactus/multi-cycle work may remain viable only if it is not reducible cycle-by-cycle to Siami + known diagonal-stability results.

---

## 3. Kushel / Kushel–Pavani: withdraw the claim that the non-convex Matignon region was untouched

Relevant references:

- O. Y. Kushel, *Unifying matrix stability concepts with a view to applications*, SIAM Review 61 (2019), arXiv:1907.07089.
- O. Y. Kushel & R. Pavani, *The problem of generalized D-stability in unbounded LMI regions and its computational aspects*, arXiv:2004.11172.
- O. Y. Kushel & R. Pavani, *Generalized D-stability and diagonal dominance with applications to stability and transient response properties of systems of ODE*, arXiv:2103.04127.
- O. Y. Kushel, *Some bounds for determinants of relatively D-stable matrices*, Linear Algebra Appl. 656 (2023), 9–26, arXiv:2205.10823.

URLs:
- https://arxiv.org/abs/1907.07089
- https://arxiv.org/abs/2004.11172
- https://arxiv.org/abs/2103.04127
- https://arxiv.org/abs/2205.10823

Kushel's ((mathfrak D,mathcal G,circ))-stability framework already allows arbitrary spectral regions and multiplier classes including positive diagonal matrices. Therefore (mathcal F_alpha) is an instance of an existing generalized D-stability concept.

More importantly, the previous baseline statement

> "all existing sufficient conditions use convex regions and are blind to the non-convex purely fractional sliver"

is too strong and is withdrawn.

Kushel–Pavani explicitly discuss the fractional-order stability set as the complement of a cone and note that this complement is not itself an LMI region. Their forbidden-boundary machinery treats rays/sectors under diagonal scaling and extends conceptually to complements. This does **not** provide the low-dimensional characterizations we seek, but it means that the geometry "non-convex Matignon complement + positive diagonal scaling" is not untouched territory.

Kushel 2023 additionally studies relatively D-stable matrices and sector gaps. This does not by itself settle (mathcal P_alpha), because its principal sector-gap results concern classes already controlled relative to the imaginary axis / left-half-plane-type sectors, but it removes novelty from generic phrases such as "uniform sector gap under positive diagonal scaling."

### Decision

What can still be novel is not the framework, but an **explicit exact characterization, dimension threshold, or structural separation theorem** for the genuinely non-Hurwitz part of (mathcal F_alpha).

---

## 4. Abed 1986 and later robust D-stability: "strong" is not a new concept

**Reference:** E. H. Abed, *Strong D-stability*, Systems & Control Letters 7(3) (1986), 207–212.  
DOI: https://doi.org/10.1016/0167-6911(86)90116-7

Abed defines a matrix as strongly D-stable when it is D-stable and every sufficiently small perturbation is also D-stable. Therefore an assertion of the form

[
existsarepsilon>0:
|E|<arepsilon
Longrightarrow
A+E 	ext{is D-stable}
]

is classical terminology and classical prior art at (alpha=1).

Additional relevant line:

- D. J. Hartfiel, *Concerning the interior of the D-stable matrices*, Linear Algebra Appl. (1980).
- B. E. Cain, low-dimensional / topological results for D-stability.
- J. Lee & T. F. Edgar, *Real structured singular value conditions for the strong D-stability*, Systems & Control Letters 44 (2001), 273–277.
- J.-P. Casasanta & J. W. Simpson-Porco, *A Lyapunov Characterization of Robust D-Stability with Application to Decentralized Integral Control of LTI Systems*, arXiv:2603.13608 (2026), giving necessary-and-sufficient Lyapunov-type conditions for robust classical D-stability.
  URL: https://arxiv.org/abs/2603.13608

Hence "strong fractional D-stability" is only potentially new if it is mathematically specialized to the Matignon sector and produces results not inherited from the classical robust-D-stability theory.

---

## 5. Exact (2	imes2) classification

Let

[
A=egin{pmatrix}a&b\c&dend{pmatrix},qquad
D=operatorname{diag}(x,y),quad x,y>0.
]

Then

[
operatorname{tr}(DA)=xa+yd,
qquad
det(DA)=xydet A.
]

### Proposition

For every (0<alpha<1),

[
oxed{
Ainmathcal F_alpha^{(2)}
iff
det A>0,quad ale0,quad dle0.
}
]

### Proof

**Sufficiency.** If (det A>0) and (a,dle0), then for every (x,y>0),

[
det(DA)>0,qquad operatorname{tr}(DA)le0.
]

If the eigenvalues are real, they are both negative. If they are nonreal, they are conjugate with nonpositive real part. Hence every eigenvalue satisfies

[
|arglambda|gepi/2>alphapi/2.
]

**Necessity.** If (det Ale0), then (DA) has a zero eigenvalue or a nonnegative real eigenvalue, violating Matignon stability. If (a>0), let (x/y	oinfty). The characteristic polynomial

[
lambda^2-(xa+yd)lambda+xydet A
]

eventually has a positive real root (indeed the dominant root behaves like (xa)); similarly, (d>0) is excluded by (y/x	oinfty).

Thus the equivalence holds.

### Classical D-stable subset

For the same (2	imes2) family, classical Hurwitz D-stability requires

[
det A>0,qquad ale0,qquad dle0,qquad (a,d)
eq(0,0).
]

Therefore

[
oxed{
mathcal P_alpha^{(2)}
=
left{
egin{pmatrix}0&b\c&0end{pmatrix}:bc<0
ight},
}
]

so

[
oxed{
operatorname{int}_{mathbb R^4}
mathcal P_alpha^{(2)}
=
arnothing.
}
]

**Proof status:** analytic, complete at the level above.  
**Novelty status:** useful structural proposition; prior-art search has not yet established it as title-level new and it should not carry the paper by itself.

---

## 6. (P)-matrix bridge and the dimension-three construction

A classical theorem of Kellogg states that if (Pinmathbb R^{n	imes n}) is a (P)-matrix, then every eigenvalue (mu) satisfies

[
|argmu|<pi-rac{pi}{n}.
]

Positive diagonal left scaling preserves the (P)-matrix property because each principal minor is multiplied by a positive product of diagonal entries.

Therefore:

### Lemma (Kellogg-to-Matignon bridge)

If (-A) is a (P)-matrix, then

[
Ainmathcal F_alpha^{(n)}
qquad
	ext{for every }0<alphalerac{2}{n}.
]

Indeed, for each (Dsucc0), (D(-A)) is again a (P)-matrix. Rotating its spectrum by (pi) gives

[
|arglambda(DA)|>rac{pi}{n}
ge
rac{alphapi}{2}.
]

This lemma itself is a short consequence of classical (P)-matrix spectral theory and must not be sold as the main novelty.

### Explicit (3	imes3) family

Define

[
A_gamma=
egin{pmatrix}
-1&0&-gamma\
gamma&-1&0\
0&gamma&-1
end{pmatrix},
qquad gamma>2.
]

All principal minors of (-A_gamma) are strictly positive:

- the three order-one minors equal (1);
- the three order-two principal minors equal (1);
- (det(-A_gamma)=1+gamma^3>0).

Hence (-A_gamma) is a (P)-matrix, so

[
A_gammainmathcal F_alpha^{(3)}
qquad
(0<alphale2/3).
]

But

[
sigma(A_gamma)
=
left{
-1-gamma,,
-1+rac{gamma}{2}
pm irac{sqrt3,gamma}{2}
ight},
]

and for (gamma>2) the complex pair has positive real part. Hence (A_gamma
otinmathcal D_H^{(3)}).

### Open-set strengthening

The (P)-matrix conditions for (-A_gamma) are strict polynomial inequalities in the entries, so they persist on a sufficiently small full-dimensional ball around (A_gamma). The positive spectral abscissa of (A_gamma) at (D=I) also persists under sufficiently small perturbations.

Thus there exists (arepsilon>0) such that

[
B_arepsilon(A_gamma)
subset
mathcal F_alpha^{(3)}
setminus
mathcal D_H^{(3)}
qquad
	ext{for every }0<alphale2/3.
]

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

Combined with the exact (n=1,2) analysis,

[
oxed{
min{n:
operatorname{int}mathcal P_alpha^{(n)}
eqarnothing}
=3
qquad
(0<alphale2/3).
}
]

**Proof status:** analytic derivation complete, assuming the standard Kellogg (P)-matrix wedge theorem.  
**Novelty status:** **STRONG NOVELTY CANDIDATE — NOT YET FROZEN**. Targeted searches found the ingredients separately, but not this minimal-dimension robust genuinely-fractional separation statement.

---

## 7. Why (2/3) is structural in the cubic problem

For a cubic with positive coefficients,

[
p(lambda)=lambda^3+alambda^2+blambda+c,
]

a root on the Matignon boundary (lambda=re^{i	heta}), paired with its conjugate and a third real root (-s), gives with (t=s/r),

[
a=r(t-2cos	heta),qquad
b=r^2(1-2tcos	heta),qquad
c=tr^3.
]

For (a,b>0), one needs

[
2cos	heta<t<rac{1}{2cos	heta}.
]

This interval exists exactly when

[
	heta>pi/3,
]

i.e.

[
alpha>rac23
quad	ext{when}quad
	heta=alphapi/2.
]

Thus (alpha=2/3) is not an artifact of the example; it is the natural cubic angular transition.

---

## 8. Highest-value open target: (n=3,;2/3<alpha<1)

For (2/3<alpha<1), the (P)-matrix wedge alone is insufficient. Siami nevertheless supplies structured cycle centers (A_gamma) with

[
2<gamma<R_3(alpha)
]

that are fractionally stable but classically unstable.

The unresolved issue is full-dimensional robustness:

[
oxed{
A_gammainoperatorname{int}mathcal F_alpha^{(3)} ?
}
]

A proof cannot invoke ordinary continuity alone because the diagonal orbit (Dsucc0), modulo scalar normalization, approaches degenerate faces where some diagonal ratios tend to (0) or (infty). The correct route is likely:

1. normalize the diagonal orbit to a compact simplex;
2. analyze all boundary faces via principal submatrices / limiting characteristic polynomials;
3. exclude contact with the two Matignon boundary rays;
4. derive an explicit cubic inequality, ideally the fractional analogue of Cain's (3	imes3) D-stability condition.

If successful, the desired global theorem becomes

[
oxed{
min{n:
operatorname{int}mathcal P_alpha^{(n)}
eqarnothing}=3
quad
orall,0<alpha<1.
}
]

This is currently the highest-value mathematical target.

---

## 9. Reopened-audit answers

1. **Does Siami quantify over the same (DA) orbit?** Not explicitly as the theorem statement, but its cycle ratio is invariant under all positive left-diagonal row scalings, and the orbit can equalize the diagonal parameters. Hence the proposed single-cycle D-orbit theorem is substantially subsumed.
2. **Can our single-cycle target be recovered from Siami?** Yes, to a dangerous degree; treat it as prior art/corollary unless a genuinely stronger statement is proved.
3. **Does Siami reach the RHP Matignon sliver?** Yes, fractional stability of a classically unstable cycle is permitted for suitable (alpha<1); the theorem is not confined to Hurwitz matrices.
4. **Relationship of Kushel relative D-stability to (Sigma_alpha)?** Generalized/relative D-stability supplies the ambient framework; sector and forbidden-boundary results overlap the angular geometry but do not give our low-dimensional (mathcal P_alpha) characterization.
5. **Does Kushel already give a proposed generic uniform sector-gap theorem?** Sector-gap estimates exist for important D-stable subclasses. Therefore "uniform angular margin" alone is not a novelty claim.
6. **Which topology claims survive Siami?** Not single-cycle secant. Potential survivors: dimension-threshold theorem, multi-cycle/cactus results strictly beyond cyclewise Siami, or minimal motifs explaining full-dimensional robust separation.
7. **Is the (2	imes2) classification immediate?** It is elementary from trace/determinant scaling and is now analytically proved in this audit; its independent novelty remains secondary.
8. **Is (operatorname{int}mathcal P_alpha
eqarnothing) possible in dimension 3?** Yes, analytically for (0<alphale2/3), via the (P)-matrix construction above. The range (2/3<alpha<1) remains open.
9. **How must strong fractional D-stability differ from Abed?** It must concern the Matignon angular region and yield a non-Hurwitz robust class not reducible to classical strong D-stability.
10. **Smallest title-worthy package now visible?** Exact (2	imes2) obstruction + dimension-three full-dimensional separation + extension to all (0<alpha<1), preferably accompanied by an exact (3	imes3) criterion or minimal motif theorem.

---

## 10. Current verdict

**GO-NARROWED — AUDIT STILL OPEN.**

The baseline graph/cactus theorem should not be the immediate proof target. The project should first close the low-dimensional program:

- (n=2): exact classification — analytically closed here;
- (n=3,;0<alphale2/3): full-dimensional robust separation — analytically closed here modulo imported Kellogg theorem;
- (n=3,;2/3<alpha<1): **OPEN / highest priority**;
- only after that: identify the motif mechanism and generalize structurally.

No manuscript should claim final novelty until the (3	imes3) high-order range has either been proved or shown impossible and this reopened literature audit is frozen.
