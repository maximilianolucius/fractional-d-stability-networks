# Novelty audit

Maintained as a living claim-by-claim audit. Last full audit: 2026-09-24 (see `../NOVELTY_REPORT.md`).

| Proposed contribution | Closest prior literature | Exact difference | Evidence/source | Status |
|---|---|---|---|---|
| Graph-indexed purely fractional stabilization region `S_α(G)` | Matignon 1996 (sector iff); Brandibur–Garrappa–Kaslik 2021 (α-monotonicity, Remark 4); fractional consensus literature (sector on `σ(L(G))`); Grilli–Rogers–Allesina 2016 (topology→spectrum at α=1) | The phenomenon "fractionally stable / order-1 unstable" is the if-direction of Matignon's theorem and folklore since Ahmed–El-Sayed–El-Saka 2007; only a *structural* theorem (topology + diagonal orbit) would be new | https://www.mdpi.com/2227-7390/9/8/914 ; https://arxiv.org/abs/1105.2071 | phenomenon: KNOWN/STANDARD; structural version: NEEDS PROOF |
| Fractional D-stability under positive diagonal scaling | Kushel 2019 `(𝔇,𝒢,∘)`-stability framework (SIAM Review 61:643); Kushel–Pavani 2021 Sec. 8 (diagonal dominance w.r.t. conic region ⇒ stability and D-stability of fractional-order systems); Zhang–Chen 2015 (D-stability LMI criteria for fractional systems) | All existing sufficient conditions use convex regions; the Matignon sector for α<1 is non-convex and its RHP sliver `απ/2<|arg λ|≤π/2` (the purely fractional zone) is uncovered; no characterization found | https://arxiv.org/abs/2103.04127 ; https://arxiv.org/abs/1907.07089 | CLOSE BUT NOT EQUIVALENT — viable only in the non-convex zone, as characterization theorem |
| Topological conditions/obstructions | Jeffries–Klee–van den Driessche 1977 (sign stability); Berman–Hershkowitz 1983 (acyclic graphs); Arcak–Sontag 2006 (secant criterion); Arcak 2011 (cactus graphs) — all at α=1, half-plane condition | No fractional/angular analogue found: eigenvalue *arguments* under diagonal scaling are governed by non-Hermitian geometry that principal-minor criteria do not capture | https://www.cambridge.org/core/journals/canadian-journal-of-mathematics/article/when-is-a-matrix-sign-stable/6C79B9A529225742F8A8C57653ACD4AB | NEW THEOREM CANDIDATE (unproved) |
| Cross-topology comparative laws | Allesina–Tang 2012 (elliptic law); Grilli et al. 2016 (modularity); fractional consensus (Laplacian spectrum only) | Would be new only as proved α-dependent thresholds `α_c(G)` tied to motif structure, not as numerical scans | https://arxiv.org/abs/1105.2071 | OPEN — subordinate to the target theorem in `../CLAIMS.md` |

## Rule

A contribution is not marked novel merely because no identical title or keyword was found. The audit must compare theorem hypotheses, conclusions, model class, fractional-order assumptions, graph class, and scaling invariances against the closest literature.
