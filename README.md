# fractional-d-stability-networks

Research repository for a new mathematical project on **fractional-order stability, positive diagonal scalings, and network structure**, with ecological interaction networks as the primary motivating class.

The repository is intentionally organized as a **research + reproducibility + manuscript workspace**. Its immediate objective is to determine whether the candidate framework supports a genuinely new theorem-level contribution before the new paper is written.

> **Current status:** novelty audit pending. No candidate concept in this repository should be described as new until the closest-literature comparison has been completed.

---

## 1. Core mathematical object

We consider commensurate Caputo systems

\[
{}^C D^\alpha x = F_G(x;\theta), \qquad 0<\alpha\le 1,
\]

where \(G\) is a directed interaction graph and \(\theta\) denotes model parameters. At an equilibrium \(x^*\),

\[
J_G = D F_G(x^*).
\]

For \(0<\alpha<1\), Matignon's sector criterion allows asymptotic stability even when the corresponding first-order system has eigenvalues in the open right half-plane. This motivates the graph-indexed **purely fractional stabilization region**

\[
\mathcal S_\alpha(G)
=
\left\{
\theta:
|\arg\lambda_i(J_G)|>\frac{\alpha\pi}{2}\ \forall i,
\quad
\max_i \operatorname{Re}\lambda_i(J_G)>0
\right\}.
\]

The project asks whether this phenomenon admits a useful structural theory across networks, especially under positive diagonal scalings

\[
J_G \mapsto D J_G, \qquad D=\operatorname{diag}(d_1,\ldots,d_n),\quad d_i>0,
\]

and whether a fractional/sector analogue of classical **D-stability** can be related to graph topology, motifs, sign structure, or other network invariants.

These are **research questions**, not novelty claims.

---

## 2. Main research questions

The current investigation is organized around five candidate directions:

1. **Purely fractional stabilization:** characterize equilibria that are unstable at \(\alpha=1\) but asymptotically stable for some \(\alpha<1\).
2. **Graph-indexed stabilization regions:** understand how \(\mathcal S_\alpha(G)\) depends on interaction topology.
3. **Fractional D-stability:** investigate stability of \(D J_G\) for all positive diagonal \(D\) under the fractional sector criterion, and determine the precise relationship to classical D-stability and diagonal stability.
4. **Topology-to-spectrum mechanisms:** identify graph/motif/sign conditions that force, prohibit, enlarge, or shrink fractional stabilization sectors.
5. **Robustness:** replace isolated examples by open-set or parameter-family theorems whenever possible.

A central requirement of the project is to distinguish carefully between:

- proved theorem;
- exact symbolic consequence;
- certified computation;
- numerical corroboration;
- conjecture/open problem.

Finite diagonal sampling is useful for falsification and exploration, but is **not** a proof of D-stability.

---

## 3. Previous accepted paper: format reference

The directory [`reference-paper/`](reference-paper/) contains the complete source package of our previous paper, already accepted for publication:

> **Exact Stability Atlases and a Memoryless-Surrogate Failure Theorem for a Caputo Allee Predator-Prey Model**

That paper is included here primarily as the **format, editorial, and presentation reference** for the new manuscript.

Important files:

- [`reference-paper/mathematics-4528508.tex`](reference-paper/mathematics-4528508.tex) — accepted manuscript source;
- [`reference-paper/mathematics-4528508.pdf`](reference-paper/mathematics-4528508.pdf) — compiled accepted paper;
- [`reference-paper/Definitions/`](reference-paper/Definitions/) — MDPI *Mathematics* class and bibliography/template files used by the accepted version;
- [`reference-paper/fig*.pdf`](reference-paper/) — publication figures;
- [`reference-paper/ORIGINAL_PACKAGE_SHA256.txt`](reference-paper/ORIGINAL_PACKAGE_SHA256.txt) — provenance checksum of the original uploaded archive. The redundant archival ZIP itself is not mirrored in GitHub.

### What should be reused

The new paper may reuse the accepted paper's:

- MDPI *Mathematics* LaTeX structure;
- theorem/proposition/corollary presentation;
- title, abstract, keywords and MSC placement;
- table and figure conventions;
- multi-panel visual style;
- bibliography and end-matter organization;
- overall density and level of mathematical exposition.

### What should **not** be reused automatically

The previous paper's mathematical novelty, claims, model-specific conclusions, and literature positioning do **not** establish novelty for this project. The new work requires an independent novelty audit and its own theorem-level center of gravity.

The `reference-paper/` directory should therefore be treated as an **immutable reference snapshot**. New manuscript development belongs in `paper/`.

---

## 4. Repository layout

