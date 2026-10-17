# Response to Reviewers — Round 1
**Journal:** Mathematics (MDPI) · **Manuscript ID:** mathematics-4633263

We thank both reviewers for the constructive suggestions. All references below refer to the revised source in `paper/review/round1/revised-source/`, derived from the *exact submitted ZIP*, and not from the working manuscript of another branch. Both reports recommended minor revision.

## Reviewer 1

**R1-1 (Lemma 1, cubic factorization).** Added the explicit factorization `(lambda^2-2ur lambda+r^2)(lambda+a+2ur)`, the quadratic relation for `r`, and identification of the conjugate boundary pair and negative third root. Location: section 04, Lemma 1 proof.

**R1-2 (attainment of `T_alpha`).** Included `h_alpha(0)>0` for `2/3<alpha<1` and the boundary-divergence proof; treated `alpha=1` separately using `h_1(b)=b` and the reciprocal-coordinate expression. Location: section 04, following definition of `T_alpha`.

**R1-3 (strict order monotonicity).** The proof now evaluates both objectives at the attained minimizer for the smaller order to establish a strict three-term inequality; the comparison to `T_1` is explicit. Location: section 05, order-dependence theorem.

**R1-4 (the endpoint `alpha=2/3`).** Written the strict Kellogg wedge comparison `|arg lambda|>pi/3 >= alpha*pi/2`. Location: section 04, Corollary 1 proof.

**R1-5 (fractional-only set versus interior).** Distinguished the exact set `T_1<=kappa<T_alpha` from its full-dimensional interior `T_1<kappa<T_alpha`. At equality, a purely imaginary pair excludes Hurwitz stability while remaining strictly Matignon stable for `alpha<1`. Location: section 04.

**R1-6 (reduced matrix and simulation Jacobian).** Distinguished `B=DF(u*)`, the unscaled Jacobian `J=diag(u*)B`, and the chosen row-scaled Jacobian `R_*J=D_*B`. Explicitly defined what failure of Hurwitz D-stability means. Location: section 07.

**R1-7 (interval certificates, precision, internal names).** Added `mpmath.iv` software, 50-digit parameter-box and 40-digit logit threshold computations, interval Hessian lower bounds, minimizer localization, and validated lower threshold `underline T_alpha` that exceeds the upper `kappa` enclosure. Distinguishes the 60-digit numerical root and its residual from the 15-digit printed `m_0`. Removed internal claim labels from revised visible prose and the rewritten captions; the two original figure artworks carrying internal codes (Figures 2 and 3) have been regenerated without those codes; the agent's rebuilt PDF was checked for absent claim labels. Location: section 07 and rewritten captions.

## Reviewer 2

**R2-1 / R2-2 (minor wording).** Corrected the missing comma after “Therefore” and checked the “consistent with” wording. Locations: sections 03 and 07.

**R2-3 (scope of strict-P condition).** Added an explicit remark that the threshold characterizes the open full-dimensional strict-P stratum and does not classify matrices with zero principal minors. Location: section 04, before principal-minor necessity.

**R2-4 (biological feasibility under perturbation).** Clarified local parameter feasibility through the implicit-function theorem, including strict positivity and equilibrium inequalities, and distinguished small positive initial perturbations from global permanence. Location: sections 07 and 08.

**R2-5 (self-contained figure captions).** Expanded the existing figure captions to identify axes/objects, mathematical boundaries, computational versus interval-certified markers, and limitation of finite numerical search. Locations: sections 03, 04, 06, 07. The artwork of Figures 2 and 3 was regenerated to remove internal labels, and the new Figure 10 has a self-contained caption.

**R2-6 (additional fractional orders).** Replaced the initial short-horizon \(t=180\) table, whose distances alone did not clearly distinguish slower decay from instability, by a 363-integration full nonlinear Caputo study on the Orion server. The dense scan used \(\Delta\alpha=0.001\), PECE steps \(h=0.02\) and \(0.01\), and extended horizons up to \(t=2000\) near the analytically predicted threshold \(\alpha_*=0.9505501071\ldots\). The fitted late log-distance rate changes sign between \(\alpha=0.9500\) (negative) and \(0.9506\) (positive); trajectories for \(\alpha\ge0.953\) exit the prescribed local radius by \(t=2000\). The unscaled Jacobian remains Hurwitz and the unscaled runs decay. The 339/340 agreement of the endpoint-distance proxy with the linear prediction, and the near-critical finite-horizon exception at \(0.9506\), are discussed explicitly rather than counted as an asymptotic proof. Added a long-horizon numerical table and Figure 10 with self-contained panels for the trajectories and fitted growth rates. Source: Section 07, Figure 10 and \`paper/review/round1/NUMERICS_R2-6_ALPHA_SWEEP.md\`; reproduce with \`computations/figures_wave2/scripts/alpha_sweep_nonlinear.py\`.

**R2-7 (recent references and novelty).** Added published DOI-verified 2025–2026 contributions on commensurate/incommensurate fractional ecology and ecoepidemiology and sharpened the distinction between fixed-model studies and an exact universal positive-diagonal criterion. Locations: introduction, bibliography.
