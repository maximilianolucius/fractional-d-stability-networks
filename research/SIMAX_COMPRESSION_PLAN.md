# SIMAX compression plan

**Status:** execute after Wave 2, before journal-format conversion.

The proof-complete technical manuscript is intentionally longer than the expected final submission. SIMAX states a nominal 20-page policy; longer papers are possible but harder to referee.

## Keep in the main article

1. Introduction and exact prior-art boundary.
2. Definitions and the n-dimensional orbit reduction, compressed to one lemma.
3. Exact 2x2 theorem and empty-interior corollary.
4. Exact cubic ray boundary.
5. C-10 exact 3x3 theorem.
6. P0 necessity / strict-P interior theorem.
7. Cain endpoint and exact fractional band.
8. C-15 strict convexity and uniqueness.
9. One symmetry corollary plus canonical A_gamma family.
10. C-14 classical-limit rate.
11. C-09 minimum-dimension theorem.
12. Concise GLV loop interpretation.
13. One compact computational-validation table and reproducibility paragraph.
14. Discussion and limitations.

## Likely move to appendix or supplement

1. Detailed proof algebra of the global threshold-surface parametrization if page pressure is high.
2. Full low-order alpha->2/3 expansion proof details beyond the leading structure.
3. C-11 Cauchy-Schwarz derivation and coverage-fraction derivation, retaining only statements in main text.
4. Full realizability construction details, if necessary; retain theorem and construction formula in main text.
5. Detailed stress-test mechanism table.
6. Extreme-scaling numerical pathology narrative.
7. Full certified-anchor methodology.
8. Wave 2 robustness tables and additional witnesses.
9. Additional ecological phase diagrams.

## Target final balance

A good SIMAX version should read approximately:

- 55--65% exact matrix theory/proofs;
- 10--15% prior art and motivation;
- 10--15% ecological interpretation/application;
- 10--15% computational certification and reproducibility.

The final paper should not read as a computational study.

## Figure budget

Main text: approximately 4--6 figures.

Proposed priority:

1. Matignon versus Hurwitz spectral region.
2. Exact Cain surface versus fractional threshold / fractional band.
3. T_alpha versus alpha showing both limiting regimes.
4. Threshold-simplex geometry / unique optimizer.
5. Ecological loop-space phase diagram.
6. Optional canonical nonsymmetric witness comparison.

Additional Wave 2 plots go to supplement.

## Trigger

Do not perform this compression until Wave 2 produces final figure data and canonical witness selection; otherwise the main/supplement split would have to be redone.


## Proof dependency lock

The following proof material must remain in the refereed main article because removing it would make the flagship theorem depend on an unrefereed supplement:

1. exact cubic ray-boundary derivation;
2. orbit/simplex normalization;
3. proof of the iff threshold theorem;
4. P0 necessity and strict-P interior argument;
5. recovery of Cain and strict inequality \(T_\alpha>T_1\);
6. strict logit-convexity theorem;
7. minimum-dimension theorem.

The following can move to an appendix or supplement while retaining the theorem statement and essential formula in the main article:

1. detailed algebra of the global \((x,r)\) threshold-surface parametrization;
2. second-order bookkeeping in the \(\alpha\downarrow2/3\) expansion;
3. full C-11 Cauchy--Schwarz certificate derivation;
4. C-11 coverage-fraction proof;
5. detailed realizability sign-case analysis, provided the explicit construction and theorem remain in the main text;
6. full computational stress-test table;
7. extreme-scaling numerical pathology;
8. interval branch-and-bound implementation detail;
9. Wave 2 robustness tables and extended witness library.

## Compression rule

Do not move a proof to unrefereed supplementary material if the main theorem would become logically dependent on that material.

If SIMAX length pressure remains severe after normal prose/table/figure compression, prefer a refereed appendix within the manuscript over an unrefereed supplement for load-bearing mathematics.
