# Closest-work novelty matrix — final specialist state

**Date:** 2026-09-25  
**Branch:** `agent/final-novelty-c10-c15-20260925`  
**Rule:** compare hypotheses, quantifiers, region, matrix dimension and conclusion. Keyword mismatch is never evidence of novelty.

| Reference | Exact occupied territory | Positive diagonal orbit? | Fractional / angular? | Exactness | Relation to C-09 / C-10 / C-15 / C-16 |
|---|---|---:|---:|---|---|
| Matignon 1996; Brandibur–Garrappa–Kaslik 2021 | commensurate fractional angular stability and α-monotonicity | no | yes | exact for fixed system | Imported foundation; basic fractional stabilization is not novel |
| Ahmed–El-Sayed–El-Saka 2007 | explicit fractional-stable / integer-unstable low-dimensional equilibria | no | yes | model/coefficient criteria | Kills novelty of the phenomenon itself |
| Čermák–Nechvátal 2017 | fractional Routh–Hurwitz/root-location conditions | no | yes | fixed polynomial/system | Fixed-cubic part of C-10 is occupied territory |
| Bourafa–Abdelouahab–Moussaoui 2020 | fractional Routh–Hurwitz conditions across α∈[0,2) | no | yes | fixed polynomial/system | Fixed-coefficient angular machinery is not flagship novelty |
| Holtz–Khrushchev–Kushel 2016 | forbidden sectors for positive-coefficient polynomials via generalized Hurwitz matrices | no | angular | sufficient structural root-location theory | Sector-polynomial predecessor; no all-D matrix elimination |
| Joya–Furuta 1991 | polynomial “D-stability” = roots in a desired domain D, including sector coefficient domains | no matrix multiplier | yes, domain/sector | N&S for their polynomial-domain problem | Terminology/sector predecessor; not multiplicative matrix D-stability |
| **Cain 1976** | complete real 3×3 classical D-stability; homogeneous all-D Routh–Hurwitz minimization in principal minors; exact determinant threshold | **yes, every positive D** | half-plane α=1 | **exact N&S** | **Major structural predecessor.** C-10 recovers/deforms this endpoint; homogeneity/minimization over D are not novel |
| **Bahl–Cain 1977** | fixed inertia of MD for every positive diagonal D in real 3×3, algebraic principal-minor conditions | **yes** | half-plane inertia | **exact classifications** | Very close low-dimensional orbit predecessor; inertia cannot distinguish Matignon angles inside a half-plane |
| Cain 1984; Hartfiel 1980 | interior/topology of classical D-stable matrices | yes | half-plane | structural | Interior/robustness language is classical |
| Abed 1986; Lee–Edgar 2001 | strong/robust classical D-stability | yes | half-plane | robust criteria | “strong D-stability” is occupied terminology/concept |
| Kushel 2019 | general region/multiplier/operation stability framework | yes | arbitrary region | framework | F_α is an instance of known generalized D-stability |
| **Kushel–Pavani 2020/2022, Theorem 3.3** | forbidden-boundary characterization for conic relative D-stability **and complement of the closed conic sector**; determinant nonvanishing for every positive D | **yes** | **sector/complement** | **abstract N&S** | **Closest conceptual theorem.** After sign reversal it covers the abstract Matignon complement problem. C-10 is therefore not the first N&S criterion; surviving novelty is explicit 3×3 elimination to κ<T_α(β) |
| Kushel–Pavani 2021 | diagonal region-dominance/generalized D-stability; fractional applications | yes for specified classes | yes | sufficient | Direct prior art for fractional multiplicative region stability; no exact C-10 threshold |
| Kushel 2023 | relative D-stability, determinant bounds and sector gaps | yes | sector | sufficient/bounds | Sector gaps are not new; no T_α equivalence |
| Kushel 2016 “D_θ-stability” | D-stability for θ-**ordered diagonal entries**, with θ a permutation/order | yes | **not angular** | classical criteria | False terminology collision; does not threaten C-10 |
| Kushel 2026 recursive determinantal framework | principal-minor delete/zero recursion; hierarchy of sufficient classical D-stability tests | yes | half-plane | sufficient | Current methodology; no exact Matignon threshold or C-15 geometry |
| Kellogg 1972 P-matrix wedge | eigenvalue wedge for P-matrices | preserved under positive diagonal left scaling | angular | exact bound | Imported low-order bridge; not novelty |
| **Siami 2020/2021** | generalized fractional secant condition for single-circuit networks; necessity for equal diagonal coefficients | cycle ratio invariant under row scaling | yes | exact/sufficient structured theorem | Single-cycle novelty rejected; β=(1,1,1) structured slice of C-10/C-15 |
| Arcak–Sontag 2006; Arcak 2011 | cyclic/cactus diagonal stability via secant-type structure | related | α=1 | exact/sufficient by class | Graph-structural predecessor |
| Mohsenipour–Liu 2020 | robust “D-stability” of uncertain fractional characteristic roots in desired D-regions/value sets | no multiplicative DA quantifier | yes | robust root-region test | Terminology collision only |
| Shao et al. 2017 | title: N&S D-stability of fractional-order linear systems; primary body not retrieved | no accessible evidence of multiplicative DA | likely D-region/pole-location | unresolved body | Bibliography follow-up only; not load-bearing |
| Al Ahmadieh 2026 | principal-minor map and diagonal equivalence/fibers | similarity-type diagonal equivalence | no | algebraic | Confirms principal-minor coordinates/equivalence are standard; not left-multiplication C-10 |
| Kinkhabwala 2015; classical network loop literature | characteristic coefficients ↔ principal minors ↔ feedback cycles | no full fractional D orbit | α=1/network | structural | Generic loop/minor dictionary is classical; C-13 only interprets C-10 |
| Clark–Hallam 1982 | three-species community-matrix stability | no | α=1 | low-dimensional ecology | Ecological three-species stability is not standalone novelty |

