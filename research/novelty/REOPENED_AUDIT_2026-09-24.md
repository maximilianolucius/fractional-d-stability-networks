# Reopened novelty audit — 2026-09-24

**Role:** independent web-search / theorem-level prior-art audit  
**Status:** ACTIVE RESEARCH RECORD  
**Controlling direction:** `research/CHIEF_RESEARCH_DIRECTION_2026-09-24.md`

This note supersedes the over-broad conclusions of the baseline audit at commit `0b3b4df394eceec0dc9951a33fda01560de2f731` wherever they conflict with the findings below.

## 1. Central objects

For 0 < α < 1 define

```text
Σ_α = { z ≠ 0 : |arg z| > απ/2 }

F_α^(n) = { A ∈ R^(n×n) : σ(DA) ⊂ Σ_α for every positive diagonal D }

P_α^(n) = F_α^(n) \ D_H^(n)
```

where D_H^(n) is the classical Hurwitz D-stable class.

Definitions alone are not contributions. The novelty target is exact structural mathematics for the genuinely non-Hurwitz part P_α^(n).

---

## 2. Siami 2020/2021: the single-cycle target is substantially occupied

**Reference:** Milad Siami, *Stability and Robustness Analysis of Commensurate Fractional-order Networks*, arXiv:2011.04204; later IEEE TCNS.  
URL: https://arxiv.org/abs/2011.04204

Siami studies a single-circuit interconnection with negative diagonal terms a_i > 0, coupling magnitudes c_i > 0, and geometric ratio

```text
γ = ( Π_i c_i / Π_i a_i )^(1/n).
```

His generalized fractional secant result gives a sufficient stability condition for the cyclic system and becomes necessary in a special uniform/equalized case. In the notation relevant here, the nontrivial threshold has the form

```text
γ < R_n(α)
R_n(α) = sin(απ/2) / sin(απ/2 - π/n)
```

when α > 2/n; the small-order regime is automatically stable for that structured family.

### Consequence for the positive diagonal orbit

For D = diag(d_i) > 0, row i multiplies both the associated diagonal coefficient and outgoing cycle coefficient by d_i. Therefore

```text
γ(DA)
= [ (Π_i d_i)(Π_i c_i) / ((Π_i d_i)(Π_i a_i)) ]^(1/n)
= γ(A).
```

Thus Siami's sufficient condition is invariant over the full positive diagonal orbit.

Conversely, choosing d_i = k/a_i equalizes all diagonal magnitudes of DA. Hence the special case in which Siami's criterion is necessary can be reached inside the same diagonal orbit. Subject to matching the exact sign convention of the family, a theorem of the form

> single-cycle fractional D-stability iff a fractional secant inequality holds

is corollary-level or near-corollary-level prior art.

### Decision

- "fractional secant criterion": **NOT NOVEL** as a title-level claim.
- "single-cycle characterization": **NOT APPROVED as novelty** without a theorem strictly beyond Siami.
- cactus/multi-cycle work remains viable only if it is not reducible cycle-by-cycle to Siami plus known diagonal-stability results.

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

Kushel's generalized stability framework already permits arbitrary spectral regions and multiplier classes including positive diagonal matrices. Therefore F_α is an instance of an existing generalized D-stability concept.

The previous baseline statement

> all existing sufficient conditions use convex regions and are blind to the non-convex purely fractional sliver

is too strong and is withdrawn.

Kushel–Pavani explicitly discuss the fractional-order stability set as the complement of a cone and note that the complement is not itself an LMI region. Their forbidden-boundary machinery treats sector/ray boundaries under diagonal scaling and extends conceptually to complements. This does **not** provide the low-dimensional characterizations sought here, but it means that the geometry "non-convex Matignon complement + positive diagonal scaling" is not untouched territory.

Kushel 2023 additionally studies relatively D-stable matrices and sector gaps. It does not by itself settle P_α, but it removes novelty from generic phrases such as "uniform sector gap under positive diagonal scaling."

### Decision

What can still be new is not the framework, but an **explicit exact characterization, dimension threshold, or structural separation theorem** for the genuinely non-Hurwitz portion of F_α.

---

## 4. Abed 1986 and later robust D-stability: "strong" is not a new concept

**Reference:** E. H. Abed, *Strong D-stability*, Systems & Control Letters 7(3) (1986), 207–212.  
DOI: https://doi.org/10.1016/0167-6911(86)90116-7

Abed defines a matrix as strongly D-stable when it is D-stable and every sufficiently small perturbation is also D-stable.

