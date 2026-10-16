From Cain to Matignon: Exact Positive-Diagonal Stability in Dimension Three
and a Nonlinear Caputo Ecological Realization

Submission package for Mathematics / MDPI.

Contents:
- from-cain-to-matignon-positive-diagonal-stability.pdf : compiled 26-page manuscript
- latex-source/main.tex : standalone manuscript source
- latex-source/references.bib : audited published-source bibliography
- latex-source/sections/ : manuscript section sources
- latex-source/Definitions/ : MDPI class/style dependencies used by the manuscript
- latex-source/figures/ : seven figures used in the manuscript

Recompile:
  cd latex-source
  latexmk -pdf -file-line-error -interaction=nonstopmode main.tex

The supplied MDPI reference package contains the converted PDF logo but not the
original logo-mdpi.eps. The class may emit a non-fatal missing-EPS warning in
submit mode; this does not prevent successful PDF compilation.
