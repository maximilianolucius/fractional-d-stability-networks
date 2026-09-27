# Final Frozen-Claim Novelty Audit — C-09/C-10/C-15 + Caputo Double-Allee Realization

**Date:** 2026-09-26  
**Role:** Chief Researcher  
**Branch:** \`chief/final-frozen-novelty-20260926\`  
**Search horizon:** literature checked through 2026-09-26  
**Scope:** final theorem wording only; no model-first novelty claims

## Executive verdict

\`\`\`text
C-09  NOVEL WITH NARROWED CLAIM
C-10  NOVEL WITH NARROWED CLAIM
C-15  NOVEL WITH NARROWED CLAIM
C-16  NOT NOVEL / STRUCTURAL LEMMA
C-17  NOT NOVEL / FOUNDATION
C-18  NOVELTY SURVIVES TARGETED SEARCH
C-19  NOVELTY SURVIVES ONLY AT THEOREM-REALIZATION LEVEL
C-20  FLAGSHIP ECOLOGICAL NOVELTY SURVIVES TARGETED SEARCH
C-21  NOVELTY SURVIVES TARGETED SEARCH
C-22  NOVELTY SURVIVES TARGETED SEARCH
\`\`\`

**Overall:** \`FINAL NOVELTY GATE PASS WITH NARROWED WORDING\`.

No published source located in the final search gives the same theorem package:

\[
\text{all positive diagonal multipliers}
+
\text{Matignon sector}
+
\text{exact real 3x3 elimination}
+
\text{open non-GLV ecological realization}
+
\text{Allee-driven exact Cain crossing}.
\]

The project must nevertheless avoid any claim that the underlying Caputo/IGP/double-Allee model class is itself new.

---

# 1. Frozen mathematical object

For fixed \(0<\alpha<1\),

\[
\Sigma_\alpha
=
\{z\ne0:|\arg z|>\alpha\pi/2\},
\]

\[
\mathcal F_\alpha^{(n)}
=
\{
A\in\mathbb R^{n\times n}:
\sigma(DA)\subset\Sigma_\alpha
\quad
\forall D\succ0\text{ diagonal}
\}.
\]

The genuinely fractional class is

\[
\mathcal P_\alpha^{(n)}
=
\mathcal F_\alpha^{(n)}
\setminus
\mathcal D_H^{(n)}.
\]

The quantifier

\[
\forall D\succ0
\]

is essential. Ordinary local Matignon stability of one fixed Jacobian is not the same problem.

---

# 2. C-09 — minimum robust dimension

Frozen claim:

\[
\min
\left\{
n:
\operatorname{int}
\left(
\mathcal F_\alpha^{(n)}
\setminus
\mathcal D_H^{(n)}
\right)
\ne\varnothing
\right\}
=
3
\qquad
\forall\,0<\alpha<1.
\]

## Prior art that does not kill it

Published literature already contains:
- Matignon-type fractional spectral stability;
- classical multiplicative D-stability;
- P-matrix sector/eigenvalue bounds;
- exact low-dimensional classical D-stability;
- structured fractional network examples whose integer-order counterpart can be unstable.

No published source located states the exact minimum-dimension theorem with all of:

1. multiplicative positive-diagonal orbit;
2. Matignon stability;
3. exclusion of classical Hurwitz D-stability;
4. nonempty **full-dimensional interior**;
5. exact 2D obstruction;
6. every \(0<\alpha<1\).

## Verdict

**NOVEL WITH NARROWED CLAIM.**

Approved wording:

> We identify the minimum matrix dimension in which the genuinely fractional multiplicative-D-stable class has nonempty full-dimensional interior, and prove that it is three for every \(0<\alpha<1\).

Never shorten this to “dimension three is the first dimension with fractional stabilization.”

---

# 3. C-10 — exact real 3x3 positive-diagonal Matignon threshold

On the strict-P\((-A)\) stratum,

\[
p_i=-a_{ii}>0,
\qquad
m_{ij}>0,
\qquad
q=-\det A>0,
\]

\[
\beta_{ij}
=
\frac{m_{ij}}{p_ip_j},
\qquad
\kappa
=
\frac{q}{p_1p_2p_3}.
\]

For \(2/3<\alpha<1\),

\[
A\in\mathcal F_\alpha^{(3)}
\iff
\kappa<T_\alpha(\beta),
\]

where

\[
T_\alpha(\beta)
=
\min_{x\in\Delta_2^\circ}
\frac{h_\alpha(B_\beta(x))}
{x_1x_2x_3}.
\]

At \(\alpha=1\),

\[
T_1(\beta)
=
\left(
\sqrt{\beta_{12}}
+
\sqrt{\beta_{13}}
+
\sqrt{\beta_{23}}
\right)^2.
\]

## Strongest prior-art threat

Kushel and Pavani give a published generalized multiplicative D-stability framework for unbounded LMI regions, including a necessary-and-sufficient forbidden-boundary condition for conic regions and complements of conic regions.

Therefore C-10 is **not**:
- the first generalized D-stability formulation;
- the first all-positive-diagonal region criterion;
- the first necessary-and-sufficient abstract criterion.

Cain already gives the exact classical real 3x3 all-D threshold at \(\alpha=1\), including homogeneous minimization over diagonal multipliers.

Fixed-polynomial fractional Routh-Hurwitz / sector root-location theory is also known.

## What remains new in the search

No published source located explicitly eliminates the entire positive-diagonal multiplier orbit for arbitrary strict-P real 3x3 matrices in the Matignon problem to the four invariant coordinates

\[
(\beta_{12},\beta_{13},\beta_{23},\kappa)
\]

and the scalar iff threshold

\[
\kappa<T_\alpha(\beta).
\]

## Verdict

**NOVEL WITH NARROWED CLAIM.**

Approved wording:

> For real \(3\times3\) matrices on the strict-P\((-A)\) stratum, we explicitly eliminate the complete positive-diagonal multiplier orbit from the Matignon generalized-D-stability problem, obtaining the necessary-and-sufficient four-invariant threshold \(\kappa<T_\alpha(\beta)\).

Forbidden wording:

> “first necessary-and-sufficient criterion for fractional D-stability.”

---

# 4. C-15 — geometry of the exact threshold

Frozen contribution:
- strict convexity of the specific C-10 objective in logit coordinates;
- unique nondegenerate optimizer;
- smooth parameter dependence;
- global threshold-surface geometry;
- exact symmetric slice;
- \(\alpha\to1^-\) asymptotic;
- \(\alpha\downarrow2/3^+\) asymptotic;
- realizability of the full difference band.

Generic:
- logit coordinates;
- log-sum-exp convexity;
- geometric programming;
- convex optimization.

are not novelty.

No published source located gives this geometric package for the specific \(T_\alpha(\beta)\) generated by the exact all-D Matignon problem.

## Verdict

**NOVEL WITH NARROWED CLAIM.**

Approved wording:

> We prove that the threshold functional generated by the exact three-dimensional Matignon D-orbit problem has a strictly convex logit representation, a unique nondegenerate optimizer, and a smooth global threshold geometry.

---

# 5. C-16/C-17 — explicitly non-novel foundations

## C-16

General positive-diagonal simplex normalization via characteristic-polynomial principal minors is a structural lemma.

**Verdict:** NOT NOVEL.

## C-17

For a Kolmogorov system

\[
{}^CD_t^\alpha x_i=x_iF_i(x)
\]

at a positive equilibrium,

\[
J(x^*)=\operatorname{diag}(x^*)DF(x^*),
\]

and multiplication by the equilibrium diagonal merely reparametrizes the positive-diagonal orbit.

This is elementary and consistent with established Kolmogorov linearization / D-stability literature.

**Verdict:** FOUNDATION / NOT NOVEL.

---

# 6. Current published ecological prior art is substantially occupied

The final search deliberately targeted recent published 2025–2026 literature.

## Fractional IGP already exists

Published examples include:

- Prabir Panja (2019), *Dynamics of a fractional order predator-prey model with intraguild predation*, International Journal of Modelling and Simulation 39(4), 256–268, DOI 10.1080/02286203.2019.1611311.
- A. B. Munde and G. A. Birajdar (2026), *Analysis of a Fractional Order Three Species Food Web Model*, Dynamics of Continuous, Discrete and Impulsive Systems Series B 33(3), 143–155.
- Prajjwal Gupta, Satyabhan Singh, Anupam Priyadarshi (2026), *Periodic structures and memory–fear interactions in a fractional order intraguild predation model*, International Journal of Modelling and Simulation, published online 22 July 2026, DOI 10.1080/02286203.2026.2703016.

These papers study fixed-model feasibility, local stability, bifurcation and numerical dynamics. They do not formulate the all-positive-diagonal Matignon orbit problem.

## Allee + IGP already exists

Bai, Kang, Ruan and Wang (2021) study a three-species IGP food web with a strong Allee effect in the basal prey, including multiple interior equilibria, stability and bifurcation structure.

Hence:
- IGP is not new;
- 3D IGP + Allee is not new.

## Fractional + double Allee already exists

Published fractional double-Allee ecological models include:
- Rahmi et al. (2023), fractional Leslie–Gower eco-epidemiological model with double Allee effect, DOI 10.1155/2023/5030729;
- Mondal et al. (2025), Caputo predator-prey dynamics with double Allee effects, DOI 10.1007/s10867-025-09670-0;
- Alraddadi, Ahmed and Seol (2026), fractional/discrete double-Allee predator-prey dynamics, DOI 10.3390/fractalfract10050304;
- Tassaddiq et al. (2026), double-Allee predator-prey stability/dynamics, DOI 10.3934/math.2026048.

Thus the manuscript must not sell:
- Caputo ecology;
- fractional IGP;
- a 3D fractional food web;
- double Allee effects;
- memory-induced stabilization;
- ordinary local Matignon stability.

as contributions.

---

# 7. C-18 — competitive two-consumer no-go

Frozen theorem:

For the natural double-Allee prey + two competing consumers architecture, the exact invariant identities force

\[
\kappa<T_1(\beta)
\]

throughout the relevant strict-P stratum.

Therefore this architecture cannot realize the open genuinely fractional-only C-10 band.

## Search outcome

The literature contains many competitive predator/prey, Allee and food-web stability studies, but no published source located derives this exact invariant obstruction relative to the positive-diagonal Cain/Matignon thresholds.

## Verdict

**NOVELTY SURVIVES TARGETED SEARCH.**

Position as a structural negative theorem, not as a claim that the ecological architecture itself is new.

---

# 8. C-19 — exact IGP invariant realization

Frozen theorem-level result:

For the adopted double-Allee IGP architecture,

\[
\beta_{12},
\beta_{13},
\beta_{23},
\kappa,
L_3
\]

have exact biological formulas, and the parameterization constructively realizes an open four-dimensional family of C-10 invariants.

## Threat analysis

Published fractional IGP papers establish local stability and rich nonlinear dynamics, but no located paper:
- passes to the complete positive-diagonal orbit;
- derives the C-10 invariant coordinates;
- proves a right inverse onto an open four-dimensional invariant family.

## Verdict

**NOVELTY SURVIVES ONLY AT THE THEOREM-REALIZATION LEVEL.**

Forbidden:
> “We introduce a novel fractional IGP model.”

Approved:
> “We give a constructive ecological realization of the exact four-invariant Matignon D-stability geometry.”

---

# 9. C-20 — open biological fractional-only region

Frozen flagship ecological theorem:

For every fixed

\[
0<\alpha<1,
\]

there exists a nonempty open set in the **full biological parameter space** for which a positive coexistence equilibrium satisfies

\[
J\in
\mathcal F_\alpha^{(3)}
\setminus
\mathcal D_H^{(3)}.
\]

## Why current fractional ecology does not subsume it

Published fractional ecological papers generally evaluate Matignon stability for the Jacobian associated with one model/parameter point or derive parameter conditions for that fixed system.

The frozen theorem instead demands

\[
\sigma(DJ)\subset\Sigma_\alpha
\qquad
\forall D\succ0,
\]

and proves that this all-D property occupies an open set in the full biological parameter space while classical all-D Hurwitz stability fails.

No published ecological paper located establishes that combination.

## Verdict

**FLAGSHIP ECOLOGICAL NOVELTY SURVIVES TARGETED SEARCH.**

This should be one of the central claims of the paper.

---

# 10. C-21 — Double-Allee threshold crossing of Cain's boundary

Frozen result:

Along the positive strict-P coexistence branch,

\[
\frac{dX}{dm}<0,
\qquad
\frac{ds}{dm}<0,
\qquad
\frac{d}{dm}\left(\frac1s\right)>0.
\]

The induced invariant path can be tuned to cross the exact classical Cain boundary once and transversally. With every non-\(m\) biological parameter fixed,

\[
m<m_0
\]

is classically D-stable locally on one side, while

\[
m>m_0
\]

enters the fractional-only positive-diagonal Matignon-stable band.

## Threat analysis

Published Allee literature extensively studies Allee-threshold-driven:
- equilibrium existence;
- extinction;
- local stability;
- Hopf and saddle-node bifurcations;
- multistability;
- chaos.

No published source located interprets an Allee parameter as a monotone path through exact positive-diagonal invariants and proves a transverse crossing of Cain's all-D boundary into a Matignon-only all-D region.

## Verdict

**NOVELTY SURVIVES TARGETED SEARCH.**

This is the strongest biologically interpretable mechanism in the paper.

---

# 11. C-22 — exact 2D/3D ecological contrast

Frozen result:
- corresponding 2D double-Allee system: fractional-only positive-diagonal difference is codimension one;
- 3D IGP system: fractional-only class contains a nonempty open biological region.

Existing fractional 2D double-Allee studies do not formulate this dimension/interior comparison under all positive diagonal scalings.

## Verdict

**NOVELTY SURVIVES TARGETED SEARCH.**

Use as a corollary and narrative closure, not as a standalone title claim.

---

# 12. Published ecological D-stability literature does not kill the result

The 2024 Physics Reports review on ecological stability explicitly treats classical D-stability as stability under arbitrary positive diagonal scaling and notes its role in ecological robustness.

This is important prior art and should be cited.

It strengthens, rather than weakens, the positioning:
- all-D robustness is a recognized ecological concept;
- the project extends the exact robustness question to the Matignon sector;
- the new part is the exact fractional 3D solution and nonlinear ecological realization, not the concept of D-stability itself.

---

# 13. Final approved novelty narrative

The paper should be positioned as:

> Classical generalized D-stability already provides the quantified framework, and Cain gives the exact real \(3\times3\) half-plane endpoint. We solve the corresponding real \(3\times3\) positive-diagonal Matignon problem explicitly on the strict-P stratum, obtaining an exact four-invariant threshold and its convex geometry. We then prove that the resulting genuinely fractional band is not merely an abstract matrix phenomenon: a nonlinear Caputo double-Allee intraguild-predation Kolmogorov system constructively realizes a full-dimensional open subset of that band, while a natural competing-consumer architecture is structurally excluded. Finally, the Allee threshold itself generates a monotone invariant path that crosses the exact classical Cain boundary into the fractional-only robust region.

This narrative is accurate relative to the published literature located in the final search.

---

# 14. Forbidden priority language

Do not write:
- “the first fractional D-stability criterion”;
- “the first necessary-and-sufficient generalized D-stability theorem”;
- “the first fractional IGP model”;
- “a new double-Allee model”;
- “the first demonstration that memory stabilizes an ecological system”;
- “the first 3D fractional food-web stability analysis”;
- “fractional ecology had not considered IGP”;
- “prior work cannot handle the nonconvex Matignon region.”

All are contradicted or too broad relative to published prior art.

---

# 15. Safe contribution language for abstract/introduction

Safe:

1. **Exact 3D matrix result**
   > We explicitly eliminate the complete positive-diagonal multiplier orbit for real \(3\times3\) matrices on the strict-P stratum, reducing Matignon D-stability to an exact four-invariant threshold.

2. **Dimension result**
   > We prove that dimension three is the minimum dimension in which the genuinely fractional multiplicative-D-stable class has nonempty full-dimensional interior.

3. **Threshold geometry**
   > The exact threshold has a strictly convex logit representation with a unique smooth optimizer and explicit classical/low-order limits.

4. **Ecological realization**
   > A nonlinear Caputo double-Allee IGP Kolmogorov system constructively realizes a full-dimensional open subset of the fractional-only class.

5. **Mechanism**
   > Varying only the Allee threshold moves the fixed biological system transversally across Cain's classical D-stability boundary into the fractional-only Matignon region.

---

# 16. Final novelty gate

\`\`\`text
MATRIX NOVELTY:               PASS WITH NARROWED WORDING
DIMENSION THEOREM:            PASS
C-10 EXACT ELIMINATION:       PASS
C-15 THRESHOLD GEOMETRY:      PASS
GENERIC CAPUTO ECOLOGY:       NOT NOVEL
FRACTIONAL IGP MODEL:         NOT NOVEL
DOUBLE-ALLEE MODEL:           NOT NOVEL
COMPETITIVE NO-GO:            SURVIVES SEARCH
4D ECOLOGICAL REALIZATION:    SURVIVES SEARCH
OPEN BIOLOGICAL ALL-D BAND:   SURVIVES SEARCH
ALLEE/CAIN CROSSING:          SURVIVES SEARCH
2D/3D ECOLOGICAL CONTRAST:    SURVIVES SEARCH

OVERALL:
FINAL NOVELTY GATE PASS WITH NARROWED WORDING
\`\`\`

No final claim should use absolute priority language beyond the precise search-supported formulations above.
