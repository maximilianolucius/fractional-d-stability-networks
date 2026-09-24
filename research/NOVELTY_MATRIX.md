# Closest-work novelty matrix

**Status:** reopened and updated 2026-09-24 after theorem-level second-pass audit.  
**Rule:** overlap is compared at the level of hypotheses, quantifiers, conclusions, and stability region — not keywords.

| Reference | Mathematical object | Fractional order | Spectral region | Positive diagonal orbit | Graph / structure | Robust/interior aspect | Relation to current project |
|---|---|---|---|---|---|---|---|
| Matignon 1996 (via Brandibur–Garrappa–Kaslik 2021) | commensurate fractional linear systems | yes | `|arg λ|>απ/2` iff | no | none | no | C-01 imported; C-02 is a corollary |
| Brandibur, Garrappa & Kaslik 2021, *Mathematics* 9:914 | corrected stability theory + α-monotonicity | yes | exact Matignon sector | no | none | no | kills novelty of critical-order/monotonicity claims |
| Ahmed, El-Sayed & El-Saka 2007, *JMAA* 325 | low-dimensional fractional stability criteria | yes | fractional wedge | no | specific models | no | explicit precedent for fractionally stable / integer-order unstable equilibria |
| Kushel 2019, *SIAM Review* 61:643, arXiv:1907.07089 | generalized D-stability framework | general | arbitrary spectral region | yes | general | no | F_α is an instance of an existing generalized D-stability concept |
| Kushel–Pavani 2020, arXiv:2004.11172 | generalized D-stability; forbidden-boundary approach | not specifically fractional | sector/LMI boundaries and complement machinery | yes | general | boundary exclusion | diagonal-orbit boundary machinery already exists |
| Kushel–Pavani 2021, arXiv:2103.04127 | diagonal region-dominance and applications | yes, Sec. 8 | fractional stability described via complement of a cone; non-LMI aspect acknowledged | yes for theorem-specific diagonal classes | general | some robustness implications | invalidates claim that literature is wholly blind to the non-convex Matignon complement |
| Kushel 2023, *LAA* 656:9–26, arXiv:2205.10823 | relatively D-stable matrices; determinant bounds; sector gaps | no | sectors / gaps from imaginary axis | yes | D-stable subclasses | uniform sector-gap estimates | "uniform angular gap" alone is not novelty |
| **Siami 2020/2021**, arXiv:2011.04204 / IEEE TCNS | cyclic interconnected commensurate fractional networks | yes | generalized fractional secant condition | not stated as D-orbit theorem, but cycle ratio invariant under positive row scaling | **single circuit** | H2 robustness also studied | **main killer of single-cycle novelty** |
| Arcak & Sontag 2006; Arcak 2011 | cyclic / cactus diagonal stability | no | left half-plane | related diagonal-scaling setting | cycles/cactus | no | α=1 structural template |
| Jeffries–Klee–van den Driessche 1977 | sign stability | no | left half-plane | stronger sign-robustness notion | graph characterization | yes in sign class | topology-to-stability precedent |
| Berman–Hershkowitz 1983 | diagonal stability on acyclic graph classes | no | left half-plane | yes/related | acyclic graph | no | structural α=1 precedent |
| Cain / classical low-dimensional D-stability literature | low-dimensional D-stability criteria | no | left half-plane | yes | low-dimensional matrices | some interior/topological implications | model for an exact fractional 3×3 theorem |
| Hartfiel 1980 | interior of D-stable matrices | no | left half-plane | yes | general | **interior** | openness/interior is classical territory |
| Abed 1986, *Systems & Control Letters* 7(3):207–212 | **strong D-stability** | no | left half-plane | yes | general | small perturbations remain D-stable | terminology and concept are prior art |
| Lee & Edgar 2001, *Systems & Control Letters* 44:273–277 | structured-singular-value conditions for strong D-stability | no | left half-plane | yes | general | robust conditions | reinforces that robustness alone is not novelty |
| Casasanta & Simpson-Porco 2026, arXiv:2603.13608 | Lyapunov characterization of robust (block) D-stability | no | left half-plane | yes | general | necessary-and-sufficient Lyapunov-type characterization | raises standard for any new "strong fractional D-stability" result |
| Kellogg P-matrix wedge theorem | spectrum of P-matrices | no | `|arg μ| < π-π/n` | preserved by positive diagonal left scaling | principal-minor class | strict inequalities give open class | imported bridge yielding C-08 for α<=2/n; not novelty by itself |
| Allesina–Tang 2012; Grilli–Rogers–Allesina 2016 | ecological random/community-matrix spectra | no | half-plane | no | interaction type / modularity | ensemble-level | ecology remains application layer |
| fractional consensus literature | fractional network consensus | yes | sector condition on Laplacian spectrum | no | graph Laplacian | no | occupies generic "graph-indexed fractional stability" language |

## Corrected reading

### Occupied territory

1. Purely fractional stabilization is standard Matignon geometry.
2. Generalized fractional D-stability as a concept is occupied by Kushel's framework and fractional applications.
3. Single-cycle fractional secant conditions are occupied by Siami to a degree that makes the same D-orbit theorem corollary-level.
4. Robust/strong D-stability terminology and interior questions are classical.
5. Sector-gap and forbidden-boundary machinery under diagonal scaling already exists.

### Strongest surviving candidate

```text
min { n : int(F_α^(n) \ D_H^(n)) != empty } = 3
for every 0 < α <= 2/3.
```

This statement is internally proved using the exact 2×2 obstruction plus a 3×3 P-matrix construction. Targeted searches found the ingredients separately but not the combined minimal-dimension theorem.

### Highest-value open extension

```text
2/3 < α < 1
```

either by proving the same dimension threshold or by deriving an exact 3×3 characterization of F_α.

## Audit rule

No claim is marked novel because an identical phrase was not found. The final verdict must show that the theorem's quantifier structure and conclusion are not recoverable from Siami, Kushel/Kushel–Pavani, classical low-dimensional D-stability, or strong-D-stability theory.
