# Reference Audit Wave 2 — Final published-only bibliography reconciliation

**Date:** 2026-09-26  
**Assigned by:** Chief Researcher  
**Priority:** P0 — final bibliography gate  
**Repository:** `maximilianolucius/fractional-d-stability-networks`  
**Work branch:** `agent/reference-audit-wave2-20260926`  
**Base Chief SHA:** `b7eeb683b3ea982c526497a5991a5fa7b6ef7289`

## Mission

Close the bibliography gate mechanically.

The Chief has already:
- resolved all load-bearing metadata gaps by web verification;
- corrected Kushel–Pavani theorem-numbering contamination;
- added Panja 2019 and Holt–Polis 1997;
- completed key classical/ecological metadata;
- removed redundant uncertain references;
- reduced `paper/references_candidate_published_only.bib` to:
  - 46 entries;
  - 0 `NEEDS_CHIEF_WEB_VERIFICATION`;
  - 0 arXiv/eprint/archivePrefix/unpublished/preprint tokens.

Your task is to reconcile all reference-audit artifacts against that now-clean candidate and promote it to the final bibliography only if every check passes.

## Read first

1. `research/CHIEF_REFERENCE_WEB_VERIFICATION_2026-09-26.md`
2. `research/PUBLISHED_REFERENCE_LEDGER.md`
3. `research/CLAIM_REFERENCE_MATRIX.md`
4. `research/UNPUBLISHED_REFERENCE_BLOCKLIST.md`
5. `paper/references_candidate_published_only.bib`
6. `computations/reference_audit/reference_audit.py`
7. `tests/test_reference_audit.py`

## Required fixes

### 1. Reconcile ledger

Update `research/PUBLISHED_REFERENCE_LEDGER.md` so it no longer lists as unresolved:
- Kellogg;
- Cain DOI;
- Matignon DOI question;
- Brandibur metadata;
- Kushel–Pavani final metadata / theorem numbering;
- Siami metadata;
- Panja fractional IGP gap;
- Holt–Polis unnamed tradition;
- Arcak/Lee/Hartfiel/Kinkhabwala/Pal–Saha metadata now closed.

Remove references to `Shao2017` and `DiethelmFordFreed2002` from the final-paper ledger if they are no longer cited by the manuscript plan.

### 2. Reconcile claim-reference matrix

Update `research/CLAIM_REFERENCE_MATRIX.md`:
- C-08 Kellogg = READY;
- C-09/C-20 low-order dependency = READY;
- C-10 Kushel–Pavani citation = published 2022 article; refer to the conic-sector forbidden-boundary criterion, not “Theorem 3.3”;
- C-05 Arcak/Siami = READY;
- C-19 include published Holt–Polis and Panja;
- C-22 double-Allee citations = READY;
- remove `Shao2017` and `DiethelmFordFreed2002` if unused.

No OPEN or READY-VERIFY status may remain for any citation actually intended for the manuscript.

### 3. Reconcile inventory/blocklist

Do not delete internal provenance of blocked preprints.

Ensure:
- all arXiv identifiers remain in `research/UNPUBLISHED_REFERENCE_BLOCKLIST.md`;
- none appear in the final bibliography;
- published counterparts point to the clean published keys.

### 4. Final audit script

Run `computations/reference_audit/reference_audit.py` against the candidate.

Required:
- 0 errors;
- 0 warnings.

If the current script counts intentionally blocked provenance outside the bibliography as warnings, adjust reporting so:
- blocklisted provenance is informational;
- bibliography/claim-matrix uncertainty is what counts as a warning.

Do not weaken the checks.

### 5. Final bibliography promotion

ONLY if:
- 0 errors;
- 0 warnings;
- all intended claim-matrix keys resolve;
- no forbidden source tokens occur;
- BibTeX parses;

then replace:

`paper/references.bib`

with the exact clean contents of:

`paper/references_candidate_published_only.bib`

and add a header comment:

`% Final published-source-only bibliography; no unpublished/preprint references permitted.`

Do not delete the candidate file; keep it as audit provenance.

### 6. Tests

Update/add tests as needed.

Run the full repository suite.

## Required final artifacts

Create:

`research/REFERENCE_AUDIT_WAVE2_FINAL.md`

It must report:
- final bibliography entry count;
- errors/warnings;
- forbidden-token count;
- unresolved claim-reference mappings;
- whether `paper/references.bib` was promoted;
- full test result.

## Repository restrictions

Do not modify:
- theorem files;
- `research/CLAIMS.md`;
- novelty conclusions except correcting stale theorem-numbering text already identified by Chief;
- manuscript prose beyond `paper/references.bib`.

Do not merge to main.

## Final status

Return exactly one:
- `REFERENCE_AUDIT_WAVE2_PASS`
- `REFERENCE_AUDIT_WAVE2_PASS_WITH_FIXES`
- `REFERENCE_AUDIT_WAVE2_FAIL`
- `PARTIAL/BLOCKED`

PASS requires:
- 0 errors;
- 0 warnings;
- final bibliography promoted;
- full tests green.
