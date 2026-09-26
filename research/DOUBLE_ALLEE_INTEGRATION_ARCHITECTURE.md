# Chief architecture decision memo — integrating the Double-Allee theorem package

**Date:** 2026-09-26  
**Status:** conditional on second independent audit PASS  
**Chief branch:** `chief/double-allee-kolmogorov-20260926`

## Decision

If the second independent audit also passes, the preferred strategy is:

# **MAJOR EXTENSION OF THE CURRENT C-10 PAPER**

not a separate application paper.

The Double-Allee IGP theorem package is mathematically dependent on C-10/C-15 and supplies exactly what the current manuscript architecture lacks: a non-GLV biological realization theorem proving that the invariant fractional-only band is not merely formal matrix geometry.

A standalone paper remains a fallback if journal length or scope becomes problematic.

---

# 1. Why integration is stronger than separation

The current C-10 paper already proves:

- exact 2D obstruction;
- exact real 3×3 positive-diagonal Matignon threshold;
- strict convex threshold geometry;
- recovery of Cain;
- minimum robust dimension 3;
- abstract ecological loop coordinates.

Its ecological section is currently interpretive.

The Double-Allee package adds:

1. a natural ecological architecture that **fails** structurally;
2. a standard ecological architecture that **succeeds** for an exact signed-cycle reason;
3. a constructive map from biological parameters to the four C-10 invariants;
4. a proof of a full-dimensional open biological fractional-only region;
5. an exact ecological parameter crossing of the classical Cain boundary;
6. an exact 2D/3D biological contrast.

This converts the ecology from interpretation into theorem-level realization.

That makes the central C-10 matrix theorem more compelling rather than creating an unrelated application.

---

# 2. What should be removed/replaced from the old architecture

The previous Section 7:

> Ecological network interpretation

should no longer be a stand-alone motif-discussion section.

Replace it with:

# **Ecological realization beyond GLV: a Double-Allee intraguild-predation theorem**

The generic loop identities from C-13 become preliminaries inside that section.

Do not spend pages on generic ecological phase diagrams if the theorem section is present.

---

# 3. Proposed final theorem spine

## Part I — exact matrix theory

### Theorem A — 2×2 obstruction
C-07.

### Theorem B — exact 3×3 Matignon positive-diagonal characterization
C-10.

### Theorem C — threshold geometry
C-15.

### Corollary D — Cain limit and genuinely fractional band
C-10/C-14.

### Corollary E — minimum dimension 3
C-09.

This remains the mathematical core.

---

## Part II — exact ecological realization

### Proposition F — Kolmogorov orbit equivalence

At a positive equilibrium:

~~~text
J=diag(x*) DF(x*).
~~~

This is standard and should be presented as a bridge lemma, not novelty.

### Theorem G — competitive architecture no-go

The natural double-Allee prey + two competing consumers architecture satisfies

~~~text
kappa<T1(beta)
~~~

throughout its positive-beta strict-P domain.

Interpretation:

> same-sign directed 3-cycles cannot generate the robust fractional-only band.

This theorem is valuable because it shows that not every biologically reasonable 3D extension realizes C-10.

### Theorem H — IGP invariant realization

For the selected Double-Allee IGP architecture, derive exact

~~~text
beta12,beta13,beta23,kappa,L3
~~~

and prove the four-dimensional invariant realization theorem.

This is the structural ecological theorem.

### Theorem I — open genuinely fractional biological region

For every

~~~text
0<alpha<1,
~~~

there is a nonempty open set in the full biological parameter space for which a positive coexistence branch satisfies

~~~text
J in F_alpha^(3) \ D_H^(3).
~~~

This should be the flagship ecological theorem.

### Theorem J — Double-Allee transversality

With all other biological parameters fixed, the Allee threshold m can be tuned so that:

~~~text
m<m0  -> classical D-stable,

m=m0  -> exact Cain boundary,

m>m0  -> fractional-only D-stable
~~~

locally.

Include the explicit monotone mechanism

~~~text
ds/dm<0,
dt/dm>0.
~~~

### Corollary K — exact 2D/3D contrast

