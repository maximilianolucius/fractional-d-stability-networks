# Terminology collision: matrix D-stability vs. region (\mathcal D)-stability

**Date:** 2026-09-25  
**Status:** Chief Researcher terminology audit  
**Conclusion:** the Shao et al. 2017 and Mohsenipour–Liu 2020 uses of “D-stability” are **not** the positive-diagonal-multiplier matrix D-stability studied in C-04/C-09/C-10.

## 1. Two different notions share nearly the same name

### A. Multiplicative matrix D-stability

The project uses the classical matrix-theory notion:

[
A	ext{ is D-stable}
iff
DA	ext{ is Hurwitz for every positive diagonal matrix }D.
]

Its fractional/generalized analogue is

[
Ain\mathcal F_\alpha
iff
\sigma(DA)\subset\Sigma_\alpha
quad\forall D\succ0.
]

Here **D is a positive diagonal multiplier**.

This is the tradition of Cain, Cross, Hartfiel, Abed, Kushel and generalized multiplier-region stability.

### B. Region / pole-domain \mathcal D-stability

A different control-theory terminology calls a system “D-stable” or “\mathcal D-stable” when the roots/poles of its characteristic equation lie in a prescribed region \mathcal D of the complex plane.

Here **\mathcal D is a desired pole region**, not a positive diagonal matrix.

This is the usage in the fractional robust-control papers below.

## 2. Shao et al. 2017

**Reference:** K. Shao, L. Zhou, K. Qian, Y. Yu, F. Chen, S. Zheng, “Necessary and sufficient D-stability condition of fractional-order linear systems,” 36th Chinese Control Conference (CCC), 2017, pp. 44–48. DOI: 10.23919/ChiCC.2017.8027318.

The title creates a serious keyword collision.

The full text was not available in the web sources used for this audit, so this note does not pretend to quote an unavailable theorem. However, the surrounding citation context is decisive enough to classify the terminology provisionally:

- the accessible record/citation context describes a **non-convex D-stability region for locating closed-loop poles**;
- later fractional robust-control papers in the same citation line treat D-stability through **root regions, characteristic polynomials, value sets, zero exclusion and pole-location domains**;
- no accessible evidence associates Shao et al. with the quantifier (DA) for every positive diagonal multiplier.

**Chief classification:** REGION-D-STABILITY / POLE-LOCATION PRIOR ART, not multiplicative matrix D-stability.

**Residual caution:** before submission, obtain the full conference paper or an authoritative indexed abstract and verify its formal definition. Until then, cite it only for fractional D-region stability, not for matrix D-stability.

## 3. Mohsenipour & Liu 2020 confirms the terminology line

**Reference:** R. Mohsenipour, X. Liu, “Robust D-Stability Test of LTI General Fractional Order Control Systems,” IEEE/CAA Journal of Automatica Sinica 7(3), 2020, 853–864. DOI: 10.1109/JAS.2020.1003159.

Its abstract explicitly formulates the problem through:

- roots of a closed-loop characteristic equation;
- “specific areas for the roots”;
- value sets of characteristic equations;
- uncertain coefficients/orders;
- a necessary-and-sufficient robust D-stability test.

That is a **root-location region** problem. It does not quantify over positive diagonal left multipliers of a state matrix.

The 2020 paper therefore provides strong secondary confirmation of the terminology used by the Shao citation line.

## 4. Consequence for C-09/C-10

These papers do **not** subsume the project’s core quantifier:

[
\sigma(DA)\subset\Sigma_\alpha
qquad
\forall D\succ0.
]

They may contain useful fixed-polynomial / fractional pole-region machinery, but they do not presently threaten:

- C-09: minimum dimension for a full-dimensional genuinely fractional positive-diagonal-orbit class;
- C-10: exact elimination of the positive diagonal orbit in dimension three through ((\beta_{12},\beta_{13},\beta_{23},\kappa)) and (T_\alpha(\beta)).

## 5. Writing rule for the manuscript

To avoid referee confusion, the paper must use explicit terminology such as:

> **positive-diagonal multiplicative D-stability**

or

> **D-stability under positive diagonal left scaling**

when first introducing the classical matrix concept.

When discussing control literature, use:

> **\mathcal D-region stability / pole-region stability**

for desired-region root placement.

Do not rely on the unqualified phrase “fractional D-stability” in the title or novelty statement without immediately defining which D is meant.

## Verdict

[
\boxed{\text{TERMINOLOGY COLLISION RESOLVED — NO CURRENT NOVELTY KILL}}
]

Shao 2017 remains a citation/check item, but available evidence places it in the pole-region \mathcal D-stability literature rather than the positive-diagonal multiplier D-stability literature.
