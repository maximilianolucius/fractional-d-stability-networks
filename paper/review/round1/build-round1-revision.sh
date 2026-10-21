#!/usr/bin/env bash
# Build the revision from the EXACT archived submitted ZIP, overlaying only reviewed LaTeX changes.
set -euo pipefail
ROOT="$(git rev-parse --show-toplevel)"
ORIG="$ROOT/paper/submission/round1-as-submitted/mathematics-4633263-submission-package.zip"
REV="$ROOT/paper/review/round1/revised-source"
WORK="$ROOT/paper/review/round1/_build"
OUT="$WORK/out"
rm -rf "$WORK"
mkdir -p "$WORK/source" "$OUT"
unzip -q "$ORIG" -d "$WORK/source"
MAIN="$(find "$WORK/source" -type f -name main.tex | head -n 1)"
test -n "$MAIN"
SOURCE="$(dirname "$MAIN")"
cp "$REV/main.tex" "$SOURCE/main.tex"
cp "$REV/references.bib" "$SOURCE/references.bib"
mkdir -p "$SOURCE/sections"
cp "$REV/sections/"*.tex "$SOURCE/sections/"
# figure overlays (relabelled fig02/fig03 without internal claim labels; new fig10 alpha sweep)
if [[ -d "$REV/figures" ]]; then mkdir -p "$SOURCE/figures"; cp "$REV/figures/"*.pdf "$SOURCE/figures/"; fi
# point-by-point response letters, one per reviewer (journal request): compiled from LaTeX, PDFs shipped in the ZIP
RESP="$ROOT/paper/review/round1/response"
rm -f "$SOURCE/RESPONSE_TO_REVIEWERS.md"
# the submitted package carried a stray copy of the original manuscript PDF under sections/; it is not a source file
find "$SOURCE/sections" -maxdepth 1 -name '*.pdf' -delete
printf '%s\n' "EXACT BASE ZIP: $(basename "$ORIG")" "SHA256: $(sha256sum "$ORIG" | cut -d' ' -f1)" > "$SOURCE/REVISED_BUILD_PROVENANCE.txt"
echo "Assembled manuscript source: $SOURCE"
if [[ "${1:-}" == "--assemble-only" ]]; then exit 0; fi
(cd "$RESP" && for r in response-reviewer1 response-reviewer2; do latexmk -pdf -file-line-error -halt-on-error -interaction=nonstopmode -output-directory="$WORK/response" "$r.tex" >/dev/null; done)
cp "$WORK/response/response-reviewer1.pdf" "$WORK/response/response-reviewer2.pdf" "$SOURCE/"
cp "$WORK/response/response-reviewer1.pdf" "$WORK/response/response-reviewer2.pdf" "$OUT/"
cd "$SOURCE"
latexmk -pdf -file-line-error -halt-on-error -interaction=nonstopmode main.tex
cp main.pdf "$OUT/from-cain-to-matignon-round1-revised.pdf"
cp main.pdf "$SOURCE/from-cain-to-matignon-round1-revised.pdf"
zip -qr "$OUT/mathematics-4633263-round1-revised-submission.zip" . -x "*.aux" "*.fdb_latexmk" "*.fls" "*.log" "*.bbl" "*.blg" "*.out" "*.synctex.gz"
(cd "$OUT" && sha256sum *.pdf *.zip > SHA256SUMS.txt)
echo "Built: $OUT"
