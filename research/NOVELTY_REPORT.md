# Deep novelty audit report

**Date:** 2026-09-24
**Scope:** audit of the candidate contributions C-01..C-06 in `research/CLAIMS.md` against the published literature, per `research/NOVELTY_AGENT_TASK.md` and `AGENT_ACCESS.md`.
**Method:** parallel deep-literature searches (D-stability / diagonal stability; fractional-order stability; sector / LMI-region / fractional D-stability; ecological community matrices and graph spectral stability; fractional dynamics on networks), followed by direct verification of the closest hits. Every cited work below was located through a real search result with a verifiable URL; theorem correspondences are stated at the level of hypotheses and conclusions, not keywords.

---

## 1. Verdict per candidate contribution

### C-01 — Matignon sector criterion — `KNOWN/STANDARD`

Matignon (1996) proved that the commensurate Caputo system `^C D^α x = A x`, `0<α<2`, is asymptotically stable iff `σ(A) ⊂ {|arg λ| > απ/2}`, with the boundary case decided by Jordan-block size. Brandibur, Garrappa & Kaslik (2021), *Mathematics* 9(8):914, give a corrected self-contained proof (index vs. geometric multiplicity) and explicitly state α-monotonicity (their Remark 4): stability at order α₂ implies stability at every α₁ < α₂. This criterion is imported machinery; any use of it must cite the exact hypotheses (commensurate order, linearization validity for the nonlinear system).

### C-02 — Purely fractional stabilization — `DERIVABLE BUT NOT NOVEL`

"Stable for some α<1 while Hurwitz-unstable at α=1" is **the sufficient direction of Matignon's if-and-only-if**, applied to a matrix with spectrum in the sliver `απ/2 < |arg λ| ≤ π/2`. It has been stated explicitly in the applied literature since Ahmed, El-Sayed & El-Saka (2007), *J. Math. Anal. Appl.* 325:542–553 (fractional Routh–Hurwitz-type conditions on non-Hurwitz Jacobians), is presented as standard in Petráš's survey (*Fract. Calc. Appl. Anal.* 12(3), 2009) and book (Springer 2011), and the existence of a critical order α\* is a corollary of the monotonicity in Brandibur–Garrappa–Kaslik (2021, Remark 4). The critical-order function `α_c = (2/π) min_i |arg λ_i|` implemented in `src/fdsn/spectral.py` is a restatement of the criterion, not a theorem. **The phenomenon must never be presented as a contribution.** What is *not* settled by the literature is which structural classes of matrices/graphs admit this phenomenon robustly under diagonal rescaling — that is C-04/C-05.

### C-03 — Graph-indexed region `S_α(G)` — `APPARENT GAP — NEEDS PROOF`

As currently defined, `S_α(G)` is a spectral preimage: it is a definition, not a result. Two pieces of prior art bound it from both sides:

- **Fractional consensus / multi-agent literature** (Cao–Li–Ren–Chen school, e.g. Cao & Ren 2010 and successors): stability/consensus of fractional multi-agent systems is certified by the *same* sector condition applied to the Laplacian spectrum `σ(L(G))`. There the graph enters only through its Laplacian eigenvalues. This is the closest existing "graph-indexed fractional stability" object and must be cited and differentiated: our candidate object depends on the full Jacobian `J_G` (not only a Laplacian) and on positive diagonal scalings.
- **Grilli, Rogers & Allesina (2016)**, *Nature Communications* 7:12031: analytic (cavity-method) decomposition showing how block/modular structure of the interaction graph relocates outlier eigenvalues of the community matrix — a topology→spectrum theorem at α=1. Allesina & Tang (2012), *Nature* 483:205–208, give the elliptic-law spectral criterion. Both show that "region of stability depending on graph structure" is an occupied concept at integer order.

A novelty claim for C-03 is only defensible if one proves a theorem about `S_α(G)` that does not reduce to (i) Matignon applied entry-wise, or (ii) α=1 results with the half-plane replaced by the sector. The elementary observation that `S_α(G)` is open when eigenvalues depend continuously on θ and the inequalities are strict is a remark, not a robustness theorem (see C-06).

