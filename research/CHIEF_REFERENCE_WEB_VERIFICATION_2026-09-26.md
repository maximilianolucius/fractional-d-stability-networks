# Chief Reference Web Verification — Closure of Load-Bearing Gaps

**Date:** 2026-09-26  
**Branch:** \`chief/reference-closure-20260926\`

## Decision

All load-bearing bibliographic gaps from Reference Audit Wave 1 are now closed.

The manuscript may proceed using published sources only, subject to one final mechanical reconciliation wave that removes remaining non-load-bearing metadata warnings.

## 1. Kellogg 1972 — CLOSED

R. B. Kellogg, **“On complex eigenvalues of M and P matrices,”** *Numerische Mathematik* 19(2), 170–175 (1972).

DOI: \`10.1007/BF01402527\`

This is the load-bearing source for the P-matrix eigenvalue wedge:

\[
|\arg\mu|<\pi-\frac{\pi}{n}
\]

for eigenvalues of real P-matrices.

Use:
- C-08;
- C-10 low-order case;
- DA-08 / DA-11 for \(\alpha\le2/3\).

## 2. Kushel–Pavani generalized D-stability — CLOSED WITH NUMBERING CORRECTION

Olga Y. Kushel and Raffaella Pavani, **“The Problem of Generalized D-Stability in Unbounded LMI Regions and Its Computational Aspects,”** *Journal of Dynamics and Differential Equations* 34, 651–669 (2022).

DOI: \`10.1007/s10884-020-09891-y\`

Important correction:

> **“Theorem 3.3” was incorrect.**  
> Section 3.3 is the classical forbidden-boundary subsection.  
> The conic-sector/complement necessary-and-sufficient criterion relevant to our positioning is **Theorem 6** in the published-text lineage.

Manuscript policy:
- cite the paper and describe it as the conic-sector forbidden-boundary criterion;
- do not hardcode “Theorem 3.3”.

This correction has been propagated into the final novelty audit files.

## 3. Siami 2021 — CLOSED

Milad Siami, **“Stability and Robustness Analysis of Commensurate Fractional-Order Networks,”** *IEEE Transactions on Control of Network Systems* 8(3), 1261–1269 (2021).

DOI: \`10.1109/TCNS.2021.3061931\`

The cyclic fractional secant condition is Theorem 2 in the article lineage.

Use as:
- structured symmetric/single-cycle prior art;
- not as an all-positive-diagonal arbitrary-\(\beta\) theorem.

## 4. Matignon 1996 — CLOSED

Denis Matignon, **“Stability results for fractional differential equations with applications to control processing,”** CESA'96 IMACS Multiconference, Symposium on Control, Optimization and Supervision, Lille, vol. 2, pp. 963–968 (1996).

ISBN: \`2-9502908-9-2\`

No DOI was located in the bibliographic records inspected. Do not invent one.

The final paper may cite this formally published proceedings paper and/or the modern Brandibur–Garrappa–Kaslik journal treatment.

## 5. Brandibur–Garrappa–Kaslik 2021 — CLOSED

Oana Brandibur, Roberto Garrappa, Eva Kaslik, **“Stability of Systems of Fractional-Order Differential Equations with Caputo Derivatives,”** *Mathematics* 9(8), 914 (2021).

DOI: \`10.3390/math9080914\`

Use as the modern published foundation for the Matignon-type Caputo stability criterion and its limiting conventions.

## 6. Cain 1976 — CLOSED

Bryan E. Cain, **“Real, 3 × 3, D-Stable Matrices,”** *Journal of Research of the National Bureau of Standards B* 80B(1), 75–77 (1976).

DOI: \`10.6028/jres.080B.013\`

Use as:
- exact classical \(\alpha=1\) endpoint;
- classical all-D optimization predecessor;
- crossing classifier at \(m_0\).

## 7. Additional classical D-stability metadata closed

### Hartfiel 1980

Darald J. Hartfiel, **“Concerning the interior of the D-stable matrices,”** *Linear Algebra and its Applications* 30, 201–207 (1980).

DOI: \`10.1016/0024-3795(80)90195-0\`

### Lee–Edgar 2001

Jietae Lee and Thomas F. Edgar, **“Real structured singular value conditions for the strong D-stability,”** *Systems & Control Letters* 44(4), 273–277 (2001).

DOI: \`10.1016/S0167-6911(01)00147-5\`

### Arcak–Sontag 2006

Murat Arcak and Eduardo D. Sontag, **“Diagonal stability of a class of cyclic systems and its connection with the secant criterion,”** *Automatica* 42(9), 1531–1537 (2006).

DOI: \`10.1016/j.automatica.2006.04.009\`

### Arcak 2011

Murat Arcak, **“Diagonal Stability on Cactus Graphs and Application to Network Stability Analysis,”** *IEEE Transactions on Automatic Control* 56(12), 2766–2777 (2011).

DOI: \`10.1109/TAC.2011.2125130\`

## 8. Ecological prior-art metadata closed

### Holt–Polis 1997

Robert D. Holt and Gary A. Polis, **“A Theoretical Framework for Intraguild Predation,”** *The American Naturalist* 149(4), 745–764 (1997).

DOI: \`10.1086/286018\`

This is the preferred foundational source for “IGP is a standard ecological module.”

### Panja 2019

Prabir Panja, **“Dynamics of a fractional order predator–prey model with intraguild predation,”** *International Journal of Modelling and Simulation* 39(4), 256–268 (2019).

DOI: \`10.1080/02286203.2019.1611311\`

This source is mandatory for novelty positioning:
- fractional IGP already exists;
- our novelty is not “Caputo + IGP”.

### Kinkhabwala 2015

Ali Kinkhabwala, **“Implications of Network Topology on Stability,”** *PLOS ONE* 10(3), e0122150 (2015).

DOI: \`10.1371/journal.pone.0122150\`

### Pal–Saha 2015

Pallav Jyoti Pal and Tapan Saha, **“Qualitative analysis of a predator–prey system with double Allee effect in prey,”** *Chaos, Solitons & Fractals* 73, 36–63 (2015).

DOI: \`10.1016/j.chaos.2014.12.007\`

### Alraddadi–Ahmed–Seol 2026

Ibrahim Alraddadi, Rizwan Ahmed, Youngsoo Seol, **“Bifurcation Structure and Chaos Control in a Discrete-Time Fractional Predator–Prey Model with Double Allee Effect,”** *Fractal and Fractional* 10(5), 304 (2026).

DOI: \`10.3390/fractalfract10050304\`

### Tassaddiq–Ahmed–Khan–Lee 2026

Asifa Tassaddiq, Rizwan Ahmed, Jawad Khan, Youngmoon Lee, **“Impact of double Allee effect on the dynamics and stability of a predator-prey model,”** *AIMS Mathematics* 11(1), 1117–1144 (2026).

DOI: \`10.3934/math.2026048\`

## 9. Published-only policy reaffirmed

The final manuscript bibliography must not contain:
- arXiv identifiers;
- eprint fields;
- archivePrefix fields;
- preprints;
- working papers;
- submitted/unpublished manuscripts;
- technical drafts;
- personal communications.

The following are blocked as manuscript references:
- Kushel 2026 arXiv-only work;
- Casasanta–Simpson-Porco 2026 arXiv-only work;
- Cong et al. arXiv-only item appearing only in the reference paper;
- any other unpublished source found during research.

If a published version exists, cite only the published version.

## 10. Gate state

\`\`\`text
LOAD-BEARING REFERENCE GAPS: CLOSED
KELLOGG:                     VERIFIED
CAIN DOI:                    VERIFIED
MATIGNON PROCEEDINGS:        VERIFIED
BRANDIBUR ET AL.:            VERIFIED
KUSHEL-PAVANI:               VERIFIED + NUMBERING FIX
SIAMI:                       VERIFIED
FRACTIONAL IGP PRIOR ART:    PANJA 2019 ADDED
IGP FOUNDATION:              HOLT-POLIS 1997 ADDED
UNPUBLISHED SOURCES:         BLOCKED
REFERENCE GATE:              READY FOR FINAL MECHANICAL WAVE
\`\`\`

Reference Audit Wave 2 must now:
1. remove remaining non-load-bearing \`NEEDS_CHIEF_WEB_VERIFICATION\` notes where metadata can be verified;
2. reconcile all keys against this Chief record;
3. rerun the full audit;
4. produce a zero-warning final published-only candidate bibliography if possible;
5. flag only truly optional references that should simply be omitted rather than guessed.
