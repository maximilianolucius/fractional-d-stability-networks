# Reference Audit Wave 1 — Published-source-only bibliography gate

**Date:** 2026-09-26
**Assigned by:** Chief Researcher
**Priority:** P0 — final pre-manuscript gate
**Repository:** `maximilianolucius/fractional-d-stability-networks`
**Work branch:** `agent/reference-audit-wave1-20260926`
**Base Chief SHA:** `155207f1435f1bf7e13170ad65e310350aa8ef14`

## Mission

Build the complete reference inventory needed for the final paper and enforce the project's publication rule:

> **The submitted manuscript may cite formally published sources only.**

Forbidden as final references:
- arXiv/preprints;
- working papers;
- submitted/unpublished manuscripts;
- technical drafts;
- personal communications.

Internal novelty notes may mention unpublished material for provenance, but no manuscript claim may depend on it.

This wave is primarily a repository extraction, consistency and bibliographic sanitation task. Do not change theorem claims.

---

# Read first

1. `agent_directives_publishable_first_submission.md`
2. `research/CLAIMS.md`
3. `research/Q1_PAPER_ARCHITECTURE.md`
4. `research/MANUSCRIPT_STORYBOARD_2026-09-26.md`
5. `research/CHIEF_FINAL_DOUBLE_ALLEE_GATE_2026-09-26.md`
6. `research/CHIEF_FINAL_VISUAL_GATE_2026-09-26.md`
7. all files under `research/novelty/`
8. theorem files C-07 through C-16 and the Double-Allee theorem file;
9. existing `paper/references.bib`.

---

# Part A — exhaustive citation inventory

Search the repository for all external scholarly references mentioned in theorem notes, novelty audits, Chief reports, figure captions, paper architecture, and README/research-status where relevant.

Create:

`research/REFERENCE_INVENTORY_ALL.md`

Each unique work should have:
- normalized author list;
- year;
- title;
- journal/conference/book;
- volume/issue/pages or article number;
- DOI;
- URL if useful internally;
- where it is currently mentioned in the repo;
- manuscript role: LOAD-BEARING THEOREM / CLOSEST PRIOR ART / ECOLOGY CONTEXT / NUMERICAL METHOD / OPTIONAL BACKGROUND;
- publication status: PUBLISHED / UNPUBLISHED-PREPRINT / UNKNOWN-NEEDS-CHIEF-VERIFICATION.

Deduplicate variant citations of the same work.

# Part B — unpublished-source detection

Create:

`research/UNPUBLISHED_REFERENCE_BLOCKLIST.md`

List every arXiv ID, preprint, working paper, unpublished/submitted manuscript, or personal communication that appears anywhere in the research material.

For each:
- exact repo location;
- whether a published version exists in repository evidence;
- proposed published replacement if known;
- whether any current claim depends on it.

Do not delete research provenance. The goal is to ensure no such item reaches the manuscript bibliography.

# Part C — load-bearing reference ledger

Create:

`research/PUBLISHED_REFERENCE_LEDGER.md`

At minimum include published sources needed for:
1. classical D-stability / Cain;
2. Matignon fractional stability;
3. generalized / relative / strong D-stability closest prior art;
4. P-matrix / sector / Kellogg-type low-order argument;
5. ecological/Kolmogorov D-stability background;
6. fractional intraguild predation prior art;
7. double-Allee ecological prior art;
8. any numerical fractional method actually mentioned in the final manuscript;
9. closest literature identified in the C-10/C-15 novelty audits.

For every load-bearing source, record:
- exact theorem/result imported;
- exact claim in our paper that needs the citation;
- exact publication metadata;
- DOI;
- whether metadata has been independently verified or still needs Chief web verification.

# Part D — bibliography draft

Create:

`paper/references_candidate_published_only.bib`

This is NOT yet the final `paper/references.bib`.

Rules:
- include only sources classified PUBLISHED;
- no arXiv fields;
- no eprint fields;
- no archivePrefix;
- no unpublished entry type;
- DOI normalized as bare DOI;
- preserve full journal title unless journal template requires abbreviation later;
- one canonical BibTeX key per source.

Do not overwrite `paper/references.bib`.

# Part E — claim-to-reference matrix

Create:

`research/CLAIM_REFERENCE_MATRIX.md`

Rows:
- C-01 through C-22 where an external citation is needed;
- major introduction/novelty statements.

Columns:
- claim;
- whether internally proved;
- external citation purpose;
- published source(s);
- citation status;
- unresolved risk.

Important distinction:
- our original theorem does not need a citation as authority;
- imported background theorem/criterion does;
- novelty wording needs closest-prior-art citations.

# Part F — automated checks

Create `computations/reference_audit/reference_audit.py`.

Required checks:
1. detect forbidden tokens such as arxiv, eprint, archivePrefix, unpublished, submitted, preprint in candidate final bibliography;
2. duplicate DOI detection;
3. duplicate normalized-title detection;
4. missing DOI for works that are supposed to have one;
5. malformed DOI;
6. duplicate BibTeX keys;
7. candidate `.bib` parses;
8. every citation in claim-reference matrix maps to a BibTeX entry.

Add namespaced tests:

`tests/test_reference_audit.py`

Run full repository suite.

# Important scope rule

You are NOT authorized to invent metadata.

If DOI/journal/pages cannot be verified from repository evidence, mark:

`NEEDS_CHIEF_WEB_VERIFICATION`

Do not guess. Do not use arXiv as a fallback.

# Repository restrictions

Work only on `agent/reference-audit-wave1-20260926`.

Allowed:
- new research reference-audit files;
- candidate bibliography;
- audit scripts/tests.

Forbidden:
- theorem files;
- `research/CLAIMS.md`;
- final novelty conclusions;
- existing `paper/references.bib`;
- manuscript prose;
- main.

No merge.

# Final status

Return exactly one:
- `REFERENCE_AUDIT_WAVE1_PASS`
- `REFERENCE_AUDIT_WAVE1_PASS_WITH_GAPS`
- `REFERENCE_AUDIT_WAVE1_FAIL`
- `PARTIAL/BLOCKED`

PASS requires:
- repository-wide inventory;
- unpublished blocklist;
- candidate published-only BibTeX;
- claim-reference matrix;
- automated checks green.

It is acceptable to return PASS_WITH_GAPS if some metadata explicitly requires Chief web verification.

At completion report:
- branch;
- final SHA;
- tests;
- number of unique references found;
- number published;
- number unpublished/blocked;
- number needing Chief web verification;
- load-bearing unresolved items;
- artifact paths.