### C-04 — Fractional D-stability under all positive diagonal scalings `D J` — `CLOSE BUT NOT EQUIVALENT` (the dangerous one)

This is where the audit found the closest prior art:

- **Kushel (2019)**, "Unifying matrix stability concepts with a view to applications", *SIAM Review* 61(3):643–729 (arXiv:1907.07089), already defines the general framework of `(𝔇, 𝒢, ∘)`-stability: spectrum localization in an *arbitrary* region `𝔇 ⊂ ℂ` preserved under multiplication by matrices from a class `𝒢` (including positive diagonal). "Fractional D-stability" as a *named concept* is therefore a special case of a published definition — renaming is not novelty.
- **Kushel & Pavani (2021)**, "Generalized D-stability and diagonal dominance with applications to stability and transient response properties of systems of ODE" (arXiv:2103.04127), introduce diagonal `𝔇`-dominance for LMI regions (including the conic sector around the negative real axis) and prove that diagonal `𝔇`-dominance implies `(𝔇,𝒟)`-stability (preservation under all positive diagonal multipliers). **Section 8 explicitly applies this to fractional-order systems**: diagonal dominance with respect to a conic region is a *sufficient* condition for stability and D-stability of fractional-order systems.
- **Kushel & Pavani (2020)**, *J. Dyn. Diff. Equat.* (arXiv:2004.11172): generalized D-stability in unbounded LMI regions and its computational aspects.
- **Sabatier, Moze & Farges (2010)**, *Comput. Math. Appl.* 59:1594–1609: LMI stability conditions for fractional systems; **Zhang & Chen (2015)** (ASME IDETC): "D-stability based LMI criteria of stability and stabilization for fractional order systems" — the phrase "fractional D-stability" in the LMI-region sense already exists in the control literature.

**Why a gap remains.** The Matignon stability region for `0<α<1` is `Σ_α = {λ : |arg λ| > απ/2}`, which is **non-convex**: it contains the right-half-plane sliver `απ/2 < |arg λ| ≤ π/2`. LMI regions are convex by construction, and the conic sectors treated by Kushel–Pavani lie strictly inside the left half-plane side (half-angle `< π/2` around the negative real axis). Consequently all existing sufficient conditions certify fractional stability only through convex subregions of `Σ_α` and **cannot see the purely fractional zone** — exactly the zone in which C-02 lives. The problem "characterize the matrices A such that `σ(DA) ⊂ Σ_α` for **all** `D ∈ 𝒟⁺`, including spectra in the non-convex sliver" was not found in the literature, neither as a sufficient-condition improvement nor as a characterization. Classical D-stability characterization is famously open in general (Hershkowitz 1992, *LAA* 171:161–186; solved only for n ≤ 4, Cain 1976, Kanovei–Logofet 1998), so a *full* characterization is out of reach; a characterization for **structured classes** (graph-restricted sign patterns, low rank, cactus/cyclic) is the realistic gap.

### C-05 — Topology/motifs determine or obstruct fractional D-stability — `NEW THEOREM CANDIDATE` (conditional)

Integer-order precedent is strong and must be cited:

- Jeffries, Klee & van den Driessche (1977), *Canad. J. Math.* 29:315–326: complete graph-theoretic characterization of sign-stable matrices.
- Berman & Hershkowitz (1983), *SIAM J. Alg. Disc. Meth.* 4:377–382: for matrices whose undirected graph is acyclic, diagonal stability ⇔ positivity of principal minors.
- Arcak & Sontag (2006), *Automatica* 42(9): diagonal stability of cyclic systems via the secant criterion; Arcak (2011), *IEEE TAC* 56(12):2766–2777: diagonal stability on cactus graphs certified cycle-by-cycle.