```text
fractional-d-stability-networks/
├── README.md
├── AGENT_ACCESS.md
├── agent_directives_publishable_first_submission.md
├── reference-paper/          # previous accepted paper; format reference
├── paper/                    # new manuscript workspace
├── research/                 # novelty audit, claims, scope, research status
├── src/fdsn/                 # reusable computational core
├── scripts/                  # reproducibility entry points
├── tests/                    # unit tests
├── experiments/              # numerical experiments/configurations
├── data/                     # machine-readable research data
├── docs/                     # project and reproducibility documentation
└── supplement/               # internal-only derivations/checks
```

`reference-paper/` and `paper/` have deliberately different roles: the former is a frozen reference; the latter is the evolving new article.

---

## 5. Novelty audit comes before manuscript drafting

The next major task is an independent **deep novelty audit**.

An agent working on that task should read, in order:

1. [`AGENT_ACCESS.md`](AGENT_ACCESS.md)
2. [`agent_directives_publishable_first_submission.md`](agent_directives_publishable_first_submission.md)
3. [`research/NOVELTY_AGENT_TASK.md`](research/NOVELTY_AGENT_TASK.md)
4. [`research/CLAIMS.md`](research/CLAIMS.md)
5. [`research/NOVELTY_MATRIX.md`](research/NOVELTY_MATRIX.md)
6. [`research/SCOPE_MATRIX.md`](research/SCOPE_MATRIX.md)
7. [`research/research-status.md`](research/research-status.md)
8. [`reference-paper/mathematics-4528508.tex`](reference-paper/mathematics-4528508.tex)
9. [`paper/main.tex`](paper/main.tex)
10. [`src/fdsn/`](src/fdsn/) and [`tests/`](tests/)

The novelty agent should compare the proposed framework against the closest work in:

- classical D-stability;
- multiplicative/diagonal D-stability;
- diagonal stability;
- sector stability and D-sector stability;
- fractional-order linear and nonlinear stability;
- positive diagonal scaling of Jacobians/community matrices;
- ecological network stability;
- sign-stability and qualitative matrix theory;
- graph-spectral and motif-based stability results.

The deliverable should identify the strongest defensible new theorem, or explicitly conclude that the current formulation needs strengthening.

---

## 6. Publication constraints

The working publication directives are in [`agent_directives_publishable_first_submission.md`](agent_directives_publishable_first_submission.md).

Among the main constraints:

- the final journal-formatted article should remain within **25 pages**;
- the mathematical contribution should be identified before prose polishing;
- benchmark calculations are examples, not substitutes for a family theorem;
- equality/boundary cases must be explicit;
- exact claims should use exact arithmetic where possible;
- numerical experiments corroborate theorems rather than replace them;
- the final article should be logically self-contained and should not rely on supplementary material for any load-bearing conclusion;
- figures should be publication-grade and mathematically informative.

The repository may contain extensive internal research material even though the final article remains self-contained.

---

## 7. Reproducibility

Create a fresh environment and run:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e '.[dev]'
pytest -q
python scripts/demo_fractional_stability.py
```

Minimal test invocation without installation:

```bash
PYTHONPATH=src pytest -q
```

Every numerical result intended for the manuscript should be reproducible from committed code/configuration and should record, where applicable:

- graph/model definition;
- parameter values;
- fractional order;
- diagonal scaling specification;
- random seed;
- solver and tolerances;
- software version;
- commit SHA.

---

## 8. Access for another research agent

Canonical repository identifier:

```text
maximilianolucius/fractional-d-stability-networks
```

Public URL:

```text
https://github.com/maximilianolucius/fractional-d-stability-networks
```

Shell access:

```bash
git clone https://github.com/maximilianolucius/fractional-d-stability-networks.git
cd fractional-d-stability-networks
git checkout main
git rev-parse HEAD
```

A GitHub-enabled agent should be given the exact repository identifier above and instructed to inspect the `main` branch, beginning with `AGENT_ACCESS.md`.

---

## 9. Repository policy

This repository is intended to be **public** so that research agents and collaborators can inspect the mathematical development, code, reproducibility artifacts, and manuscript sources.

No open-source license is asserted merely by making the repository public. A license should be added only after the intended reuse policy for code and manuscript sources has been decided.

---

## 10. Current milestone

**Milestone 1: novelty validation.**

Before substantial drafting of the new paper, determine:

- what is already known;
- what is only a reformulation of known D-/sector-stability theory;
- whether the graph-indexed/fractional formulation yields genuinely new mathematics;
- what exact theorem would make the contribution strong enough for a high-quality journal submission.

Only after that audit should the new manuscript be rebuilt in `paper/`, using `reference-paper/` as the accepted formatting template.