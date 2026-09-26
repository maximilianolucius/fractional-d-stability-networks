# Published-reference ledger — load-bearing and positioning sources

**Reference Audit Wave 1 · 2026-09-26.** Keys refer to `paper/references_candidate_published_only.bib` (written with a leading at-sign; the audit script checks that every such key exists). "Verified" = bibliographic record verified in the repository's novelty audits (grades A/B in `research/novelty/FINAL_BIBLIOGRAPHY_VERIFICATION.md`) or copied from the authors' published article; "Chief web" = field(s) still needing Chief web verification. Nothing was looked up outside the repository in this wave.

## 1. Classical D-stability / Cain

| source | exact result imported | claim in our paper that needs it | metadata (repo) | DOI | verification |
|---|---|---|---|---|---|
| `@Cain1976` | Complete real 3×3 D-stability criterion: with a,b,c / A,B,C the order-1/2 principal minors and δ the determinant, D-stability ⇔ sign conditions and δ < (√(aA)+√(bB)+√(cC))²; proof minimises the homogeneous Routh–Hurwitz ratio over positive diagonals | C-10 §6 (T₁(β) = (Σ√β_ij)² is Cain's strict-P threshold; α=1 endpoint), C-11 Cor. 1, C-14 (limit toward Cain), DA-02/DA-10 (classification of both sides of the crossing), FIG-03/06/08 captions | J. Res. NBS B 80B (1976) 75–77 | — | grade A (theorem verified); **DOI: Chief web** |
| `@BahlCain1977` | Real 3×3 matrices with fixed inertia of MD for every positive diagonal D, via principal minors | novelty positioning of C-10 (inertia cannot see the Matignon angle) | LAA 18(3) (1977) 267–280 | 10.1016/0024-3795(77)90056-8 | grade B |
| `@Hartfiel1980`, `@Cain1984` | interior of the classical D-stable set | C-06 positioning ("interior/robust" is classical) | LAA 1980 (vol/pages: Chief web); LAA 56 (1984) 237–243 | 10.1016/0024-3795(80)90195-0; 10.1016/0024-3795(84)90129-0 | grade B |

## 2. Matignon fractional stability

| source | exact result imported | claim | metadata | DOI | verification |
|---|---|---|---|---|---|
| `@Matignon1996` | Commensurate linear Caputo system of order α is asymptotically stable iff every eigenvalue satisfies \|arg λ\| > απ/2 | C-01 (imported theorem; definition of Σ_α, F_α); C-02; framework section | Proc. Computational Engineering in Systems Applications, Lille, July 1996, pp. 963–968 | — | metadata from the authors' published article; theorem verified "via modern restatement" (grade A); **DOI: Chief web (may not exist)** |
| `@BrandiburGarrappaKaslik2021` | Corrected modern statement of the Matignon-type criterion and monotonicity in α | C-01 (modern reference), C-14 §1 (region enlarges as α decreases) | Mathematics 9 (2021) 914 | — (MDPI URL only) | grade A/B; **DOI/issue: Chief web** |
| `@AhmedElSayedElSaka2007` | explicit fractional-stable / integer-unstable equilibria in low-dimensional models | C-02 (phenomenon is known) | JMAA 325 (2007) 542–553 | 10.1016/j.jmaa.2006.01.087 | metadata from the authors' published article |

## 3. Generalized / relative / strong D-stability — closest prior art

| source | exact result | claim | metadata | DOI | verification |
|---|---|---|---|---|---|
| `@KushelPavaniJDDE` | Multiplicative generalized D-stability; forbidden-boundary criterion for conic sectors and their complements | C-04; **C-10 novelty positioning** | J. Dyn. Differ. Equ. 34 (2022), 651–669 | 10.1007/s10884-020-09891-y | **CHIEF WEB VERIFIED**. The relevant conic criterion is Theorem 6 in the published-text numbering; do not call it “Theorem 3.3” (3.3 is a section number). |
| `@Kushel2019` | general (region, multiplier class, operation) stability framework | C-04 | SIAM Review 61 (2019) | 10.1137/18M119241X | grade A/B; issue/pages: Chief web |
| `@KushelPavani2021` | diagonal region-dominance / generalized D-stability with fractional applications (sufficient conditions) | C-04, C-10 positioning | LAA 630 (2021) 204–224 | 10.1016/j.laa.2021.08.004 | grade B; **title discrepancy: Chief web** |
| `@Kushel2023` | relative D-stability in a conic sector around the negative real axis; determinant bounds; sector gaps | C-04/C-06 positioning ("uniform sector gap" is occupied language) | LAA 656 (2023) 9–26 | 10.1016/j.laa.2022.09.018 | grade B |
| `@Abed1986`, `@LeeEdgar2001` | strong D-stability = perturbational persistence; structured-singular-value conditions | C-06 ("strong/robust" not new) | SCL 7(3) (1986) 207–212; SCL 44 (2001) 273–277 | 10.1016/0167-6911(86)90116-7; — | grade B; Lee–Edgar DOI: Chief web |
| `@Kushel2016` | D_θ-stability with θ an index order (not an angle) | terminology disambiguation only | Special Matrices 4 (2016) 181–188 | 10.1515/spma-2016-0017 | grade A |
| `@ArcakSontag2006`, `@Arcak2011` | cyclic / cactus diagonal stability (secant-type), α = 1 | C-05 positioning (graph-structural predecessors) | Automatica 42(9) (2006); IEEE TAC 56(12) (2011) 2766–2777 | — | **titles/DOIs: Chief web** (only journal/volume in repo) |

## 4. P-matrix / sector / Kellogg-type low-order argument

| source | exact result | claim | metadata | DOI | verification |
|---|---|---|---|---|---|
| `@Kellogg1972` | If P is a real n×n P-matrix then each eigenvalue μ satisfies \(|\arg \mu|<\pi-\pi/n\) | **C-08**, C-10 low-order theorem, DA-08/DA-11 for α≤2/3 | R. B. Kellogg, *On complex eigenvalues of M and P matrices*, Numerische Mathematik 19(2) (1972), 170–175 | 10.1007/BF01402527 | **CHIEF WEB VERIFIED — LOAD-BEARING CLOSED** |
| `@CermakNechvatal2017`, `@BourafaAbdelouahabMoussaoui2020` | optimal fractional Routh–Hurwitz conditions for a fixed cubic (Bourafa Props. 1–3 incl. the α<2/3 regime and a Cardano-form cubic criterion) | C-10 Lemma 1 positioning (fixed-cubic boundary h_α is occupied territory); C-09 §7 (α = 2/3 cubic transition) | Nonlinear Dyn. 87 (2017) 939–954; CSF 133 (2020) 109623 | 10.1007/s11071-016-3090-9; 10.1016/j.chaos.2020.109623 | grade B |
| `@HoltzKhrushchevKushel2016`, `@JoyaFuruta1991` | forbidden sectors for positive-coefficient polynomials; polynomial D-region stability incl. sectors | C-10 positioning (sector root-location prior art; terminology) | CMFT 16 (2016) 395–431; Trans. SICE 27(3) (1991) 298–305 | 10.1007/s40315-016-0156-0; 10.9746/sicetr1965.27.298 | grade B / A-B |
| `@MohsenipourLiu2020`, `@Shao2017` | fractional robust "D-stability" = pole-region stability | terminology disambiguation paragraph (must say "positive-diagonal multiplicative D-stability") | IEEE/CAA JAS 7(3) (2020) 853–864; 36th CCC (2017) 44–48 | 10.1109/JAS.2020.1003159; 10.23919/ChiCC.2017.8027318 | grade A/B; Shao: grade C (**body not retrieved; cite only for terminology**) |

## 5. Ecological / Kolmogorov D-stability background

| source | exact result | claim | metadata | DOI | verification |
|---|---|---|---|---|---|
| `@HouBaigent2015` | diagonal-stability / Lyapunov methods extended from Lotka–Volterra to autonomous Kolmogorov systems | C-17 (Kolmogorov factorisation J = diag(x*)DF(x*) is standard) | CPAA 14 (2015) 1205–1238 | 10.3934/cpaa.2015.14.1205 | recorded in DOUBLE_ALLEE novelty audit (not graded) |
| `@ChenWangLiu2024` | review: diagonal-stability methods extend beyond GLV to Kolmogorov systems | C-12/C-17 context | Physics Reports 1088 (2024) 1–41 | 10.1016/j.physrep.2024.08.001 | recorded (not graded) |
| `@ClarkHallam1982` | exact three-species community-matrix stability | C-13 positioning | J. Math. Biol. 16 (1982) 25–31 | 10.1007/BF00275158 | grade B |
| `@Kinkhabwala2015` | characteristic coefficients via principal minors; principal minors via non-overlapping feedback cycles | C-13 and C-16 positioning (dictionary is classical) | PLOS ONE 2015 | — | grade A/B; **vol/article/DOI: Chief web** |

## 6. Fractional intraguild predation prior art

| source | exact content | claim | metadata | DOI | verification |
|---|---|---|---|---|---|
| `@BaiKangRuanWang2021` | IGP food-web model with strong Allee effect in the basal prey (integer order) | C-19 context (IGP + Allee is established; our claim is the exact realization) | NARWA 58 (2021) 103206 | 10.1016/j.nonrwa.2020.103206 | recorded (not graded) |
| `@LiuLiu2020` | stochastic three-species IGP model | C-19 context | JAAC 10 (2020) 81–103 | 10.11948/jaac20190002 | recorded |
| Holt–Polis tradition | (no work identified) | C-19 context | — | — | **Chief web: choose a published source** |
| fractional IGP specifically | none located in the repository | — | — | — | gap: if the text claims "no fractional IGP D-stability result exists", that is a novelty-audit statement, not a citation |

## 7. Double-Allee ecological prior art

| source | exact content | claim | metadata | DOI | verification |
|---|---|---|---|---|---|
| `@FractalFract2026DoubleAllee` | Caputo 2D double-Allee predator–prey; discrete approximation; bifurcation/chaos control | C-22 context; "double-Allee models are heavily occupied" | Fractal Fract. 10 (2026) 304 | 10.3390/fractalfract10050304 | **authors: Chief web** |
| `@Tassaddiq2026` | double-Allee predator–prey dynamics and stability | same | AIMS Math. 11 (2026) 1117–1144 | 10.3934/math.2026048 | co-authors: Chief web |
| `@ChaosSolitonsFractals2015DoubleAllee` | earlier double-Allee predator–prey analysis | same | CSF 73 (2015) 36–63 | 10.1016/j.chaos.2014.12.007 | **authors/title: Chief web** |
| `@Ramesh2025`, `@Mondal2025`, `@Saha2026`, `@WangHan2025`, `@Baghel2026` | memory / double-Allee / Allee fractional predator–prey models (from the authors' published article) | C-22 and introduction context | PLoS ONE 20 (2025) e0305179; J. Biol. Phys. 51 (2025) 5; FCAA 29 (2026) 1486–1515; QTDS 24 (2025) 49; CSF 205 (2026) 117880 | 10.1371/journal.pone.0305179; 10.1007/s10867-025-09670-0; 10.1007/s13540-026-00515-8; 10.1007/s12346-024-01212-8; 10.1016/j.chaos.2026.117880 | copied from the authors' published article |

## 8. Numerical fractional methods actually mentioned in the final manuscript

Per `research/MANUSCRIPT_STORYBOARD_2026-09-26.md` §7 and `research/CHIEF_FINAL_VISUAL_GATE_2026-09-26.md`, the final manuscript reports interval-certified margins (interval Newton, outward rounding) and a scale-invariant spectral corroboration; the Wave-1 time-domain predictor–corrector panel (FIG-07d) was dropped. **No fractional time-stepping method is cited by the storyboard.** If a PECE run is nevertheless mentioned: `@DiethelmFordFreed2002` (DOI: Chief web), `@Garrappa2010`, `@Garrappa2018`; monographs `@Podlubny1999`, `@Diethelm2010`. Interval arithmetic was done with mpmath (software, not a scholarly reference; if the journal requires a software citation the Chief must add a verified one).

## 9. Closest literature identified in the C-10 / C-15 novelty audits

`@KushelPavaniJDDE` (Theorem 3.3), `@Cain1976`, `@BahlCain1977`, `@Siami2021` (Theorem 2: for n=3, T_α(1,1,1) = 1 + R₃(α)³ with R₃(α) = sin(απ/2)/sin(απ/2 − π/3); C-15 recovers it as the symmetric slice), `@CermakNechvatal2017`, `@BourafaAbdelouahabMoussaoui2020`, `@HoltzKhrushchevKushel2016`, `@JoyaFuruta1991`, `@Kushel2023`, `@Kinkhabwala2015`, `@AlAhmadieh2026` (optional). For C-15 the audits located no source for the strict logit convexity of T_α; generic log-sum-exp / geometric-programming convexity is standard and needs no citation, or a textbook the Chief selects (none in repository evidence).

## Load-bearing items still unresolved

**None of the six load-bearing metadata gaps from Wave 1 remain open.**

Chief web verification closed:
- Kellogg 1972: title, journal, volume/issue/pages, DOI and wedge statement;
- Kushel–Pavani: final 2022 volume/pages/DOI and correction of theorem numbering;
- Siami 2021: IEEE TCNS 8(3), 1261–1269, DOI verified; cyclic secant theorem is Theorem 2 in the article lineage;
- Matignon 1996: published CESA'96 proceedings metadata verified; no DOI was located and none should be invented;
- Brandibur–Garrappa–Kaslik 2021: Mathematics 9(8), 914, DOI verified;
- Cain 1976: NIST DOI 10.6028/jres.080B.013 and issue verified.

Remaining warnings are non-load-bearing metadata/optional-background cleanup for Reference Audit Wave 2.