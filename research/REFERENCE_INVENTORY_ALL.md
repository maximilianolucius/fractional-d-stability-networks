# Reference inventory — all external scholarly works mentioned in the repository

**Reference Audit Wave 1 · 2026-09-26 · branch `agent/reference-audit-wave1-20260926`**

Scope of the sweep: `research/**/*.md` (theorem files, novelty audits, Chief reports, figure captions/registries, paper architecture, storyboard, research-status), `README.md`, `AGENT_ACCESS.md`, `paper/**` (the existing `paper/references.bib` is empty apart from a comment), and `reference-paper/mathematics-4528508.tex` (the authors' earlier accepted article; its bibliography is repository evidence for metadata and is inventoried separately in §D). Automated part of the sweep: `computations/reference_audit/reference_audit.py` (e-print identifiers).

**Rules applied.** (i) Every metadata value below is copied from repository text; the "where mentioned" column names the source file(s). (ii) A field that no repository file states is written `—` and the work carries `NEEDS_CHIEF_WEB_VERIFICATION`. (iii) Nothing was looked up outside the repository; the two places where an agent recollection is offered (Kellogg 1972, Cong et al. 2016) are labelled as unverified recollection, never as evidence. (iv) Variant citations of one work (e.g. an e-print identifier and the journal record) are merged into one row; the e-print identifiers go to `UNPUBLISHED_REFERENCE_BLOCKLIST.md`.

Roles: **LBT** = LOAD-BEARING THEOREM (imported result the proofs use) · **CPA** = CLOSEST PRIOR ART (novelty positioning) · **ECO** = ECOLOGY CONTEXT · **NUM** = NUMERICAL METHOD · **OPT** = OPTIONAL BACKGROUND · **NN** = NOT NEEDED (inventoried only).
Status: **PUB** = PUBLISHED · **UNPUB** = UNPUBLISHED (e-print / manuscript only) · **UNK** = UNKNOWN-NEEDS-CHIEF-VERIFICATION.

## Summary counts

| quantity | count |
|---|---|
| unique scholarly works identified | 74 (§A rows A1–A39: 39, of which 2 e-print-only and 2 unspecified traditions; §D ★ works not in §A: 11; §D published works not needed: 23; §D e-print-only: 1) |
| published (journal / proceedings / book record in repository evidence) | 69 (35 in §A + 11 ★ + 23 NN) |
| unpublished-only (e-print / manuscript, no published version in repository evidence) | 3 (`Kushel2026`, `CasasantaSimpsonPorco2026`, `Cong2016eprint`) |
| named traditions with no specific work identified | 2 (Holt–Polis IGP; Grilli–Rogers–Allesina) |
| e-print identifiers found by the sweep (all blocklisted) | 8 |
| works in the candidate published-only .bib | 46 |
| works carrying `NEEDS_CHIEF_WEB_VERIFICATION` (some field missing or discrepant) | 23 in the .bib + 2 unspecified traditions = 25 |
| name-only mentions that are not references (no work identifiable) | Cross; Johnson; "fractional consensus"; "modern principal-minor-map literature" |

## A. Works cited in the research material (theorem notes, novelty audits, Chief reports)

| # | key | authors (as in repo) | year | title | venue | vol/issue/pages | DOI | where mentioned | role | status |
|---|---|---|---|---|---|---|---|---|---|---|
| A1 | `Cain1976` | B. E. Cain | 1976 | Real, 3×3, D-stable matrices | Journal of Research of the National Bureau of Standards B | 80B, 75–77 | — | novelty/FINAL_BIBLIOGRAPHY_VERIFICATION, FINAL_C10_C15_SPECIALIST_AUDIT, C10_TARGETED_AUDIT, NOVELTY_MATRIX, THEOREM_C10 §6, THEOREM_C11 Cor. 1, README, DA audits | LBT (α=1 endpoint; classification of both sides in DA-10) | PUB; DOI `NEEDS_CHIEF_WEB_VERIFICATION` |
| A2 | `BahlCain1977` | C. A. Bahl, B. E. Cain | 1977 | The inertia of diagonal multiples of 3×3 real matrices | Linear Algebra and its Applications | 18(3), 267–280 | 10.1016/0024-3795(77)90056-8 | FINAL_BIBLIOGRAPHY_VERIFICATION, FINAL_C10_C15 §4, NOVELTY_MATRIX | CPA | PUB |
| A3 | `Cain1984` | B. E. Cain | 1984 | Inside the D-stable matrices | Linear Algebra and its Applications | 56, 237–243 | 10.1016/0024-3795(84)90129-0 | FINAL_BIBLIOGRAPHY_VERIFICATION, NOVELTY_MATRIX | CPA (interior language) | PUB |
| A4 | `Hartfiel1980` | D. J. Hartfiel | 1980 | Concerning the interior of the D-stable matrices | Linear Algebra and its Applications | — | 10.1016/0024-3795(80)90195-0 | FINAL_BIBLIOGRAPHY_VERIFICATION, REOPENED_AUDIT §4, NOVELTY_REPORT, CLAIMS (C-06) | CPA | PUB; vol/pages `NEEDS_CHIEF_WEB_VERIFICATION` |
| A5 | `Abed1986` | E. H. Abed | 1986 | Strong D-stability | Systems & Control Letters | 7(3), 207–212 | 10.1016/0167-6911(86)90116-7 | CHIEF_RESEARCH_DIRECTION, REOPENED_AUDIT, NOVELTY_REPORT, FINAL_BIBLIOGRAPHY_VERIFICATION, CLAIMS (C-06) | CPA | PUB |
| A6 | `LeeEdgar2001` | J. Lee, T. F. Edgar | 2001 | Real structured singular value conditions for the strong D-stability | Systems & Control Letters | 44, 273–277 | — | REOPENED_AUDIT, NOVELTY_REPORT, FINAL_BIBLIOGRAPHY_VERIFICATION, CLAIMS (C-06) | CPA | PUB; DOI/issue `NEEDS_CHIEF_WEB_VERIFICATION` |
| A7 | `Kellogg1972` | Kellogg | 1972 | — (cited as "Kellogg's P-matrix wedge theorem": eigenvalues of a P-matrix satisfy \|arg μ\| < π − π/n) | — | — | — | REOPENED_AUDIT §6, NOVELTY_REPORT §4, NOVELTY_MATRIX ("Kellogg 1972"), THEOREM_C09, THEOREM_C10 §5, THEOREM_C13, THEOREM_DOUBLE_ALLEE, CLAIMS (C-08), DA audits | **LBT** (C-08; C-10 Thm 2 for α≤2/3; DA-08/DA-11 for α≤2/3) | PUB (classical theorem) but **all metadata `NEEDS_CHIEF_WEB_VERIFICATION`**; unverified agent recollection: R. B. Kellogg, "On complex eigenvalues of M and P matrices", Numer. Math. 19 (1972) 170–175 |
| A8 | `Kushel2016` | O. Y. Kushel | 2016 | On a criterion of D-stability for P-matrices | Special Matrices | 4, 181–188 | 10.1515/spma-2016-0017 | FINAL_BIBLIOGRAPHY_VERIFICATION, FINAL_C10_C15 §5, NOVELTY_MATRIX | OPT (terminology false friend) | PUB |
| A9 | `Kushel2019` | O. Y. Kushel | 2019 | Unifying matrix stability concepts with a view to applications | SIAM Review | 61 | 10.1137/18M119241X | REOPENED_AUDIT, NOVELTY_REPORT, FINAL_BIBLIOGRAPHY_VERIFICATION, CLAIMS (C-04), NOVELTY_MATRIX | CPA (framework) | PUB; issue/pages `NEEDS_CHIEF_WEB_VERIFICATION` (e-print 1907.07089 blocklisted) |
| A10 | `KushelPavaniJDDE` | O. Y. Kushel, R. Pavani | 2020/2022 (repo inconsistent) | The problem of generalized D-stability in unbounded LMI regions and its computational aspects | Journal of Dynamics and Differential Equations | — | 10.1007/s10884-020-09891-y | REOPENED_AUDIT, C10_TARGETED_AUDIT §1, FINAL_C10_C15 §2, FINAL_BIBLIOGRAPHY_VERIFICATION, NOVELTY_MATRIX, CLAIMS | **CPA (closest predecessor of C-10: Theorem 3.3)** | PUB; year/vol/pages `NEEDS_CHIEF_WEB_VERIFICATION` (e-print 2004.11172 blocklisted) |
| A11 | `KushelPavani2021` | O. Y. Kushel, R. Pavani | 2021 | Generalization of the concept of diagonal dominance with applications to matrix D-stability (FINAL_BIBLIOGRAPHY_VERIFICATION) — REOPENED_AUDIT gives a different title for the same e-print | Linear Algebra and its Applications | 630, 204–224 | 10.1016/j.laa.2021.08.004 | REOPENED_AUDIT, FINAL_BIBLIOGRAPHY_VERIFICATION, NOVELTY_MATRIX | CPA | PUB; title discrepancy `NEEDS_CHIEF_WEB_VERIFICATION` (e-print 2103.04127 blocklisted) |
| A12 | `Kushel2023` | O. Y. Kushel | 2023 | Some bounds for determinants of relatively D-stable matrices | Linear Algebra and its Applications | 656, 9–26 | 10.1016/j.laa.2022.09.018 | CHIEF_RESEARCH_DIRECTION, NOVELTY_AGENT_TASK, REOPENED_AUDIT, C09_TARGETED_AUDIT, FINAL_BIBLIOGRAPHY_VERIFICATION | CPA | PUB (e-print 2205.10823 blocklisted) |
| A13 | `Kushel2026` | O. Y. Kushel | 2026 | Recursive determinantal framework for testing D-stability. I | e-print only (arXiv:2604.16526) | — | — | FINAL_BIBLIOGRAPHY_VERIFICATION, FINAL_C10_C15 §13.1 | CPA (methodology) | **UNPUB — blocklisted; not in .bib** |
| A14 | `HoltzKhrushchevKushel2016` | O. Holtz, S. Khrushchev, O. Kushel | 2016 | Generalized Hurwitz matrices, generalized Euclidean algorithm, and forbidden sectors of the complex plane | Computational Methods and Function Theory | 16, 395–431 | 10.1007/s40315-016-0156-0 | FINAL_BIBLIOGRAPHY_VERIFICATION, FINAL_C10_C15 §6.4, NOVELTY_MATRIX | CPA (fixed-polynomial sector) | PUB |
| A15 | `CasasantaSimpsonPorco2026` | J.-P. Casasanta, J. W. Simpson-Porco | 2026 | A Lyapunov characterization of robust D-stability with application to decentralized integral control of LTI systems | e-print only (arXiv:2603.13608) | — | — | REOPENED_AUDIT §4, NOVELTY_REPORT, novelty-audit | OPT | **UNPUB — blocklisted; not in .bib** |
| A16 | `AlAhmadieh2026` | A. Al Ahmadieh | 2026 | — ("principal-minor-map / fiber work") | Journal of Algebra | 685, 46–61 | 10.1016/j.jalgebra.2025.07.030 | FINAL_BIBLIOGRAPHY_VERIFICATION, FINAL_C10_C15 §13.2 | OPT | PUB; title `NEEDS_CHIEF_WEB_VERIFICATION` |
| A17 | `Matignon1996` | D. Matignon | 1996 | Stability results for fractional differential equations with applications to control processing | Proceedings of the Computational Engineering in Systems Applications, Lille, France, 9–12 July 1996 | pp. 963–968 | — | CLAIMS (C-01), SCOPE_MATRIX, NOVELTY_MATRIX, NOVELTY_REPORT, all theorem files (as "Matignon"), paper/sections/02-framework.tex, figure captions; metadata from reference-paper tex | **LBT** (C-01 sector criterion) | PUB (proceedings); DOI `NEEDS_CHIEF_WEB_VERIFICATION` |
| A18 | `BrandiburGarrappaKaslik2021` | M. Brandibur, R. Garrappa, E. Kaslik | 2021 | Stability of systems of fractional-order differential equations with Caputo derivatives | Mathematics | 9, 914 | — (URL https://www.mdpi.com/2227-7390/9/8/914) | CLAIMS (C-01), NOVELTY_MATRIX, NOVELTY_REPORT, FINAL_BIBLIOGRAPHY_VERIFICATION, novelty-audit | **LBT** (modern statement of C-01; α-monotonicity) | PUB; DOI `NEEDS_CHIEF_WEB_VERIFICATION` |
| A19 | `Siami2021` | M. Siami | — (journal year not in repo; "2020/2021") | Stability and Robustness Analysis of Commensurate Fractional-order Networks | IEEE Transactions on Control of Network Systems | — | 10.1109/TCNS.2021.3061931 | CHIEF_RESEARCH_DIRECTION, REOPENED_AUDIT §2, NOVELTY_REPORT, C10_TARGETED_AUDIT §5, FINAL_C10_C15 §8, THEOREM_C10 §7, THEOREM_C13, C14, C15, README, CLAIMS (C-05) | **CPA** (Theorem 2 = symmetric slice of C-10/C-15) | PUB; year/vol/pages `NEEDS_CHIEF_WEB_VERIFICATION` (e-print 2011.04204 blocklisted) |
| A20 | `CermakNechvatal2017` | J. Čermák, L. Nechvátal | 2017 | The Routh–Hurwitz conditions of fractional type in stability analysis of the Lorenz dynamical system | Nonlinear Dynamics | 87, 939–954 | 10.1007/s11071-016-3090-9 | C09_TARGETED_AUDIT, FINAL_BIBLIOGRAPHY_VERIFICATION, NOVELTY_MATRIX, README | CPA (fixed-cubic fractional Routh–Hurwitz; THEOREM_C10 Lemma 1 context) | PUB |
| A21 | `BourafaAbdelouahabMoussaoui2020` | S. Bourafa, M.-S. Abdelouahab, A. Moussaoui | 2020 | On some extended Routh–Hurwitz conditions for fractional-order autonomous systems of order α∈(0,2) | Chaos, Solitons & Fractals | 133, 109623 | 10.1016/j.chaos.2020.109623 | C09_TARGETED_AUDIT, FINAL_BIBLIOGRAPHY_VERIFICATION, NOVELTY_MATRIX | CPA (fixed cubic, Propositions 1–3) | PUB |
| A22 | `JoyaFuruta1991` | K. Joya, K. Furuta | 1991 | A Necessary and Sufficient Condition for the D-Stability of Convex Combinations of D-Stable Polynomials | Transactions of SICE | 27(3), 298–305 | 10.9746/sicetr1965.27.298 | FINAL_BIBLIOGRAPHY_VERIFICATION, FINAL_C10_C15 §6.1, NOVELTY_MATRIX | CPA (polynomial D-region terminology) | PUB |
| A23 | `MohsenipourLiu2020` | R. Mohsenipour, X. Liu | 2020 | Robust D-Stability Test of LTI General Fractional Order Control Systems | IEEE/CAA Journal of Automatica Sinica | 7(3), 853–864 | 10.1109/JAS.2020.1003159 | D_STABILITY_TERMINOLOGY_COLLISION, FINAL_BIBLIOGRAPHY_VERIFICATION, NOVELTY_MATRIX | CPA (terminology disambiguation) | PUB |
| A24 | `Shao2017` | K. Shao, L. Zhou, K. Qian, Y. Yu, F. Chen, S. Zheng | 2017 | Necessary and sufficient D-stability condition of fractional-order linear systems | 36th Chinese Control Conference (CCC) | 44–48 | 10.23919/ChiCC.2017.8027318 | D_STABILITY_TERMINOLOGY_COLLISION, FINAL_BIBLIOGRAPHY_VERIFICATION, FINAL_C10_C15 §7.2 | CPA (terminology; body not retrieved) | PUB (proceedings); definition `NEEDS_CHIEF_WEB_VERIFICATION` (obtain PDF) |
| A25 | `AhmedElSayedElSaka2007` | E. Ahmed, A. M. A. El-Sayed, H. A. A. El-Saka | 2007 | Equilibrium points, stability and numerical solutions of fractional-order predator–prey and rabies models | Journal of Mathematical Analysis and Applications | 325, 542–553 | 10.1016/j.jmaa.2006.01.087 | NOVELTY_REPORT (C-02), NOVELTY_MATRIX, novelty-audit; metadata from reference-paper tex | ECO / CPA for C-02 | PUB |
| A26 | `SabatierMozeFarges2010` | Sabatier, Moze, Farges | 2010 | — | Comput. Math. Appl. | 59, 1594–1609 | — | NOVELTY_REPORT §13 | OPT | PUB; title/DOI `NEEDS_CHIEF_WEB_VERIFICATION` |
| A27 | `ArcakSontag2006` | Arcak, Sontag | 2006 | — (cyclic/secant diagonal stability) | Automatica | 42(9) | — | NOVELTY_REPORT §13, NOVELTY_MATRIX, novelty-audit, FINAL_NOVELTY_AUDIT_TASK | CPA (α=1 graph-structural) | PUB; title/pages/DOI `NEEDS_CHIEF_WEB_VERIFICATION` |
| A28 | `Arcak2011` | Arcak | 2011 | — (cactus diagonal stability) | IEEE TAC | 56(12), 2766–2777 | — | NOVELTY_REPORT §13, NOVELTY_MATRIX, novelty-audit | CPA (α=1) | PUB; title/DOI `NEEDS_CHIEF_WEB_VERIFICATION` |
| A29 | `ClarkHallam1982` | T. J. Clark, T. G. Hallam | 1982 | The community matrix in three species community models | Journal of Mathematical Biology | 16, 25–31 | 10.1007/BF00275158 | FINAL_BIBLIOGRAPHY_VERIFICATION, FINAL_C10_C15 §12, NOVELTY_MATRIX | ECO | PUB |
| A30 | `Kinkhabwala2015` | A. Kinkhabwala | 2015 | Implications of Network Topology on Stability | PLOS ONE | — | — | FINAL_BIBLIOGRAPHY_VERIFICATION, FINAL_C10_C15 §10/§12, NOVELTY_MATRIX | ECO / CPA for C-13/C-16 (principal minors ↔ cycles) | PUB; vol/article/DOI `NEEDS_CHIEF_WEB_VERIFICATION` |
| A31 | `HouBaigent2015` | Z. Hou, S. Baigent | 2015 | Global stability and repulsion in autonomous Kolmogorov systems | Communications on Pure and Applied Analysis | 14, 1205–1238 | 10.3934/cpaa.2015.14.1205 | novelty/DOUBLE_ALLEE_KOLMOGOROV_NOVELTY_AUDIT §2 | ECO (Kolmogorov diagonal-stability background; C-17) | PUB |
| A32 | `ChenWangLiu2024` | C. Chen, X.-W. Wang, Y.-Y. Liu | 2024 | Stability of ecological systems: A theoretical review | Physics Reports | 1088, 1–41 | 10.1016/j.physrep.2024.08.001 | DOUBLE_ALLEE_KOLMOGOROV_NOVELTY_AUDIT §2 | ECO (review; D-/diagonal stability in ecology) | PUB |
| A33 | `FractalFract2026DoubleAllee` | — | 2026 | Bifurcation Structure and Chaos Control in a Discrete-Time Fractional Predator–Prey Model with Double Allee Effect | Fractal and Fractional | 10, 304 | 10.3390/fractalfract10050304 | DOUBLE_ALLEE_KOLMOGOROV_NOVELTY_AUDIT §3 | ECO (double-Allee Caputo prior art) | PUB; authors `NEEDS_CHIEF_WEB_VERIFICATION` |
| A34 | `Tassaddiq2026` | A. Tassaddiq et al. | 2026 | Impact of double Allee effect on the dynamics and stability of a predator-prey model | AIMS Mathematics | 11, 1117–1144 | 10.3934/math.2026048 | DOUBLE_ALLEE_KOLMOGOROV_NOVELTY_AUDIT §3 | ECO | PUB; co-authors `NEEDS_CHIEF_WEB_VERIFICATION` |
| A35 | `ChaosSolitonsFractals2015DoubleAllee` | — | 2015 | — ("earlier double-Allee predator–prey analysis") | Chaos, Solitons & Fractals | 73, 36–63 | 10.1016/j.chaos.2014.12.007 | DOUBLE_ALLEE_KOLMOGOROV_NOVELTY_AUDIT §3 | ECO | PUB; authors/title `NEEDS_CHIEF_WEB_VERIFICATION` |
| A36 | `LiuLiu2020` | R. Liu, G. Liu | 2020 | Dynamics of a stochastic three species prey-predator model with intraguild predation | Journal of Applied Analysis and Computation | 10, 81–103 | 10.11948/jaac20190002 | DOUBLE_ALLEE_KOLMOGOROV_NOVELTY_AUDIT §4 | ECO (IGP module) | PUB |
| A37 | `BaiKangRuanWang2021` | D. Bai, Y. Kang, S. Ruan, L. Wang | 2021 | Dynamics of an intraguild predation food web model with strong Allee effect in the basal prey | Nonlinear Analysis: Real World Applications | 58, 103206 | 10.1016/j.nonrwa.2020.103206 | DOUBLE_ALLEE_KOLMOGOROV_NOVELTY_AUDIT §4 | ECO (IGP + Allee prior art) | PUB |
| A38 | — (Holt–Polis) | "Holt–Polis IGP tradition, summarized in later IGP work" | — | — | — | — | — | DOUBLE_ALLEE_KOLMOGOROV_NOVELTY_AUDIT §4 | ECO | **UNK — no specific work in repository; Chief must choose and verify the published IGP source** |
| A39 | — (Grilli–Rogers–Allesina) | Grilli, Rogers, Allesina | — | — | — | — | — | novelty/novelty-audit.md (row S_α(G)) | OPT | **UNK — no metadata in repository** |
| A40–A50 | see the 11 §D rows marked ★ | numerical-method and fractional-ecology works whose only repository record is the reference-paper bibliography but which the storyboard/figures may need (`DiethelmFordFreed2002`, `Garrappa2010`, `Garrappa2018`, `Podlubny1999`, `Diethelm2010`, `CermakKiselaNechvatal2013`, `Ramesh2025`, `Mondal2025`, `Saha2026`, `WangHan2025`, `Baghel2026`) | | | | | | reference-paper/mathematics-4528508.tex; FIG-07 Wave-1 caption ("predictor–corrector scheme") | NUM / ECO | PUB |

Name-only mentions with no identifiable work (not references): "Cross" and "Johnson" (D_STABILITY_TERMINOLOGY_COLLISION §1, FINAL_NOVELTY_AUDIT_TASK); "fractional consensus" (novelty-audit, NOVELTY_REPORT); "modern principal-minor-map literature" (FINAL_C10_C15 §10); "tridiagonal predator–prey Kolmogorov systems" work (DOUBLE_ALLEE_KOLMOGOROV_NOVELTY_AUDIT §2, no citation given).

## B. E-print-only works (no published version in repository evidence)

| key | work | repo location | published version in repo? | action |
|---|---|---|---|---|
| `Kushel2026` | O. Y. Kushel, Recursive determinantal framework for testing D-stability. I, arXiv:2604.16526 (2026) | novelty/FINAL_BIBLIOGRAPHY_VERIFICATION.md (row), FINAL_C10_C15_SPECIALIST_AUDIT.md §13.1 | no | blocklisted; provenance only |
| `CasasantaSimpsonPorco2026` | Casasanta & Simpson-Porco, arXiv:2603.13608 (2026) | REOPENED_AUDIT §4, NOVELTY_REPORT (twice), novelty-audit.md | no | blocklisted; provenance only |

## C. Named traditions without a specific work

Holt–Polis intraguild predation (A38) and Grilli–Rogers–Allesina (A39): listed in §A; both `NEEDS_CHIEF_WEB_VERIFICATION`.

## D. Bibliography of `reference-paper/mathematics-4528508.tex` (authors' earlier accepted article; metadata source)

All entries are published except `Cong2016eprint` (arXiv:1512.04989, blocklisted). ★ = carried into the candidate .bib because the storyboard/figure pipeline may cite it; otherwise NN.

| key in reference paper | work (as in the tex) | status / role |
|---|---|---|
| Matignon1996 ★ | see A17 | PUB / LBT |
| Ahmed2007 ★ | see A25 | PUB / ECO |
| Saha2026 ★ | Saha, Pal, Kesh, Mukherjee, Fract. Calc. Appl. Anal. 29 (2026) 1486–1515, 10.1007/s13540-026-00515-8 | PUB / ECO |
| Ramesh2025 ★ | Ramesh, Ranjith Kumar, Khan, Abdeljawad, PLoS ONE 20 (2025) e0305179, 10.1371/journal.pone.0305179 (memory + double Allee) | PUB / ECO |
| WangHan2025 ★ | Wang, Han, Qual. Theory Dyn. Syst. 24 (2025) 49, 10.1007/s12346-024-01212-8 | PUB / ECO |
| Baghel2026 ★ | Baghel, Chaos Solitons Fractals 205 (2026) 117880, 10.1016/j.chaos.2026.117880 | PUB / ECO |
| Mondal2025 ★ | Mondal, Mondal, Kesh, Mukherjee, J. Biol. Phys. 51 (2025) 5, 10.1007/s10867-025-09670-0 (double Allee) | PUB / ECO |
| Rahmi2026 | PLoS ONE 21 (2026) e0339351, 10.1371/journal.pone.0339351 | PUB / NN |
| Cermak2013 ★ | Čermák, Kisela, Nechvátal, Appl. Math. Comput. 219 (2013) 7012–7022, 10.1016/j.amc.2012.12.019 (stability regions) | PUB / OPT |
| CressonSzafranska2017 | Commun. Nonlinear Sci. Numer. Simul. 44 (2017) 424–448, 10.1016/j.cnsns.2016.07.016 | PUB / NN |
| Elsadany2015 | J. Appl. Math. Comput. 49 (2015) 269–283, 10.1007/s12190-014-0838-6 | PUB / NN |
| Mondal2020 | J. Appl. Math. Comput. 63 (2020) 311–340, 10.1007/s12190-020-01319-6 | PUB / NN |
| Lubich1986 | SIAM J. Math. Anal. 17 (1986) 704–719, 10.1137/0517050 | PUB / NN |
| Diethelm2002 ★ | Diethelm, Ford, Freed, Nonlinear Dynam. 29 (2002) 3–22 (no DOI in tex) | PUB / NUM (only if a PECE simulation is mentioned) |
| Garrappa2010 ★ | Int. J. Comput. Math. 87 (2010) 2281–2290, 10.1080/00207160802624331 | PUB / NUM |
| Garrappa2018 ★ | Mathematics 6 (2018) 16, 10.3390/math6020016 | PUB / NUM |
| RauhJaulin2021 | Fractal Fract. 5 (2021) 17, 10.3390/fractalfract5010017 | PUB / NN |
| Cong2016 | Cong, Doan, Siegmund, Tuan, arXiv:1512.04989 (2016) | **UNPUB — blocklisted** |
| Cong2016b | Discret. Contin. Dyn. Syst. Ser. B 22 (2017) 3079–3090 (no DOI in tex) | PUB / NN |
| Diethelm2010 ★ | Springer LNM 2004 (2010) | PUB / NUM (monograph) |
| Lubich1983 | Math. Comp. 41 (1983) 87–102, 10.1090/S0025-5718-1983-0701626-6 | PUB / NN |
| DiethelmFordFreed2004 | Numer. Algorithms 36 (2004) 31–52, 10.1023/B:NUMA.0000027736.85078.be | PUB / NN |
| Diethelm2007 | Fract. Calc. Appl. Anal. 10 (2007) 151–160 | PUB / NN |
| Luchko2009 | J. Math. Anal. Appl. 351 (2009) 218–223, 10.1016/j.jmaa.2008.10.018 | PUB / NN |
| LuchkoSuzukiYamamoto2022 | J. Math. Anal. Appl. 505 (2022) 125579, 10.1016/j.jmaa.2021.125579 | PUB / NN |
| AlRefai2012 | Electron. J. Qual. Theory Differ. Equ. 55 (2012) 1–5, 10.14232/ejqtde.2012.1.55 | PUB / NN |
| CongTuan2017 | J. Integral Equ. Appl. 29 (2017) 585–608 | PUB / NN |
| Tavazoei2009 | Automatica 45 (2009) 1886–1890, 10.1016/j.automatica.2009.04.001 | PUB / NN |
| Kaslik2012 | Nonlinear Anal. Real World Appl. 13 (2012) 1489–1497, 10.1016/j.nonrwa.2011.11.013 | PUB / NN |
| BaffetHesthaven2017 | SIAM J. Numer. Anal. 55 (2017) 496–520, 10.1137/15M1043960 | PUB / NN |
| Jiang2017 | Commun. Comput. Phys. 21 (2017) 650–678, 10.4208/cicp.OA-2016-0136 | PUB / NN |
| Podlubny1999 ★ | Academic Press (1999) | PUB / NUM (monograph) |
| HairerWanner1996 | Springer (1996) | PUB / NN |
| FlajoletSedgewick2009 | Cambridge UP (2009) | PUB / NN |
| CarvalhoFehlberg2018 | Acta Appl. Math. 154 (2018) 15–29, 10.1007/s10440-017-0130-5 | PUB / NN |
| Du2013 | Sci. Rep. 3 (2013) 3431, 10.1038/srep03431 | PUB / NN |
| Saeedian2017 | Phys. Rev. E 95 (2017) 022409, 10.1103/PhysRevE.95.022409 | PUB / NN |

(§D: 37 entries = 11 ★ carried into the candidate .bib + 23 NN published + 1 e-print + 2 already counted in §A (Matignon1996, Ahmed2007).)
