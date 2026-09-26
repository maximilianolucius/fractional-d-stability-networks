# Published-reference ledger — load-bearing and positioning sources (final, Wave 2)

**Reference Audit Wave 2 · 2026-09-26.** Reconciled against `research/CHIEF_REFERENCE_WEB_VERIFICATION_2026-09-26.md`. Keys (written with a leading at-sign) refer to `paper/references_candidate_published_only.bib`, which is promoted verbatim to `paper/references.bib`; the audit script `computations/reference_audit/reference_audit.py` checks that every key here exists, and it reports 0 errors / 0 warnings on this ledger. Verification column: **CWV** = Chief web verification (record above) · **A/B** = grade in `research/novelty/FINAL_BIBLIOGRAPHY_VERIFICATION.md` (primary theorem / publisher record inspected) · **RP** = copied from the authors' published article (`reference-paper/mathematics-4528508.tex`). No entry in this ledger is unresolved.

Entries dropped from the final bibliography by the Chief (Wave 2) and therefore absent from this ledger: `Shao2017` (proceedings body never retrieved; the terminology point is carried by `@MohsenipourLiu2020`) and `DiethelmFordFreed2002` (no time-domain predictor–corrector run is reported in the manuscript plan). Both remain inventoried in `REFERENCE_INVENTORY_ALL.md`.

## 1. Classical D-stability / Cain

