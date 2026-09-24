# Deep novelty audit report — reopened second pass

**Date:** 2026-09-24  
**Status:** `GO-NARROWED — AUDIT STILL OPEN`  
**Scope:** theorem-level novelty audit for `fractional-d-stability-networks`, updated after the Chief reopened the baseline audit at commit `0b3b4df394eceec0dc9951a33fda01560de2f731`.

Mandatory prior art incorporated in this pass:

- Milad Siami, *Stability and Robustness Analysis of Commensurate Fractional-order Networks*, arXiv:2011.04204 / IEEE TCNS.
- Olga Y. Kushel, *Some bounds for determinants of relatively D-stable matrices*, LAA 656 (2023), arXiv:2205.10823.
- Eyad H. Abed, *Strong D-stability*, Systems & Control Letters 7(3) (1986), 207–212.
- Re-reading of Kushel 2019 and Kushel–Pavani 2020/2021.
- Casasanta–Simpson-Porco 2026, arXiv:2603.13608.

Detailed derivations: `research/novelty/REOPENED_AUDIT_2026-09-24.md`.

## 1. Central objects

For 0 < α < 1,

```text
Σ_α = { z ≠ 0 : |arg z| > απ/2 }

F_α^(n) = { A ∈ R^(n×n) : σ(DA) ⊂ Σ_α for every positive diagonal D }

P_α^(n) = F_α^(n) \ D_H^(n)
```

where D_H^(n) is the classical Hurwitz D-stable class.

The scientific question is no longer whether fractional stabilization or generalized D-stability exists. Both are known. The live question is exact structural mathematics for the genuinely non-Hurwitz part P_α^(n).

---

## 2. Corrected verdicts

### C-01 — Matignon sector criterion — KNOWN / IMPORTED

For commensurate Caputo systems, asymptotic stability is governed by

```text
|arg λ| > απ/2.
```

Brandibur–Garrappa–Kaslik provide a corrected modern treatment and α-monotonicity.

### C-02 — fractionally stable but integer-order unstable — KNOWN

The region

```text
απ/2 < |arg λ| <= π/2
```

is exactly the purely fractional sliver. Ahmed–El-Sayed–El-Saka already use the phenomenon explicitly.

### C-03 — graph-indexed S_α(G) — DEFINITION ONLY

A graph-indexed stability set is not a contribution unless accompanied by a theorem beyond Matignon, fractional consensus, or classical topology-to-spectrum results.

### C-04 — fractional D-stability under all positive diagonal scalings — FRAMEWORK KNOWN

Kushel's generalized D-stability framework already permits arbitrary spectral regions and positive diagonal multiplier classes. The previous baseline claim that all literature was blind to the non-convex Matignon complement is **withdrawn**. Kushel–Pavani discuss the fractional stability set as the complement of a cone and develop boundary machinery relevant to diagonal scaling. Kushel 2023 studies relative D-stability and sector gaps.

What may still be new: exact low-dimensional characterization, dimension thresholds, or structural separation inside the genuinely non-Hurwitz class.

### C-05 — single-cycle / motif fractional D-stability — SINGLE-CYCLE NOVELTY REJECTED

Siami studies the single-circuit fractional network and generalized secant condition. Its key ratio

```text
γ = (Π c_i / Π a_i)^(1/n)
```

is invariant under positive left-diagonal row scaling. Choosing d_i proportional to 1/a_i equalizes the diagonal magnitudes inside the same orbit, which reaches Siami's necessary special case.

Therefore a single-cycle fractional D-stability iff fractional-secant theorem is substantially recoverable from prior art.

### C-06 — robustness / openness — CONCEPT KNOWN, FRACTIONAL NON-HURWITZ VERSION MAY BE NEW

Hartfiel studied the interior of the classical D-stable set; Abed introduced strong D-stability; Lee–Edgar and current work give further robust-D-stability characterizations. Robustness alone is not novelty.

What can still be new is a full-dimensional open subset of matrices that are robustly stable in the Matignon region while lying outside classical Hurwitz D-stability.

---

## 3. Exact 2×2 theorem

Let A = [[a,b],[c,d]] and D = diag(x,y), with x,y > 0.

```text
tr(DA)  = xa + yd
det(DA) = xy det(A).
```

For every 0 < α < 1,

```text
A ∈ F_α^(2)
iff
det(A) > 0,  a <= 0,  d <= 0.
```

Reason:

- sufficiency: det(DA)>0 and tr(DA)<=0 for every D>0, so eigenvalues are negative real or a conjugate pair with nonpositive real part; therefore |arg λ|>=π/2>απ/2;
- necessity: det(A)<=0 gives a zero/nonnegative real eigenvalue; a>0 is excluded by x/y→∞; d>0 is excluded by y/x→∞.

The classical Hurwitz D-stable subset additionally requires (a,d)!=(0,0). Hence

```text
P_α^(2) = { [[0,b],[c,0]] : bc<0 }.
```