Additional relevant line:

- D. J. Hartfiel, *Concerning the interior of the D-stable matrices*, Linear Algebra Appl. (1980).
- Classical low-dimensional D-stability work of B. E. Cain.
- J. Lee & T. F. Edgar, *Real structured singular value conditions for the strong D-stability*, Systems & Control Letters 44 (2001), 273–277.
- J.-P. Casasanta & J. W. Simpson-Porco, *A Lyapunov Characterization of Robust D-Stability with Application to Decentralized Integral Control of LTI Systems*, arXiv:2603.13608 (2026).
  URL: https://arxiv.org/abs/2603.13608

Hence "strong fractional D-stability" is only potentially new if it is specialized to the Matignon angular region and produces results not inherited from classical robust-D-stability theory.

---

## 5. Exact 2×2 classification

Let

```text
A = [[a,b],[c,d]]
D = diag(x,y),  x,y > 0.
```

Then

```text
tr(DA)  = xa + yd
det(DA) = xy det(A).
```

### Proposition

For every 0 < α < 1,

```text
A ∈ F_α^(2)   iff   det(A) > 0,  a ≤ 0,  d ≤ 0.
```

### Proof

**Sufficiency.** If det(A) > 0 and a,d ≤ 0, then for every x,y > 0,

```text
det(DA) > 0
tr(DA) ≤ 0.
```

If the eigenvalues are real they are both negative; if they are nonreal they form a conjugate pair with nonpositive real part. Hence every eigenvalue satisfies

```text
|arg λ| ≥ π/2 > απ/2.
```

**Necessity.** If det(A) ≤ 0, then DA has a zero eigenvalue or a nonnegative real eigenvalue. If a > 0, let x/y → ∞; the dominant eigenvalue becomes positive. Similarly, d > 0 is excluded by y/x → ∞.

Thus the equivalence holds.

### Classical D-stable subset

Classical Hurwitz D-stability additionally requires (a,d) ≠ (0,0). Therefore

```text
P_α^(2) = { [[0,b],[c,0]] : bc < 0 }.
```

Hence

```text
int_R4 P_α^(2) = ∅.
```

**Proof status:** analytic, complete at the level above.  
**Novelty status:** useful structural proposition; independent novelty remains secondary.

---

## 6. P-matrix bridge and dimension-three construction

A classical theorem of Kellogg states that if P ∈ R^(n×n) is a P-matrix, every eigenvalue μ satisfies

```text
|arg μ| < π - π/n.
```

Positive diagonal left scaling preserves the P-matrix property because each principal minor is multiplied by a positive product of diagonal entries.

Therefore:

### Lemma — Kellogg-to-Matignon bridge

If -A is a P-matrix, then

```text
A ∈ F_α^(n)   for every   0 < α ≤ 2/n.
```

Indeed, D(-A) is again a P-matrix for every D > 0. Rotating the spectrum by π gives

```text
|arg λ(DA)| > π/n ≥ απ/2.
```

This lemma is a short consequence of classical P-matrix theory and is not the main novelty.

### Explicit 3×3 family

Define

```text
A_γ = [ [-1, 0, -γ],
        [ γ,-1,  0],
        [ 0, γ, -1] ],   γ > 2.
```

All principal minors of -A_γ are strictly positive:

- all order-one principal minors equal 1;
- all order-two principal minors equal 1;
- det(-A_γ) = 1 + γ^3 > 0.

Hence -A_γ is a P-matrix, so

```text
A_γ ∈ F_α^(3)   for every   0 < α ≤ 2/3.
```

The spectrum is

```text
σ(A_γ) =
{ -1-γ,
  -1+γ/2 + i(√3 γ/2),
  -1+γ/2 - i(√3 γ/2) }.
```

For γ > 2, the complex pair has positive real part. Therefore A_γ is not Hurwitz at D = I and hence A_γ ∉ D_H^(3).

### Open-set strengthening

The strict P-matrix inequalities for -A_γ are strict polynomial inequalities in the matrix entries, so they persist on a sufficiently small full-dimensional ball around A_γ. The positive spectral abscissa at D = I also persists under sufficiently small perturbations.

Thus there exists ε > 0 such that

```text
B_ε(A_γ) ⊂ F_α^(3) \ D_H^(3)
```

for every 0 < α ≤ 2/3. Therefore

```text
int P_α^(3) ≠ ∅   for 0 < α ≤ 2/3.
```

Combined with the n = 1 and n = 2 analysis,

