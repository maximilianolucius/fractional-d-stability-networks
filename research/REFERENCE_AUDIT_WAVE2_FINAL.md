# Reference Audit Wave 2 — final report

**Status: `REFERENCE_AUDIT_WAVE2_PASS`**
**Branch** `agent/reference-audit-wave2-20260926` (base Chief SHA `b7eeb68`, HEAD prepared `1d8fe96`) · **Date** 2026-09-26

## Result

| item | value |
|---|---|
| final bibliography `paper/references.bib` | **promoted** = mandated header line + exact contents of `paper/references_candidate_published_only.bib` |
| entries | 46 (43 `@article`, 1 `@inproceedings`, 2 `@book` — 45 with DOI; Matignon 1996 identified by ISBN 2-9502908-9-2, no DOI exists per the Chief record) |
| audit errors / warnings | **0 / 0** (`computations/reference_audit/reference_audit.py`; report in `computations/reference_audit/reference_audit_report.json`) |
| forbidden tokens (arxiv, eprint, archivePrefix, unpublished, submitted, preprint, working paper, personal communication, …) | **0** in the candidate and in the body of the final file (the mandated header line itself states the rule and is excluded from the scan) |
| `NEEDS_CHIEF_WEB_VERIFICATION` marks in bibliography / ledger / matrix | 0 |
| unresolved claim-reference mappings | **0** — every key cited in `CLAIM_REFERENCE_MATRIX.md` (41 keys) and `PUBLISHED_REFERENCE_LEDGER.md` (46 keys) resolves; no OPEN / READY-VERIFY status remains |
| blocklisted e-print identifiers retained as provenance | 8 (informational; none appears in either .bib) |
| full test suite | **62 passed, 0 failed** (52 pre-existing + 10 in `tests/test_reference_audit.py`) |

## What was reconciled

1. **Ledger** (`research/PUBLISHED_REFERENCE_LEDGER.md`, rewritten): Kellogg 1972, Cain DOI, Matignon (no DOI; ISBN), Brandibur et al., Kushel–Pavani (JDDE 34 (2022) 651–669; conic-sector forbidden-boundary criterion, no theorem number hardcoded), Siami (TCNS 8(3) 1261–1269), Hartfiel, Lee–Edgar, Arcak–Sontag, Arcak, Kinkhabwala, Pal–Saha, Alraddadi et al., Tassaddiq et al. all recorded as closed; `HoltPolis1997` and `Panja2019` added (§6); `Shao2017` and `DiethelmFordFreed2002` removed (both dropped from the candidate by the Chief; still inventoried). "Load-bearing items unresolved": none.
2. **Claim matrix** (`research/CLAIM_REFERENCE_MATRIX.md`, rewritten): every row READY or NONE NEEDED; C-08/C-09/C-20 Kellogg dependency READY; C-10 cites the published 2022 Kushel–Pavani article's conic-sector criterion (no "Theorem 3.3"); C-05 Siami/Arcak READY; C-19 includes `@HoltPolis1997` and `@Panja2019` (fractional IGP exists; novelty is the exact positive-diagonal realization); C-22 double-Allee citations READY; Shao2017 / DiethelmFordFreed2002 removed.
3. **Blocklist** (`research/UNPUBLISHED_REFERENCE_BLOCKLIST.md`): all 8 arXiv identifiers retained (2011.04204, 2205.10823, 1907.07089, 2004.11172, 2103.04127, 2603.13608, 2604.16526, 1512.04989); published counterparts now point to the final keys with complete metadata; Holt–Polis resolved to `@HoltPolis1997`; e-print-only items (Kushel 2026, Casasanta–Simpson-Porco 2026, Cong et al. 2016) remain blocked. No provenance deleted.
4. **Inventory** (`research/REFERENCE_INVENTORY_ALL.md`): Wave-1 rows kept as the pre-verification record; a Wave-2 reconciliation note at the top lists every closure, the two additions and the two drops (unique works 75, published 71, e-print-only 3, unidentified 1: Grilli–Rogers–Allesina, not cited).
5. **Stale theorem numbering** (correction already identified by the Chief): "Theorem 3.3" replaced by "conic-sector forbidden-boundary criterion" in `research/novelty/C10_TARGETED_AUDIT.md` (2 places) and `research/NOVELTY_MATRIX.md` (2 places); no other novelty conclusion touched.
6. **Audit script**: reporting split into `errors` (block promotion), `warnings` (bibliography / claim-matrix uncertainty: flagged notes, missing DOI or required field, any OPEN / READY-VERIFY / NEEDS_CHIEF_WEB_VERIFICATION status token in the matrix or ledger) and `info` (blocklisted provenance outside the bibliography; ISBN-identified proceedings). New checks, none weakened: a proceedings paper without DOI passes only with an `isbn`; `paper/references.bib`, when it contains entries, must equal the mandated header + the exact candidate text and its body must contain no forbidden token. Exit status is 0 only at 0 errors and 0 warnings.
7. **Candidate header** rewritten to a neutral Wave-2 statement (the Wave-1 header said "NOT the final references.bib", which would have been copied verbatim into the final file).

## Promotion record

`paper/references.bib` = `% Final published-source-only bibliography; no unpublished/preprint references permitted.` + `\n` + `paper/references_candidate_published_only.bib` (byte-exact; enforced by `test_final_bibliography_promoted_verbatim`). The candidate file is kept as audit provenance.

## Residual notes (not warnings)

- Theorem numbers ("Theorem 2" of Siami 2021) should be re-checked against the page proofs at drafting time; the matrix says so.
- Grilli–Rogers–Allesina (name-only mention in an early novelty note) is not identified and is not cited.
- General fractional-calculus background entries (`Garrappa2010`, `Garrappa2018`, `Podlubny1999`, `Diethelm2010`, `SabatierMozeFarges2010`, `CermakKiselaNechvatal2013`) and `AlAhmadieh2026` are in the bibliography as optional background; unused keys are harmless to BibTeX and can be pruned at typesetting.
