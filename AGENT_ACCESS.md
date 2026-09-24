# Agent access and handoff

## Canonical repository

**Repository:** `maximilianolucius/fractional-d-stability-networks`

**Public URL:** `https://github.com/maximilianolucius/fractional-d-stability-networks`

The public repository is live. An agent can access it in any of these ways:

```bash
git clone https://github.com/maximilianolucius/fractional-d-stability-networks.git
cd fractional-d-stability-networks
git checkout main
git rev-parse HEAD
```

If the agent has a GitHub connector/tool rather than shell access, give it the exact repository identifier:

```text
maximilianolucius/fractional-d-stability-networks
```

and instruct it to inspect the `main` branch.

## Read this first

Read, in order:

1. `agent_directives_publishable_first_submission.md` — controlling publication/research constraints.
2. `README.md` — project scope and core mathematical object.
3. `research/NOVELTY_AGENT_TASK.md` — exact novelty-audit assignment and deliverables.
4. `research/CLAIMS.md` — claim registry; do not upgrade a claim without evidence.
5. `research/NOVELTY_MATRIX.md` — closest-work comparison matrix to populate.
6. `research/SCOPE_MATRIX.md` — scope discipline for claims.
7. `research/research-status.md` — current mathematical framing.
8. `reference-paper/mathematics-4528508.tex` — previous accepted paper; reuse its MDPI Mathematics format and presentation conventions, not its novelty claims.
9. `paper/main.tex` — current manuscript scaffold, not a finalized paper.
10. `src/fdsn/` and `tests/` — computational definitions and tests.

## Novelty-agent mission

The next agent should **audit novelty before drafting the paper**. It must identify the closest literature and determine whether the project supports a genuinely new theorem rather than a new application of a standard fractional stability criterion.

Candidate central objects to audit include:

- fractional stabilization of an integer-order unstable equilibrium;
- the graph-indexed stabilization region `S_alpha(G)`;
- positive diagonal scaling `D J_G` and a fractional analogue/extension of classical D-stability;
- topology/motif dependence of fractional sector stability;
- open-set/robustness results showing the phenomenon is not fine-tuned.

No item above is asserted to be novel merely by appearing in this repository.

## Required novelty output

The novelty agent should commit or return:

- `research/NOVELTY_REPORT.md` — dated deep-literature audit with a conservative verdict for each candidate contribution;
- populated `research/NOVELTY_MATRIX.md` — closest papers × comparison axes;
- updated `research/CLAIMS.md` — label each central statement as `NEW THEOREM CANDIDATE`, `KNOWN/STANDARD`, `DERIVABLE BUT NOT NOVEL`, or `OPEN` until proved;
- a shortlist of the 5–15 closest works, with exact theorem/result correspondence rather than keyword similarity;
- a <=3-sentence statement of the strongest defensible novelty, or an explicit conclusion that novelty is insufficient;
- precise next mathematical theorem(s) needed to reach publishable novelty if the current claim is too weak.

## Reproducibility sanity check

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e '.[dev]'
pytest -q
python scripts/demo_fractional_stability.py

# Minimal alternative without installation:
PYTHONPATH=src pytest -q
```

Finite diagonal sampling in `src/fdsn/d_stability.py` is exploratory/falsification evidence only; it must never be cited as a proof of D-stability.
