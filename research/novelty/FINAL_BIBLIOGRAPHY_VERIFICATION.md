# Final bibliography verification — C-09 / C-10 / C-15 / C-16

**Date:** 2026-09-25  
**Branch:** `agent/final-novelty-c10-c15-20260925`  
**Purpose:** source-by-source verification for the final specialist novelty audit.  
**Rule:** a citation is load-bearing only when its exact mathematical role has been verified from a primary source or an authoritative publisher record.

## Verification grades

- **A — PRIMARY THEOREM VERIFIED:** full text/theorem/proof inspected.
- **B — PRIMARY METADATA/ABSTRACT VERIFIED:** publisher or authoritative record inspected; enough for the limited claim made here.
- **C — PRIMARY BODY NOT RETRIEVED:** bibliographic record verified, but theorem wording not directly inspected; never used as a load-bearing novelty kill.

---

## Load-bearing matrix-theory and generalized-D-stability sources

| Reference | Grade | Exact verified content relevant here | Relation to project | DOI / stable source |
|---|---:|---|---|---|
| B. E. Cain, **“Real, 3 × 3, D-Stable Matrices,”** *Journal of Research of the National Bureau of Standards B* 80B (1976), 75–77 | **A** | Defines D-stability under every positive diagonal multiplier; gives complete real 3×3 criterion in principal-minor notation. For D=diag(x,y,z), Routh–Hurwitz produces the homogeneous all-D inequality and Cain proves the infimum of the associated ratio is the square of a sum of square roots of principal-minor products. | Mandatory α=1 endpoint of C-10. Shows that principal-minor encoding, homogeneity, minimization over D, and an exact determinant threshold are classical. | NIST historical journal PDF; article title/year/pages verified |
| C. A. Bahl and B. E. Cain, **“The inertia of diagonal multiples of 3×3 real matrices,”** *Linear Algebra and its Applications* 18(3) (1977), 267–280 | **B** | Publisher abstract states that for every inertia triple with total dimension 3 they characterize real matrices M such that In(MD) is fixed for every positive definite diagonal D, using algebraic conditions on principal minors. | Very close all-D 3×3 predecessor. Does not determine eigenvalue angle inside a half-plane, so it does not imply C-10. | DOI: 10.1016/0024-3795(77)90056-8 |
| B. E. Cain, **“Inside the D-stable matrices,”** *Linear Algebra and its Applications* 56 (1984), 237–243 | **B** | Publisher metadata/abstract verifies study of the interior of the classical D-stable set. | Prior art for interior/robustness language; not fractional Matignon geometry. | DOI: 10.1016/0024-3795(84)90129-0 |
| D. J. Hartfiel, **“Concerning the interior of the D-stable matrices,”** *Linear Algebra and its Applications* (1980) | **B** | Publisher record verifies direct study of the interior of the D-stable matrices. | Classical predecessor for any “open D-stable set” language. | DOI: 10.1016/0024-3795(80)90195-0 |
| E. H. Abed, **“Strong D-stability,”** *Systems & Control Letters* 7(3) (1986), 207–212 | **B** | Establishes/uses strong D-stability as perturbational persistence of classical D-stability. | “Strong/robust D-stability” is not new terminology or a new generic concept. | DOI: 10.1016/0167-6911(86)90116-7 |
| J. Lee and T. F. Edgar, **“Real structured singular value conditions for the strong D-stability,”** *Systems & Control Letters* 44 (2001), 273–277 | **B** | Authoritative record verifies robust/strong D-stability criteria through structured singular values. | Additional classical robustness prior art. | journal record verified |
| O. Y. Kushel, **“Unifying matrix stability concepts with a view to applications,”** *SIAM Review* 61 (2019) | **A/B** | General `(region, multiplier class, operation)` stability framework includes spectral localization under multiplier classes such as positive diagonal matrices. | The project object F_α is an instance of an existing generalized-D-stability framework. | DOI: 10.1137/18M119241X; arXiv:1907.07089 |
| O. Y. Kushel and R. Pavani, **“The problem of generalized D-stability in unbounded LMI regions and its computational aspects,”** later *Journal of Dynamics and Differential Equations* | **A** | Definitions use every positive diagonal multiplier. The forbidden-boundary theorem gives region-D-stability iff initial region stability plus boundary avoidance over all D. **Theorem 3.3 explicitly treats a conic region and the complement of the closed conic region**, with equivalent determinant nonvanishing conditions for every positive diagonal D. | **Closest abstract predecessor to C-10.** After B=-A, the α<1 Matignon problem is a complement-of-cone generalized-D-stability problem. C-10 is not the first N&S criterion; its surviving novelty is explicit real-3×3 elimination to κ<T_α(β). | DOI: 10.1007/s10884-020-09891-y; arXiv:2004.11172 |
| O. Y. Kushel and R. Pavani, **“Generalization of the concept of diagonal dominance with applications to matrix D-stability,”** *Linear Algebra and its Applications* 630 (2021), 204–224 | **B** | Develops diagonal region-dominance / generalized D-stability machinery and fractional-order applications; conditions are sufficient for specified regions/classes. | Direct conceptual prior art; does not supply C-10’s exact 3×3 threshold. | DOI: 10.1016/j.laa.2021.08.004; arXiv:2103.04127 |
| O. Y. Kushel, **“Some bounds for determinants of relatively D-stable matrices,”** *Linear Algebra and its Applications* 656 (2023), 9–26 | **B** | Gives sufficient relative-D-stability conditions, determinant bounds and sector-gap estimates for selected classes. | “Uniform sector gap” is occupied language; no exact κ<T_α(β) equivalence located. | DOI: 10.1016/j.laa.2022.09.018; arXiv:2205.10823 |
| O. Y. Kushel, **“On a criterion of D-stability for P-matrices,”** *Special Matrices* 4 (2016), 181–188 | **A** | Defines `D_θ` using **θ as a permutation/order of diagonal entries**: D is θ-ordered and A is D_θ-stable if stability holds for every such ordered D. It is not an angular-sector notion. | Terminology false friend; no collision with C-10’s spectral angle θ. | DOI: 10.1515/spma-2016-0017 |
| O. Y. Kushel, **“Recursive determinantal framework for testing D-stability. I,”** arXiv preprint (2026) | **A/B** | Develops delete/zero recursions for real/imaginary determinant parts and a hierarchy of **sufficient** classical D-stability conditions in principal minors. | Current methodology to cite; classical half-plane, not exact Matignon 3×3 threshold. | arXiv:2604.16526 |

