# Claim → reference matrix

**Reference Audit Wave 1 · 2026-09-26.** One row per claim of `research/CLAIMS.md` (C-01…C-22) that needs an external citation, plus the major introduction/novelty statements. Keys written with a leading at-sign exist in `paper/references_candidate_published_only.bib` (enforced by `computations/reference_audit/reference_audit.py`). Distinction used throughout: an **original theorem** of ours needs no citation as authority; an **imported** theorem/criterion needs its published source; **novelty wording** needs the closest-prior-art citations.

Citation status codes: **READY** (published, metadata complete in repo) · **READY-VERIFY** (published; some field `NEEDS_CHIEF_WEB_VERIFICATION`) · **OPEN** (source not identified / all metadata missing) · **NONE NEEDED**.

| claim | internally proved? | purpose of the external citation | published source(s) | status | unresolved risk |
|---|---|---|---|---|---|
| C-01 Matignon sector criterion | no — IMPORTED | authority for \|arg λ\| > απ/2 | `@Matignon1996`; modern statement `@BrandiburGarrappaKaslik2021` | READY-VERIFY | DOI/issue of both; sign/argument convention must match ours (verify theorem statement in the journal version of Brandibur et al.) |
| C-02 fractionally stable / integer-order unstable | elementary | show the phenomenon is known (motivation only) | `@AhmedElSayedElSaka2007`; `@Matignon1996` | READY | none |
| C-03 S_α(G) definition | definition | none (no novelty claimed) | — | NONE NEEDED | do not present as a contribution |
| C-04 F_α framework | definition | state that F_α is an instance of generalized multiplicative D-stability | `@Kushel2019`; `@KushelPavaniJDDE`; `@KushelPavani2021`; `@Kushel2023` | READY-VERIFY | JDDE year/vol/pages; Kushel 2019 pages; KP2021 title |
| C-05 single-cycle secant (rejected as novelty) | n/a | attribute the cyclic threshold to prior art | `@Siami2021`; classical-order predecessors `@ArcakSontag2006`, `@Arcak2011` | READY-VERIFY | Siami year/vol/pages; Arcak titles/DOIs |
| C-06 strong / interior D-stability as concept | n/a | show the concept is classical | `@Hartfiel1980`; `@Abed1986`; `@LeeEdgar2001`; `@Cain1984` | READY-VERIFY | Hartfiel vol/pages; Lee–Edgar DOI |
| C-07 exact 2×2 classification | **yes (internal)** | none as authority; optional background on 2×2 D-stability | — (`@Cain1976` only if the α=1 2×2 remark is attributed) | NONE NEEDED | none |
| C-08 dimension-3 separation for α ≤ 2/3 | yes, **modulo Kellogg** | IMPORTED: P-matrix eigenvalue wedge \|arg μ\| < π − π/n | `@Kellogg1972` | **OPEN** | **load-bearing metadata entirely unverified**; also the exact statement (strict inequality, real P-matrices) must be checked against the source |
| C-09 minimum dimension = 3 for all α (flagship) | **yes (internal)** | novelty wording: ingredients are prior art, combination is not | `@Matignon1996`; `@Kellogg1972`; `@Cain1976`; `@Hartfiel1980`; `@Abed1986`; `@Siami2021`; `@CermakNechvatal2017`; `@BourafaAbdelouahabMoussaoui2020`; `@KushelPavaniJDDE` | READY-VERIFY (Kellogg OPEN) | approved wording must keep "genuinely fractional", "multiplicative D-stable", "full-dimensional interior" (FINAL_C10_C15 §15) |
| C-10 exact 3×3 threshold κ < T_α(β) (flagship) | **yes (internal)** | (a) IMPORTED α=1 endpoint and optimisation template: Cain; (b) closest abstract N&S predecessor: Kushel–Pavani Thm 3.3; (c) fixed-cubic component is occupied: fractional Routh–Hurwitz / sector polynomials; (d) symmetric slice: Siami; (e) inertia analogue: Bahl–Cain; (f) terminology disambiguation | `@Cain1976`; `@KushelPavaniJDDE`; `@CermakNechvatal2017`; `@BourafaAbdelouahabMoussaoui2020`; `@HoltzKhrushchevKushel2016`; `@JoyaFuruta1991`; `@Siami2021`; `@BahlCain1977`; `@MohsenipourLiu2020`; `@Shao2017` | READY-VERIFY | must NOT say "first N&S criterion" (Kushel–Pavani); Cain DOI; JDDE metadata; Shao body unread (terminology only) |
| C-11 orbit minimum Φ(A) / fractional Cain certificate | yes (internal) | bridge to Cain's classical theorem (Cor. 1) | `@Cain1976` | READY-VERIFY | none beyond Cain DOI |
| C-12 GLV abundance-scaling invariance | yes (internal corollary) | background: diagonal/D-stability in ecological (GLV) models | `@ChenWangLiu2024`; `@HouBaigent2015` | READY | none |
| C-13 ecological loop coordinates | yes (internal corollary) | loop/principal-minor dictionary is classical; three-species community matrices | `@Kinkhabwala2015`; `@ClarkHallam1982` | READY-VERIFY | Kinkhabwala vol/DOI |
| C-14 monotonicity in α and α→1 rate | yes (internal) | monotonicity of the Matignon region in α (imported remark) | `@BrandiburGarrappaKaslik2021`; `@Cain1976` (limit); `@Siami2021` (slice cross-check) | READY-VERIFY | as above |
| C-15 threshold geometry (convexity, unique optimiser, Siami slice, α→2/3) | **yes (internal)** | novelty wording: generic convexity tools are standard; Siami slice; Cain endpoint | `@Siami2021`; `@Cain1976`; (optional convex-analysis textbook: none in repo) | READY-VERIFY | if a textbook is cited for log-sum-exp convexity the Chief must supply verified metadata |
| C-16 general simplex reduction | yes (elementary; NOT NOVEL) | attribute the principal-minor coefficient identity as standard | `@Kinkhabwala2015` (explicit use); optional `@AlAhmadieh2026` | READY-VERIFY | present as a lemma, no priority language |
| C-17 Kolmogorov orbit equivalence | yes (externally audited lemma; NOT NOVEL) | factorisation J = diag(x*)DF(x*) is standard | `@HouBaigent2015`; `@ChenWangLiu2024` | READY | the "tridiagonal Kolmogorov" paper mentioned in the DA novelty audit has no citation in the repo — do not cite |
| C-18 two-consumer no-go theorem | **yes (externally audited)** | context: competitive consumers on a double-Allee prey (no prior no-go found) | `@BaiKangRuanWang2021` (Allee basal prey), `@ChaosSolitonsFractals2015DoubleAllee` | READY-VERIFY | CSF 2015 authors/title |
| C-19 IGP architecture with exact invariant coordinates | **yes (externally audited)** | IGP/omnivory is a standard module; IGP + Allee prior art | `@BaiKangRuanWang2021`; `@LiuLiu2020`; Holt–Polis source (**OPEN**) | READY-VERIFY / OPEN | Chief must pick a published Holt–Polis-line source or drop the attribution |
| C-20 open biological fractional-only set for every α | **yes (externally audited)** | none as authority; uses C-10, C-15, Cain, Kellogg (α ≤ 2/3) | `@Cain1976`; `@Kellogg1972` | READY-VERIFY (Kellogg OPEN) | Kellogg |
| C-21 m-driven transverse Cain crossing | **yes (externally audited)** | classification of both sides uses Cain (α=1) and C-10 | `@Cain1976` | READY-VERIFY | none |
| C-22 2D codimension-one vs 3D open region | **yes (externally audited corollary)** | 2D double-Allee fractional predator–prey models are heavily studied | `@FractalFract2026DoubleAllee`; `@Tassaddiq2026`; `@Ramesh2025`; `@Mondal2025` | READY-VERIFY | FF2026 authors; Tassaddiq co-authors |

