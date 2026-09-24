# Claim registry

**Chief status 2026-09-24: NOVELTY AUDIT REOPENED — SECOND-PASS WEB AUDIT INCORPORATED.**

The baseline audit at commit `0b3b4df394eceec0dc9951a33fda01560de2f731` is superseded where necessary by `research/novelty/REOPENED_AUDIT_2026-09-24.md`.

| ID | Statement / object | Novelty status | Proof status | Mandatory dependency |
|---|---|---|---|---|
| C-01 | Matignon sector criterion | KNOWN/STANDARD | IMPORTED | Matignon; Brandibur–Garrappa–Kaslik |
| C-02 | Fractionally stable while integer-order unstable | DERIVABLE BUT NOT NOVEL | elementary | motivation only |
| C-03 | graph-indexed `S_alpha(G)` | DEFINITION ONLY / NEEDS THEOREM | OPEN | fractional consensus + integer-order topology/spectrum |
| C-04 | `F_alpha = {A: sigma(DA) subset Sigma_alpha for all D>0}` | KNOWN GENERALIZED-D-STABILITY FRAMEWORK; EXACT SUBCLASS CHARACTERIZATION MAY BE NEW | framework known / low-dimensional results below | Kushel 2019; Kushel–Pavani 2020/2021; Kushel 2023 |
| C-05 | topology/motifs characterize genuinely non-Hurwitz fractional D-stability | REOPENED — SINGLE-CYCLE NOVELTY REJECTED | OPEN beyond single cycle | Siami 2020/2021 + Arcak/Sontag |
| C-06 | perturbational robustness / interior of fractional D-stability | CONCEPT HAS CLASSICAL PRIOR ART; FRACTIONAL NON-HURWITZ VERSION MAY BE NEW | PARTIAL | Hartfiel 1980; Abed 1986; Lee–Edgar 2001; Casasanta–Simpson-Porco 2026 |
| C-07 | exact 2×2 classification of F_alpha; no open purely-fractional separation in n=2 | STRUCTURAL RESULT; NOVELTY SECONDARY / STILL AUDITING | **THEOREM — analytic proof in reopened audit** | trace/determinant scaling |
| C-08 | min dimension with nonempty interior of P_alpha equals 3 for 0<alpha<=2/3 | **STRONG NOVELTY CANDIDATE — NOT FROZEN** | **THEOREM — analytic proof modulo Kellogg P-matrix wedge theorem** | Kellogg P-matrix spectral wedge + C-07 |
| C-09 | same dimension-threshold result for every 0<alpha<1 | **HIGHEST-VALUE OPEN TARGET** | OPEN for 2/3<alpha<1 | compactified diagonal orbit + boundary-face analysis |
| C-10 | exact 3×3 characterization of F_alpha for 2/3<alpha<1 | POTENTIALLY TITLE-WORTHY | OPEN | fractional analogue of Cain + Kushel forbidden-boundary framework |

## Current objects

```text
Σ_α = { z ≠ 0 : |arg z| > απ/2 }

F_α^(n) = { A ∈ R^(n×n) : σ(DA) ⊂ Σ_α for every D > 0 }

P_α^(n) = F_α^(n) \ D_H^(n)
```

The main scientific target is now **low-dimensional structural mathematics for P_α^(n)** before any graph-family generalization.

## C-07 — exact 2×2 classification

For every real A = [[a,b],[c,d]] and every 0 < α < 1,

```text
A ∈ F_α^(2)  iff  det(A)>0, a<=0, d<=0.
```

Moreover,

```text
P_α^(2) = { [[0,b],[c,0]] : bc<0 }
```

and therefore

```text
int_R4 P_α^(2) = empty.
```

Proof: `research/novelty/REOPENED_AUDIT_2026-09-24.md`.

## C-08 — proved dimension-three separation for 0 < α ≤ 2/3

Use

```text
A_γ = [ [-1, 0, -γ],
        [ γ,-1,  0],
        [ 0, γ, -1] ],   γ>2.
```

Then -A_γ is a strict P-matrix. By Kellogg's spectral wedge theorem, for every D > 0,

```text
|arg λ(DA_γ)| > π/3.
```

Thus A_γ ∈ F_α^(3) for 0 < α ≤ 2/3. But

```text
σ(A_γ) =
{ -1-γ,
  -1+γ/2 ± i(√3 γ/2) }.
```

Hence A_γ is not Hurwitz for γ>2. Strict P-matrix inequalities and positive spectral abscissa persist under sufficiently small full-matrix perturbations, yielding an open ball contained in P_α^(3).

Therefore

```text
min { n : int P_α^(n) != empty } = 3
for every 0 < α ≤ 2/3.
```

**Important:** this is an internal analytic theorem result; the **novelty claim remains under active literature audit**.

## C-09/C-10 — current proof frontier

The unresolved regime is

```text
n = 3
2/3 < α < 1.
```

Targets:

1. prove int P_α^(3) != empty for every 0 < α < 1; or
2. derive an exact 3×3 criterion for F_α in the high-order regime.

Ordinary continuity at fixed D is insufficient; the proof must control degenerate diagonal directions where ratios d_i/d_j tend to 0 or infinity.

## Q1 gate

No central-paper drafting until there is:

1. one exact characterization theorem;
2. one genuine separation/obstruction theorem versus classical D-stability and Siami/Kushel prior art;
3. one nontrivial structural extension: complete dimension threshold, exact 3×3 criterion, or motif theorem not reducible to Siami.

## Evidence labels

- `THEOREM` — analytic proof.
- `IMPORTED THEOREM` — published result used as a lemma.
- `CERTIFIED COMPUTATION` — rigorous certificate.
- `NUMERICAL CORROBORATION` — floating-point evidence only.
- `OPEN` — unresolved.

Finite diagonal sampling is never proof.
