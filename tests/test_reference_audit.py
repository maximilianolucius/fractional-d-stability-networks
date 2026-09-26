"""Reference Audit Waves 1–2 — automated checks on the published-only bibliography and its promotion."""
import os
import re
import sys

import pytest

ROOT = os.path.join(os.path.dirname(__file__), "..")
sys.path.insert(0, os.path.join(ROOT, "computations", "reference_audit"))
import reference_audit as RA  # noqa: E402

BIB_TEXT = open(RA.BIB, encoding="utf-8").read()
FINAL_TEXT = open(RA.FINAL_BIB, encoding="utf-8").read()


@pytest.fixture(scope="module")
def report():
    return RA.audit()


def test_candidate_bib_parses_and_has_entries(report):
    assert not [e for e in report["errors"] if e.startswith("parse:")]
    assert report["n_entries"] == 46


def test_no_forbidden_tokens(report):
    assert report["forbidden_token_count"] == 0
    # the mandated header line of the final file states the rule ("no unpublished/preprint references") and is skipped
    for text in (BIB_TEXT, FINAL_TEXT[len(RA.FINAL_HEADER):]):
        low = text.lower()
        for tok in ("arxiv", "eprint", "archiveprefix", "@unpublished", "preprint", "submitted", "working paper", "personal communication"):
            assert tok not in low, tok


def test_no_duplicate_keys_dois_titles(report):
    assert not [e for e in report["errors"] if e.startswith("duplicate")]


def test_dois_are_bare_and_well_formed(report):
    assert not [e for e in report["errors"] if "malformed DOI" in e]
    for doi in re.findall(r"doi\s*=\s*\{([^}]*)\}", BIB_TEXT):
        assert RA.DOI_RE.match(doi) and "doi.org" not in doi


def test_every_article_has_doi_or_verified_isbn():
    entries, _ = RA.parse_bib(BIB_TEXT)
    for e in entries:
        f = e["fields"]
        if e["type"] in RA.ENTRY_TYPES_NEED_DOI:
            assert "doi" in f or (e["type"] == "inproceedings" and "isbn" in f), e["key"]
        for req in RA.REQUIRED.get(e["type"], ()):
            assert req in f, (e["key"], req)
        assert RA.FLAG not in f.get("note", ""), e["key"]


def test_load_bearing_keys_present_with_dois():
    entries, _ = RA.parse_bib(BIB_TEXT)
    d = {e["key"]: e["fields"] for e in entries}
    assert d["Kellogg1972"]["doi"] == "10.1007/BF01402527"
    assert d["KushelPavaniJDDE"]["year"] == "2022" and d["KushelPavaniJDDE"]["pages"] == "651--669"
    assert d["Siami2021"]["volume"] == "8" and d["Siami2021"]["number"] == "3"
    assert d["Cain1976"]["doi"] == "10.6028/jres.080B.013"
    assert d["BrandiburGarrappaKaslik2021"]["doi"] == "10.3390/math9080914"
    assert "isbn" in d["Matignon1996"] and "doi" not in d["Matignon1996"]
    assert "HoltPolis1997" in d and "Panja2019" in d
    assert "Shao2017" not in d and "DiethelmFordFreed2002" not in d


def test_matrix_and_ledger_citations_map_to_entries(report):
    assert not [e for e in report["errors"] if "not in the candidate .bib" in e]
    assert len(report.get("cited_in_CLAIM_REFERENCE_MATRIX.md", [])) >= 30
    assert not [w for w in report["warnings"] if "unresolved status" in w]
    for path in (RA.MATRIX, RA.LEDGER):
        txt = open(path, encoding="utf-8").read()
        assert "@Shao2017" not in txt and "@DiethelmFordFreed2002" not in txt
        assert "@KushelPavaniJDDE` (Theorem 3.3)" not in txt and "Thm 3.3" not in txt


def test_eprint_ids_blocklisted_and_absent_from_bibs(report):
    assert not [e for e in report["errors"] if e.startswith("e-print id")]
    ids = report["eprint_ids_in_repo"]
    assert {"2011.04204", "2004.11172", "2603.13608", "2604.16526", "1512.04989", "1907.07089", "2103.04127", "2205.10823"} <= set(ids)
    for i in ids:
        assert i not in BIB_TEXT and i not in FINAL_TEXT


def test_final_bibliography_promoted_verbatim(report):
    assert report.get("final_promoted") is True
    assert FINAL_TEXT == RA.FINAL_HEADER + "\n" + BIB_TEXT
    assert FINAL_TEXT.startswith("% Final published-source-only bibliography; no unpublished/preprint references permitted.")


def test_audit_zero_errors_zero_warnings(report):
    assert report["errors"] == [], report["errors"]
    assert report["warnings"] == [], report["warnings"]
    assert report["ok"]