```text
min { n : int P_α^(n) ≠ ∅ } = 3
for every 0 < α ≤ 2/3.
```

**Proof status:** analytic derivation complete, assuming the standard Kellogg P-matrix wedge theorem.  
**Novelty status:** **STRONG NOVELTY CANDIDATE — NOT YET FROZEN**. Targeted searches found the ingredients separately, but not this minimal-dimension robust genuinely-fractional separation statement.

---

## 7. Why 2/3 is structural in the cubic problem

For a cubic with positive coefficients

```text
p(λ) = λ^3 + a λ^2 + b λ + c,
```

suppose a conjugate pair lies on the boundary λ = r exp(±iθ), while the third root is -s. Let t = s/r. Matching coefficients gives

```text
a = r (t - 2 cos θ)
b = r^2 (1 - 2 t cos θ)
c = t r^3.
```

For a,b > 0 one needs

```text
2 cos θ < t < 1/(2 cos θ).
```

This interval exists exactly when θ > π/3. Since the Matignon boundary has θ = απ/2, the transition is

```text
α > 2/3.
```

Thus α = 2/3 is the natural cubic angular transition, not an artifact of the witness matrix.

---

## 8. Highest-value open target: n = 3 and 2/3 < α < 1

For 2/3 < α < 1 the P-matrix wedge alone is insufficient. Siami nevertheless supplies structured cyclic centers with fractional stability beyond the classical Hurwitz range.

The unresolved issue is full-dimensional robustness:

```text
Is int P_α^(3) nonempty for every 2/3 < α < 1?
```

A proof cannot invoke ordinary continuity alone because the diagonal orbit D > 0 is noncompact modulo scalar normalization: diagonal ratios can approach 0 or infinity.

Likely proof route:

1. normalize the diagonal orbit to a compact simplex;
2. analyze all boundary faces through principal submatrices / limiting characteristic polynomials;
3. exclude contact with the two Matignon boundary rays;
4. derive an explicit cubic inequality, ideally the fractional analogue of the classical 3×3 D-stability condition.

If successful, the global theorem becomes

```text
min { n : int P_α^(n) ≠ ∅ } = 3
for every 0 < α < 1.
```

---

## 9. Reopened-audit answers

1. **Does Siami quantify over the same DA orbit?** Not explicitly, but the cycle ratio is invariant under all positive left-diagonal scalings and the orbit can equalize diagonal parameters. The proposed single-cycle D-orbit theorem is therefore substantially subsumed.
2. **Can a proposed single-cycle theorem be obtained from Siami?** Yes, to a dangerous degree; treat it as prior art/corollary unless a stronger statement is proved.
3. **Does Siami allow the RHP Matignon sliver?** Yes; fractional stability can extend beyond the integer-order Hurwitz range.
4. **How does Kushel relate to Σ_α?** Generalized/relative D-stability supplies the ambient framework, and sector/forbidden-boundary results overlap the angular geometry, but they do not give our low-dimensional P_α classification.
5. **Does Kushel already give generic uniform sector gaps?** Sector-gap estimates exist for important D-stable subclasses, so "uniform angular margin" alone is not novelty.
6. **Which topology claims survive Siami?** Not single-cycle secant. Potential survivors are genuinely multi-cycle/cactus theorems not reducible to Siami plus classical results.
7. **Is the 2×2 classification settled?** Yes analytically in this audit; novelty is secondary.
8. **Is int P_α^(3) nonempty?** Yes for 0 < α ≤ 2/3. The high-order range remains open.
9. **How must strong fractional D-stability differ from Abed?** It must concern the Matignon angular region and yield a non-Hurwitz robust class not reducible to classical strong D-stability.
10. **Smallest title-worthy package?** Exact 2×2 obstruction + dimension-three full-dimensional separation + extension to all 0 < α < 1, preferably with an exact 3×3 criterion or minimal-motif theorem.

---

## 10. Current verdict

**GO-NARROWED — AUDIT STILL OPEN.**

The graph/cactus theorem should not be the immediate proof target. First close the low-dimensional program:

- n = 2: exact classification — analytically closed;
- n = 3, 0 < α ≤ 2/3: full-dimensional robust separation — analytically closed modulo imported Kellogg theorem;
- n = 3, 2/3 < α < 1: **OPEN / highest priority**;
- only then identify the motif mechanism and generalize structurally.

No manuscript should claim final novelty until the 3×3 high-order range has either been proved or shown impossible and this reopened literature audit is frozen.
