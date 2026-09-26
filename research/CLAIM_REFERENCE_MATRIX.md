# Claim → reference matrix (final, Wave 2)

**Reference Audit Wave 2 · 2026-09-26.** One row per claim of `research/CLAIMS.md` (C-01…C-22) that needs an external citation, plus the major introduction/novelty statements. Keys written with a leading at-sign exist in `paper/references_candidate_published_only.bib` = `paper/references.bib` (enforced by `computations/reference_audit/reference_audit.py`, which also fails on any unresolved status token in this file). Distinction used throughout: an **original theorem** of ours needs no citation as authority; an **imported** theorem/criterion needs its published source; **novelty wording** needs the closest-prior-art citations.

Citation status codes: **READY** (published; metadata complete and verified per `CHIEF_REFERENCE_WEB_VERIFICATION_2026-09-26.md` / novelty grades) · **NONE NEEDED**. No other status remains.

| claim | internally proved? | purpose of the external citation | published source(s) | status | residual note |
|---|---|---|---|---|---|
| C-01 Matignon sector criterion | no — IMPORTED | authority for \|arg λ\| > απ/2 | `@Matignon1996`; modern published statement `@BrandiburGarrappaKaslik2021` | READY | when drafting, match the argument convention (Σ_α = {\|arg z\| > απ/2}) to Brandibur et al.'s statement |
| C-02 fractionally stable / integer-order unstable | elementary | show the phenomenon is known (motivation only) | `@AhmedElSayedElSaka2007`; `@Matignon1996` | READY | none |
| C-03 S_α(G) definition | definition | none (no novelty claimed) | — | NONE NEEDED | do not present as a contribution |
| C-04 F_α framework | definition | state that F_α is an instance of generalized multiplicative D-stability | `@Kushel2019`; `@KushelPavaniJDDE`; `@KushelPavani2021`; `@Kushel2023` | READY | none |
| C-05 single-cycle secant (rejected as novelty) | n/a | attribute the cyclic fractional threshold to prior art; classical-order cyclic/cactus predecessors | `@Siami2021`; `@ArcakSontag2006`; `@Arcak2011` | READY | cite Siami's result as "the cyclic secant condition (Theorem 2 of the article)" only if the numbering is re-checked at proof stage; otherwise describe it |
| C-06 strong / interior D-stability as concept | n/a | show the concept is classical | `@Hartfiel1980`; `@Cain1984`; `@Abed1986`; `@LeeEdgar2001` | READY | none |
| C-07 exact 2×2 classification | **yes (internal)** | none as authority | — (`@Cain1976` only if the α=1 remark is attributed) | NONE NEEDED | none |
| C-08 dimension-3 separation for α ≤ 2/3 | yes, modulo the imported Kellogg theorem | IMPORTED: P-matrix eigenvalue wedge \|arg μ\| < π − π/n | `@Kellogg1972` | READY | none |
| C-09 minimum dimension = 3 for all α (flagship) | **yes (internal)** | novelty wording: ingredients are prior art, the combination is not | `@Matignon1996`; `@Kellogg1972`; `@Cain1976`; `@Hartfiel1980`; `@Abed1986`; `@Siami2021`; `@CermakNechvatal2017`; `@BourafaAbdelouahabMoussaoui2020`; `@KushelPavaniJDDE` | READY | approved wording keeps "genuinely fractional", "multiplicative D-stable", "full-dimensional interior" |
| C-10 exact 3×3 threshold κ < T_α(β) (flagship) | **yes (internal)** | (a) IMPORTED α=1 endpoint and optimisation template: Cain; (b) closest abstract N&S predecessor: Kushel–Pavani's conic-sector forbidden-boundary criterion (published 2022 article; no theorem number hardcoded); (c) fixed-cubic component is occupied: fractional Routh–Hurwitz / sector polynomials; (d) symmetric slice: Siami; (e) inertia analogue: Bahl–Cain; (f) terminology disambiguation | `@Cain1976`; `@KushelPavaniJDDE`; `@CermakNechvatal2017`; `@BourafaAbdelouahabMoussaoui2020`; `@HoltzKhrushchevKushel2016`; `@JoyaFuruta1991`; `@Siami2021`; `@BahlCain1977`; `@MohsenipourLiu2020` | READY | must NOT say "first N&S criterion" |
| C-11 orbit minimum Φ(A) / fractional Cain certificate | yes (internal) | bridge to Cain's classical theorem (Cor. 1) | `@Cain1976` | READY | none |
| C-12 GLV abundance-scaling invariance | yes (internal corollary) | background: diagonal/D-stability in ecological (GLV/Kolmogorov) models | `@ChenWangLiu2024`; `@HouBaigent2015` | READY | none |
| C-13 ecological loop coordinates | yes (internal corollary) | loop/principal-minor dictionary is classical; three-species community matrices | `@Kinkhabwala2015`; `@ClarkHallam1982` | READY | none |
| C-14 monotonicity in α and α→1 rate | yes (internal) | monotonicity of the Matignon region in α (imported remark); Cain limit; Siami slice cross-check | `@BrandiburGarrappaKaslik2021`; `@Cain1976`; `@Siami2021` | READY | none |
| C-15 threshold geometry (convexity, unique optimiser, Siami slice, α→2/3) | **yes (internal)** | novelty wording: generic convexity tools are standard (not cited); Siami slice; Cain endpoint | `@Siami2021`; `@Cain1976` | READY | none |
| C-16 general simplex reduction | yes (elementary; NOT NOVEL) | attribute the principal-minor coefficient identity as standard | `@Kinkhabwala2015`; optional `@AlAhmadieh2026` | READY | present as a lemma, no priority language |
| C-17 Kolmogorov orbit equivalence | yes (externally audited lemma; NOT NOVEL) | factorisation J = diag(x*)DF(x*) is standard | `@HouBaigent2015`; `@ChenWangLiu2024` | READY | none |
| C-18 two-consumer no-go theorem | **yes (externally audited)** | context: consumers on a double-Allee prey; no prior no-go located | `@BaiKangRuanWang2021`; `@ChaosSolitonsFractals2015DoubleAllee` | READY | none |
| C-19 IGP architecture with exact invariant coordinates | **yes (externally audited)** | IGP is a standard module (Holt–Polis); IGP + Allee prior art; **fractional IGP already exists (Panja) — novelty is the exact positive-diagonal realization, not "Caputo + IGP"** | `@HoltPolis1997`; `@Panja2019`; `@BaiKangRuanWang2021`; `@LiuLiu2020` | READY | none |
| C-20 open biological fractional-only set for every α | **yes (externally audited)** | none as authority; low-order case uses Kellogg, both sides use Cain; positioning against fractional IGP | `@Cain1976`; `@Kellogg1972`; `@Panja2019` | READY | none |
| C-21 m-driven transverse Cain crossing | **yes (externally audited)** | classification of both sides uses Cain (α=1) and C-10 | `@Cain1976` | READY | none |
| C-22 2D codimension-one vs 3D open region | **yes (externally audited corollary)** | 2D double-Allee (fractional) predator–prey models are heavily studied | `@ChaosSolitonsFractals2015DoubleAllee`; `@FractalFract2026DoubleAllee`; `@Tassaddiq2026`; `@Ramesh2025`; `@Mondal2025` | READY | none |

