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
| C-09 | min dimension with nonempty interior of P_alpha equals 3 for every 0<alpha<1 | **NOVELTY SURVIVES TARGETED AUDIT — PROVISIONAL FLAGSHIP THEOREM** | **THEOREM — internal analytic proof complete** | C-07 + C-08 + cubic angular certificate + uniform AM-GM diagonal-orbit bound; see `research/THEOREM_C09_DIMENSION_THRESHOLD.md` |
| C-10 | exact variational 3×3 characterization on the full-dimensional strict-P(-A) stratum | **NOVELTY SURVIVES TARGETED SEARCH — PROVISIONAL FLAGSHIP PACKAGE** | **THEOREM — internal analytic proof complete** | four orbit invariants + exact simplex threshold T_alpha; recovers Cain at alpha=1; see `research/THEOREM_C10_EXACT_3X3.md` and `research/novelty/C10_TARGETED_AUDIT.md` |
| C-11 | exact orbit minimum Phi(A) and fractional Cain-type 3x3 certificate | STRUCTURAL THEOREM / SUPPORTS FLAGSHIP; standalone novelty not required | **THEOREM — analytic proof complete** | Cain 1976 classical 3x3 criterion + C-09 cubic sector lemma; see `research/THEOREM_C11_FRACTIONAL_CAIN_CERTIFICATE.md` |
| C-12 | GLV abundance-scaling invariance: J=diag(x*)A has the same F_alpha, D_H and P_alpha membership as A | APPLICATION COROLLARY / ECOLOGICAL BRIDGE | **THEOREM — immediate group-orbit proof** | positive left-diagonal orbit invariance; C-11 gives Phi(J)=Phi(A) |

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

## C-09 — dimension threshold now internally proved for all 0<α<1

`research/THEOREM_C09_DIMENSION_THRESHOLD.md` gives an analytic proof that

```text
min { n : int P_α^(n) != empty } = 3
for every 0 < α < 1.
```

For `2/3<α<1`, the proof uses a positive-coefficient cubic angular certificate

```text
(a_D b_D)/c_D > (1 - 2 cos(απ/2))^2
```

and a uniform AM-GM lower bound over all positive diagonal scalings. The proof status is upgraded to THEOREM internally; the novelty status is not frozen until the targeted audit in `research/NOVELTY_FOLLOWUP_C09_TASK.md` is completed.

## C-10 — remaining exact-characterization frontier

An exact necessary-and-sufficient 3×3 characterization of `F_α` remains OPEN and could strengthen the paper beyond the dimension-threshold theorem.

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


## Chief decision on C-09

The dedicated audit `research/novelty/C09_TARGETED_AUDIT.md` returns:

```text
NOVELTY SURVIVES
```

for the combined dimension/interior theorem. Known ingredients remain imported and must be credited: optimal fractional Routh-Hurwitz theory, Kellogg's P-matrix wedge, generalized/relative D-stability, classical robust/interior D-stability, and Siami's cyclic fractional secant result.


## C-11/C-12 — structural bridge to classical D-stability and ecology

For strict-P 3x3 matrices define

[
\Phi(A)=
\frac{
(\sqrt{p_1m_{23}}+\sqrt{p_2m_{13}}+\sqrt{p_3m_{12}})^2
}{-\det A}.
]

Then

[
\inf_{D>0}\frac{a_Db_D}{c_D}=\Phi(A).
]

Cain's classical 3x3 D-stability threshold is \(\Phi(A)>1\) in the strict-P case. For \(2/3<\alpha<1\), the project proves the fractional sufficient certificate

[
\Phi(A)>
(1-2\cos(\alpha\pi/2))^2
\Longrightarrow
A\in F_\alpha^{(3)}.
]

The right-hand threshold is strictly below one and converges to one as \(\alpha\to1^-\).

For GLV Jacobians \(J=\operatorname{diag}(x^*)A\) with \(x^*>0\), positive diagonal orbit reparametrization gives

[
J\in F_\alpha \iff A\in F_\alpha,
\qquad
J\in D_H \iff A\in D_H,
\qquad
J\in P_\alpha \iff A\in P_\alpha,
]

and \(\Phi(J)=\Phi(A)\).


## C-10 exact threshold formulation

For strict-P(-A) define the orbit invariants

[
\beta_{12}=m_{12}/(p_1p_2),\quad
\beta_{13}=m_{13}/(p_1p_3),\quad
\beta_{23}=m_{23}/(p_2p_3),\quad
\kappa=(-\det A)/(p_1p_2p_3).
]

For 2/3<alpha<1, C-10 proves

[
A\in F_\alpha^{(3)}
\iff
\kappa<T_\alpha(\beta),
]

where (T_\alpha) is the exact two-dimensional simplex minimum in
`research/THEOREM_C10_EXACT_3X3.md`.

Moreover,

[
T_\alpha(\beta)>T_1(\beta)
=
(\sqrt{\beta_{12}}+\sqrt{\beta_{13}}+\sqrt{\beta_{23}})^2,
]

so the full-dimensional genuinely fractional band is exactly

[
T_1(\beta)<\kappa<T_\alpha(\beta).
]

C-11 remains a simpler sufficient scalar certificate; C-10 proves that it is not necessary.
