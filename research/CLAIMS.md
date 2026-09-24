# Claim registry

No central novelty claim is currently marked `PROVED` or `NOVEL` merely because it appears below. The independent literature audit and mathematical proof must determine status.

**Audit of 2026-09-24 incorporated** (see `research/NOVELTY_REPORT.md` and `research/NOVELTY_MATRIX.md` for theorem-level correspondences and URLs).

| ID | Statement / object | Scope | Evidence | Novelty status | Proof status | Dependencies / audit |
|---|---|---|---|---|---|---|
| C-01 | Matignon sector criterion for commensurate Caputo linearization | standard linear fractional system | literature theorem | KNOWN/STANDARD | IMPORTED — hypotheses must be checked | Matignon 1996; corrected proof + boundary case in Brandibur–Garrappa–Kaslik 2021, *Mathematics* 9:914 |
| C-02 | Fractional stabilization: stable at some `0<alpha<1` while integer-order system is unstable | matrix/Jacobian level | spectral calculation | DERIVABLE BUT NOT NOVEL (iff-direction of Matignon 1996; explicit since Ahmed–El-Sayed–El-Saka 2007, *JMAA* 325:542; α-monotonicity = Remark 4 of Brandibur et al. 2021) | elementary once spectrum known | usable only as motivation; forbidden as a contribution |
| C-03 | Graph-indexed region `S_alpha(G)` as a useful structural object | graph/model family | definition | APPARENT GAP — NEEDS PROOF | DEFINITION ONLY | closest objects: fractional consensus (sector on `σ(L(G))`, Cao–Ren school); Grilli–Rogers–Allesina 2016 at α=1; openness at fixed θ is a remark (eigenvalue continuity), not a theorem |
| C-04 | Fractional D-stability under all positive diagonal scalings `D J` | matrix family | candidate theorem | CLOSE BUT NOT EQUIVALENT — concept named by Kushel 2019 (*SIAM Review* 61:643, `(𝔇,𝒢,∘)`-stability); sufficient conic-region conditions by Kushel–Pavani 2021 (arXiv:2103.04127, Sec. 8) and Zhang–Chen 2015; the non-convex purely fractional sliver `απ/2<|arg λ|≤π/2` is not covered by any found result | OPEN | viable only as a characterization/uniform-margin theorem in the non-convex zone; full general characterization is out of reach (open even at α=1, Hershkowitz 1992) |
| C-05 | Network topology or motifs determine/obstruct fractional D-stability | graph family | candidate theorem | NEW THEOREM CANDIDATE — no fractional analogue found of Jeffries–Klee–van den Driessche 1977, Berman–Hershkowitz 1983, Arcak–Sontag 2006, Arcak 2011 | OPEN | target: necessary-and-sufficient cycle/motif condition for `σ(DJ) ⊂ {|arg λ|>απ/2}` for all D>0 on an explicit graph class (cactus/cyclic first) |
| C-06 | Purely fractional stabilization occupies an open, non-fine-tuned parameter region | admissible parameter family | candidate theorem | SPLIT: fixed-D openness = DERIVABLE BUT NOT NOVEL (continuity of eigenvalues); uniform-over-`𝒟⁺` angular margin = OPEN, not found in literature | OPEN | must be proved jointly with C-04: `min_i |arg λ_i(DJ)| − απ/2 ≥ ε(J) > 0` uniform over all positive diagonal D |

## Fused target theorem (post-audit reframing, 2026-09-24)

The publishable center is C-04+C-05+C-06 fused:

> For an explicit class of signed digraphs `𝒢` (cactus or single-cycle families first) and `0<α<1`: `σ(DJ) ⊂ {λ : |arg λ| > απ/2}` for all positive diagonal `D` **iff** an explicit checkable cycle/motif condition on `G` holds; the satisfying matrices form an **open** set with uniform angular margin; and for every `α<1` the class **strictly contains** the classically D-stable matrices (separation witnessed on the same graph class).

Until this (or a formally stated weaker variant) is proved, no claim below C-01 may enter an abstract or title.

## Allowed evidence labels

- `THEOREM` — analytic proof.
- `CERTIFIED COMPUTATION` — rigorous inclusion/certificate.
- `NUMERICAL CORROBORATION` — floating-point evidence only.
- `OPEN` — unresolved.

Finite diagonal sampling (`src/fdsn/d_stability.py`) is never proof of C-04/C-05; it is falsification/counterexample hunting only.
