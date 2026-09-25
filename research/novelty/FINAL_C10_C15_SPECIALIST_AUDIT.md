# Final specialist novelty audit — C-09 / C-10 / C-15 / C-16

**Date:** 2026-09-25  
**Branch:** `agent/final-novelty-c10-c15-20260925`  
**Role:** adversarial Final Novelty / Web Searcher  
**Scope:** bibliographic novelty only; no manuscript drafting  
**Search horizon:** literature located through 2026-09-25

## Executive decision

| Claim | Final verdict | What survives |
|---|---|---|
| C-09 — minimum dimension for robust genuinely fractional multiplicative D-stability | **NOVEL WITH NARROWED CLAIM** | The exact full-dimensional-interior threshold statement, not the generic fact that fractional systems can be stable while integer-order systems are unstable |
| C-10 — exact real 3×3 Matignon D-orbit threshold | **NOVEL WITH NARROWED CLAIM** | The explicit elimination of the complete positive-diagonal orbit to four invariants and the scalar threshold κ < T_α(β), not generalized D-stability, forbidden-boundary theory, fixed-cubic sector stability, or homogeneous D-orbit minimization |
| C-15 — geometry of T_α | **NOVEL WITH NARROWED CLAIM** | Strict convexity / unique nondegenerate minimizer / smooth threshold geometry of this specific fractional threshold functional; generic logit, log-sum-exp, convexity and geometric-programming machinery are not novel |
| C-16 — general simplex reduction | **NOT NOVEL** | Keep as a structural lemma / normalization device. It is a direct consequence of the standard principal-minor formula for characteristic-polynomial coefficients plus positive projective normalization |

**Overall:** **NOVELTY GATE PASSED WITH REPOSITIONING**

The central package survives, but the wording must be narrower than the current intuitive story. The strongest new object is not “fractional D-stability” and not even “a necessary-and-sufficient criterion” in the abstract. Kushel–Pavani already provide a necessary-and-sufficient forbidden-boundary criterion for multiplicative generalized D-stability in a conic region or its complement. The surviving C-10 contribution is an explicit low-dimensional solution of that quantified problem: on the strict-P(-A) real 3×3 stratum, all positive diagonal multipliers are eliminated exactly and the result becomes κ < T_α(β).

---

# 1. Exact audited objects

For 0 < α < 1 let θ = απ/2 and

```text
Σ_α = { z ≠ 0 : |arg z| > θ }.

F_α^(n) = { A ∈ R^(n×n) : σ(DA) ⊂ Σ_α for every positive diagonal D }.

P_α^(n) = F_α^(n) \ D_H^(n).
```

C-10 works on the strict-P(-A) real 3×3 stratum. With

```text
p_i   = -a_ii > 0
m_ij  = det A[{i,j}] > 0
q     = -det A > 0

β_ij  = m_ij/(p_i p_j)
κ     = q/(p_1 p_2 p_3)
```

and normalized diagonal coordinates

```text
x_i = p_i d_i / a_D,
x_i > 0,
x_1+x_2+x_3 = 1,
```

the characteristic cubic is normalized to

```text
z^3 + z^2 + B_β(x) z + κ x_1 x_2 x_3,

B_β(x) = β_12 x_1x_2 + β_13 x_1x_3 + β_23 x_2x_3.
```

For 2/3 < α < 1 the project theorem is

```text
A ∈ F_α^(3)  iff  κ < T_α(β),

T_α(β)
 = min_{x in open simplex}
   h_α(B_β(x))/(x_1 x_2 x_3).
```

C-15 proves strict convexity in logit coordinates, uniqueness and nondegeneracy of the minimizer, smooth parameter dependence, the symmetric Siami slice, the α→1 Cain limit, and the low-order threshold geometry.

C-16 states the analogous principal-minor/simplex quotient for general n.

---

# 2. The strongest prior-art threat: Kushel–Pavani 2020/2022

## 2.1 Exact overlap

Kushel–Pavani define multiplicative (𝔇,D)-stability by the same quantifier structure:

```text
σ(DA) ⊂ 𝔇 for every positive diagonal D.
```

Their Theorem 3.1 is a general forbidden-boundary theorem: region D-stability is equivalent to initial region stability plus exclusion of the region boundary throughout the diagonal orbit.

