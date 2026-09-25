# P6 — n = 4: two directed 3-cycles sharing an edge (EXPLORATORY, future-paper material)

Scripts: `computations/scripts/wave2/w2_p6_n4_shared_edge.py`, `w2_p6_verify.py`.
Data: `N4_SHARED_EDGE_DATA.json`, `N4_SHARED_EDGE_BOUNDARY.csv`, `N4_SHARED_EDGE_VERIFY.json`.
Nothing here is part of the current Q1 manuscript claims.

## 1. Invariant parametrisation

Nodes 1..4, negative unit diagonal, cycle A = 1→2→3→1, cycle B = 1→2→4→1 sharing the edge 1→2.
Positive diagonal similarity normalises a21 = a32 = a42 = 1, leaving two parameters

    a13 = −s,   a14 = −t        (s, t > 0: both cycles negative feedback; s, t > −1 keeps −A strict P).

C-16 invariants of the family: all six pair invariants β_ij = 1 (no reciprocal pairs),
β_123 = 1 + s, β_124 = 1 + t, β_134 = β_234 = 1, κ₄ = 1 + s + t.  So the family is exactly the
two-parameter slice {no 2-cycles, two loaded triples} of the 4×4 invariant space, and by C-16 the
positive-diagonal orbit is captured by the normalised quartic on the 3-simplex

    λ⁴ + λ³ + e₂(x) λ² + [e₃(x) + s x₁x₂x₃ + t x₁x₂x₄] λ + (1+s+t) x₁x₂x₃x₄.

Exact symmetry: (s, t) ↔ (t, s) (swap nodes 3, 4).

## 2. Numerical boundary (FLOAT, bisection to 1e-13 relative, 216 boundary points)

For α ∈ {1, 0.99, 0.95, 0.9, 0.85, 0.8, 0.75, 0.7} and 27 values of s ∈ [0, R₃(α)³), the supremum
t*(s) of admissible t satisfies, at every point,

    s + t*(s) = R₃(α)³           (max relative deviation 3.6e−14; R₃(1) = 2 so R₃(1)³ = 8),

where R₃(α) = sin(απ/2)/sin(απ/2 − π/3) is the Siami single-3-cycle threshold (C-10 symmetric
slice: T_α(1,1,1) = 1 + R₃³).  All other candidate forms ((1+s)(1+t), s^{1/3}+t^{1/3}, max, s²+t²)
are off by ≥ 26 %.  The region {s, t ≥ 0, s + t < R₃³} is a triangle (linear boundary); the
symmetric boundary point is s = t = R₃³/2 (at α = 1: s = t = 4).
Both computational routes agree: simplex-quartic margin vs. eigenvalues of D A at the worst diagonal
(max |difference| 2.7e−15 over 216 × 2 points; inside positive / outside negative in all cases).
At α = 1 the Routh–Hurwitz minimiser is x* = (1/4, 1/4, 1/4, 1/4) for every boundary point with s > 0.

## 3. Mechanism: cycle merging (necessity is a PROOF; sufficiency is CONJECTURE)

**Lemma (invariant subspace).** For D = diag(d₁, d₂, d, d) the subspace W = span{e₁, e₂, e₃+e₄}
is D A-invariant and D A|_W = diag(d₁, d₂, d) · C_{s+t}, where C_g is the 3×3 negative-feedback
cycle with product −g (a21 = a32 = 1, a13 = −g); the quotient eigenvalue is −d.  Hence

    spec(D A_{s,t}) = spec(D' C_{s+t}) ∪ {−d}.

Proof: A e₁ = −e₁ + e₂, A e₂ = −e₂ + (e₃+e₄), A(e₃+e₄) = −(s+t) e₁ − (e₃+e₄), and
A(e₃−e₄) = (t−s) e₁ − (e₃−e₄) ≡ −(e₃−e₄) mod W.  Verified in mpmath at 50 digits on 20 random
(s, t, D): Hausdorff distance of the two spectra ≤ 1.3e−48 (`N4_SHARED_EDGE_VERIFY.json`).

**Consequence (necessity, proved).** Taking d₃ = d₄ and applying the Siami / C-10 symmetric-slice
threshold to the merged 3-cycle: A_{s,t} ∈ F_α ⇒ s + t < R₃(α)³ (α > 2/3); at α = 1: s + t < 8.

**Conjecture (sufficiency, numerical).** For s, t ≥ 0, A_{s,t} ∈ F_α ⇔ s + t < R₃(α)³, and the
worst positive diagonal always has d₃ = d₄ (i.e. x₃* = x₄*; observed |x₃−x₄| ≤ 4e−8 at 24 boundary
probes).  Equivalently: two negative-feedback 3-cycles sharing an edge behave, for the whole
positive-diagonal orbit and every commensurate order, exactly like one 3-cycle whose gain is the
sum of the two gains.  In particular the genuinely fractional region of the family is the strip
8 < s + t < R₃(α)³ (nonempty for every 2/3 < α < 1, width → 0 as α → 1, → ∞ as α → 2/3⁺).

Reduction to known theory: necessity is Siami's single-cycle secant theorem applied to the merged
cycle; the merging lemma itself is elementary linear algebra.  The nontrivial claim is that the
non-merged diagonals (d₃ ≠ d₄) never do worse — plausibly provable by showing the quartic's
Matignon margin on the simplex is minimised on the plane x₃ = x₄ (a symmetry/convexity argument
in the spirit of C-15), which was not attempted here.

## 4. Suggested follow-ups (future paper)

1. Prove the sufficiency direction (minimum on the symmetric plane x₃ = x₄).
2. Generalise: k directed 3-cycles sharing one edge → merged gain Σ sᵢ (the same invariant-subspace
   argument applies with W = span{e₁, e₂, Σ eᵢ}).
3. Cycles sharing a node but no edge (cactus) do not merge (Wave-1 S3 data show a genuinely
   two-dimensional region); compare.
