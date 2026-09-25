# Manuscript

Current technical manuscript branch:

\`q1-manuscript-20260925\`

Entry point:

\`paper/main.tex\`

## Build

From the repository root:

\`\`\`bash
cd paper
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
\`\`\`

The manuscript uses BibTeX through \`latexmk\`.

## Continuous integration

The branch workflow

\`.github/workflows/paper.yml\`

builds the PDF on paper changes, checks the LaTeX log for warnings, and uploads \`paper/main.pdf\` as a workflow artifact.

## Status

This is the proof-complete technical version.

Scientific gates:
- novelty: PASS WITH REPOSITIONING;
- proof: PASS;
- computation: PASS.

Internal manuscript audit:
- theorem reconciliation: PASS;
- citation/reference static audit: PASS;
- clean PDF build: PASS;
- referee pass 2: scientific content ready, editorial compression pending.

The eventual target-journal version will be derived from this technical manuscript after Compute Wave 2 provides final figures, canonical witnesses and robustness data.
