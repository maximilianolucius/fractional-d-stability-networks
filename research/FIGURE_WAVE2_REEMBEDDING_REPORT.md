# Figure Wave 2 — biological re-embedding report

**Branch** `agent/compute-figures-wave2-20260926` · **Date** 2026-09-26 · α = 0.9 throughout.
**Verdict: a materially better witness exists. Selected: design W2-A (anchor m = 0.511).** Wave-1 m = 0.35 is retained only as the documented backup.

## 1. What was searched (Part A)

The C-13/DA-06/DA-07 freedom was used exactly as the theorem allows: a design is a tuple of decimal strings
`(β12, β13, β23, κ, s, c1, c2, η, ξ, a, m, ρK)` with X = 1; `realize_invariants` (DA-06) gives `(q1,q2,h,e1,e2,e3)` from the invariants, and `embed_double_allee` (DA-07) gives the full biological parameter set (with η = e1 = e3, ξ the split of the prey loss between the two consumers, and `K = X + ρK (Kmax − X)`, Kmax being the largest K compatible with a positive coexistence Y, Z at the prescribed m). Every candidate is therefore an exact-formula point of the IGP model, not a numerically fitted one.

Sampling (`scripts/reembed_search.py`, seed fixed, 4000 designs, run on the compute node with 16 workers): β ∈ [1.5, 6]³, κ = T₁ + frac·(T_α − T₁) with frac ∈ [0.35, 0.75], s, c1, c2 ∈ 10^[−1.3, 0], η ∈ [0.5, 0.9], ξ ∈ [0.2, 0.8], a ∈ 10^[−0.7, 0.5], m ∈ [0.2, 0.6], ρK ∈ [0.3, 0.95].

Acceptance (all required): all 14 biological parameters positive, efficiencies in (0,1), unique positive coexistence equilibrium, strict-P, T₁ < κ < T_α at the design point, relative classical margin ≥ 0.10, relative fractional margin ≥ 0.20, and — with all non-m parameters fixed — a unique transverse sign change of G₁(m) = κ − T₁ on the feasible branch below the anchor, with feasibility on both sides. A stricter "robust filter" was then applied: rel. classical ≥ 0.25, rel. fractional ≥ 0.30, classical conditioning ≤ 120, m_A − m₀ ≥ 0.08, m_feas,hi − m_A ≥ 0.06, m₀ − m_feas,lo ≥ 0.05.

| stage | count |
|---|---|
| designs sampled | 4000 |
| rejected: parameter/efficiency out of range | 893 |
| rejected: margins below targets | 969 |
| rejected: no unique classical crossing below the anchor | 531 |
| rejected: crossing or anchor too close to feasibility loss | 75 |
| rejected: two coexistence equilibria | 5 |
| **accepted** | **1527** |
| accepted with density ratio < 100 / < 30 | 1180 / 576 |
| robust filter | 365 (ratio < 100: 257; ratio < 30: 109; smallest ratio 3.63) |

So the Chief target (Y/X, Z/X ≥ 10⁻², ratio < 100, preferably < 30) is not a corner of the design space: hundreds of robust designs meet it. `data/reembedding_candidates.json` records every accepted design compactly (`all_accepted_compact`), the 40 best by the internal score (`top`), the rejection counts and the Wave-1 reference metrics.

## 2. Selection rule and shortlist

Among robust designs: classical conditioning ≤ 85 (not worse than the Wave-1 anchor, 80), anchor at least 0.10 in m above the crossing m₀ and at least 0.10 below the feasibility loss; then the smallest max/min density ratio. Top 10 (`design_selected.json → shortlist`; "cond" = Σ|∂ margin/∂ log pᵢ|/margin over the 14 parameters):

| # | m_A | Y/X | Z/X | ratio | rel. κ−T₁ | rel. T_α−κ | cond (cl./fr.) | m₀ | m_feas,hi |
|---|---|---|---|---|---|---|---|---|---|
| **1 (selected)** | **0.511** | 0.786 | 0.192 | **5.20** | 0.406 | 0.337 | 83 / 13 | 0.374 | 0.613 |
| 2 | 0.279 | 0.247 | 0.175 | 5.73 | 0.427 | 0.334 | 59 / 23 | 0.108 | 0.450 |
| 3 | 0.289 | 0.310 | 0.168 | 5.95 | 0.403 | 0.338 | 54 / 10 | 0.076 | 0.454 |
| 4 | 0.284 | 0.322 | 0.167 | 6.00 | 0.454 | 0.315 | 74 / 26 | 0.133 | 0.406 |
| 5 | 0.375 | 0.412 | 0.126 | 7.96 | 0.403 | 0.338 | 83 / 14 | 0.225 | 0.491 |
| 6 | 0.263 | 0.906 | 0.104 | 9.66 | 0.427 | 0.330 | 67 / 24 | 0.087 | 0.427 |
| 7 | 0.246 | 0.626 | 0.102 | 9.84 | 0.464 | 0.324 | 80 / 35 | 0.121 | 0.364 |
| 8 | 0.369 | 0.887 | 0.089 | 11.3 | 0.478 | 0.303 | 79 / 30 | 0.184 | 0.507 |
| 9 | 0.373 | 0.230 | 0.085 | 11.8 | 0.436 | 0.322 | 55 / 15 | 0.081 | 0.603 |
| 10 | 0.370 | 0.330 | 0.082 | 12.1 | 0.431 | 0.325 | 46 / 12 | 0.076 | 0.605 |

