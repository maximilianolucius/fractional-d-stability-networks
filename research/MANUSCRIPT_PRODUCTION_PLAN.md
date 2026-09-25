# Q1 Manuscript Production Plan

**Date:** 2026-09-25  
**Branch:** \`q1-manuscript-20260925\`  
**Scientific state:** novelty gate passed with repositioning; proof gate passed; compute gate passed.

## 1. Locked scientific thesis

The manuscript is about an **explicit exact real-3x3 solution of the positive-diagonal generalized-D-stability problem for the commensurate Matignon reflex sector**, not about introducing fractional D-stability.

The central theorem package is:

1. C-07 — exact real 2x2 classification and empty full-dimensional genuinely fractional interior.
2. C-10 — exact real 3x3 elimination:
   \[
   A\in\mathcal F_\alpha^{(3)}
   \iff
   \kappa<T_\alpha(\beta),
   \qquad
   2/3<\alpha<1,
   \]
   on the strict-P(-A) stratum.
3. C-15 — strict convexity, unique optimizer, explicit threshold-surface parametrization, realizability, and the alpha->2/3 asymptotic.
4. C-09 — minimum robust genuinely fractional dimension:
   \[
   \min\{n:\operatorname{int}(\mathcal F_\alpha^{(n)}\setminus\mathcal D_H^{(n)})\ne\varnothing\}=3.
   \]
5. C-14 — sharp alpha->1 collapse rate.
6. C-12/C-13 — GLV abundance invariance and exact motif coordinates/sensitivities.

C-16 is supporting structural machinery only and carries **no novelty claim**.

## 2. Mandatory prior-art positioning

The introduction and theorem discussion must explicitly credit:

- Matignon / modern Caputo restatements for the fractional angular criterion;
- Kushel for generalized matrix stability;
- Kushel–Pavani for the abstract all-positive-diagonal forbidden-boundary N&S framework for conic regions/complements;
- Cain 1976 for the exact real 3x3 classical D-stability threshold mechanism;
- Bahl–Cain 1977 for exact real 3x3 inertia preservation under all positive diagonal multipliers;
- Kellogg for the P-matrix eigenvalue wedge;
- Cermak–Nechvatal and Bourafa et al. for fixed-polynomial fractional root-location theory;
- Siami for the single-cycle fractional secant threshold, recovered as the symmetric slice.

## 3. Forbidden novelty language

Do not write:

- "we introduce fractional D-stability";
- "the first necessary-and-sufficient generalized D-stability criterion";
- "the first treatment of nonconvex Matignon regions";
- "C-16 is novel";
- "fractional stabilization first appears in dimension three".

Approved language:

> We give an explicit exact real-3x3 elimination of the positive-diagonal generalized-D-stability problem for the Matignon reflex sector on the strict-P(-A) stratum.

For C-09:

> Dimension three is the smallest real matrix dimension in which the genuinely fractional positive-diagonal Matignon-stability difference from classical Hurwitz D-stability has nonempty full-dimensional interior.

## 4. Recommended paper spine

### Section 1 — Introduction
- classical D-stability;
- fractional Matignon stability;
- generalized region D-stability prior art;
- precise unresolved low-dimensional question;
- contributions.

### Section 2 — General orbit reduction and notation
- positive diagonal left action;
- definitions of F_alpha, D_H and P_alpha;
- standard principal-minor coefficient formula;
- C-16 as a lemma;
- GLV abundance-orbit equivalence.

### Section 3 — Dimension two
- exact C-07 theorem;
- empty interior of P_alpha^(2).

### Section 4 — Dimension three: exact Matignon threshold
- strict-P(-A) robust stratum;
- four orbit invariants;
- normalized simplex;
- fixed cubic boundary;
- C-10 iff theorem.

### Section 5 — Geometry of the threshold
- C-15 strict logit convexity;
- unique optimizer;
- symmetric/two-equal slices;
- global threshold-surface parametrization;
- realizability.

### Section 6 — Classical and low-order limits
- exact recovery of Cain at alpha=1;
- exact fractional band T1<kappa<Talpha;
- C-14 alpha->1 rate;
- alpha->2/3+ blow-up;
- C-09 minimum dimension theorem;
- C-11 only as a simple closed-form sufficient corollary.

### Section 7 — Ecological network interpretation
- GLV J=diag(x*)A;
- beta_ij pair loops;
- kappa / L3 three-cycle identity;
- exact sensitivity dT/dbeta;
- theorem-driven phase diagrams.

### Section 8 — Computational validation
- 121 tests;
- 2.18M adversarial/control cases;
- 56,234 HP rechecks;
- 60 interval-certified threshold anchors;
- 8,100 direct ecological classifications;
- clearly state that computation corroborates but does not prove the theorems.

### Section 9 — Discussion
- relation to Cain/Bahl-Cain/Kushel-Pavani/Siami;
- why n=3 is the first exact robust case;
- what becomes harder at n=4;
- limitations.

### Section 10 — Conclusion

## 5. Figure plan

1. Matignon reflex sector vs classical left half-plane.
2. n=2 obstruction vs n=3 nonempty full-dimensional band.
3. normalized simplex and C-10 objective.
4. exact threshold surface / unique optimizer geometry.
5. T_alpha vs alpha with both asymptotic regimes.
6. Cain surface vs exact fractional surface.
7. ecological loop phase diagram.
8. C-11 sufficient sub-band versus exact C-10 band.

## 6. Tables

1. Prior-art comparison table.
2. Theorem/claim map.
3. Canonical certified witness matrices.
4. Computational validation summary.

## 7. Manuscript discipline

- Theorems first; numerical evidence second.
- Every proof must be self-contained modulo explicitly imported theorems.
- No Monte Carlo language in theorem statements.
- Every figure must correspond to a theorem/corollary/interpretation.
- Every load-bearing citation must be verified against a primary source or publisher record.
- Final body target: concise mathematical paper, approximately 25–35 journal pages before supplement, unless target journal dictates otherwise.

## 8. Current production order

1. replace the obsolete paper scaffold;
2. populate verified bibliography;
3. draft Sections 2–6 first;
4. draft Introduction only after theorem narrative is frozen;
5. draft ecology/compute sections;
6. abstract and title last;
7. internal referee pass;
8. journal targeting and formatting.
