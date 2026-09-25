# SIMAX submission checklist

**Verified:** 2026-09-25 against current SIAM/SIMAX author instructions.

## Fit

SIMAX publishes matrix/tensor theory, analysis, applications and computation, including systems and control, mathematical biology and theoretical work with potential application impact.

The manuscript is a plausible scope fit because its central result is an exact positive-diagonal matrix-stability theorem with control/fractional and GLV interpretations.

## Current formal requirements relevant to this manuscript

- nominal page-limit policy: 20 journal pages;
- longer papers can be considered but are harder to referee;
- abstract: one paragraph, at most 250 words;
- figures must be embedded inline in the submitted PDF;
- keywords and MSC codes required;
- SIAM standard macros are strongly encouraged;
- title should be brief and indexing-friendly;
- a running title of at most 50 characters is required in SIAM format;
- theoretical papers should explain significance to applications or numerics;
- paper and cover letter are submitted as PDF;
- supplementary materials may be submitted with the article.

## Current manuscript status

- abstract: <250 words, one paragraph;
- keywords: present;
- MSC 2020: present;
- clean article-class build: PASS;
- current technical length: ~37 pages including bibliography;
- figures: pending Wave 2;
- main/supplement split: pending Wave 2;
- SIAM class conversion: pending compression;
- running title: pending SIAM class conversion;
- affiliation/contact: pending author confirmation;
- final repository SHA: pending final submission build.

## Compression objective after Wave 2

Target:
- main paper near 20 SIAM pages if possible;
- 4--6 main figures;
- one compact witness table;
- computational implementation details and extended tables in supplement;
- retain all load-bearing proof steps necessary for referee verification.

Do not compress the technical proof-complete version destructively. Preserve it as the source from which the SIMAX submission version is derived.


## Compression benchmark

The first compact submission derivation reduced the manuscript from 39 to 24 pages in the same neutral 11-point article layout while retaining the load-bearing theorem proofs.

The decisive page-count test is now \`paper/submission-siam.tex\` with the current official SIAM standard class \`siamart251216.cls\`. Do not judge the 20-page policy from the neutral article count alone.
