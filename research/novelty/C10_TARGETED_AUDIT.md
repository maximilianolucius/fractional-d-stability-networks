# C-10 targeted novelty audit — final specialist update

**Date:** 2026-09-25  
**Status:** supersedes the provisional 2026-09-24 positioning where inconsistent  
**Final C-10 verdict:** **NOVEL WITH NARROWED CLAIM**  
**Overall gate context:** see `FINAL_C10_C15_SPECIALIST_AUDIT.md`

## Exact object

On the real 3×3 strict-P(-A) stratum, define

```text
p_i  = -a_ii > 0
m_ij = det A[{i,j}] > 0
q    = -det A > 0

β_ij = m_ij/(p_i p_j)
κ    = q/(p_1 p_2 p_3).
```

For every positive diagonal D, the orbit modulo common positive scale is represented by x in the open 2-simplex and the normalized characteristic polynomial is

```text
z^3 + z^2 + B_β(x) z + κ x_1x_2x_3,

B_β(x)
 = β_12 x_1x_2
 + β_13 x_1x_3
 + β_23 x_2x_3.
```

For 2/3 < α < 1, the project proves

```text
A ∈ F_α^(3)
iff
κ < T_α(β),

T_α(β)
 = min_x h_α(B_β(x))/(x_1x_2x_3).
```

At α=1,

```text
T_1(β)
 = (sqrt(β_12)+sqrt(β_13)+sqrt(β_23))^2,
```

recovering the strict-P classical Cain threshold.

---

# 1. New final-audit correction: Kushel–Pavani already give the abstract N&S theorem

The previous targeted audit correctly identified Kushel–Pavani as the closest framework but understated the exactness of the overlap.

In *The problem of generalized D-stability in unbounded LMI regions and its computational aspects* (arXiv:2004.11172; later JDDE), the authors define generalized multiplicative D-stability with the quantifier over **every positive diagonal multiplier**.

Their forbidden-boundary theorem gives the usual equivalence:

```text
region-D-stability
iff
initial region stability + no boundary crossing for any positive diagonal D.
```

More importantly, **Theorem 3.3 explicitly gives equivalent necessary-and-sufficient conditions for a conic region and for the complement of the closed conic region**, including determinant nonvanishing conditions for every positive diagonal D.

After the sign substitution B=-A:

- the project Matignon region Σ_α is the complement of a positive cone of half-angle θ=απ/2;
- σ(DB)=-σ(DA);
- hence B is required to remain in the complement of the corresponding negative cone under every positive diagonal multiplier.

Therefore C-10 must **not** be described as:

- the first necessary-and-sufficient criterion for fractional multiplicative D-stability;
- the first treatment of the nonconvex Matignon complement under positive diagonal scaling;
- the first forbidden-boundary characterization.

Those claims are occupied.

### What C-10 adds beyond Theorem 3.3

Kushel–Pavani leave the universal D quantifier in the condition. They do not derive for arbitrary real strict-P(-A) 3×3 matrices:

```text
(β_12,β_13,β_23,κ)
    +
a two-dimensional simplex
    +
an explicit fixed-cubic Matignon boundary
    =>
κ < T_α(β).
```

Thus the surviving novelty is **explicit low-dimensional elimination**, not existence of an abstract N&S framework.

---

# 2. Cain 1976 is more structurally overlapping than the previous audit stated

Cain does not merely give an α=1 final criterion.

For D=diag(x,y,z), his proof writes the Routh–Hurwitz all-D condition as a homogeneous expression involving:

- the order-one principal minors;
- the order-two principal minors;
- det A;
- x,y,z.

He then minimizes the resulting homogeneous ratio over x,y,z>0 and obtains the exact determinant threshold.

Therefore the following C-10 ingredients are already classical at α=1:

1. write all-D stability through principal-minor coefficient formulas;
2. quotient out common positive scale through homogeneity;
3. reduce to an optimization over diagonal ratios;
4. obtain an exact determinant threshold.

C-10 should be presented explicitly as an **α-dependent Matignon deformation / extension of Cain's exact 3×3 mechanism**, not merely as a theorem whose endpoint happens to equal Cain.

What is not in Cain is the angular Matignon boundary for α<1, including right-half-plane points, or the threshold T_α(β).

---

# 3. Bahl–Cain 1977 remains close but non-equivalent

Bahl–Cain characterize real 3×3 matrices for which MD has prescribed inertia under every positive diagonal D.