No fractional analogue of any of these was found: nothing connects graph cycles/motifs to the *angular* condition `|arg λ| > απ/2` under diagonal scalings. Because eigenvalue arguments of `D J` are controlled by cycle products and the geometry of complex eigenvalues, a theorem of the form "for graphs in class 𝒢, fractional D-stability at order α is equivalent to an explicit cycle/motif condition" would be new in *both* the fractional and the matrix-stability literature. Status remains `NEW THEOREM CANDIDATE` only until a proof exists; finite diagonal sampling (`src/fdsn/d_stability.py`) is falsification evidence only.

### C-06 — Open-set / robustness of the purely fractional region — `OPEN`, split in two

- **Fixed D, strict inequalities:** openness of `{θ : σ(J_G(θ)) ⊂ Σ_α}` under continuous dependence of `J_G` on θ follows from continuity of eigenvalues — `DERIVABLE BUT NOT NOVEL`.
- **Uniform over all D ∈ 𝒟⁺:** proving that the class of fractionally D-stable matrices is open, or that a structured family has a uniform angular margin `|arg λ_i(DJ)| ≥ απ/2 + ε` for all `D`, is nontrivial (the constraint set is a noncompact cone; uniformity needs an argument, e.g. compactification of ray directions plus boundary analysis). Combined with C-04 this is the load-bearing part of a robustness theorem and is currently unproved — `OPEN`.

---

## 2. Answers to the ten audit questions of `NOVELTY_AGENT_TASK.md`

1. **Closest object to `S_α(G)`:** the sector condition on the Laplacian spectrum in fractional consensus (Cao–Ren school) for the graph-indexing, and Grilli–Rogers–Allesina (2016) for topology-dependent stability regions at α=1. Neither involves positive diagonal scalings nor the non-convex sliver.
2. **"Stable fractionally / unstable at order 1" known?** Yes — standard since 2007 (Ahmed–El-Sayed–El-Saka), iff-direction of Matignon 1996, monotonicity in Brandibur–Garrappa–Kaslik 2021. What can still be new: *structural* conditions (graph/scaling) for the phenomenon, and its robustness uniformly over diagonal scalings.
3. **D-stability generalized to sectors/cones/fractional?** Yes, substantially: Kushel 2019 (general framework), Kushel–Pavani 2020/2021 (conic/LMI regions, explicit fractional sufficient conditions), Zhang–Chen 2015 and Sabatier–Moze–Farges 2010 (LMI criteria for fractional systems). Not covered: the non-convex Matignon region for α<1 in the RHP sliver, and characterizations (necessary-and-sufficient) for structured classes.
4. **GLV Jacobians `J = diag(x*)A`:** at α=1 the ecological interpretation is settled by classical diagonal-stability theory (Barker–Berman–Plemmons 1978; Kaszkurewicz–Bhaya 2000; Logofet 1993; Volterra multipliers, Redheffer 1985; abundance-rescaling effects in Gibbs et al. 2018, *PRE* 98:022410). Any ecological claim must be explicitly fractional-sectorial to avoid being an immediate corollary.
5. **Topology-to-spectrum theorems that trivialize the network claim:** for α=1, yes (Jeffries–Klee–van den Driessche 1977; Berman–Hershkowitz 1983; Arcak 2011). For the fractional angular condition, none found — but note the trap: results about *real* spectra and principal minors do not transfer, because fractional sector stability is governed by eigenvalue *arguments*, i.e. genuinely non-Hermitian/complex geometry. This cut is where new mathematics can live.
6. **Example → theorem over an open family:** possible; the natural vehicle is an angular-margin condition uniform over `𝒟⁺` on a structured matrix class, with openness proved via the margin.
7. **Necessary/sufficient conditions, sharp boundaries, motif obstructions:** absent from the literature in the fractional setting; the secant criterion (Arcak–Sontag 2006) is the α=1 template showing what such a result looks like. A sharp angular threshold `α_c(G)` for a graph family would be new.
8. **Separation theorem (Hurwitz D-stability vs fractional sector D-stability):** none found. Elementary separation examples exist in dimension 2 (spiral sources with small positive trace, e.g. `A = [[ε,−1],[1,ε]]`, have `arg λ → ±π/2` as ε→0⁺ uniformly on compacta of D-directions), so a *proof* that for every α<1 the fractional D-stable class strictly contains the Hurwitz D-stable class, with explicit families, is attainable and, if uniform over all D>0, is not in the literature.
9. **Invariance:** `S_α` is invariant under permutation similarity and under the GLV abundance rescaling `J = diag(x*)A` (positive diagonal *left* multiplication is the object of study, not an invariance); it is **not** invariant under general similarity (arguments are not similarity invariants). The manuscript must fix the precise class of scalings under which claims are invariant; careless invariance claims are a referee trap.
10. **Smallest title-worthy theorem:** see §4.

