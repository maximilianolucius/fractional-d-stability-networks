# Paper baggage — Canonical Caputo Double-Allee 3D ecological realization

**Date:** 2026-09-26  
**Chief decision:** ADOPTED FOR THE PAPER  
**Canonical branch:** \`chief/double-allee-submission-gate-20260926\`

## 1. Canonical ecological model

The ecological realization used in the paper is a **commensurate Caputo fractional three-species Kolmogorov system**:

\[
{}^C D_t^\alpha x
=
x\left[
\frac{r}{x+a}\left(1-\frac{x}{K}\right)(x-m)
-q_1y-q_2z
\right],
\]

\[
{}^C D_t^\alpha y
=
y\left[
e_1q_1x-\mu_1-c_1y-hz
\right],
\]

\[
{}^C D_t^\alpha z
=
z\left[
e_2q_2x+e_3hy-\mu_2-c_2z
\right],
\]

with

\[
0<\alpha<1
\]

and all biological parameters positive.

Interpretation:
- \(x\): basal prey/resource;
- \(y\): intermediate consumer / intraguild prey;
- \(z\): top omnivore / intraguild predator;
- \(m\): Allee threshold;
- \(a\): low-density saturation / second Allee component;
- \(q_1,q_2,h\): trophic attack coefficients;
- \(e_1,e_2,e_3\): conversion efficiencies;
- \(c_1,c_2\): self-limitation;
- \(\mu_1,\mu_2\): mortality.

The prey per-capita growth law is

\[
g_{DA}(x)
=
\frac{r}{x+a}\left(1-\frac{x}{K}\right)(x-m).
\]

This model is non-GLV because of the nonlinear \(g_{DA}\).

## 2. Role in the paper

The model is **not** included as a generic ecological example and is not the source of the main abstract theory.

Its role is:

> to provide an exact non-GLV ecological realization of the C-10/C-15 positive-diagonal Matignon theory and to prove that the genuinely fractional band occupies a nonempty open set of biologically feasible parameters.

The paper narrative must remain theorem-first:

\[
\text{C-10/C-15 matrix theory}
\longrightarrow
\text{Kolmogorov orbit bridge}
\longrightarrow
\text{ecological realization}.
\]

## 3. Approved theorem chain

At a positive coexistence equilibrium \((X,Y,Z)\), let

\[
B=DF(X,Y,Z),\qquad
J=\operatorname{diag}(X,Y,Z)B.
\]

Positive diagonal left scaling gives the same orbit:

\[
\{DJ:D\succ0\}
=
\{EB:E\succ0\}.
\]

Therefore C-10 applies exactly to the ecological Jacobian.

The approved ecological theorem chain is:

1. **Competitive two-consumer no-go.**  
   The naive double-Allee prey + two competing consumers architecture cannot enter the open fractional-only C-10 band on the strict-\(P\) stratum.

2. **Exact IGP invariant coordinates.**  
   For the adopted model,
   \[
   \beta_{12}
   =
   1+\frac{e_1q_1^2}{sc_1},
   \]
   \[
   \beta_{13}
   =
   1+\frac{e_2q_2^2}{sc_2},
   \]
   \[
   \beta_{23}
   =
   1+\frac{e_3h^2}{c_1c_2},
   \]
   where
   \[
   s=-g_{DA}'(X)>0.
   \]

3. **Exact determinant / cycle coordinate.**
   \[
   \kappa
   =
   \beta_{12}+\beta_{13}+\beta_{23}-2
   +
   \frac{hq_1q_2(e_1e_3-e_2)}{sc_1c_2}.
   \]

4. **Four-dimensional invariant realization.**  
   The IGP architecture realizes an open four-dimensional set of C-10 invariants and, in particular, the required fractional-only band with \(\beta_{ij}>1\).

5. **Quantified double-Allee embedding.**  
   The required reduced slope \(s\) can be embedded at a positive coexistence equilibrium with explicit feasibility bounds.

6. **Open biological fractional-only region.**  
   For every fixed \(0<\alpha<1\), there exists a nonempty open set in the full biological parameter space for which
   \[
   J\in\mathcal F_\alpha^{(3)}
   \setminus
   \mathcal D_H^{(3)}.
   \]

7. **Allee-threshold monotonicity.**  
   On the positive strict-\(P\) coexistence branch,
   \[
   \frac{dX}{dm}<0,
   \qquad
   \frac{ds}{dm}<0,
   \qquad
   \frac{d}{dm}\left(\frac1s\right)>0.
   \]

8. **Unique/transverse Cain crossing.**  
   Varying \(m\) moves the invariant point monotonically and can cross the exact classical Cain boundary once and transversally.

9. **Prescribed-\(m_0\) transition.**  
   Parameters can be selected so that, with every non-\(m\) parameter fixed,
   \[
   m<m_0
   \Rightarrow
   \text{classically D-stable},
   \]
   while locally
   \[
   m>m_0
   \Rightarrow
   \text{fractional-only positive-diagonal stable}.
   \]

10. **Exact 2D/3D contrast.**  
    The corresponding two-species double-Allee model has a fractional-only mechanism only on a codimension-one condition, whereas the three-species model has a nonempty open region.

## 4. Scientific message

The ecological message is not:

> adding memory stabilizes a predator-prey model.

The paper should instead establish:

> a biologically interpretable three-species Caputo system realizes the exact matrix-theoretic gap between classical Hurwitz D-stability and positive-diagonal Matignon stability, and the double-Allee threshold acts as a monotone control parameter that moves the system across the exact Cain boundary.

This is the strongest application-level message.

## 5. Novelty boundary

Do NOT claim novelty for:
- Caputo fractional ecological dynamics;
- fractional intraguild predation;
- the double-Allee growth law;
- generic 3D predator-prey / IGP modeling;
- local Matignon stability of a fixed Jacobian;
- Kolmogorov factorization itself.

The novelty claim is restricted to:
- exact positive-diagonal Matignon realization in this non-GLV ecological system;
- constructive four-invariant access;
- full-dimensional open biological fractional-only region;
- structural no-go for the simpler competitive architecture;
- Allee-threshold crossing of the exact classical D-stability boundary;
- 2D codimension-one versus 3D open-region contrast.

## 6. Terminology lock

Use:
- **three-dimensional ecological model**;
- **three-species Kolmogorov system**;
- **Caputo fractional IGP model**;
- **double-Allee ecological realization**;
- **illustrative/certified biological parameter set**, when appropriate.

Do NOT use:
- **experimental 3D model**, unless the model is calibrated to actual experimental data;
- **empirically validated model**, unless data fitting/validation has actually been performed;
- **new fractional IGP model** as the novelty claim.

## 7. Evidence lock

The ecological realization theorem is analytic.

Computational material may be used only as:
- certified corroboration;
- visualization;
- robustness illustration;
- reproduction of the crossing.

Finite sampling must never be presented as proof of the all-\(D\) statement.

For spectral validation over positive diagonals, use scale-invariant objectives:
- eigenvalue angle;
- \(\operatorname{Re}\lambda/|\lambda|\).

Do not optimize the raw spectral abscissa over an unnormalized positive diagonal cone.

## 8. Preferred numerical anchors

Keep the exact boundary point

\[
m_0=0.20
\]

as the symbolic Cain-crossing anchor.

Use a deeper interior point approximately

\[
m\in[0.30,0.40]
\]

for the main fractional-only figure/table, after final recertification.

Reason:
- larger distance from the classical boundary;
- visually clearer robust effect;
- less appearance of fine tuning.

## 9. Figure burden for the ecological block

The ecological realization should justify approximately three compact figure environments:

1. **Motif/no-go versus IGP mechanism**
   - failed competitive architecture;
   - successful IGP architecture;
   - signed 3-cycle direction.

2. **Invariant-space Allee path**
   - \(m\mapsto(\beta,\kappa)\);
   - Cain boundary;
   - Matignon boundary;
   - exact crossing \(m_0\).

3. **Certified biological realization**
   - representative coexistence point / parameter interval;
   - optional time-domain corroboration;
   - clear label that numerics are not theorem evidence.

Avoid generic chaos/bifurcation galleries unless a theorem specifically requires them.

## 10. Bibliography rule

The submitted paper must use **published references only**.

Do not cite:
- arXiv/preprints;
- working papers;
- submitted/unpublished manuscripts;
- technical drafts;
- personal communications.

If an internal novelty search used an unpublished source, either:
- replace it in the manuscript with a formally published source; or
- remove/downgrade any manuscript claim that depends on it.

## 11. Paper-level framing

The ecological block should appear after the exact C-10/C-15 matrix theory.

Preferred transition sentence concept:

> Having characterized the full positive-diagonal Matignon orbit in dimension three, we now ask whether the genuinely fractional band can be realized by a biologically standard nonlinear Kolmogorov system rather than by an abstract matrix construction.

The answer is then:
- not by the naive competitive two-consumer architecture;
- yes by the IGP architecture;
- robustly on an open biological parameter set;
- with \(m\) as an exact crossing control.

## 12. Status

\`\`\`text
CAPUTO 3D DOUBLE-ALLEE DIRECTION: ADOPTED
ROLE IN PAPER:                   PRINCIPAL ECOLOGICAL REALIZATION
PROOF GATE:                      PASSED
EXTERNAL AUDIT:                  PASSED WITH FIX
NOVELTY:                         THEOREM-LEVEL / NARROWED
EMPIRICAL CLAIM:                 NONE
MANUSCRIPT USE:                  APPROVED
\`\`\`