---

# Final claim-by-claim novelty boundary

## C-09 — minimum robust genuinely fractional dimension

Exact project statement:

```text
min { n : int(F_α^(n) \ D_H^(n)) != empty } = 3
for every 0 < α < 1.
```

No located source combines:

- every positive diagonal multiplier;
- the full Matignon region;
- separation from classical Hurwitz D-stability;
- full-dimensional ambient interior;
- exact n≤2 obstruction;
- dimension 3 construction/characterization;
- all 0<α<1.

**Final specialist verdict:** **NOVEL WITH NARROWED CLAIM**.

Mandatory wording: retain “genuinely fractional”, “positive-diagonal multiplicative D-stability”, and “nonempty full-dimensional interior”. Do not abbreviate this to “fractional stabilization first occurs in dimension three”.

---

## C-10 — exact real 3×3 Matignon orbit elimination

Project theorem on the strict-P(-A) stratum:

```text
A ∈ F_α^(3)  iff  κ < T_α(β),    2/3 < α < 1,
```

with four positive-left-diagonal invariants

```text
(β_12, β_13, β_23, κ).
```

### Already known

- generalized region/multiplier D-stability: Kushel;
- abstract N&S forbidden-boundary criterion for cone/complement under all D: Kushel–Pavani Theorem 3.3;
- exact α=1 3×3 all-D homogeneous optimization/principal-minor threshold: Cain;
- exact 3×3 all-D inertia classifications: Bahl–Cain;
- fixed-cubic sector/fractional root-location conditions;
- symmetric cyclic fractional threshold: Siami.

### Not located in prior art

No audited source gives, for arbitrary real strict-P(-A) 3×3 matrices:

1. exact elimination of the universal positive-diagonal multiplier;
2. four invariant coordinates β_12,β_13,β_23,κ;
3. the scalar variational threshold T_α(β);
4. the iff inequality κ<T_α(β);
5. the exact genuinely fractional band T_1(β)<κ<T_α(β).

**Final specialist verdict:** **NOVEL WITH NARROWED CLAIM**.

Approved positioning:

