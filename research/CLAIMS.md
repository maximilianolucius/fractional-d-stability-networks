# Claim registry

**Chief status 2026-09-24: NOVELTY AUDIT REOPENED — SECOND-PASS WEB AUDIT INCORPORATED.**

The baseline audit at commit `0b3b4df394eceec0dc9951a33fda01560de2f731` is superseded where necessary by `research/novelty/REOPENED_AUDIT_2026-09-24.md`.

| ID | Statement / object | Novelty status | Proof status | Mandatory dependency |
|---|---|---|---|---|
| C-01 | Matignon sector criterion | KNOWN/STANDARD | IMPORTED | Matignon; Brandibur–Garrappa–Kaslik |
| C-02 | Fractionally stable while integer-order unstable | DERIVABLE BUT NOT NOVEL | elementary | motivation only |
| C-03 | graph-indexed `S_alpha(G)` | DEFINITION ONLY / NEEDS THEOREM | OPEN | fractional consensus + integer-order topology/spectrum |
| C-04 | `F_alpha={A: sigma(DA) subset Sigma_alpha for all D>0}` | KNOWN GENERALIZED-D-STABILITY FRAMEWORK; EXACT SUBCLASS CHARACTERIZATION MAY BE NEW | framework known / low-dimensional results below | Kushel 2019; Kushel–Pavani 2020/2021; Kushel 2023 |
| C-05 | topology/motifs characterize genuinely non-Hurwitz fractional D-stability | REOPENED — SINGLE-CYCLE NOVELTY REJECTED | OPEN beyond single cycle | Siami 2020/2021 + Arcak/Sontag |
| C-06 | perturbational robustness / interior of fractional D-stability | CONCEPT HAS CLASSICAL PRIOR ART; FRACTIONAL NON-HURWITZ VERSION MAY BE NEW | PARTIAL | Hartfiel 1980; Abed 1986; Lee–Edgar 2001; Casasanta–Simpson-Porco 2026 |
| C-07 | exact (2\times2) classification of `F_alpha`; no open purely-fractional separation in (n=2) | STRUCTURAL RESULT; NOVELTY SECONDARY / STILL AUDITING | **THEOREM — analytic proof in reopened audit** | trace/determinant scaling |
| C-08 | (min\{n:\operatorname{int}P_\alpha^{(n)}\neq\varnothing\}=3) for (0<\alpha\le2/3) | **STRONG NOVELTY CANDIDATE — NOT FROZEN** | **THEOREM — analytic proof modulo Kellogg P-matrix wedge theorem** | Kellogg P-matrix spectral wedge + C-07 |
| C-09 | same dimension-threshold result for every (0<\alpha<1) | **HIGHEST-VALUE OPEN TARGET** | OPEN for (2/3<\alpha<1) | compactified diagonal orbit + boundary-face analysis |
| C-10 | exact (3\times3) characterization of `F_alpha` for (2/3<\alpha<1) | POTENTIALLY TITLE-WORTHY | OPEN | fractional analogue of Cain + Kushel forbidden-boundary framework |

## Current objects

[
Sigma_alpha={z
e0:|arg z|>alphapi/2},
]

[
mathcal F_alpha^{(n)}
=
{Ainmathbb R^{n	imes n}:
sigma(DA)subsetSigma_alpha orall Dsucc0},
]

[
mathcal P_alpha^{(n)}
=
mathcal F_alpha^{(n)}
setminus
mathcal D_H^{(n)}.
]

The main scientific target is now **low-dimensional structural mathematics for (mathcal P_alpha^{(n)})** before any graph-family generalization.

## C-07 — exact (2\times2) classification

For every real

[
A=
egin{pmatrix}a&b\\c&dend{pmatrix}
]

and every (0<alpha<1),

[
oxed{
Ainmathcal F_alpha^{(2)}
iff
det A>0,quad ale0,quad dle0.
}
]

Moreover,

[
oxed{
mathcal P_alpha^{(2)}
=
left{
egin{pmatrix}0&b\\c&0end{pmatrix}:bc<0
ight},
}
]

hence

[
oxed{
operatorname{int}_{mathbb R^4}
mathcal P_alpha^{(2)}
=
arnothing.
}
]

Proof is recorded in `research/novelty/REOPENED_AUDIT_2026-09-24.md`.

## C-08 — proved dimension-three separation for (0<\alpha\le2/3)

Use

[
A_gamma=
egin{pmatrix}
-1&0&-gamma\\
gamma&-1&0\\
0&gamma&-1
end{pmatrix},
qquad gamma>2.
]

Then (-A_gamma) is a strict P-matrix. By Kellogg's spectral wedge theorem, for every (Dsucc0),

[
|arglambda(DA_gamma)|>pi/3.
]

Therefore

[
A_gammainmathcal F_alpha^{(3)}
qquad
(0<alphale2/3).
]

But

[
sigma(A_gamma)
=
left{
-1-gamma,,
-1+gamma/2pm isqrt3,gamma/2
ight},
]

so (A_gamma
otinmathcal D_H^{(3)}) for (gamma>2). The strict P-matrix inequalities and the positive spectral-abscissa inequality persist under sufficiently small full-matrix perturbations, yielding

[
B_arepsilon(A_gamma)
subset
mathcal P_alpha^{(3)}
]

for some (arepsilon>0).

Together with C-07,

[
oxed{
min{n:
operatorname{int}mathcal P_alpha^{(n)}
eqarnothing}
=3
qquad(0<alphale2/3).
}
]

**Important:** this is an internal analytic theorem result; the **novelty claim is still under literature audit**.

## C-09/C-10 — current proof frontier

The unresolved regime is

[
n=3,qquad 2/3<alpha<1.
]

The target is either:

1. prove (operatorname{int}mathcal P_alpha^{(3)}
eqarnothing) for every (0<alpha<1), completing the dimension-threshold theorem; or
2. derive an exact (3	imes3) criterion for (mathcal F_alpha) in the high-order regime, analogous in spirit to Cain's low-dimensional classical D-stability conditions but for the Matignon boundary rays.

Ordinary continuity at a fixed (D) is insufficient; the proof must control degenerate diagonal directions (d_i/d_j	o0,infty).

## Q1 gate

No central-paper drafting until there is:

1. one exact characterization theorem;
2. one genuine separation/obstruction theorem versus classical D-stability and Siami/Kushel prior art;
3. one nontrivial structural extension: complete dimension threshold, exact (3	imes3) criterion, or motif theorem not reducible to Siami.

## Evidence labels

- `THEOREM` — analytic proof.
- `IMPORTED THEOREM` — published result used as a lemma.
- `CERTIFIED COMPUTATION` — rigorous certificate.
- `NUMERICAL CORROBORATION` — floating-point evidence only.
- `OPEN` — unresolved.

Finite diagonal sampling is never proof.