That theorem is exact and uses principal minors, but inertia sees only counts in left/right half-planes. It cannot distinguish:

```text
απ/2 < |arg λ| <= π/2
```

from

```text
0 < |arg λ| <= απ/2
```

inside the right half-plane.

Therefore replacing “inertia” by “Matignon angle” is not a formal specialization. The angular root-boundary calculation and threshold deformation are genuinely additional mathematics.

---

# 4. Fixed cubic h_α is not the novelty target

Fractional Routh–Hurwitz and sector-stable polynomial literature already covers substantial fixed-polynomial root-location territory:

- Čermák–Nechvátal;
- Bourafa–Abdelouahab–Moussaoui;
- Joya–Furuta domain/sector-stable polynomial coefficient descriptions;
- Holtz–Khrushchev–Kushel forbidden-sector polynomial results.

The paper should therefore treat the exact cubic boundary function h_α as a component lemma, not as an independent priority claim, unless an exhaustive theorem-level comparison establishes otherwise.

The candidate novelty is its combination with the entire positive-diagonal matrix orbit.

---

# 5. Siami is exactly the symmetric structured slice

For the single negative-feedback 3-cycle,

```text
β = (1,1,1).
```

C-15 gives

```text
T_α(1,1,1) = 1 + R_3(α)^3,
```

equivalent to Siami's cycle threshold.

This is important prior art, but it does not exhaust C-10:

- β is invariant under positive left-diagonal scaling;
- principal minors, hence β and κ, are invariant under diagonal similarity;
- generic positive β triples cannot be converted to (1,1,1) by those transformations.

Thus Siami is a one-dimensional/symmetric invariant slice of the general threshold surface.

---

# 6. Kushel 2016 D_theta is not an angular-sector collision

The paper *On a criterion of D-stability for P-matrices* uses θ as a permutation/order of indices.

A diagonal matrix is θ-ordered when its diagonal entries satisfy that order, and D_θ-stability means stability for all such ordered diagonal multipliers.

It has no spectral-angle θ and does not subsume C-10.

---

# 7. Fractional “D-stability” terminology

Mohsenipour–Liu 2020 was verified from its primary publisher record: its “robust D-stability” concerns uncertain characteristic equations, root/value sets and prescribed pole regions.

It is D-**region** stability, not

```text
σ(DA) ⊂ Σ_α  for every positive diagonal D.
```

Shao et al. 2017 remains a bibliographic access flag: title/DOI/proceedings record are verified, but the primary body was not retrieved. All accessible citation context places it in the same D-region/pole-location line. This does not block the C-10 novelty conclusion because the much stronger multiplicative-D generalized theorem of Kushel–Pavani has already been compared directly.

---

# 8. Final novelty boundary for C-10

## Already occupied

Do not claim novelty for:

- generalized multiplicative D-stability;
- arbitrary-region multiplier frameworks;
- forbidden-boundary N&S theory for a cone or its complement;
- principal-minor characteristic-coefficient formulas;
- homogeneous optimization over positive diagonal ratios at α=1;
- Cain's 3×3 classical threshold;
- Bahl–Cain inertia classifications;
- fixed-cubic fractional/sector root localization;
- Siami's single-cycle fractional secant threshold.

## Surviving candidate contribution

The defensible claim is:

> For arbitrary real 3×3 matrices on the full-dimensional strict-P(-A) stratum, the complete positive-diagonal Matignon generalized-D-stability problem can be **explicitly solved** by eliminating the universal diagonal multiplier and reducing it to four orbit invariants and the exact scalar inequality κ<T_α(β). This yields the exact genuinely fractional band between the classical Cain surface and the fractional threshold surface.

No theorem equivalent to that explicit elimination was located in the final specialist search.

---

# 9. Approved final verdict

## **C-10: NOVEL WITH NARROWED CLAIM**

Recommended paper language:

> “We give an explicit exact real-3×3 solution of the positive-diagonal generalized-D-stability problem for the Matignon reflex sector on the strict-P(-A) stratum.”

Avoid:

> “We introduce fractional D-stability.”

Avoid:

> “We give the first necessary-and-sufficient generalized-D-stability criterion.”

Avoid:

> “Prior work cannot treat the nonconvex Matignon region.”

For full source verification and final C-09/C-15/C-16 verdicts, see:

- `FINAL_C10_C15_SPECIALIST_AUDIT.md`
- `FINAL_BIBLIOGRAPHY_VERIFICATION.md`
- `../NOVELTY_MATRIX.md`