---

## Fractional / sector root-location sources

| Reference | Grade | Exact verified content relevant here | Relation to project | DOI / stable source |
|---|---:|---|---|---|
| D. Matignon, 1996 stability theorem for commensurate fractional systems | **A via modern verified restatement** | Stability iff eigenvalues satisfy the familiar angular Matignon condition for the commensurate linear system. | Imported stability region; no novelty. | Original conference result; modern verification below |
| M. Brandibur, R. Garrappa, E. Kaslik, **“Stability of systems of fractional-order differential equations with Caputo derivatives,”** *Mathematics* 9 (2021), 914 | **A/B** | Modern corrected treatment of Matignon-type stability and α-monotonicity. | Imported foundation; kills novelty of “critical order” monotonicity. | DOI/source: https://www.mdpi.com/2227-7390/9/8/914 |
| M. Siami, **“Stability and Robustness Analysis of Commensurate Fractional-order Networks,”** IEEE TCNS / arXiv | **A** | Theorem 2: single-circuit network; automatic stability for α≤2/n; for α>2/n the generalized fractional secant threshold involving sin(απ/2)/sin(απ/2−π/n); necessary when diagonal coefficients are identical. | Exact structured slice recovered by C-10/C-15. Does not exhaust arbitrary β. | DOI: 10.1109/TCNS.2021.3061931; arXiv:2011.04204 |
| J. Čermák and L. Nechvátal, fractional Routh–Hurwitz work, *Nonlinear Dynamics* 87 (2017), 939–954 | **B** | Fractional Routh–Hurwitz/root-location conditions for a fixed fractional system / characteristic polynomial. | Fixed-cubic sector machinery is occupied; no universal positive-diagonal matrix orbit. | DOI: 10.1007/s11071-016-3090-9 |
| A. Bourafa, A. Abdelouahab, A. Moussaoui, fractional Routh–Hurwitz extension, *Chaos, Solitons & Fractals* (2020) | **B** | Extends fractional Routh–Hurwitz conditions across α∈[0,2), including low-dimensional coefficient cases. | Fixed-polynomial component adjacent/prior art; no exact elimination of all positive D. | DOI: 10.1016/j.chaos.2020.109623 |
| O. Holtz, S. Khrushchev, O. Kushel, **“Generalized Hurwitz matrices, generalized Euclidean algorithm, and forbidden sectors of the complex plane,”** *Computational Methods and Function Theory* 16 (2016), 395–431 | **B** | Gives forbidden-sector results for positive-coefficient polynomials using generalized Hurwitz matrices / total nonnegativity. | Sector root-location prior art; not the positive-diagonal matrix-orbit theorem. | DOI: 10.1007/s40315-016-0156-0 |
| K. Joya and K. Furuta, **“A Necessary and Sufficient Condition for the D-Stability of Convex Combinations of D-Stable Polynomials,”** *Transactions of SICE* 27(3) (1991), 298–305 | **A/B** | Here D-stability means roots in a prescribed **domain D**; gives explicit coefficient-space descriptions for domains including sectors. | Polynomial region-stability terminology; not multiplicative matrix D-stability. | DOI: 10.9746/sicetr1965.27.298 |
| R. Mohsenipour and X. Liu, **“Robust D-Stability Test of LTI General Fractional Order Control Systems,”** *IEEE/CAA Journal of Automatica Sinica* 7(3) (2020), 853–864 | **A/B** | Abstract explicitly formulates uncertain characteristic equations, root regions, value sets and zero-exclusion ideas. “D-stability” is desired pole/root **D-region stability**. | Terminology collision only; does not quantify over every positive diagonal left multiplier DA. | DOI: 10.1109/JAS.2020.1003159 |
| K. Shao, L. Zhou, K. Qian, Y. Yu, F. Chen, S. Zheng, **“Necessary and sufficient D-stability condition of fractional-order linear systems,”** 36th CCC (2017), 44–48 | **C** | IEEE proceedings metadata and DOI verified. Primary body was not retrievable in this audit. Accessible citation context places it in fractional pole-region/D-region stability, not multiplicative matrix D-stability. | **Residual bibliography check only; not load-bearing.** Obtain PDF before submission if possible. | DOI: 10.23919/ChiCC.2017.8027318 |

