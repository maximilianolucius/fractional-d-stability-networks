# N4 reconnaissance (P5) — EXPLORATORY, not theorem evidence

Script: `computations/scripts/p5_n4_recon.py`; data: `computations/results/N4_RECON.json`.
Method: direct Matignon margin minimised over positive diagonal D (3 free log-ratios, grid
[−9,9]³ step 0.75 + pattern search from 3 starts, LAPACK eigenvalues), at α and at α=1.
"Genuinely fractional (GF)" = min_D margin_α > 1e−9 and min_D margin_1 < −1e−9. All results
are NUMERICAL on finite parameter grids; grid points are not open-set proofs.

## Results

| study | finding |
|---|---|
| S1 single 4-cycle −I+γC₄ (negative feedback) | direct crossing brackets contain Siami's R₄(α)=sin(απ/2)/sin(απ/2−π/4) for α∈{0.55,…,0.99}; Hurwitz crossing brackets contain √2. **Covered by Siami (single-cycle) — nothing new.** R₄→∞ as α→1/2⁺, so the Kellogg wedge threshold α=2/n=1/2 is sharp for n=4 (also covered). |
| S2 two 3-cycles sharing edge 1→2 (γ₁,γ₂)∈[0.5,3]² | GF points: 485/676 (α=.75), 252 (α=.9), 19 (α=.99). Every scanned point is in F at α=.75. Open GF families exist; not a single-cycle structure. |
| S3 3-cycle + reciprocal antagonistic pair (1,4), (γ,c) | GF: 494 (α=.75), 234 (.9), 0 (.99, grid too coarse near γ≈2). Best GF points at c=0 (pair absent). |
| S4 3-cycle ⊕ node 4, two-way coupling ε, sign s | s=−1 (antagonistic pair 1–4): F members 464/464 at α=.75, 320 at .9. s=+1 (mutualistic/competitive): F members 290 at .75, 133 at .9. Hurwitz D-stable count also drops (64 → 18). |
| S5 random strict-P 4×4 (8000 matrices, entry space) | Hurwitz D-stable 97.9%; GF 2.06% for α≤0.75, 1.86% at .9, 0.34% at .99. **No non-F strict-P matrix for α≤0.75** (min margin 0.122 at α=.75); non-F counts 16 (α=.9), 138 (α=.99). |
| S6 orbit reduction for n=4 | the margin of the normalised quartic λ⁴+λ³+B₂(x)λ²+B₃(x)λ+κ₄x₁x₂x₃x₄, built from the 11 normalised principal-minor invariants on the 3-simplex, equals the eigenvalue margin of DA to 1.5e−13 (40 matrices × 300 points). |
| S7 adversarial DE over unit-diagonal 4×4 (|a_ij|≤4) | best score min(m_α, −m₁) = 0.1959 / 0.0785 / 0.0078 for α=.75/.9/.99. **This objective is uninformative:** with φ=inf_D min|arg λ|, the score is min(φ−απ/2, π/2−φ) ≤ (1−α)π/4 = 0.1963 / 0.0785 / 0.00785 for any n. Both n=4 and the 3×3 cycle saturate it (3×3 at .99 only missed it because of γ-grid resolution). Retracted as a discriminating experiment; a matrix-norm robustness radius is needed instead. |

## Conjecture families (3–10 requested; exploratory)

1. **Exact orbit reduction for n=4 (near-certain; elementary).** Parameterisation: A with −A strict P;
   11 invariants β_ij = m_ij/(p_ip_j), γ_ijk = −m_ijk/(p_ip_jp_k) (signs per −A), κ₄ = det(A)/(p₁…p₄).
   A∈F_α ⇔ the quartic above is Matignon-stable for every x in the open 3-simplex. Mechanism: same
   as C-10 §3 (coefficients of det(λI−DA) are symmetric sums of principal minors times products of
   d_i). Numerical margin agreement 1.5e−13. Structurally the generic-n version of the C-10 reduction;
   the open question is an exact fixed-quartic boundary (two-parameter family instead of H_θ).
2. **Two 3-cycles sharing an edge (S2).** Family A(γ₁,γ₂) with a₂₁=1, a₃₂=γ₁, a₁₃=−γ₁²,
   a₄₂=γ₂, a₁₄=−γ₂². GF for α=.75 on most of [0.5,3]² minus the Hurwitz D-stable corner; margins up to
   the trivial bound ~0.196. Candidate invariant: the two normalised 3-cycle gains −γ₁³, −γ₂³ plus zero
   2-cycles; mechanism beyond single-cycle secant conditions (not covered by Siami's single-cycle
   theorem; possibly covered by classical cycle-sum/loop analysis at α=1 only).
3. **Pendant-species coupling sign rule (S4).** 3-cycle witness (γ) coupled to a 4th species by a
   reciprocal pair of strength ε: antagonistic coupling (a₁₄a₄₁<0, β₁₄>1) preserved F membership at every
   scanned point (α=.75), mutualistic/competitive coupling (β₁₄<1) removed 37%. Conjectured mechanism:
   n=4 analogue of C-13 §7 monotonicity (threshold nondecreasing in each β_ij). α range 0.75–0.9.
4. **Low-order window (S5).** For random strict-P 4×4, F held at α≤0.75 in all 8000 samples, while the
   universal (Kellogg) guarantee is only α≤1/2 and the 4-cycle exits F for α∈(1/2,1) at large γ.
   Conjecture: non-membership for α∈(1/2, 2/3] requires a strong 4-cycle. Heuristic only: every 3×3
   principal submatrix of a strict-P matrix is strict-P, hence in F_α for α≤2/3 by C-10's low-order
   clause, which suggests (but does not prove) that pure 3-cycle mechanisms are not enough.
   Status: plausible, untested beyond random sampling.
5. **GF density decays like the band width.** GF fraction among random strict-P 4×4 drops from 2.06%
   (α≤.75) to 0.34% (α=.99), consistent with an O(1−α) band as in C-14; conjectured n=4 analogue of
   C-14's linear collapse. Weak evidence (3 α values).

Coverage: family 1 is the straightforward n-dimensional version of the C-10 reduction; S1 is
Siami; the α≤2/n statement is Kellogg. Families 2–5 are not covered by single-cycle theory as far
as this compute agent can tell (no literature search was performed, per instructions).