## Introduction / novelty statements

| statement | citations | status | residual note |
|---|---|---|---|
| "Classical D-stability under positive diagonal scaling (Cain, Hartfiel, Abed) …" | `@Cain1976`; `@BahlCain1977`; `@Hartfiel1980`; `@Cain1984`; `@Abed1986`; `@LeeEdgar2001`; `@Kushel2016` | READY | none |
| "Generalized/relative D-stability for arbitrary spectral regions is known (Kushel; Kushel–Pavani) and already contains a necessary-and-sufficient conic-sector forbidden-boundary criterion" | `@Kushel2019`; `@KushelPavaniJDDE`; `@KushelPavani2021`; `@Kushel2023` | READY | describe the criterion; do not cite "Theorem 3.3" |
| "Fractional Routh–Hurwitz / sector root location for a fixed polynomial is known" | `@CermakNechvatal2017`; `@BourafaAbdelouahabMoussaoui2020`; `@HoltzKhrushchevKushel2016`; `@JoyaFuruta1991`; `@SabatierMozeFarges2010`; `@CermakKiselaNechvatal2013` | READY | the last two are optional background |
| "The single-cycle fractional secant condition is due to Siami; classical cyclic/cactus diagonal stability to Arcak–Sontag/Arcak" | `@Siami2021`; `@ArcakSontag2006`; `@Arcak2011` | READY | none |
| "'D-stability' in fractional control means pole-region stability; we mean positive-diagonal multiplicative D-stability" | `@MohsenipourLiu2020` | READY | Shao 2017 dropped (body never retrieved) |
| "Fractional ecological models use Matignon stability at one Jacobian; double-Allee and IGP models, including fractional IGP, are established" | `@AhmedElSayedElSaka2007`; `@Panja2019`; `@HoltPolis1997`; `@BaiKangRuanWang2021`; `@LiuLiu2020`; `@ChaosSolitonsFractals2015DoubleAllee`; `@FractalFract2026DoubleAllee`; `@Tassaddiq2026`; `@Ramesh2025`; `@Mondal2025`; `@Saha2026`; `@WangHan2025`; `@Baghel2026` | READY | none |
| "Diagonal-stability methods extend from GLV to Kolmogorov systems" | `@HouBaigent2015`; `@ChenWangLiu2024` | READY | none |
| "Interval-certified anchors / numerical corroboration" | none required (own computation); general fractional-calculus background `@Podlubny1999`, `@Diethelm2010`, `@Garrappa2018`, `@Garrappa2010` only if numerical solution of Caputo systems is discussed | NONE NEEDED | no predictor–corrector run is reported (DiethelmFordFreed2002 dropped) |

## Blocked from the manuscript (see `UNPUBLISHED_REFERENCE_BLOCKLIST.md`)

`Kushel2026` (arXiv-only), `CasasantaSimpsonPorco2026` (arXiv-only), `Cong2016eprint` (arXiv-only, reference paper only). No claim above depends on any of them.