---

## 3. Closest works (comparison at theorem level)

Full comparison matrix in `research/NOVELTY_MATRIX.md`. The five most dangerous:

1. **Kushel & Pavani 2021 (arXiv:2103.04127), Section 8** — proves diagonal dominance w.r.t. a conic region ⇒ stability and D-stability of fractional-order systems under positive diagonal multiplication. Our C-04 survives only because (a) their regions are convex and miss the purely fractional sliver, and (b) they give sufficient, not structural/characterizing, conditions.
2. **Kushel 2019 (SIAM Review 61:643–729)** — the `(𝔇,𝒢,∘)`-stability framework already names the general concept. We must present fractional D-stability as an instantiation with a specific non-convex `𝔇 = Σ_α` that the framework's existing results do not cover.
3. **Matignon 1996 + Brandibur–Garrappa–Kaslik 2021** — C-02 is a corollary. Any draft presenting the phenomenon as new is desk-rejectable.
4. **Arcak 2011 (IEEE TAC 56:2766–2777) and Berman–Hershkowitz 1983** — occupy "graph topology controls diagonal stability" at α=1. Our C-05 must be proved for the angular condition, not re-derived for the half-plane.
5. **Fractional consensus literature (Cao–Ren and successors)** — occupies "fractional stability condition indexed by a graph spectrum". Differentiation: their region depends on `σ(L(G))` only; ours would depend on cycle/motif structure of `J_G` beyond the Laplacian spectrum, and on the diagonal-scaling orbit.

---

## 4. Required closing statements

### Strongest defensible novelty (≤ 3 sentences)

The stabilization of an integer-order-unstable equilibrium at order α<1 is a 1996 theorem (Matignon), and sufficient LMI/diagonal-dominance conditions for fractional D-stability exist (Sabatier–Moze–Farges 2010; Kushel–Pavani 2021) — but all of them certify stability through *convex* subregions of the Matignon sector and therefore cannot reach the non-convex "purely fractional" sliver `απ/2 < |arg λ| ≤ π/2`. A characterization of the matrices — organized by interaction-graph topology — whose spectra remain in that sliver under *all* positive diagonal rescalings `D J`, with a uniform angular margin, does not appear in the D-stability, diagonal-stability, or fractional-control literature we audited. If proved, such a topology-indexed fractional D-stability theorem with an open-set robustness statement is a genuine new theorem; everything else in the current repository is standard machinery or numerical corroboration.

### Strongest theorem that still needs to be proved

> **Target theorem (fractional D-stability on a graph class).** Let `𝒢` be an explicit class of signed digraphs (e.g. cactus graphs or single-cycle families) and `0<α<1`. Prove that for `J` in the corresponding matrix class, `σ(DJ) ⊂ {λ : |arg λ| > απ/2}` for **all** positive diagonal `D` **if and only if** an explicit, checkable condition on the cycles/motifs of `G` holds (the α=1 analogue being the secant criterion of Arcak–Sontag); prove moreover that (i) the condition defines an **open** set of matrices with a uniform angular margin `min_i |arg λ_i(DJ)| − απ/2 ≥ ε(J) > 0` over all `D`, and (ii) for every `α<1` this class **strictly contains** the classically D-stable matrices, with the separation witnessed on the same graph class.