More importantly, their Theorem 3.3 gives equivalent necessary-and-sufficient conditions for conic relative D-stability **and for the complement of the closed conic sector**. One equivalent condition is

```text
det(A - zD) ≠ 0 and det(A - conjugate(z)D) ≠ 0
for every positive diagonal D,
```

with z on the sector boundary ray.

This is not merely “related framework”. After the sign change B = -A, it is the abstract generalized-D-stability problem underlying the α<1 Matignon region:

- Σ_α is the complement of the closed positive cone of half-angle θ = απ/2;
- multiplying the spectrum by -1 turns that positive cone into the negative cone C^-_θ;
- hence A ∈ F_α iff -A is multiplicatively D-stable with respect to the complement of that negative cone, with boundary conventions handled by the strict inequalities.

Therefore:

> **C-10 is NOT the first necessary-and-sufficient theorem for the quantified sector/complement D-stability problem.**

That claim would be false.

## 2.2 What Kushel–Pavani do not provide

Their theorem retains the universal multiplier quantifier. It does not derive, for real 3×3 matrices,

- the four orbit invariants (β_12,β_13,β_23,κ);
- the projective-simplex representation of all positive D;
- the exact cubic boundary function h_α;
- the variational scalar threshold T_α(β);
- the iff inequality κ < T_α(β);
- the exact fractional-only band T_1(β) < κ < T_α(β);
- the C-15 convex geometry of T_α.

Thus C-10 should be positioned as:

> **an explicit exact real-3×3 elimination / solution of the generalized forbidden-boundary problem for the Matignon reflex sector on the strict-P(-A) stratum.**

This is a materially narrower and more defensible claim.

---

# 3. Cain 1976: the α=1 optimization mechanism is prior art

Cain's primary 1976 paper gives a complete characterization of real 3×3 classical D-stable matrices.

Using his positive-stability sign convention, write the order-one principal minors as a,b,c, order-two principal minors as A,B,C, determinant δ, and

```text
Δ = sqrt(aA) + sqrt(bB) + sqrt(cC).
```

Cain proves D-stability iff the sign conditions hold and the determinant satisfies δ ≤ Δ² or δ < Δ² depending on his boundary type.

The proof is directly relevant to C-10. For D = diag(x,y,z), Routh–Hurwitz produces the all-D inequality

```text
(ax+by+cz)(Ayz+Bxz+Cxy) - xyz δ > 0.
```

Cain then minimizes the homogeneous ratio

```text
f(x,y,z)
 = (ax+by+cz)(Ayz+Bxz+Cxy)/(xyz)
```

over x,y,z>0 and proves that its infimum is Δ².

This means the following ideas are **not novel**:

1. encoding the diagonal orbit through principal minors;
2. exploiting homogeneity to remove a common scale;
3. optimizing a scalar expression over positive diagonal multipliers;
4. obtaining an exact determinant threshold in dimension three.

At α=1, C-10 must explicitly be presented as recovering Cain, not independently rediscovering this mechanism.

The surviving novelty is the non-Hurwitz angular deformation for 2/3<α<1, where the fixed-cubic Matignon boundary modifies the objective and the exact all-D threshold becomes T_α(β).

---

# 4. Bahl–Cain 1977: close, but inertia does not imply C-10

Bahl and Cain characterize, for every inertia triple (r,s,t) with r+s+t=3, the real 3×3 matrices M whose MD has that fixed inertia for every positive diagonal D. Their conditions are algebraic conditions on principal minors.

This is a very close predecessor because it is:

- exact;
- real 3×3;
- quantified over every positive diagonal multiplier;
- expressed through principal minors.

However inertia records only counts of roots in the left half-plane, right half-plane and imaginary axis. It does not record the eigenvalue argument inside a half-plane.

C-10 specifically allows the genuinely fractional right-half-plane sliver

```text
απ/2 < |arg λ| ≤ π/2,
```

and distinguishes eigenvalues in that sliver from eigenvalues nearer the positive real axis. Two matrices can therefore have the same inertia and different Matignon status.

**Conclusion:** C-10 is not Bahl–Cain with a notational substitution “inertia → angle”. A new angular boundary calculation is genuinely required.

---

# 5. Kushel 2016 D_theta-stability is a false terminology collision

