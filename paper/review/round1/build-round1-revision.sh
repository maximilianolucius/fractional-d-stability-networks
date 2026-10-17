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
cp "$ROOT/paper/review/round1/RESPONSE_TO_REVIEWERS.md" "$SOURCE/RESPONSE_TO_REVIEWERS.md"
printf '%s\n' "EXACT BASE ZIP: $(basename "$ORIG")" "SHA256: $(sha256sum "$ORIG" | cut -d' ' -f1)" > "$SOURCE/REVISED_BUILD_PROVENANCE.txt"
echo "Assembled manuscript source: $SOURCE"
if [[ "${1:-}" == "--assemble-only" ]]; then exit 0; fi
cd "$SOURCE"
latexmk -pdf -file-line-error -halt-on-error -interaction=nonstopmode main.tex
cp main.pdf "$OUT/from-cain-to-matignon-round1-revised.pdf"
cp main.pdf "$SOURCE/from-cain-to-matignon-round1-revised.pdf"
zip -qr "$OUT/mathematics-4633263-round1-revised-submission.zip" . -x "*.aux" "*.fdb_latexmk" "*.fls" "*.log" "*.bbl" "*.blg" "*.out" "*.synctex.gz"
(cd "$OUT" && sha256sum *.pdf *.zip > SHA256SUMS.txt)
echo "Built: $OUT"