## Introduction / novelty statements

| statement | citations | status | risk |
|---|---|---|---|
| "Classical D-stability under positive diagonal scaling (Cain, Hartfiel, Abed) …" | `@Cain1976`; `@BahlCain1977`; `@Hartfiel1980`; `@Cain1984`; `@Abed1986`; `@LeeEdgar2001`; `@Kushel2016` | READY-VERIFY | Cain DOI; Hartfiel vol/pages; Lee–Edgar DOI |
| "Generalized/relative D-stability for arbitrary spectral regions is known (Kushel; Kushel–Pavani) and already contains an abstract N&S forbidden-boundary criterion for the complement of a cone" | `@Kushel2019`; `@KushelPavaniJDDE`; `@KushelPavani2021`; `@Kushel2023` | READY-VERIFY | JDDE metadata + theorem numbering |
| "Fractional Routh–Hurwitz / sector root location for a fixed polynomial is known" | `@CermakNechvatal2017`; `@BourafaAbdelouahabMoussaoui2020`; `@HoltzKhrushchevKushel2016`; `@JoyaFuruta1991` | READY | none |
| "The single-cycle fractional secant condition is due to Siami; classical cyclic/cactus diagonal stability to Arcak–Sontag/Arcak" | `@Siami2021`; `@ArcakSontag2006`; `@Arcak2011` | READY-VERIFY | Siami/Arcak metadata |
| "'D-stability' in fractional control means pole-region stability; we mean positive-diagonal multiplicative D-stability" | `@MohsenipourLiu2020`; `@Shao2017` | READY-VERIFY | Shao body |
| "Fractional ecological models use Matignon stability at one Jacobian; double-Allee and IGP models are established" | `@AhmedElSayedElSaka2007`; `@FractalFract2026DoubleAllee`; `@Tassaddiq2026`; `@BaiKangRuanWang2021`; `@LiuLiu2020`; `@Ramesh2025`; `@Saha2026`; `@WangHan2025`; `@Baghel2026` | READY-VERIFY | FF2026 authors |
| "Diagonal-stability methods extend from GLV to Kolmogorov systems" | `@HouBaigent2015`; `@ChenWangLiu2024` | READY | none |
| "Interval-certified anchors / numerical corroboration" | none required (own computation); `@DiethelmFordFreed2002`, `@Garrappa2018` only if a time-domain PECE run is mentioned | NONE NEEDED / READY-VERIFY | DFF2002 DOI |

## Blocked from the manuscript (see `UNPUBLISHED_REFERENCE_BLOCKLIST.md`)

`Kushel2026` (arXiv-only), `CasasantaSimpsonPorco2026` (arXiv-only), `Cong2016eprint` (arXiv-only, reference paper only). No claim above depends on any of them.