A targeted search found Olga Kushel, *On a criterion of D-stability for P-matrices* (2016), which at first sight is dangerous because it introduces “D_theta-stability”.

Primary-text verification resolves the ambiguity:

- theta is a **permutation/order of indices**;
- a positive diagonal D is theta-ordered if its diagonal entries satisfy the corresponding monotone order;
- A is D_theta-stable if DA is stable for every theta-ordered D.

It is **not** angular sector stability and theta is not a spectral angle.

The paper proves criteria for classical positive/Hurwitz D-stability of P-matrices and is relevant background, but it does not kill C-10 or C-15.

---

# 6. Fixed-polynomial sector stability is prior art

Several literature lines already occupy the fixed-polynomial component of the proof.

## 6.1 Joya–Furuta 1991

They define a polynomial as D-stable when all roots lie in a prescribed domain D and derive explicit coefficient-space descriptions when D is a convex domain whose boundary is a conic section or a sector.

This is **polynomial D-region stability**, not multiplicative matrix D-stability.

## 6.2 Čermák–Nechvátal 2017

They develop fractional Routh–Hurwitz conditions in the Lorenz-system setting. This is fixed-system / fixed-characteristic-polynomial root localization.

## 6.3 Bourafa–Abdelouahab–Moussaoui 2020

They extend fractional Routh–Hurwitz conditions to α in (0,2), including low-dimensional cases and coefficient criteria.

## 6.4 Holtz–Khrushchev–Kushel 2016

They prove forbidden-sector results for positive-coefficient polynomials from generalized Hurwitz matrices.

### Consequence for C-10

The function h_α for one normalized cubic should **not** be advertised as a standalone novelty result without a separate theorem-by-theorem priority proof. For publication positioning, treat the fixed-cubic angular boundary as a solved or heavily occupied component.

What survives is the composition:

```text
fixed cubic Matignon boundary
+ full positive-diagonal matrix orbit
+ principal-minor invariants
+ exact elimination of D
= C-10.
```

---

# 7. Fractional papers using “D-stability”: terminology audit

## 7.1 Mohsenipour–Liu 2020 — verified

Their “robust D-stability” is root localization of uncertain fractional closed-loop characteristic equations in a desired D-region. Their abstract explicitly describes uncertain polynomial coefficients/orders, value sets, and root areas.

There is no positive-diagonal matrix-multiplier quantifier of the project form.

**Verdict:** terminology collision only.

## 7.2 Shao et al. 2017 — primary text not retrievable here

Citation:

Keyong Shao, Lipeng Zhou, Kun Qian, Yeqiang Yu, Feng Chen, Shuang Zheng, “Necessary and sufficient D-stability condition of fractional-order linear systems,” 36th Chinese Control Conference (2017), pp. 44–48, DOI 10.23919/ChiCC.2017.8027318.

The IEEE proceedings record is verified, but the article body was not retrievable from the accessible web endpoint during this audit.

Every accessible citation context places it in the control-theoretic **D-region / pole-placement** tradition, and Kushel–Pavani cite it in their fractional-order-system discussion rather than as multiplicative matrix D-stability. Mohsenipour–Liu 2020 provides primary accessible confirmation that this terminology is used in that sense.

**Residual bibliography flag:** obtain the Shao PDF before journal submission if possible.  
**Gate effect:** non-load-bearing; it does not force an incomplete overall audit because no accessible evidence indicates the all-positive-diagonal multiplier quantifier and the later primary literature clarifies the terminology.

---

# 8. Siami 2020/2021: exact structured slice, not the general C-10 theorem

Siami's Theorem 2 studies a single-circuit commensurate fractional network. With geometric means a and c, and γ=c/a, it proves:

- automatic stability for α ≤ 2/n;
- for α > 2/n, the generalized secant sufficient condition
  γ < sin(απ/2)/sin(απ/2 - π/n);
- necessity when the diagonal coefficients a_i are identical.

For the project symmetric 3-cycle, C-10/C-15 recovers this threshold.

The key question is whether hidden scaling or similarity can force every C-10 matrix into that symmetric slice.

It cannot:

- positive left diagonal scaling preserves β_ij and κ;
- diagonal similarity also preserves principal minors and therefore the β_ij and κ invariants;
- permutation similarity only permutes the β triple;
- the single-cycle sparsity structure imposes β=(1,1,1), whereas the general strict-P(-A) stratum has nontrivial β triples.

