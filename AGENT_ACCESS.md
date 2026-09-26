# Agent access and handoff

## ACTIVE TASK — REFERENCE AUDIT WAVE 1

**Date:** 2026-09-26
**Repository:** `maximilianolucius/fractional-d-stability-networks`
**Work branch:** `agent/reference-audit-wave1-20260926`
**Base Chief SHA:** `155207f1435f1bf7e13170ad65e310350aa8ef14`

### Your only active assignment

Read and execute:

`research/REFERENCE_AUDIT_WAVE1_TASK.md`

### Mission

Build a repository-wide published-source-only citation inventory, candidate bibliography, unpublished-source blocklist, and claim-to-reference matrix.

Do not invent metadata.

If publication status, DOI, pages, or venue cannot be established from repository evidence, mark it `NEEDS_CHIEF_WEB_VERIFICATION`.

### Publication rule

The submitted paper may cite formally published sources only.

Forbidden final references:
- arXiv/preprints;
- working papers;
- submitted/unpublished manuscripts;
- technical drafts;
- personal communications.

Do not delete internal research provenance; only prevent unpublished material from flowing into the manuscript bibliography.

### Required artifacts

- `research/REFERENCE_INVENTORY_ALL.md`
- `research/UNPUBLISHED_REFERENCE_BLOCKLIST.md`
- `research/PUBLISHED_REFERENCE_LEDGER.md`
- `research/CLAIM_REFERENCE_MATRIX.md`
- `paper/references_candidate_published_only.bib`
- `computations/reference_audit/reference_audit.py`
- `tests/test_reference_audit.py`

### Restrictions

Do NOT modify:
- theorem files;
- `research/CLAIMS.md`;
- novelty conclusions;
- `paper/references.bib`;
- manuscript prose;
- main.

Do not merge.

### Final status

Return exactly one:
- `REFERENCE_AUDIT_WAVE1_PASS`
- `REFERENCE_AUDIT_WAVE1_PASS_WITH_GAPS`
- `REFERENCE_AUDIT_WAVE1_FAIL`
- `PARTIAL/BLOCKED`

At completion report branch, final SHA, test count, reference counts, unpublished/blocked items, unresolved load-bearing metadata, and artifact paths.

---

All previous proof/figure waves are historical context only.