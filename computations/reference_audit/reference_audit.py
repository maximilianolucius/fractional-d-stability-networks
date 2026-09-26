"""Reference audit — automated checks for the published-source-only candidate bibliography.

Checks (Reference Audit Wave 1, Part F):
 1. forbidden tokens (e-print servers / non-published status words) anywhere in the candidate .bib;
 2. duplicate DOIs;
 3. duplicate normalised titles;
 4. missing DOI for journal articles / proceedings papers, unless the entry carries an explicit
    NEEDS_CHIEF_WEB_VERIFICATION note (then it is reported as "flagged", not as an error);
 5. malformed DOI (must be a bare DOI: 10.NNNN/suffix, no URL prefix, no trailing punctuation);
 6. duplicate BibTeX keys;
 7. the candidate .bib parses (balanced braces, every entry has a type and a key);
 8. every citation key referenced as @Key in the claim-reference matrix (and the ledger) maps to a BibTeX entry;
 9. (repository sweep) every e-print identifier mentioned anywhere in research material is listed in the
    blocklist, and none of them appears in the candidate .bib.

Usage:  python computations/reference_audit/reference_audit.py [--json report.json]
Exit status 0 iff no error (flags are allowed).
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
BIB = os.path.join(ROOT, "paper", "references_candidate_published_only.bib")
MATRIX = os.path.join(ROOT, "research", "CLAIM_REFERENCE_MATRIX.md")
LEDGER = os.path.join(ROOT, "research", "PUBLISHED_REFERENCE_LEDGER.md")
BLOCKLIST = os.path.join(ROOT, "research", "UNPUBLISHED_REFERENCE_BLOCKLIST.md")
SWEEP_DIRS = ("research", "paper", "README.md", "AGENT_ACCESS.md", "reference-paper", "agent_directives_publishable_first_submission.md")

FORBIDDEN_TOKENS = ("arxiv", "eprint", "archiveprefix", "unpublished", "submitted", "preprint",
                    "working paper", "personal communication", "in preparation", "biorxiv", "ssrn", "hal-", "researchgate")
FLAG = "NEEDS_CHIEF_WEB_VERIFICATION"
DOI_RE = re.compile(r"^10\.\d{4,9}/[^\s]+$")
EPRINT_ID_RE = re.compile(r"(?<![\w/.])(?:arXiv:)?(\d{4}\.\d{4,5})(?:v\d+)?(?![\w.])", re.IGNORECASE)
ENTRY_TYPES_NEED_DOI = {"article", "inproceedings"}
REQUIRED = {"article": ("author", "title", "journal", "year"), "inproceedings": ("author", "title", "booktitle", "year"), "book": ("author", "title", "publisher", "year")}


def parse_bib(text: str):
    """Minimal BibTeX parser: returns (entries, errors). entries = list of dict(type, key, fields, raw)."""
    entries, errors = [], []
    i = 0
    n = len(text)
    while True:
        j = text.find("@", i)
        if j < 0:
            break
        # skip '@' inside comments
        line_start = text.rfind("\n", 0, j) + 1
        if text[line_start:j].lstrip().startswith("%"):
            i = j + 1
            continue
        m = re.match(r"@(\w+)\s*\{", text[j:])
        if not m:
            errors.append(f"malformed entry header at offset {j}")
            i = j + 1
            continue
        etype = m.group(1).lower()
        k = j + m.end()  # position after '{'
        depth, p = 1, k
        while p < n and depth:
            if text[p] == "{":
                depth += 1
            elif text[p] == "}":
                depth -= 1
            p += 1
        if depth:
            errors.append(f"unbalanced braces in entry starting at offset {j}")
            break
        body = text[k:p - 1]
        comma = body.find(",")
        key = body[:comma].strip() if comma >= 0 else body.strip()
        if not key or " " in key:
            errors.append(f"entry of type {etype} without a valid key at offset {j}")
        fields = {}
        rest = body[comma + 1:] if comma >= 0 else ""
        q = 0
        while q < len(rest):
            fm = re.match(r"\s*(\w+)\s*=\s*", rest[q:])
            if not fm:
                if rest[q:].strip(" ,\n\t"):
                    errors.append(f"{key}: unparsable field text {rest[q:q+30]!r}")
                break
            name = fm.group(1).lower()
            q += fm.end()
            if rest[q] == "{":
                d, r = 1, q + 1
                while r < len(rest) and d:
                    if rest[r] == "{":
                        d += 1
                    elif rest[r] == "}":
                        d -= 1
                    r += 1
                if d:
                    errors.append(f"{key}: unbalanced braces in field {name}")
                    break
                val = rest[q + 1:r - 1]
                q = r
            elif rest[q] == '"':
                r = rest.find('"', q + 1)
                val = rest[q + 1:r]
                q = r + 1
            else:
                r = q
                while r < len(rest) and rest[r] not in ",\n":
                    r += 1
                val = rest[q:r].strip()
                q = r
            fields[name] = " ".join(val.split())
            cm = re.match(r"\s*,", rest[q:])
            q += cm.end() if cm else 0
        entries.append({"type": etype, "key": key, "fields": fields, "raw": text[j:p]})
        i = p
    return entries, errors


def normalise_title(t: str) -> str:
    t = re.sub(r"\$[^$]*\$", " ", t)
    t = re.sub(r"[{}\\'`\"^~]", "", t)
    t = re.sub(r"[^a-z0-9]+", " ", t.lower())
    return t.strip()


def audit(bib_path=BIB, matrix_path=MATRIX, ledger_path=LEDGER, blocklist_path=BLOCKLIST, root=ROOT):
    rep = {"errors": [], "flags": [], "n_entries": 0, "keys": []}
    text = open(bib_path, encoding="utf-8").read()
    # 1. forbidden tokens (whole file, case-insensitive)
    low = text.lower()
    for tok in FORBIDDEN_TOKENS:
        for m in re.finditer(re.escape(tok), low):
            ln = low.count("\n", 0, m.start()) + 1
            rep["errors"].append(f"forbidden token {tok!r} at line {ln}")
    # 7. parse
    entries, perr = parse_bib(text)
    rep["errors"] += [f"parse: {e}" for e in perr]
    rep["n_entries"] = len(entries)
    rep["keys"] = [e["key"] for e in entries]
    # 6. duplicate keys
    seen = {}
    for e in entries:
        seen.setdefault(e["key"], 0)
        seen[e["key"]] += 1
    rep["errors"] += [f"duplicate key {k}" for k, c in seen.items() if c > 1]
    # 2., 5. DOIs
    dois = {}
    for e in entries:
        f = e["fields"]
        if e["type"] == "unpublished":
            rep["errors"].append(f"{e['key']}: entry type denotes non-published work")
        doi = f.get("doi")
        flagged = FLAG in f.get("note", "")
        if doi:
            if not DOI_RE.match(doi) or doi.endswith((".", ",", ";")) or "doi.org" in doi.lower():
                rep["errors"].append(f"{e['key']}: malformed DOI {doi!r}")
            dois.setdefault(doi.lower(), []).append(e["key"])
        elif e["type"] in ENTRY_TYPES_NEED_DOI:
            (rep["flags"] if flagged else rep["errors"]).append(f"{e['key']}: no DOI" + (" (flagged for Chief verification)" if flagged else ""))
        # required fields
        for req in REQUIRED.get(e["type"], ()):
            if req not in f:
                (rep["flags"] if flagged else rep["errors"]).append(f"{e['key']}: missing field {req}" + (" (flagged)" if flagged else ""))
        if "url" in f and "doi.org" in f["url"].lower():
            rep["errors"].append(f"{e['key']}: url duplicates a DOI; use the doi field")
        if flagged:
            rep["flags"].append(f"{e['key']}: {FLAG}")
    rep["errors"] += [f"duplicate DOI {d} in {ks}" for d, ks in dois.items() if len(ks) > 1]
    # 3. duplicate normalised titles
    titles = {}
    for e in entries:
        if "title" in e["fields"]:
            titles.setdefault(normalise_title(e["fields"]["title"]), []).append(e["key"])
    rep["errors"] += [f"duplicate title {t[:40]!r} in {ks}" for t, ks in titles.items() if len(ks) > 1]
    # 8. matrix / ledger citations map to entries
    keys = set(rep["keys"])
    for path in (matrix_path, ledger_path):
        if os.path.exists(path):
            cited = set(re.findall(r"@([A-Za-z][A-Za-z0-9_]+)", open(path, encoding="utf-8").read()))
            missing = sorted(cited - keys)
            rep["errors"] += [f"{os.path.basename(path)} cites @{k} which is not in the candidate .bib" for k in missing]
            rep[f"cited_in_{os.path.basename(path)}"] = sorted(cited)
    # 9. repository sweep of e-print identifiers vs blocklist
    ids_found = {}
    for d in SWEEP_DIRS:
        p = os.path.join(root, d)
        files = [p] if os.path.isfile(p) else [os.path.join(dp, fn) for dp, _, fns in os.walk(p) for fn in fns if fn.endswith((".md", ".tex", ".bib"))]
        for fp in files:
            if os.path.abspath(fp) in (os.path.abspath(bib_path), os.path.abspath(blocklist_path)):
                continue
            try:
                t = open(fp, encoding="utf-8", errors="replace").read()
            except OSError:
                continue
            for m in re.finditer(r"arxiv(?:\.org/abs/|:)\s*(\d{4}\.\d{4,5})", t, re.IGNORECASE):
                ids_found.setdefault(m.group(1), set()).add(os.path.relpath(fp, root))
    rep["eprint_ids_in_repo"] = {k: sorted(v) for k, v in sorted(ids_found.items())}
    block = open(blocklist_path, encoding="utf-8").read() if os.path.exists(blocklist_path) else ""
    rep["errors"] += [f"e-print id {i} mentioned in {sorted(v)[0]} is not listed in the blocklist" for i, v in ids_found.items() if i not in block]
    rep["errors"] += [f"e-print id {i} appears in the candidate .bib" for i in ids_found if i in text]
    rep["ok"] = not rep["errors"]
    return rep


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", default=None)
    a = ap.parse_args(argv)
    rep = audit()
    if a.json:
        json.dump(rep, open(a.json, "w"), indent=1)
    print(f"entries: {rep['n_entries']}  errors: {len(rep['errors'])}  flags: {len(rep['flags'])}")
    for e in rep["errors"]:
        print("ERROR", e)
    for f in rep["flags"]:
        print("FLAG ", f)
    return 0 if rep["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