Therefore Siami occupies exactly the symmetric structured slice but does not exhaust C-10.

---

# 9. C-15 threshold geometry

## 9.1 Search result

Targeted searches were performed around:

- D-stability + logit coordinates;
- D-stability + log-sum-exp;
- geometric programming + diagonal multipliers;
- simplex convexity + principal minors;
- sector D-stability + unique optimizer;
- fractional D-stability + convex threshold surface.

No source was located that proves the C-15 package for T_α:

- strict convexity of the log-threshold objective in logit coordinates;
- unique interior minimizer for arbitrary positive β;
- nondegenerate Hessian;
- smooth dependence of the minimizer / threshold on β;
- the exact global threshold-surface parametrization.

## 9.2 What is standard and must not be claimed

The following tools are standard:

- softmax/logit parametrization of the simplex;
- convexity of log-sum-exp;
- geometric-programming conversion of positive monomials/posynomials;
- envelope/implicit-function arguments after strict nondegeneracy.

The novelty claim must therefore be theorem-specific:

> the C-15 threshold functional arising from the exact fractional 3×3 D-orbit problem has this strict global convex geometry.

The symmetric β=(b,b,b) case is not independently novel: it interfaces directly with Siami. The α=1 endpoint is constrained by Cain.

### C-15 verdict

**NOVEL WITH NARROWED CLAIM.**

---

# 10. C-16 general simplex reduction

C-16 states for strict-P(-A) in dimension n:

```text
c_k(D) = Σ_{|I|=k} m_I Π_{i∈I} d_i,
```

followed by

```text
s = c_1(D),
x_i = p_i d_i / s,
Σ x_i = 1,
```

and normalized coefficient polynomials B_k(x).

This is mathematically useful, but it is not a defensible standalone novelty claim.

The core inputs are standard:

1. the coefficient of λ^(n-k) in det(λI-A) is the signed sum of k×k principal minors;
2. left diagonal multiplication multiplies principal minor I by Π_{i∈I} d_i;
3. a positive diagonal vector modulo a common positive scalar is a point of the positive projective simplex.

Kinkhabwala's network-stability treatment explicitly writes characteristic coefficients in terms of principal minors and principal minors in terms of cycle products. The modern principal-minor-map literature likewise treats det(diag(x)+A) as the determinantal polynomial encoding principal minors.

No special fractional theorem is needed to obtain C-16.

### C-16 verdict

**NOT NOVEL.**

**Exact implication:** the standard characteristic-polynomial/principal-minor coefficient identity, applied to DA, yields the displayed c_k(D) formula; homogeneity of degree k under D and the substitution x_i=p_i d_i/Σ_j p_j d_j yield the simplex statement directly. C-16 should remain a named structural lemma for reuse, with no priority language.

---

# 11. C-09 minimum-dimension theorem

C-09 states, precisely,

```text
min { n : int(F_α^(n) \ D_H^(n)) ≠ empty } = 3
for every 0 < α < 1.
```

No located prior result combines all six essential qualifiers:

1. multiplicative positive-diagonal orbit;
2. full Matignon region for α<1;
3. genuine separation from classical Hurwitz D-stability;
4. full-dimensional interior in the ambient real matrix space;
5. exact lower-dimensional obstruction;
6. all 0<α<1.

The ingredients are individually prior art:

- Matignon sector;
- Kellogg P-matrix wedge;
- classical D-stability;
- robust/interior D-stability;
- Siami cyclic fractional condition;
- fixed-cubic fractional Routh–Hurwitz.

But none of the audited papers implies the dimension theorem.

In particular, Siami supplies a structured cycle family, not a full-dimensional ambient open set. Cain/Hartfiel/Abed address α=1 and therefore cannot produce the genuinely fractional non-Hurwitz interior. Kushel–Pavani supplies the generalized quantified framework but not the dimension threshold.

### Required narrowing

Do not shorten C-09 to:

> “dimension three is the first dimension with fractional stabilization.”

That would be false/misleading: dimension two already has lower-dimensional genuinely fractional examples.

The title-level statement must preserve **nonempty full-dimensional interior of the genuinely non-Hurwitz multiplicative D-stable class**.

### C-09 verdict

**NOVEL WITH NARROWED CLAIM.**

---