A full characterization for arbitrary matrices is known to be out of reach even at α=1 (Hershkowitz 1992), so the quantifier structure above (structured class + necessity and sufficiency *within* the class + openness + separation) is the smallest statement strong enough to carry a title and abstract.

### Main prior-art risk

**Kushel & Pavani (2021), arXiv:2103.04127, Section 8** (backed by the framework of Kushel 2019, SIAM Review). A referee can read "fractional D-stability under positive diagonal scaling" as already defined and already supplied with sufficient conditions. The defense must be mathematical, not terminological: their conic regions are convex and strictly contained in the left-half-plane side, hence structurally blind to the purely fractional sliver; the paper must say this explicitly and prove something in the zone they cannot reach. Secondary risk: the fractional-consensus literature for any graph-indexing claim, and Matignon triviality for any stabilization-phenomenon claim.

### Recommendation

**Proceed, but narrowed and mathematically reframed.** Drop C-02 as a contribution (demote to motivation). Reframe the paper around C-04+C-05+C-06 fused into the single target theorem above: fractional D-stability in the non-convex Matignon zone, on an explicit graph class, with necessary-and-sufficient motif conditions, uniform angular margin, and separation from classical D-stability. Keep the ecological GLV interpretation strictly as an application layer, since the α=1 ecological content is classical. Do not write the manuscript until the target theorem (or a formally stated weaker variant) is proved; `src/fdsn/d_stability.py` sampling may be used only to hunt counterexamples while proving.

---

## 5. Sources

All items located via live searches; URLs in `research/NOVELTY_MATRIX.md`. Key verified entries:

- Matignon 1996 (statement and hypotheses verified via Brandibur–Garrappa–Kaslik 2021, *Mathematics* 9(8):914, https://www.mdpi.com/2227-7390/9/8/914 — includes Remark 4 on α-monotonicity).
- Kushel 2019, *SIAM Review* 61(3):643–729, https://arxiv.org/abs/1907.07089.
- Kushel & Pavani 2020, *J. Dyn. Diff. Equat.*, https://arxiv.org/abs/2004.11172.
- Kushel & Pavani 2021, https://arxiv.org/abs/2103.04127 (abstract and Section 8 verified by direct fetch: diagonal 𝔇-dominance for conic regions; sufficient condition for stability and D-stability of fractional-order systems).
- Sabatier, Moze & Farges 2010, *Comput. Math. Appl.* 59:1594–1609, https://www.sciencedirect.com/science/article/pii/S0898122109005355.
- Zhang & Chen 2015, "D-stability based LMI criteria of stability and stabilization for fractional order systems", ASME IDETC 2015 (reference verified through multiple citing papers).
- Ahmed, El-Sayed & El-Saka 2007, *JMAA* 325:542–553.
- Petráš 2009, *Fract. Calc. Appl. Anal.* 12(3):269–298.
- Cross 1978, *LAA* 20:253–263; Johnson 1974, *J. Econ. Theory* 9:53–62; Barker–Berman–Plemmons 1978, *Linear Multilinear Algebra* 5:249–256; Kaszkurewicz & Bhaya 2000, Birkhäuser; Hershkowitz 1992, *LAA* 171:161–186.
- Jeffries, Klee & van den Driessche 1977, *Canad. J. Math.* 29:315–326; Berman & Hershkowitz 1983, *SIAM J. Alg. Disc. Meth.* 4:377–382; Arcak & Sontag 2006, *Automatica* 42(9); Arcak 2011, *IEEE TAC* 56(12):2766–2777.
- Allesina & Tang 2012, *Nature* 483:205–208; Grilli, Rogers & Allesina 2016, *Nat. Commun.* 7:12031; Gibbs et al. 2018, *PRE* 98:022410.
- Cao–Ren fractional consensus line (sector condition on Laplacian spectrum); Riascos & Mateos 2014, *PRE* 90:032809 (fractional Laplacian — adjacent but distinct object).
