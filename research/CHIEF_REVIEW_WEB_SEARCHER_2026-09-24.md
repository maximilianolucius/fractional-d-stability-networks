# Chief Researcher review of the reopened web-search audit

**Date:** 2026-09-24  
**Reviewed HEAD:** `72cef68762b24cfa01527796e28078fc2328e6b7`  
**Chief verdict on web-search work:** **ACCEPT WITH MATHEMATICAL EXTENSION; NOVELTY STILL NOT FROZEN**

## What is accepted

The second-pass web audit correctly changes the project direction in four important ways:

1. **Single-cycle fractional secant novelty is rejected.** Siami 2020/2021 substantially occupies that target.
2. **Generic generalized/fractional D-stability is not new.** Kushel and Kushel–Pavani provide the ambient generalized-region framework.
3. **Robust/interior/strong D-stability is not new terminology or a new concept.** Hartfiel/Abed and successors must be treated as prior art.
4. The low-dimensional programme is the strongest surviving line:
   - exact n=2 obstruction/classification;
   - full-dimensional genuinely non-Hurwitz fractional D-stability first appearing in n=3.

The web agent's C-07 proof is accepted as an internal theorem. Its C-08 argument for `0<alpha<=2/3` is also accepted modulo correct citation of Kellogg's P-matrix wedge theorem.

## Chief correction to the remaining open frontier

The web agent left `n=3, 2/3<alpha<1` open. That range admits a direct analytic sufficient criterion for positive-coefficient cubics which, combined with AM-GM over the diagonal orbit, appears to close C-09 for **all** `0<alpha<1`.

The full proof is recorded in:

- `research/THEOREM_C09_DIMENSION_THRESHOLD.md`

The result must be treated as:

> **INTERNALLY PROVED / NOVELTY NOT YET FROZEN**

until a targeted theorem-level literature audit is completed.

## Publication significance if novelty survives

The resulting theorem package is substantially stronger and cleaner than the former graph/cactus target:

\[
\min\{n:\operatorname{int}(\mathcal F_\alpha^{(n)}\setminus\mathcal D_H^{(n)})\neq\varnothing\}=3
\qquad\forall\,0<\alpha<1.
\]

This gives:

- an exact dimension threshold;
- a sharp distinction between boundary-only separation in n=2 and full-dimensional separation in n=3;
- a concrete open family;
- a mechanism based on cubic angular geometry and principal-minor structure;
- a natural route back to motifs/ecological interpretation after the matrix theorem is secured.

## Q1 decision

**GO-NARROWED, with upgraded mathematical priority.**

The immediate research target is no longer "prove the high-order range"; it is now:

1. audit the new C-09 theorem against the optimal fractional Routh-Hurwitz literature and generalized D-stability literature;
2. check whether the cubic sufficient certificate is already published verbatim or is an easy corollary of a published necessary-and-sufficient criterion;
3. determine whether the **dimension-threshold theorem itself** has appeared;
4. only after novelty survives, build the structural/motif and ecological layers.

No manuscript title or abstract should yet say "new theorem" until this targeted audit is complete.