# 12. Ecology / C-13 cross-check

Classical ecology and network stability already connect:

- community matrices and local stability;
- characteristic coefficients to principal minors;
- principal minors to signed non-overlapping feedback cycles;
- low-dimensional three-species stability to Routh–Hurwitz-type conditions.

Clark–Hallam (1982) studied exact three-species community-matrix stability at integer order. Kinkhabwala (2015) explicitly develops principal-minor / cycle decompositions and reduced stability coordinates.

Therefore the generic statements

> “loops determine stability”  
> “principal minors correspond to feedback motifs”

are not novel.

What remains new, conditional on C-10, is the **exact fractional all-positive-diagonal threshold written in ecological loop coordinates**, together with the particular GLV abundance-row-scaling invariance inherited from the C-10 orbit.

C-13 should remain an interpretation/application theorem, not an independent priority claim.

---

# 13. Current 2026 literature sweep

## 13.1 Kushel 2026

Olga Kushel's 2026 preprint *Recursive determinantal framework for testing D-stability. I* develops a delete/zero recursion and sufficient classical D-stability tests expressed through principal minors.

It is highly relevant methodologically, but it does not subsume C-10/C-15:

- target region: classical half-plane;
- result type: hierarchy of sufficient conditions;
- no exact 3×3 Matignon-reflex-sector threshold;
- no T_α(β);
- no C-15 strict-convex threshold geometry.

## 13.2 Ahmadieh 2026

Abeer Al Ahmadieh studies fibers of the principal-minor map and diagonal equivalence. This confirms that principal-minor coordinates and diagonal-equivalence questions are active standard matrix theory.

Its “diagonal equivalence” is similarity-type equivalence (A=DBD^{-1}, or transpose variant), not the project's positive **left multiplication** orbit DA.

It does not imply C-10.

## 13.3 No 2025–2026 kill found

The current-literature sweep did not locate a paper that gives the same real-3×3 exact Matignon multiplicative-D threshold or the C-15 threshold geometry.

---

# 14. Required falsification questions — final answers

## Q1. Is C-10 already Bahl–Cain after replacing inertia by an angular condition?

**No.** Bahl–Cain fixes half-plane inertia under all D. Angular position within a half-plane is invisible to inertia, while C-10 must separate the Matignon-stable RHP sliver from the forbidden positive wedge. The quantifier structure overlaps strongly; the conclusion does not.

## Q2. Is T_α equivalent to a known relative-D-stability determinant bound?

**No equivalence located.** Kushel 2023 gives sufficient relative-D-stability conditions, determinant upper bounds, and sector-gap estimates for selected D-stable classes. It does not give the exact real-3×3 invariant threshold T_α(β). However, Kushel–Pavani Theorem 3.3 is an exact **abstract** forbidden-boundary criterion for the same sign-transformed generalized-D-stability problem. C-10 must be described as explicit elimination of that abstract condition.

## Q3. Is C-15 strict convexity/logit geometry already a D-stability or geometric-programming theorem?

**Not located.** Generic logit/log-sum-exp and GP convexity are standard. The potentially novel result is strict convexity and uniqueness for the specific T_α objective, not the coordinate transform.

## Q4. Is C-16 standard enough to be a lemma rather than novelty?

**Yes.** Final verdict: NOT NOVEL. It is a direct corollary of the standard principal-minor coefficient identity plus homogeneous/projective normalization.

## Q5. Is there already an exact N&S 3×3 positive-diagonal sector-stability theorem?

**There is an exact general N&S boundary criterion, but no explicit C-10 elimination located.** Kushel–Pavani Theorem 3.3 handles all n abstractly via determinant nonvanishing for every D. Cain solves the α=1 real-3×3 half-plane case explicitly. No audited source supplies the intermediate α-dependent real-3×3 κ<T_α(β) solution.

## Q6. Does prior work handle the nonconvex α<1 Matignon region including the RHP sliver?

**Yes at the framework / root-region level; no exact matrix-orbit elimination located.** It is incorrect to say the region itself was untouched. Fractional control papers explicitly use the nonconvex Matignon domain, and after sign reversal Kushel–Pavani's complement-of-cone theorem is directly applicable abstractly.

## Q7. Do fractional “D-stability” papers use ∀D>0 matrix multipliers?