| source | exact result imported | claim in our paper that needs it | metadata | DOI | verification |
|---|---|---|---|---|---|
| `@Cain1976` | Complete real 3×3 D-stability criterion: with a,b,c / A,B,C the order-1/2 principal minors and δ the determinant, D-stability ⇔ sign conditions and δ < (√(aA)+√(bB)+√(cC))²; the proof minimises the homogeneous Routh–Hurwitz ratio over positive diagonals | C-10 §6 (T₁(β) = (Σ√β_ij)² is Cain's strict-P threshold; α=1 endpoint and optimisation template), C-11 Cor. 1, C-14 (limit toward Cain), C-20, DA-02/DA-10/C-21 (classification of both sides of the crossing at m₀), FIG-03/06/08 captions | J. Res. Natl. Bur. Stand. B 80B(1) (1976) 75–77 | 10.6028/jres.080B.013 | A + CWV |
| `@BahlCain1977` | Real 3×3 matrices with fixed inertia of MD for every positive diagonal D, via principal minors | novelty positioning of C-10 (inertia cannot see the Matignon angle) | LAA 18(3) (1977) 267–280 | 10.1016/0024-3795(77)90056-8 | B |
| `@Hartfiel1980` | interior of the classical D-stable set | C-06 positioning ("interior/robust" is classical) | LAA 30 (1980) 201–207 | 10.1016/0024-3795(80)90195-0 | B + CWV |
| `@Cain1984` | inside the D-stable matrices (interior) | C-06 positioning | LAA 56 (1984) 237–243 | 10.1016/0024-3795(84)90129-0 | B |
| `@Abed1986` | strong D-stability = perturbational persistence of D-stability | C-06 ("strong/robust" is not new) | SCL 7(3) (1986) 207–212 | 10.1016/0167-6911(86)90116-7 | B |
| `@LeeEdgar2001` | structured-singular-value conditions for strong D-stability | C-06 | SCL 44(4) (2001) 273–277 | 10.1016/S0167-6911(01)00147-5 | B + CWV |
| `@Kushel2016` | D_θ-stability with θ an index order (not an angle); D-stability criteria for P-matrices | terminology disambiguation only | Special Matrices 4 (2016) 181–188 | 10.1515/spma-2016-0017 | A |

## 2. Matignon fractional stability

| source | exact result imported | claim | metadata | DOI | verification |
|---|---|---|---|---|---|
| `@Matignon1996` | Commensurate linear Caputo system of order α is asymptotically stable iff every eigenvalue satisfies \|arg λ\| > απ/2 | **C-01** (imported theorem; definition of Σ_α, F_α); C-02; framework section | CESA'96 IMACS Multiconference, Symposium on Control, Optimization and Supervision, Lille, vol. 2 (1996) 963–968, ISBN 2-9502908-9-2 | none exists (CWV: no DOI located; proceedings paper identified by ISBN) | RP + CWV |
| `@BrandiburGarrappaKaslik2021` | Modern published statement of the Matignon-type Caputo criterion, limiting conventions and monotonicity in α | C-01 (modern foundation), C-14 §1 (Matignon region enlarges as α decreases) | Mathematics 9(8) (2021) 914 | 10.3390/math9080914 | A/B + CWV |
| `@AhmedElSayedElSaka2007` | explicit fractional-stable / integer-unstable equilibria in low-dimensional predator–prey models | C-02 (phenomenon is known; motivation only) | JMAA 325 (2007) 542–553 | 10.1016/j.jmaa.2006.01.087 | RP |
| `@CermakKiselaNechvatal2013` | stability regions of linear fractional systems and their discretisations | optional background for C-01 | Appl. Math. Comput. 219 (2013) 7012–7022 | 10.1016/j.amc.2012.12.019 | RP |
| `@SabatierMozeFarges2010` | LMI stability conditions for fractional-order systems (fixed system, convex region machinery) | optional background: fixed-Jacobian fractional stability tests | Comput. Math. Appl. 59(5) (2010) 1594–1609 | 10.1016/j.camwa.2009.08.003 | CWV (metadata completed by the Chief in the candidate) |

## 3. Generalized / relative / strong D-stability — closest prior art

| source | exact result | claim | metadata | DOI | verification |
|---|---|---|---|---|---|
| `@KushelPavaniJDDE` | Multiplicative generalized D-stability (quantifier over every positive diagonal D); forbidden-boundary equivalence; **necessary-and-sufficient conic-sector / complement-of-cone criterion** (determinant non-vanishing for every positive diagonal D). Cite it as "the conic-sector forbidden-boundary criterion"; do not hardcode a theorem number (earlier notes said "Theorem 3.3", which is a section number; the Chief record places the criterion at Theorem 6 of the published text) | C-04 (framework known); **C-10 novelty wording** ("explicit real-3×3 elimination of the universal-D condition; not the first N&S criterion"); C-09 positioning | J. Dyn. Differ. Equ. 34 (2022) 651–669 | 10.1007/s10884-020-09891-y | A + CWV |
| `@Kushel2019` | general (region, multiplier class, operation) stability framework | C-04 | SIAM Review 61(4) (2019) 643–729 | 10.1137/18M119241X | A/B + CWV |
| `@KushelPavani2021` | diagonal region-dominance / generalized D-stability with fractional applications (sufficient conditions) | C-04, C-10 positioning | LAA 630 (2021) 204–224 | 10.1016/j.laa.2021.08.004 | B (journal title confirmed by the Chief in the candidate) |
| `@Kushel2023` | relative D-stability in a conic sector around the negative real axis; determinant bounds; sector gaps | C-04/C-06 positioning ("uniform sector gap" is occupied language) | LAA 656 (2023) 9–26 | 10.1016/j.laa.2022.09.018 | B |
| `@ArcakSontag2006` | diagonal stability of cyclic systems and the secant criterion (α = 1) | C-05 positioning (graph-structural predecessor of the cyclic threshold) | Automatica 42(9) (2006) 1531–1537 | 10.1016/j.automatica.2006.04.009 | CWV |
| `@Arcak2011` | diagonal stability on cactus graphs (α = 1) | C-05 positioning | IEEE TAC 56(12) (2011) 2766–2777 | 10.1109/TAC.2011.2125130 | CWV |
| `@Siami2021` | Theorem 2 (article lineage): single-circuit commensurate fractional network; automatic stability for α ≤ 2/n; for α > 2/n the generalized secant threshold γ < sin(απ/2)/sin(απ/2 − π/n), necessary when the diagonal coefficients coincide | C-05 (single-cycle novelty rejected); C-10 §7 / C-15 (T_α(1,1,1) = 1 + R₃(α)³ is exactly the symmetric slice); C-14 cross-check | IEEE TCNS 8(3) (2021) 1261–1269 | 10.1109/TCNS.2021.3061931 | A + CWV |

## 4. P-matrix / sector / Kellogg-type low-order argument

| source | exact result | claim | metadata | DOI | verification |
|---|---|---|---|---|---|
| `@Kellogg1972` | If P is a real n×n P-matrix then every eigenvalue μ satisfies \|arg μ\| < π − π/n | **C-08** (−A P-matrix ⇒ A ∈ F_α for α ≤ 2/n), **C-10 Theorem 2** (low-order case α ≤ 2/3), C-13 low-order remark, **C-20 and DA-08 / DA-11 for α ≤ 2/3** | Numer. Math. 19(2) (1972) 170–175 | 10.1007/BF01402527 | **CWV — load-bearing gap closed** |
| `@CermakNechvatal2017` | optimal fractional Routh–Hurwitz conditions (fixed characteristic polynomial, Lorenz setting) | C-10 Lemma 1 positioning (fixed-cubic boundary h_α is occupied territory) | Nonlinear Dyn. 87 (2017) 939–954 | 10.1007/s11071-016-3090-9 | B |
| `@BourafaAbdelouahabMoussaoui2020` | extended fractional Routh–Hurwitz conditions for α ∈ (0,2); Props. 1–3 incl. the α < 2/3 regime and a Cardano-form cubic criterion | C-10 Lemma 1 positioning; C-09 §7 (α = 2/3 cubic transition) | CSF 133 (2020) 109623 | 10.1016/j.chaos.2020.109623 | B |
| `@HoltzKhrushchevKushel2016` | forbidden sectors for positive-coefficient polynomials via generalized Hurwitz matrices | C-10 positioning (sector root-location prior art) | CMFT 16(3) (2016) 395–431 | 10.1007/s40315-016-0156-0 | B |
| `@JoyaFuruta1991` | polynomial "D-stability" = roots in a prescribed domain (incl. sectors); coefficient-space description | C-10 positioning; terminology | Trans. SICE 27(3) (1991) 298–305 | 10.9746/sicetr1965.27.298 | A/B |
| `@MohsenipourLiu2020` | fractional robust "D-stability" = pole-region stability of uncertain characteristic equations | terminology disambiguation paragraph (the paper must say "positive-diagonal multiplicative D-stability") | IEEE/CAA JAS 7(3) (2020) 853–864 | 10.1109/JAS.2020.1003159 | A/B |
| `@AlAhmadieh2026` | fibers of the principal-minor map; diagonal (similarity-type) equivalence | optional background for C-16 (principal-minor coordinates are standard) | J. Algebra 685 (2026) 46–61 | 10.1016/j.jalgebra.2025.07.030 | B (title completed by the Chief) |

## 5. Ecological / Kolmogorov D-stability background

| source | exact result | claim | metadata | DOI | verification |
|---|---|---|---|---|---|
| `@HouBaigent2015` | diagonal-stability / Lyapunov methods extended from Lotka–Volterra to autonomous Kolmogorov systems | C-17 (Kolmogorov factorisation J = diag(x*)DF(x*) is standard); C-12 | CPAA 14 (2015) 1205–1238 | 10.3934/cpaa.2015.14.1205 | recorded in the Double-Allee novelty audit |
| `@ChenWangLiu2024` | review: diagonal-stability methods extend beyond GLV to Kolmogorov systems | C-12 / C-17 context | Phys. Rep. 1088 (2024) 1–41 | 10.1016/j.physrep.2024.08.001 | recorded |
| `@ClarkHallam1982` | exact three-species community-matrix stability | C-13 positioning | J. Math. Biol. 16 (1982) 25–31 | 10.1007/BF00275158 | B |
| `@Kinkhabwala2015` | characteristic coefficients via principal minors; principal minors via non-overlapping feedback cycles | C-13 and C-16 positioning (the dictionary is classical) | PLOS ONE 10(3) (2015) e0122150 | 10.1371/journal.pone.0122150 | A/B + CWV |

## 6. Intraguild predation prior art (classical and fractional)

| source | exact content | claim | metadata | DOI | verification |
|---|---|---|---|---|---|
| `@HoltPolis1997` | theoretical framework for intraguild predation (foundational IGP module) | C-19 ("IGP is a standard ecological module") | Am. Nat. 149(4) (1997) 745–764 | 10.1086/286018 | CWV |
| `@Panja2019` | fractional-order predator–prey model with intraguild predation | **mandatory novelty positioning for C-19/C-20: fractional IGP already exists; our contribution is not "Caputo + IGP" but the exact positive-diagonal Matignon realization** | Int. J. Model. Simul. 39(4) (2019) 256–268 | 10.1080/02286203.2019.1611311 | CWV |
| `@BaiKangRuanWang2021` | IGP food-web model with strong Allee effect in the basal prey (integer order) | C-18/C-19 context (IGP + Allee is established) | NARWA 58 (2021) 103206 | 10.1016/j.nonrwa.2020.103206 | recorded |
| `@LiuLiu2020` | stochastic three-species IGP model | C-19 context | JAAC 10 (2020) 81–103 | 10.11948/jaac20190002 | recorded |

## 7. Double-Allee ecological prior art

| source | exact content | claim | metadata | DOI | verification |
|---|---|---|---|---|---|
| `@ChaosSolitonsFractals2015DoubleAllee` | Pal & Saha: qualitative analysis of a predator–prey system with double Allee effect in prey | C-18/C-22 context ("double-Allee models are heavily occupied") | CSF 73 (2015) 36–63 | 10.1016/j.chaos.2014.12.007 | CWV |
| `@FractalFract2026DoubleAllee` | Alraddadi, Ahmed & Seol: Caputo 2D double-Allee predator–prey, discrete approximation, bifurcation/chaos control | C-22 context | Fractal Fract. 10(5) (2026) 304 | 10.3390/fractalfract10050304 | CWV |
| `@Tassaddiq2026` | Tassaddiq, Ahmed, Khan & Lee: double-Allee predator–prey dynamics and stability | C-22 context | AIMS Math. 11(1) (2026) 1117–1144 | 10.3934/math.2026048 | CWV |
| `@Ramesh2025` | memory effect + double Allee effect + Holling I | C-22 / introduction context | PLOS ONE 20 (2025) e0305179 | 10.1371/journal.pone.0305179 | RP |
| `@Mondal2025` | double Allee effect in prey | C-22 context | J. Biol. Phys. 51 (2025) 5 | 10.1007/s10867-025-09670-0 | RP |
| `@Saha2026`, `@WangHan2025`, `@Baghel2026` | fractional predator–prey models with Allee effects (commensurate/incommensurate; refuge; age structure) | introduction context ("fractional ecological models use Matignon stability at one Jacobian") | FCAA 29 (2026) 1486–1515; QTDS 24 (2025) 49; CSF 205 (2026) 117880 | 10.1007/s13540-026-00515-8; 10.1007/s12346-024-01212-8; 10.1016/j.chaos.2026.117880 | RP |

## 8. Numerical fractional methods actually mentioned in the final manuscript

Per `research/MANUSCRIPT_STORYBOARD_2026-09-26.md` §7 and `research/CHIEF_FINAL_VISUAL_GATE_2026-09-26.md`, the manuscript reports interval-certified margins (interval Newton, outward rounding) and a scale-invariant spectral corroboration; no time-domain fractional integrator is reported, so no predictor–corrector paper is cited (`DiethelmFordFreed2002` dropped). Retained as general fractional-calculus background, to be cited only if the text refers to numerical solution of Caputo systems: `@Garrappa2010`, `@Garrappa2018`; monographs `@Podlubny1999`, `@Diethelm2010`. Interval arithmetic used mpmath (software, not a scholarly reference).

## 9. Closest literature identified in the C-10 / C-15 novelty audits

`@KushelPavaniJDDE` (conic-sector forbidden-boundary criterion), `@Cain1976`, `@BahlCain1977`, `@Siami2021` (Theorem 2; symmetric slice T_α(1,1,1) = 1 + R₃(α)³, R₃(α) = sin(απ/2)/sin(απ/2 − π/3)), `@CermakNechvatal2017`, `@BourafaAbdelouahabMoussaoui2020`, `@HoltzKhrushchevKushel2016`, `@JoyaFuruta1991`, `@Kushel2023`, `@Kinkhabwala2015`, `@AlAhmadieh2026` (optional). For C-15 the audits located no source for the strict logit convexity of T_α; generic log-sum-exp / geometric-programming convexity is standard and is not cited.

## Load-bearing items: all resolved

| item | closure |
|---|---|
| Kellogg 1972 | title, journal, volume/issue/pages, DOI 10.1007/BF01402527 and the wedge statement verified (CWV §1) |
| Kushel–Pavani | JDDE 34 (2022) 651–669; theorem-numbering corrected: cite the conic-sector forbidden-boundary criterion, not "Theorem 3.3" (CWV §2) |
| Siami 2021 | IEEE TCNS 8(3) 1261–1269; cyclic secant condition is Theorem 2 (CWV §3) |
| Matignon 1996 | CESA'96 proceedings, vol. 2, 963–968, ISBN 2-9502908-9-2; no DOI exists (CWV §4) |
| Brandibur–Garrappa–Kaslik 2021 | Mathematics 9(8) 914, DOI 10.3390/math9080914 (CWV §5) |
| Cain 1976 | DOI 10.6028/jres.080B.013, issue 1 (CWV §6) |
| fractional IGP prior art | `@Panja2019` added (CWV §8) |
| IGP foundation | `@HoltPolis1997` added (CWV §8) |
| Hartfiel / Lee–Edgar / Arcak–Sontag / Arcak / Kinkhabwala / Pal–Saha / Alraddadi et al. / Tassaddiq et al. | metadata completed (CWV §7–8) |
