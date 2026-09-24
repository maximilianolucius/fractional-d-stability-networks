# Closest-work novelty matrix

**Status:** reopened and updated 2026-09-24 after theorem-level second-pass audit.  
**Rule:** overlap is compared at the level of hypotheses, quantifiers, conclusions, and stability region — not keywords.

| Reference | Mathematical object | Fractional order | Spectral region | Positive diagonal orbit | Graph / structure | Robust/interior aspect | Relation to current project |
|---|---|---|---|---|---|---|---|
| Matignon 1996 (via Brandibur–Garrappa–Kaslik 2021) | commensurate fractional linear systems | yes | `|arg λ|>απ/2` iff | no | none | no | C-01 imported; C-02 is a corollary, not novelty |
| Brandibur, Garrappa & Kaslik 2021, *Mathematics* 9:914 | corrected stability theory + α-monotonicity | yes | exact Matignon sector | no | none | no | kills novelty of critical-order/monotonicity claims |
| Ahmed, El-Sayed & El-Saka 2007, *JMAA* 325 | low-dimensional fractional stability criteria | yes | fractional wedge | no | specific models | no | explicit precedent for fractionally stable / integer-order unstable equilibria |
| Kushel 2019, *SIAM Review* 61:643, arXiv:1907.07089 | `(𝔇,𝒢,∘)`-stability | general framework | arbitrary `𝔇⊂C` | yes, including positive diagonal classes | general | no | `F_α` is an instance of an existing generalized D-stability concept |
| Kushel–Pavani 2020, arXiv:2004.11172 | generalized D-stability; forbidden-boundary approach | not specifically fractional | LMI regions / sector boundaries; complement machinery | yes | general | boundary exclusion | important: diagonal-orbit boundary machinery already exists |
| Kushel–Pavani 2021, arXiv:2103.04127 | diagonal `𝔇`-dominance and applications | yes, Sec. 8 | fractional stability described via complement of a cone; non-LMI aspect acknowledged | yes for theorem-specific diagonal classes | general | some robustness-type implications | invalidates baseline claim that literature is wholly blind to the non-convex Matignon complement |
| Kushel 2023, *LAA* 656:9–26, arXiv:2205.10823 | relatively D-stable matrices; determinant bounds; sector gaps | no | sectors / gaps from imaginary axis | yes | several D-stable subclasses | uniform sector-gap estimates for subclasses | "uniform angular gap" language alone is not novel |
| **Siami 2020/2021**, arXiv:2011.04204 / IEEE TCNS | cyclic interconnected commensurate fractional networks | yes | generalized fractional secant stability condition | not stated as D-orbit theorem, but cycle ratio is invariant under positive row scaling | **single circuit** | robustness also studied in H2 sense | **main killer of single-cycle novelty**; exact D-orbit criterion is largely recoverable by invariance + diagonal equalization |
| Arcak & Sontag 2006; Arcak 2011 | cyclic / cactus diagonal stability | no | left half-plane | diagonal-stability setting | cycles/cactus | no | α=1 structural template; cactus novelty survives only if strictly beyond Siami + Arcak |
| Jeffries–Klee–van den Driessche 1977 | sign stability | no | left half-plane | stronger sign-robustness notion | graph characterization | yes in sign class | topology→stability precedent |
| Berman–Hershkowitz 1983 | diagonal stability on acyclic graph classes | no | left half-plane | yes/related | acyclic graph | no | structural α=1 precedent |
| Cain 1976 and classical low-dimensional D-stability literature | exact/special low-dimensional D-stability conditions | no | left half-plane | yes | low-dimensional matrices | topology/interior implications | model for what an exact fractional 3x3 theorem should look like |
| Hartfiel 1980, *LAA* | interior of the D-stable matrices | no | left half-plane | yes | general | **interior** | openness/interior is classical research territory |
| Abed 1986, *Systems & Control Letters* 7(3):207–212 | **strong D-stability** | no | left half-plane | yes | general | **small perturbations remain D-stable** | "strong/robust D-stability" terminology and concept are prior art |
| Lee & Edgar 2001, *Systems & Control Letters* 44:273–277 | structured-singular-value conditions for strong D-stability | no | left half-plane | yes | general | necessary/sufficient-style robust conditions | reinforces that robustness alone is not novelty |
| Casasanta & Simpson-Porco 2026, arXiv:2603.13608 | Lyapunov characterization of robust (block) D-stability | no | left half-plane | yes | general | necessary-and-sufficient Lyapunov-type characterization | raises standard for any new "strong fractional D-stability" result |
| Kellogg P-matrix wedge theorem | spectrum of P-matrices | no | `|arg μ|<π-π/n` | preserved by positive diagonal left scaling | principal-minor class | strict inequalities give open class | imported bridge yielding C-08 for `α<=2/n`; not novelty by itself |
| Allesina–Tang 2012; Grilli–Rogers–Allesina 2016 | ecological random/community-matrix spectra | no | half-plane | no | interaction type / modularity | ensemble-level | ecology remains application layer, not novelty source |
| fractional consensus literature (Cao–Ren line) | fractional network consensus | yes | sector condition on Laplacian spectrum | no | graph Laplacian | no | occupies generic "graph-indexed fractional stability" language |

## Corrected reading

### What is occupied

1. **Purely fractional stabilization:** standard consequence of Matignon.
2. **Generalized fractional D-stability as a concept:** occupied by Kushel's framework and fractional applications.
3. **Single-cycle fractional secant conditions:** occupied by Siami to a degree that makes a D-orbit theorem on the same family corollary-level.
4. **Robust/strong D-stability terminology and interior questions:** occupied classically by Hartfiel, Abed, Lee–Edgar and current work.
5. **Sector-gap / forbidden-boundary machinery under diagonal scaling:** already present in Kushel/Kushel–Pavani.

### What still appears unoccupied after this pass

The current strongest candidate is the **minimal-dimension robust genuinely-fractional separation theorem**:

[
min{n:
operatorname{int}(mathcal F_alpha^{(n)}setminusmathcal D_H^{(n)})
eqarnothing}
=3
]

proved internally for

[
0<alphale2/3.
]

The ingredients (Matignon, P-matrix wedge, classical D-stability, strong D-stability, cyclic fractional stability) are individually known, but targeted searches have not located the combined dimension-threshold statement.

The highest-value open extension is the same result for

[
2/3<alpha<1,
]

or, stronger still, an exact `3x3` characterization of (mathcal F_alpha) in that range.

## Audit rule

No claim is marked novel because an identical phrase was not found. A future final novelty verdict must show that the theorem's quantifier structure and conclusion are not recoverable from Siami, Kushel/Kushel–Pavani, classical low-dimensional D-stability, or strong-D-stability theory.
