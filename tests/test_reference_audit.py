"""Reference Audit Wave 1 — automated checks on the published-only candidate bibliography."""
import os
import re
import sys

import pytest

ROOT = os.path.join(os.path.dirname(__file__), "..")
sys.path.insert(0, os.path.join(ROOT, "computations", "reference_audit"))
import reference_audit as RA  # noqa: E402

BIB_TEXT = open(RA.BIB, encoding="utf-8").read()


@pytest.fixture(scope="module")
def report():
    return RA.audit()


def test_candidate_bib_parses_and_has_entries(report):
    assert not [e for e in report["errors"] if e.startswith("parse:")]
    assert report["n_entries"] >= 40


def test_no_forbidden_tokens(report):
    assert not [e for e in report["errors"] if e.startswith("forbidden token")]
    low = BIB_TEXT.lower()
    for tok in ("arxiv", "eprint", "archiveprefix", "@unpublished", "preprint", "submitted"):
        assert tok not in low, tok


def test_no_duplicate_keys_dois_titles(report):
    assert not [e for e in report["errors"] if e.startswith("duplicate")]


def test_dois_are_bare_and_well_formed(report):
    assert not [e for e in report["errors"] if "malformed DOI" in e]
    for doi in re.findall(r"doi\s*=\s*\{([^}]*)\}", BIB_TEXT):
        assert RA.DOI_RE.match(doi) and "doi.org" not in doi


def test_missing_doi_only_when_flagged(report):
    assert not [e for e in report["errors"] if "no DOI" in e or "missing field" in e]
    # entries without DOI must be explicitly flagged for the Chief
    entries, _ = RA.parse_bib(BIB_TEXT)
    for e in entries:
        if e["type"] in RA.ENTRY_TYPES_NEED_DOI and "doi" not in e["fields"]:
            assert RA.FLAG in e["fields"].get("note", ""), e["key"]


def test_matrix_and_ledger_citations_map_to_entries(report):
    assert not [e for e in report["errors"] if "not in the candidate .bib" in e]
    assert len(report.get("cited_in_CLAIM_REFERENCE_MATRIX.md", [])) >= 30


def test_eprint_ids_blocklisted_and_absent_from_bib(report):
    assert not [e for e in report["errors"] if e.startswith("e-print id")]
    ids = report["eprint_ids_in_repo"]
    assert {"2011.04204", "2004.11172", "2603.13608", "2604.16526", "1512.04989"} <= set(ids)
    for i in ids:
        assert i not in BIB_TEXT


def test_audit_is_green(report):
    assert report["ok"], report["errors"]


def test_final_references_bib_untouched():
    txt = open(os.path.join(ROOT, "paper", "references.bib"), encoding="utf-8").read()
    assert "@" not in txt  # still the Chief's empty placeholder; this wave writes only the candidate file