> explicit exact 3×3 solution/elimination of the generalized forbidden-boundary Matignon D-stability problem on the strict-P(-A) stratum.

Do **not** claim “first N&S criterion for fractional D-stability”.

---

## C-15 — exact threshold geometry

No audited source proves for the specific C-10 threshold functional:

- global strict convexity of the log objective in logit coordinates;
- unique nondegenerate optimizer for arbitrary positive β;
- smooth threshold dependence;
- the stated global threshold-surface parametrization.

Generic softmax/logit coordinates, log-sum-exp convexity, geometric-programming ideas and implicit/envelope methods are standard tools and are not novelty.

The β=(1,1,1) symmetric slice is occupied structurally by Siami; the α=1 endpoint is constrained by Cain.

**Final specialist verdict:** **NOVEL WITH NARROWED CLAIM**.

Approved positioning: theorem-specific convex geometry of the exact C-10 threshold, not novelty of the optimization machinery.

---

## C-16 — general simplex reduction

For strict-P(-A),

```text
c_k(D) = sum_{|I|=k} m_I product_{i∈I} d_i
```

is the standard characteristic-coefficient/principal-minor identity applied to DA.

The substitution

```text
x_i = p_i d_i / sum_j p_j d_j
```

is standard positive projective/simplex normalization.

Therefore the general n-dimensional reduction is valuable organization but not a defensible standalone priority claim.

**Final specialist verdict:** **NOT NOVEL**.

Keep C-16 as a structural lemma/proposition with citations to standard characteristic-polynomial/principal-minor machinery. No novelty language.

---

# Mandatory falsification answers

1. **Is C-10 already Bahl–Cain 1977 after replacing inertia by angular condition?** No. Inertia cannot resolve angular location within a half-plane. C-10 requires new Matignon ray geometry.
2. **Is T_α a known relative-D determinant bound?** No equivalence located. Kushel–Pavani already give the abstract N&S boundary condition; Kushel 2023 gives bounds/sufficient relative-D results, not T_α.
3. **Is C-15 logit convexity known?** Generic tools yes; this specific strict global convexity/unique optimizer theorem was not located.
4. **Is C-16 standard enough to be only a lemma?** Yes — **NOT NOVEL**.
5. **Does prior art give an exact N&S 3×3 positive-diagonal sector theorem?** It gives an abstract all-n N&S forbidden-boundary criterion, but no explicit real-3×3 κ<T_α(β) elimination was located.
6. **Does prior work cover the nonconvex Matignon region including RHP points?** Yes at framework/root-region level. It is wrong to say the region was untouched.
7. **Do fractional “D-stability” papers quantify over every positive diagonal D?** Mohsenipour–Liu: no; D is a desired root region. Shao 2017 remains primary-body unverified, with all accessible context pointing to the same D-region usage.
8. **Is C-09 immediate from a published theorem?** No.
9. **Does Siami exhaust C-10 under hidden scaling/similarity?** No. The β triple is invariant under the relevant row scalings and principal minors under diagonal similarity; the cycle slice fixes β=(1,1,1).
10. **Is C-13 generic ecological loop novelty?** No. Loop/principal-minor analysis is classical; only the exact fractional all-D threshold inherited from C-10 is new.

---

# Overall final specialist recommendation

## **NOVELTY GATE PASSED WITH REPOSITIONING**

The manuscript should be positioned as:

```text
known generalized multiplicative-D framework
+ known forbidden-boundary N&S principle
+ known fixed-cubic fractional sector machinery
+ known Cain α=1 exact all-D threshold
+ known Siami symmetric cyclic slice
        ↓
new explicit real-3×3 Matignon all-D elimination (C-10)
+ new full-dimensional minimum-dimension consequence (C-09)
+ new theorem-specific threshold geometry (C-15)
```

C-16 is supporting algebra, not a contribution.

Detailed theorem-level reasoning: `research/novelty/FINAL_C10_C15_SPECIALIST_AUDIT.md`.  
Bibliographic verification: `research/novelty/FINAL_BIBLIOGRAPHY_VERIFICATION.md`.