**Mohsenipour–Liu: no; D means desired root region. Shao 2017: primary body not retrieved, but all accessible context points to D-region/pole-location usage.** This terminology must be disambiguated in the paper.

## Q8. Is C-09 immediate from a published theorem?

**No.** No audited theorem implies the full-dimensional-interior minimum-dimension statement for all 0<α<1.

## Q9. Does Siami's symmetric slice exhaust C-10 under hidden similarity/scaling?

**No.** β and κ are invariant under the relevant positive row scalings; principal minors are also invariant under diagonal similarity. Siami's cycle sparsity gives β=(1,1,1); generic C-10 β cannot be transformed to that value except on the corresponding invariant slice.

## Q10. Is the ecological loop form C-13 already known under other notation?

**The loop/principal-minor dictionary is classical; the exact fractional all-D inequality is not located independently of C-10.** Position C-13 as an interpretation/application of C-10, not as generic loop novelty.

---

# 15. Claim language approved for a future manuscript

## C-09 approved wording

> We identify the minimum matrix dimension in which the genuinely fractional multiplicative-D-stable class has nonempty full-dimensional interior, and prove that it is three for every 0<α<1.

Always retain “genuinely fractional”, “multiplicative D-stable”, and “full-dimensional interior”.

## C-10 approved wording

> For real 3×3 matrices on the strict-P(-A) stratum, we explicitly eliminate the complete positive-diagonal multiplier orbit from the Matignon generalized-D-stability problem, obtaining a necessary-and-sufficient four-invariant threshold κ<T_α(β).

Do **not** say “first necessary-and-sufficient criterion for fractional D-stability”; Kushel–Pavani already have an abstract N&S forbidden-boundary criterion.

## C-15 approved wording

> We prove that the specific threshold functional T_α generated by the exact 3×3 Matignon D-orbit problem has a strictly convex logit representation, a unique nondegenerate optimizer, and a smooth global threshold geometry.

Do not claim logit or convex optimization methodology itself.

## C-16 approved wording

> Structural normalization lemma; no novelty claim.

---

# 16. Publication-risk ranking

| Risk | Severity | Required mitigation |
|---|---:|---|
| Referee says “Kushel–Pavani already gave N&S generalized D-stability” | **HIGH** | Cite Theorem 3.3 explicitly and state that C-10's novelty is exact 3×3 elimination of the universal-D condition |
| Referee says “Cain already minimized over D in 3×3” | **HIGH** | Present Cain as the α=1 endpoint and acknowledge the homogeneous optimization template |
| Referee says “fixed cubic fractional RH is known” | **HIGH** | Treat h_α as component machinery, not flagship novelty |
| Referee says “Siami already has the threshold” | **MEDIUM-HIGH** | Show invariant β: Siami is β=(1,1,1), C-10 permits arbitrary realizable positive β |
| Referee says “C-16 is elementary” | **CERTAIN** | Agree; demote to structural lemma |
| Shao 2017 definition ambiguity | **LOW-MEDIUM** | Obtain full text before submission if possible; current accessible evidence points to D-region terminology |
| Older obscure exact sector-D 3×3 theorem not indexed | **RESIDUAL** | No hit after targeted theorem-level search; cite the final bibliography audit and keep priority wording precise |

---

# 17. Final gate

## Claim verdicts

- **C-09: NOVEL WITH NARROWED CLAIM**
- **C-10: NOVEL WITH NARROWED CLAIM**
- **C-15: NOVEL WITH NARROWED CLAIM**
- **C-16: NOT NOVEL**

## Overall verdict

# **NOVELTY GATE PASSED WITH REPOSITIONING**

No exact prior theorem was located that implies C-09, C-10's explicit κ<T_α(β) elimination, or C-15's threshold geometry.

The package is publishable from a novelty-positioning standpoint only if it is framed as:

```text
classical generalized-D framework
+ known fixed-sector cubic machinery
+ known α=1 Cain endpoint
        ↓
new explicit 3×3 Matignon orbit elimination (C-10)
+ new exact dimension-interior consequence (C-09)
+ new threshold geometry (C-15)
```

C-16 is supporting algebra, not a contribution.

---

## References and verification

See `research/novelty/FINAL_BIBLIOGRAPHY_VERIFICATION.md` for source-by-source verification status, exact theorem relevance, DOI/URLs, and unresolved access flags.