Therefore

```text
int_R4 P_α^(2) = empty.
```

**Proof status:** analytic theorem.  
**Novelty status:** useful structural result, but too elementary to carry the paper alone.

---

## 4. P-matrix bridge

Kellogg's classical wedge theorem for a P-matrix P ∈ R^(n×n) gives

```text
|arg μ| < π - π/n
for every μ ∈ σ(P).
```

Positive diagonal left scaling preserves the P-matrix property. Therefore, if -A is a P-matrix,

```text
|arg λ(DA)| > π/n
for every D>0.
```

So

```text
-A P-matrix  =>  A ∈ F_α^(n)
for every 0 < α <= 2/n.
```

This is an imported bridge, not the main novelty.

---

## 5. Dimension three supports an open genuinely fractional class for 0 < α <= 2/3

Define

```text
A_γ = [ [-1, 0, -γ],
        [ γ,-1,  0],
        [ 0, γ, -1] ],   γ>2.
```

All principal minors of -A_γ are strictly positive, so -A_γ is a P-matrix. Thus

```text
A_γ ∈ F_α^(3)
for every 0 < α <= 2/3.
```

Its spectrum is

```text
σ(A_γ) =
{ -1-γ,
  -1+γ/2 + i(√3 γ/2),
  -1+γ/2 - i(√3 γ/2) }.
```

For γ>2 the complex pair has positive real part. Hence A_γ is not Hurwitz at D=I and therefore is not classically D-stable.

Because the P-matrix principal-minor inequalities and the positive spectral-abscissa inequality are strict, both persist on a sufficiently small full-dimensional ball around A_γ. Consequently there exists ε>0 such that

```text
B_ε(A_γ) ⊂ F_α^(3) \ D_H^(3)
```

for every 0<α<=2/3.

Therefore

```text
int P_α^(3) != empty
for every 0 < α <= 2/3.
```

Combining n=1, n=2, and n=3:

```text
min { n : int P_α^(n) != empty } = 3
for every 0 < α <= 2/3.
```

**Mathematical status:** internally proved, modulo the imported Kellogg theorem.  
**Novelty status:** **STRONG NOVELTY CANDIDATE — NOT YET FROZEN**. Targeted searches found the ingredients separately but not this combined minimal-dimension robust genuinely-fractional separation theorem.

---

## 6. Why α = 2/3 is structural

For a cubic

```text
p(λ) = λ^3 + a λ^2 + b λ + c
```

with positive coefficients, suppose a conjugate pair lies on λ = r exp(±iθ) and the third root is -s. Let t=s/r. Then coefficient matching gives

```text
a = r (t - 2 cos θ)
b = r^2 (1 - 2 t cos θ)
c = t r^3.
```

For a,b>0 one needs

```text
2 cos θ < t < 1/(2 cos θ).
```

This interval exists exactly when θ>π/3. Since the Matignon boundary is θ=απ/2, the transition is α>2/3.

Thus 2/3 is the natural cubic angular threshold, not an artifact of the chosen witness matrix.

---

## 7. Highest-value open problem

The unresolved range is

```text
n = 3
2/3 < α < 1.
```

The main target is

```text
int P_α^(3) != empty
for every 2/3 < α < 1.
```

Ordinary continuity at a fixed D is insufficient because the diagonal orbit is noncompact modulo scalar normalization. A proof must control degenerate diagonal directions.

Preferred route:

1. normalize D to a compact simplex;
2. analyze boundary faces using principal submatrices / limiting characteristic polynomials;
3. exclude contact with the two Matignon boundary rays;
4. derive an explicit cubic inequality, ideally a fractional analogue of the classical 3×3 D-stability criterion.

A stronger alternative is an exact characterization of F_α^(3) in the high-order regime.

---

## 8. Reopened mandatory questions — answers

1. **Does Siami quantify over the same DA orbit?** Not explicitly, but its key cycle ratio is invariant under positive left-diagonal scaling and diagonal scaling can equalize the diagonal coefficients.
2. **Can the single-cycle target be recovered from Siami?** Yes, to a degree that makes it unsafe as novelty.
3. **Does Siami reach the right-half-plane Matignon sliver?** Yes; fractional stability can extend beyond the integer-order Hurwitz range.
4. **What is the relationship between Kushel and Σ_α?** Kushel supplies the generalized-D-stability framework and sector/boundary machinery; it does not give the present low-dimensional P_α characterization.
5. **Does Kushel already give generic uniform sector gaps?** Sector-gap estimates exist for important D-stable subclasses, so "uniform angular margin" alone is not novelty.
6. **Which topology claims survive Siami?** Not single-cycle secant; only genuinely non-reducible multi-cycle/motif results remain candidates.
7. **Is the 2×2 classification settled?** Yes analytically in this audit.
8. **Is int P_α^(3) nonempty?** Yes for 0<α<=2/3; high-order range remains open.
9. **How must strong fractional D-stability differ from Abed?** It must concern the Matignon angular region and a non-Hurwitz robust class not reducible to classical strong D-stability.
10. **Smallest title-worthy package?** Exact 2×2 obstruction + dimension-three full-dimensional separation + extension to all 0<α<1, preferably with an exact 3×3 criterion or a minimal-motif theorem.