The corresponding 2D Double-Allee predator–prey system has genuinely fractional D-stability only on the codimension-one set

~~~text
g_DA'(X)=0,
~~~

while the 3D IGP model has a nonempty open fractional-only region.

This is a particularly strong closing result.

---

# 4. Suggested paper section order after integration

1. **Introduction**
2. **Generalized positive-diagonal Matignon framework**
3. **Dimension two**
4. **Exact dimension-three reduction**
5. **Exact threshold and convex geometry**
6. **Cain limit, memory width and minimum dimension**
7. **Double-Allee Kolmogorov realization**
   - bridge lemma;
   - naive architecture no-go;
   - IGP model;
   - invariant realization;
   - open-region theorem;
   - m crossing;
   - 2D/3D contrast.
8. **Certified numerical illustration**
9. **Discussion**
10. **Conclusion**

The ecological theorem section should be mathematically substantive but compact.

Long symbolic derivations and interval-certification details can go to the supplement.

---

# 5. What not to add

Do not turn the extended paper into a standard nonlinear-dynamics survey.

Exclude unless needed for theorem illustration:

- Hopf bifurcation catalogs;
- chaos diagrams;
- period-doubling;
- arbitrary time-series simulations;
- parameter sweeps unrelated to the exact D-stability boundary;
- ecological claims beyond the mathematical model.

Those topics are already heavily occupied in the fractional IGP/Allee literature and would dilute the novelty.

---

# 6. Figure plan after extension

A compact set is enough:

1. Matignon versus Hurwitz region.
2. Exact C-10 threshold geometry.
3. 2D versus 3D robust-interior schematic.
4. Two ecological motif diagrams:
   - failed competitive two-consumer motif;
   - successful IGP motif with opposite-sign 3-cycles.
5. Exact m-crossing plot:
   - kappa(m);
   - T1(beta(m));
   - T_alpha(beta(m)).
6. Certified interior biological point / interval, preferably around m≈0.35 rather than m=0.21.
7. Optional invariant-space path generated by m.

No decorative bifurcation plots.

---

# 7. Preferred example for the manuscript

Retain:

~~~text
m0=0.2
~~~

only as the exact symbolic classical-boundary anchor.

For the robust fractional-only numerical example choose an interior value such as

~~~text
m≈0.30–0.40
~~~

subject to re-certification after the second audit.

Reason:
- larger Cain margin;
- less visual impression of a boundary artifact;
- better parameter robustness;
- still belongs to the same fixed biological model.

The first compute audit already certifies

~~~text
m in [0.2005,0.45]
~~~

with all other parameters fixed.

---

# 8. Title strategy if integrated

Do not put “Double Allee” at the front of the title. The paper remains a matrix-theory paper with an exact ecological realization.

Preferred forms:

1. **Exact Positive-Diagonal Matignon Stability in Dimension Three with a Double-Allee Ecological Realization**
2. **From Cain to Matignon: Exact Three-Dimensional D-Stability Thresholds and a Nonlinear Ecological Realization**
3. **Fractional D-Stability Beyond Hurwitz Stability: Exact Three-Dimensional Theory and Double-Allee Kolmogorov Realization**

The second is currently the strongest balance.

---

# 9. Standalone-paper fallback

Split the extension into a separate paper only if one of these occurs:

1. target journal has a severe page/word limit;
2. reviewers/editors strongly prefer a purely matrix-theory submission;
3. the Double-Allee theorem requires too much ecological setup to remain concise;
4. the second proof audit identifies caveats that weaken its role as a clean corollary/application of C-10.

A standalone applied-math paper would then center:

~~~text
no-go architecture
-> signed-cycle mechanism
-> invariant realization
-> open biological region
-> Allee-threshold crossing
-> 2D/3D contrast.
~~~

---

# 10. Current architecture verdict

Pending the second independent audit:

~~~text
INTEGRATE INTO CURRENT PAPER: PREFERRED
STANDALONE PAPER:             FALLBACK
MANUSCRIPT DRAFTING:          STILL LOCKED
~~~

The extension materially strengthens the existing paper because it converts an abstract ecological interpretation into a non-GLV realization theorem with an open biological parameter set and a directly interpretable control parameter.