---

## Principal-minor / orbit-coordinate / ecology sources

| Reference | Grade | Exact verified content relevant here | Relation to project | DOI / stable source |
|---|---:|---|---|---|
| A. Al Ahmadieh, principal-minor-map / fiber work, *Journal of Algebra* 685 (2026), 46–61 | **B** | Studies the principal-minor map and diagonal equivalence; diagonal equivalence is similarity-type (e.g. A=DBD^{-1}, with transpose variants), not positive left multiplication DA. | Confirms principal-minor coordinates/equivalence are standard matrix-theory objects; does not imply C-10. | DOI: 10.1016/j.jalgebra.2025.07.030 |
| A. Kinkhabwala, **“Implications of Network Topology on Stability,”** *PLOS ONE* (2015) | **A/B** | Explicitly expresses characteristic coefficients through sums of principal minors and principal minors through non-overlapping feedback cycles. | Generic principal-minor/cycle dictionary is classical; supports demotion of C-16 and positioning of C-13 as interpretation. | PLOS ONE primary article |
| T. J. Clark and T. G. Hallam, **“The community matrix in three species community models,”** *Journal of Mathematical Biology* 16 (1982), 25–31 | **B** | Classical exact three-species community-matrix stability setting. | Ecological 3-species stability and loop language are not standalone novelty. | DOI: 10.1007/BF00275158 |

---

# Source-specific consequences for the claims

## C-09

No verified source states or implies the exact quantified theorem

```text
min { n : int(F_α^(n) \ D_H^(n)) ≠ ∅ } = 3
for every 0 < α < 1.
```

The ingredients are distributed across Matignon, Kellogg, classical D-stability/interior theory, Siami and fixed-polynomial fractional stability. No exact published combination was located.

**Bibliographic status:** supports **NOVEL WITH NARROWED CLAIM**.

## C-10

The novelty boundary is now exact:

- **known:** generalized multiplicative region D-stability (Kushel);
- **known:** abstract N&S forbidden-boundary theorem for conic region/complement under all D (Kushel–Pavani Theorem 3.3);
- **known:** exact homogeneous all-D minimization/determinant threshold at α=1 (Cain);
- **known:** inertia under all D in 3×3 (Bahl–Cain);
- **known:** fixed-polynomial sector/fractional root-location criteria;
- **known:** symmetric cyclic fractional secant slice (Siami);
- **not located:** exact arbitrary-strict-P real 3×3 elimination to four positive-left-diagonal invariants and the iff scalar threshold κ<T_α(β).

**Bibliographic status:** supports **NOVEL WITH NARROWED CLAIM**.

## C-15

No verified source gives the strict logit convexity, unique nondegenerate optimizer and global threshold-surface geometry for the specific C-10 functional T_α. Generic convex-analysis / log-sum-exp / geometric-programming machinery is standard and must be credited as technique rather than discovery.

**Bibliographic status:** supports **NOVEL WITH NARROWED CLAIM**.

## C-16

The formula

```text
c_k(D) = Σ_{|I|=k} m_I Π_{i∈I} d_i
```

is an immediate application of the standard characteristic-polynomial coefficient/principal-minor identity to DA. Normalizing the positive vector (p_i d_i) by its sum is standard projective/simplex normalization. No special fractional theorem is required.

**Bibliographic status:** **NOT NOVEL** as a standalone claim; retain as structural lemma.

---

# Residual access flags

1. **Shao et al. 2017:** primary article body not retrieved. Metadata is verified; all accessible context points to D-region/pole-location terminology. Because C-10 is already compared against the much stronger load-bearing Kushel–Pavani multiplicative-D theorem, this missing PDF does **not** block the novelty gate. It should nevertheless be obtained before final journal submission if feasible.
2. Older obscure/non-indexed generalized-sector multiplier literature remains a generic literature-search residual risk. The searches specifically targeted low-dimensional sector D-stability, inertia preservation, relative D-stability, conic D-stability, fractional diagonal uncertainty, principal-minor normalization and current 2025–2026 work; no theorem equivalent to C-10/C-15 was found.

## Final bibliography conclusion

The load-bearing primary sources are sufficient to draw the final novelty boundary. The project must cite Cain and Kushel–Pavani as **structural predecessors**, not merely background citations.

The correct novelty statement is the explicit real-3×3 solution of an already-known generalized-D-stability problem, together with its genuinely fractional dimension-interior consequence and threshold geometry.
