# C-09 targeted novelty audit

**Date:** 2026-09-24
**Role:** Chief Researcher
**Verdict:** **NOVELTY SURVIVES**

## Exact theorem audited

For fixed 0 < alpha < 1, let

[
F_alpha^(n) = { A in R^(n x n) : sigma(D A) subset Sigma_alpha for every positive diagonal D }
]

and let D_H^(n) be the classical Hurwitz D-stable class. The audited theorem is

[
min { n : int(F_alpha^(n) \ D_H^(n)) != empty } = 3
quad for every 0 < alpha < 1.
]

This verdict applies to the combined quantified dimension/interior theorem. It does **not** assert novelty of Matignon stability, fractional Routh-Hurwitz criteria, P-matrix spectral wedges, generalized D-stability, sector gaps, strong D-stability, or cyclic fractional secant criteria.

## 1. Fractional cubic root-location criteria are prior art

### Cermak-Nechvatal (2017)

J. Cermak and L. Nechvatal, *The Routh-Hurwitz conditions of fractional type in stability analysis of the Lorenz dynamical system*, Nonlinear Dynamics 87 (2017), 939-954, DOI 10.1007/s11071-016-3090-9.

They derive optimal fractional Routh-Hurwitz conditions, i.e. necessary-and-sufficient coefficient conditions for zeros of a characteristic polynomial to lie in the Matignon stability sector.

**Overlap:** fixed-polynomial / fixed-matrix angular root location.

**Not supplied:** the positive-diagonal orbit quantifier for one matrix, the class F_alpha \ D_H, its full-dimensional interior, or a minimum-dimension theorem.

### Bourafa-Abdelouahab-Moussaoui (2020)

S. Bourafa, M-S. Abdelouahab, A. Moussaoui, *On some extended Routh-Hurwitz conditions for fractional-order autonomous systems of order alpha in (0,2)*, Chaos, Solitons & Fractals 133 (2020), 109623, DOI 10.1016/j.chaos.2020.109623.

Relevant exact results:
- Proposition 1: necessary-and-sufficient n=2 criterion.
- Proposition 2: explicit cubic conditions, including the alpha < 2/3 regime.
- Proposition 3: necessary-and-sufficient cubic Matignon criterion for the negative-discriminant case using Cardano variables.

Therefore the cubic angular certificate used in the project is **not** a standalone novelty claim.

What these propositions do not do is quantify uniformly over all positive diagonal scalings D of a fixed matrix, optimize a coefficient condition over that orbit, or prove a full-dimensional genuinely non-Hurwitz difference class.

## 2. Generalized and relative D-stability are prior art

Kushel 2019 defines the general (D-region, multiplier-class, operation)-stability framework, so F_alpha is an instance of an existing generalized D-stability concept.

Kushel-Pavani 2020/2021 develop generalized D-stability / forbidden-boundary and diagonal-region-dominance machinery, including fractional-order applications.

Kushel 2023, *Some bounds for determinants of relatively D-stable matrices*, LAA 656 (2023), 9-26, DOI 10.1016/j.laa.2022.09.018, defines relative D-stability in a conic sector around the **negative real axis** and studies sector gaps.

**Overlap:** preservation of spectral localization under every positive diagonal left multiplier.

**Key difference:** relative D-stability keeps the orbit in a left-half-plane conic sector; the project class F_alpha uses the full Matignon region and the difference class P_alpha = F_alpha \ D_H deliberately requires genuinely non-Hurwitz fractional stability.

No located Kushel theorem gives the full-dimensional interior of P_alpha or its minimum dimension.

## 3. Classical robust/interior D-stability is prior art

Cain, Hartfiel, Abed and later work study low-dimensional D-stability, the interior of the classical D-stable set, and strong/robust D-stability.

These results prevent any novelty claim based merely on the words "interior", "robust", or "strong D-stability".

They do not establish the topology of F_alpha \ D_H for the Matignon region, nor the minimum dimension where that difference acquires nonempty full-dimensional interior.

## 4. Siami kills the structured cycle as a novelty claim, but not C-09

Siami 2020/2021 gives a fractional generalized secant condition for a single-circuit network. Its cycle ratio is invariant under positive row scaling, so the structured cyclic center A_gamma cannot be presented as new.

C-09 is stronger: the project proves an **open ball in unrestricted 3x3 matrix space**

[
B_epsilon(A_gamma) subset F_alpha^(3) \ D_H^(3),
]

not merely a one-parameter cyclic family. The all-D certificate survives arbitrary sufficiently small full-matrix perturbations.

## 5. Exact novelty surviving the audit

The following combined quantifier structure was not located in the audited literature:

1. every positive diagonal left scaling D;
2. full Matignon stability region, including right-half-plane fractionally stable spectra;
3. exclusion from classical Hurwitz D-stability;
4. full-dimensional interior of that difference class;
5. exact obstruction in dimensions 1 and 2;
6. exact minimum dimension 3;
7. validity for every 0 < alpha < 1.

Targeted searches across fractional Routh-Hurwitz theory, P-matrix stability, positive diagonal scaling, generalized/relative D-stability, robust/interior D-stability, and fractional cyclic-network stability found the ingredients separately, but no equivalent theorem.

## 6. Approved provisional flagship statement

Subject to one final independent pre-submission bibliography audit, the project may center its mathematics on:

> For every commensurate fractional order 0 < alpha < 1, dimension three is the smallest real matrix dimension in which the matrices whose entire positive left-diagonal orbit is Matignon-stable, but which are not classically Hurwitz D-stable, contain a nonempty full-dimensional open subset.

## 7. What must NOT be claimed as new

- Matignon stabilization.
- Fractional Routh-Hurwitz conditions.
- The alpha = 2/3 cubic threshold by itself.
- Generalized D-stability.
- Relative D-stability or sector gaps.
- Strong D-stability / robustness as a concept.
- Single-cycle fractional secant conditions.
- Kellogg's P-matrix spectral wedge.

## 8. Residual risk

The residual bibliographic risk is an obscure generalized-region / low-dimensional multiplier-stability theorem whose title and abstract do not advertise the specialization needed to recover C-09. No such result was found in this targeted audit.

## Final verdict

**NOVELTY SURVIVES**

Mathematical status: internally proved.
Literature status: no theorem-equivalent prior art found in the closest theorem families.
Publication status: promote C-09 to provisional flagship theorem, while preserving a final independent novelty check before submission.
