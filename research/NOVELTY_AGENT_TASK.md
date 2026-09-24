# Novelty audit task

## Objective

Determine whether the proposed research direction contains enough **mathematical novelty** for a strong journal submission, and identify the exact theorem-level contribution that should become the center of the paper.

The controlling publication directives are in `../agent_directives_publishable_first_submission.md`. In particular, the audit must follow the rule: **find the theorem before writing the paper**.

## Candidate research question

For a graph-indexed family of commensurate Caputo systems

```math
{}^C D^\alpha x = F_G(x;\theta), \qquad 0<\alpha\le 1,
```

with equilibrium Jacobian

```math
J_G = D F_G(x^*),
```

study parameter regimes where the fractional system is asymptotically stable under the Matignon sector condition while the corresponding first-order system is not Hurwitz stable. A candidate region is

```math
\mathcal S_\alpha(G)=
\left\{\theta:
|\arg\lambda_i(J_G)|>\frac{\alpha\pi}{2}\ \forall i,
\quad \max_i\Re\lambda_i(J_G)>0
\right\}.
```

The project also asks whether positive diagonal rescaling `D J_G` creates a useful fractional analogue or extension of classical matrix D-stability, and whether graph topology controls that property.

## Do not assume novelty

The following are **not** enough by themselves:

- applying Matignon's criterion to a new ecological model;
- scanning several network topologies numerically;
- combining fractional derivatives and ecological networks;
- finding one matrix/parameter benchmark stabilized by `alpha < 1`;
- finite sampling over positive diagonal matrices;
- renaming a known sector-stability notion as fractional D-stability.

The audit must determine whether a genuinely new theorem remains after those standard ingredients are removed.

## Literature searches to cover

At minimum, search combinations and synonyms around:

1. `fractional-order ecological networks stability topology`;
2. `Caputo ecological network Jacobian Matignon stability`;
3. `fractional-order complex networks sector stability`;
4. `fractional D-stability matrix` / `D-stability fractional systems`;
5. `diagonal stability fractional-order systems`;
6. `positive diagonal scaling sector stable matrices`;
7. `D-stability sector stability` / `D-stable matrices sectors`;
8. `robust sector stability diagonal scaling`;
9. `community matrix fractional ecology stability`;
10. `fractional stabilization unstable equilibrium order alpha`;
11. `fractional-order stabilization by derivative order`;
12. graph/motif spectral results that may imply the proposed claims without fractional-specific mathematics.

Also inspect the terminology of **D-stability**, **diagonal stability**, **multiplicative D-stability**, **sector stability**, **D-alpha stability**, **Schur/Hurwitz D-stability**, and any existing fractional generalizations. Do not treat terminological mismatch as novelty.

## Questions the audit must answer

1. What is the closest existing mathematical object to the proposed `\mathcal S_\alpha(G)`?
2. Is “stable for fractional order but unstable at order 1” already a standard/known phenomenon? If yes, what part could still be new?
3. Has classical D-stability already been generalized to sectors, cones, fractional-order systems, or positive diagonal rescalings?
4. For `J = diag(x^*) A` in generalized Lotka--Volterra systems, do existing D-stability/diagonal-stability theorems already settle the proposed ecological interpretation?
5. Are there topology-to-spectrum theorems that would make the network contribution an immediate corollary?
6. Can the candidate contribution be raised from an example to a theorem over an open matrix/parameter family?
7. Can one derive necessary/sufficient conditions, sharp boundaries, motif obstructions, or an exact classification that appears absent from the literature?
8. Is there a nontrivial separation theorem between integer-order Hurwitz D-stability and fractional sector D-stability?
9. Is the proposed concept invariant under the relevant ecological scalings, permutations, similarity transformations, or row/column positive diagonal scalings?
10. What is the smallest theorem strong enough to support a title/abstract without overselling standard machinery?

## Evidence standard

For each candidate novelty claim, identify the closest paper and compare exact hypotheses/conclusions. Prefer theorem numbers and equations when available. Separate:

- `KNOWN/STANDARD`;
- `CLOSE BUT NOT EQUIVALENT`;
- `APPARENT GAP — NEEDS PROOF`;
- `NEW THEOREM CANDIDATE`;
- `OPEN/UNCERTAIN`.

Do not use “to the best of our knowledge” as a substitute for a comparison matrix.

## Deliverables

Create/update:

- `research/NOVELTY_REPORT.md`;
- `research/NOVELTY_MATRIX.md`;
- `research/CLAIMS.md`;
- `research/SCOPE_MATRIX.md` if scope changes;
- optionally `research/LITERATURE.bib` or a literature ledger with DOI/URL/theorem notes.

End the report with:

1. the strongest defensible novelty in <=3 sentences;
2. the strongest theorem that still needs to be proved;
3. the main prior-art risk;
4. whether the research direction should proceed unchanged, be narrowed, or be mathematically reframed.