Candidates 2–4 have better conditioning but a crossing m₀ ≈ 0.08–0.13 very close to the branch start, which makes the "classical side" of FIG-06 a thin strip; #1 has the most balanced densities and the widest classical side (m₀ = 0.374, classical point at m = 0.19), at conditioning statistically indistinguishable from Wave-1. Any of #1–#5 would be acceptable; the choice among them is presentational, not mathematical.

## 3. Selected design W2-A

Design (exact decimal strings): β = (4.79, 4.506, 5.607), κ = 62.735, s = 0.8231, c1 = 0.065, c2 = 0.0509, η = 0.773, ξ = 0.393, a = 0.229, m = 0.511, ρK = 0.605.

Biological parameters (derived, float): a = 0.229, K = 1.49134, r = 7.81045, q1 = 0.512168, q2 = 3.23382, h = 0.140422, e1 = e3 = 0.773, e2 = 0.0140459, μ1 = 0.317854, μ2 = 0.120917, c1 = 0.065, c2 = 0.0509. All positive, efficiencies in (0,1); e1e3 = 0.598 > e2 (the C-13 sign condition L₃ < 0).

Coexistence at the anchor: X = 1, Y = 0.78563, Z = 0.19218 (ratio 5.20); s = −a₁₁ = 0.8231; β = (4.79, 4.506, 5.607); κ = 62.735, T₁ = 44.6124, T_{0.9} = 94.5719; κ − T₁ = 18.1226 (40.6 % of T₁), T_{0.9} − κ = 31.8369 (33.7 % of T_{0.9}).

m-branch (all non-m parameters fixed): feasible strict-P branch on [0.005, 0.6125]; G₁ = κ − T₁ changes sign exactly once, at **m₀ = 0.37445128124251493523908034461904384927176466921467** (60-digit bisection of the exact formulas, |G₁(m₀)| < 10⁻⁵⁹); classical point m = 0.19 (G₁ = −5.6); the branch loses strict-P at m ≈ 0.6125 where s → 0⁺ (κ − T₁ → +∞, T_α − κ → −∞ there, i.e. the path leaves 𝔽_{0.9} through the upper boundary just before feasibility is lost).

Certification (`computations/scripts/double_allee_interval_box.check_box`, interval Newton for X with outward rounding at 50 digits; C-11 certificate unconditional, C-10-bracket certificate conditional on C-15 Thm 1):
- points m = 0.481, 0.511, 0.541: all certified feasible, strict-P, κ − T₁ ≥ 10.7999 / 18.1226 / 31.8474, T_{0.9} − κ ≥ 33.5717 / 31.8369 / 28.2792;
- **m-interval [0.394, 0.578] fully certified** (83 boxes, 42 sub-intervals, no failures): κ − T₁ ≥ 0.0332 and T_{0.9} − κ ≥ 1.342 on the whole interval (the minima are attained at the two ends; at the anchor the bounds are those above).

Direct scale-invariant spectral corroboration (not proof): min over positive diagonals of min|arg λ(DB)| = 1.4931 > 0.9π/2 = 1.4137 (margin +0.0794 rad), with Re λ > 0 at the worst diagonal (margin −0.0777 at α = 1): Matignon-stable for every diagonal found, not Hurwitz D-stable, consistent with the certified classification.

## 4. Comparison with the Wave-1 anchor m = 0.35

| | Wave-1 (Chief design, m = 0.35) | Wave-2 W2-A (m = 0.511) |
|---|---|---|
| Y/X, Z/X | 0.0369, 0.00128 | 0.786, 0.192 |
| max/min density ratio | 780 | 5.2 |
| κ − T₁ (rel. to T₁) | 2.77 (14.1 %) | 18.12 (40.6 %) |
| T_{0.9} − κ (rel. to T_{0.9}) | 20.42 (47.7 %) | 31.84 (33.7 %) |
| conditioning classical / fractional | 80 / 5.6 | 83 / 13 |
| distance anchor − m₀ ; feasibility loss − anchor | 0.15 ; 0.29 | 0.137 ; 0.10 |
| certified m-interval | [0.2005, 0.45] (Audit 1) | [0.394, 0.578] |
| direct spectral margin α = 0.9 / α = 1 | +0.126 / −0.032 | +0.079 / −0.078 |
| e1e3 vs e2 | 0.25 vs 0.00126 | 0.598 vs 0.0140 |

Evidenced: the new witness improves the presentational weakness by two orders of magnitude (ratio 780 → 5.2) and increases the classical margin threefold, at the same conditioning of the classical margin. Costs, stated plainly: the fractional margin is smaller in relative terms (34 % vs 48 %), the fractional conditioning is worse (13 vs 5.6, both comfortable), and the anchor is nearer to the feasibility loss (0.10 in m instead of 0.29). None of these weakens any theorem-level statement: both margins are certified with room at the anchor and on a whole m-interval.

Caveat (stated plainly): the Wave-1 certified interval [0.2005, 0.45] is longer (0.25) than the Wave-2 one [0.394, 0.578] (0.184), because the Wave-2 branch exits 𝔽_{0.9} through the upper boundary T_{0.9} = κ at m ≈ 0.59 (then loses strict-P at 0.6125). The Wave-2 interval is [m₀ + 0.02, m_exit − 0.01] and cannot be extended much further. This is inherent to a balanced design: Z of order X requires s of order 1, and along the branch s → 0⁺ makes β and κ blow up close to the end.

## 5. Decision

Adopt W2-A as the canonical biological design for FIG-06/07/08 (Wave-2 exports); keep the Wave-1 m = 0.35 witness, its certificate and its figures untouched in `computations/figures/` as backup. Neither point is a calibrated ecosystem: both are constructive witnesses of the open fractional-only class, chosen inside the re-embedding freedom of the theorem.