---

## 9. Strongest novelty surviving the reopened audit

For 0<α<=2/3, the project now has an analytic proof that dimension three is the first dimension in which the genuinely non-Hurwitz fractional D-stable class can have nonempty full-dimensional interior: the class is empty in dimension one, has empty interior in dimension two, and contains an explicit open ball in dimension three. The individual ingredients are known, but the combined minimal-dimension separation theorem was not located in the targeted literature audit. The high-value unresolved extension is to prove the same dimension threshold for every 0<α<1 or derive an exact 3×3 characterization for 2/3<α<1.

## 10. Exact theorem target

> **Target theorem.** For every 0<α<1,
>
> ```text
> min { n : int(F_α^(n) \ D_H^(n)) != empty } = 3.
> ```
>
> For 0<α<=2/3 this is already proved internally; the remaining proof burden is 2/3<α<1.

## 11. Prior-art result most likely to kill the current target

No single located paper presently kills the dimension-threshold theorem. The closest structural threats are:

1. Kushel/Kushel–Pavani generalized-D-stability and forbidden-boundary theory, if a low-dimensional specialization already implies the same result;
2. classical low-dimensional D-stability/interior results, if a direct region substitution yields the fractional statement;
3. Siami, for any proof that remains confined to a single-cycle submanifold instead of producing a full-dimensional open class.

## 12. Final verdict

**GO-NARROWED**

Proceed with the low-dimensional theorem program. Do **not** draft the central manuscript around a single-cycle/cactus novelty claim. Immediate research priority:

```text
n = 3
2/3 < α < 1.
```

Numerical diagonal sampling remains counterexample hunting only.

## 13. Key sources

- Brandibur, Garrappa & Kaslik 2021: https://www.mdpi.com/2227-7390/9/8/914
- Kushel 2019: https://arxiv.org/abs/1907.07089
- Kushel & Pavani 2020: https://arxiv.org/abs/2004.11172
- Kushel & Pavani 2021: https://arxiv.org/abs/2103.04127
- Kushel 2023 preprint: https://arxiv.org/abs/2205.10823
- Siami 2020/2021: https://arxiv.org/abs/2011.04204
- Abed 1986 DOI: https://doi.org/10.1016/0167-6911(86)90116-7
- Casasanta & Simpson-Porco 2026: https://arxiv.org/abs/2603.13608
- Sabatier, Moze & Farges 2010, *Comput. Math. Appl.* 59:1594–1609.
- Ahmed, El-Sayed & El-Saka 2007, *J. Math. Anal. Appl.* 325:542–553.
- Arcak & Sontag 2006, *Automatica* 42(9).
- Arcak 2011, *IEEE TAC* 56(12):2766–2777.
- Hartfiel 1980, *Linear Algebra and its Applications*.
- Lee & Edgar 2001, *Systems & Control Letters* 44:273–277.


---

## 14. Chief targeted audit of C-09

The range 2/3 < alpha < 1 is now internally proved in `research/THEOREM_C09_DIMENSION_THRESHOLD.md`. The exact combined theorem is

[
min{n:operatorname{int}(F_alpha^{(n)}setminus D_H^{(n)})
eqarnothing}=3
quadorall,0<alpha<1.
]

A dedicated theorem-level audit is recorded in `research/novelty/C09_TARGETED_AUDIT.md`.

Additional prior art checked:

- Cermak-Nechvatal (2017): optimal necessary-and-sufficient fractional Routh-Hurwitz conditions. Fixed-cubic angular criteria are therefore prior art.
- Bourafa-Abdelouahab-Moussaoui (2020), Propositions 1-3: explicit n=2/n=3 fractional coefficient criteria, including an exact Cardano-form cubic angular criterion.
- Kushel 2023: relative D-stability in a conic sector around the negative real axis and sector-gap estimates.
- Cain/Hartfiel/Abed: low-dimensional, interior, and robust classical D-stability.
- Siami: structured single-cycle fractional stability.

None of the located results contains the full C-09 quantifier package: all positive diagonal scalings, full Matignon region with genuinely non-Hurwitz spectra, full-dimensional interior, exact lower-dimensional obstruction, and minimum dimension 3 for every 0<alpha<1.

### Updated verdict for C-09

**NOVELTY SURVIVES**

This is theorem-specific. The cubic root-location lemma, generalized D-stability framework, P-matrix bridge, robustness notion, and cyclic witness are not independently claimed as new.

### Updated project status

C-09 is the provisional flagship theorem. The next mathematical priority is to sharpen the all-diagonal 3x3 certificate and determine how close it is to a necessary-and-sufficient characterization.
