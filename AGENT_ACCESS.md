# Agent access and handoff

## ACTIVE TASK — REFERENCE AUDIT WAVE 2

**Date:** 2026-09-26  
**Repository:** `maximilianolucius/fractional-d-stability-networks`  
**Work branch:** `agent/reference-audit-wave2-20260926`  
**Base Chief SHA:** `b7eeb683b3ea982c526497a5991a5fa7b6ef7289`

### Your only active assignment

Read and execute:

`research/REFERENCE_AUDIT_WAVE2_TASK.md`

### Mission

Perform the final mechanical reconciliation of the now web-verified published-only bibliography.

The Chief has already reduced the candidate bibliography to:
- 46 entries;
- 0 `NEEDS_CHIEF_WEB_VERIFICATION`;
- 0 forbidden unpublished/preprint tokens.

Your job is to:
- reconcile ledger/matrix/blocklist;
- rerun the audit;
- reach 0 errors / 0 warnings;
- promote the candidate to `paper/references.bib` only if every gate passes.

### Critical correction

For Kushel–Pavani:
- do NOT write “Theorem 3.3”;
- the relevant result is the conic-sector forbidden-boundary criterion;
- the published-text lineage numbers it as Theorem 6.

### Final bibliography rule

No:
- arXiv;
- eprint;
- archivePrefix;
- preprint;
- unpublished;
- working paper;
- submitted manuscript;
- technical draft;
- personal communication.

### Restrictions

Do NOT modify:
- theorem files;
- `research/CLAIMS.md`;
- manuscript prose other than final `paper/references.bib`;
- main.

Do not merge.

### Final status

Return exactly one:
- `REFERENCE_AUDIT_WAVE2_PASS`
- `REFERENCE_AUDIT_WAVE2_PASS_WITH_FIXES`
- `REFERENCE_AUDIT_WAVE2_FAIL`
- `PARTIAL/BLOCKED`

At completion report:
- branch;
- final SHA;
- bibliography count;
- errors/warnings;
- forbidden-token count;
- unresolved mappings;
- whether final references.bib was promoted;
- full test count.
