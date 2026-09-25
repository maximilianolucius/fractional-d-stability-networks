# Provisional canonical witness selection for the manuscript

**Source:** Compute Wave 2 P2, branch \`agent/compute-wave2-20260925\`  
**Status:** provisional until Wave 2 final report and P3 robustness are complete.

The main paper should contain a compact 4--5-row witness table. The full 35-matrix library belongs in supplementary material/data.

## Recommended rows

### W03 — analytic symmetric reference / Siami slice

\[
\alpha=0.95,\qquad
A=
\begin{pmatrix}
-1&0&-2.1\\
2.1&-1&0\\
0&2.1&-1
\end{pmatrix}.
\]

- \(\beta=(1,1,1)\).
- \(\kappa=10.261\).
- \(T_1=9\).
- \(T_\alpha=13.4172204387\ldots\), interval certified.
- \(A\) is already non-Hurwitz at \(D=I\).
- Role: bridge to the exact Siami/cyclic slice; not the generic novelty example.

### W10 — nonsymmetric matrix with certified threshold

\[
\alpha=0.8,\qquad
A=
\begin{pmatrix}
-1&-3&0\\
0&-1&-2\\
-2&0&-1
\end{pmatrix}.
\]

- generic nonsymmetric matrix;
- \(\beta=(1,1,1)\), \(\kappa=13\);
- \(T_1=9\);
- \(T_\alpha=96.7154941467\ldots\), interval certified;
- not Hurwitz at \(D=I\);
- direct spectral checks agree with the invariant classification.

Role: shows that even the symmetric invariant slice contains matrices not presented in the canonical cyclic orientation.

### W22 — Hurwitz at \(D=I\), but not Hurwitz D-stable

\[
\alpha=0.7,\qquad
A=
\begin{pmatrix}
-1&-3/2&0\\
-1/2&-1&-3\\
-3&0&-2
\end{pmatrix}.
\]

- \(\beta=(1/4,1,1)\);
- \(\kappa=7\);
- \(T_1=6.25\);
- \(T_\alpha=4726.93970104\ldots\) (HP);
- \(A\) itself is Hurwitz:
  \[
  \max\Re\sigma(A)\approx-0.0788952;
  \]
- nevertheless the classical positive-diagonal orbit fails Hurwitz stability;
- explicit Cain-minimizing diagonal, geometric-mean normalized:
  \[
  D_H\approx\operatorname{diag}(1.58740,1.58740,0.396850),
  \]
  with
  \[
  \max\Re\sigma(D_HA)\approx0.0384324>0.
  \]

Role: particularly strong conceptual example. It distinguishes ordinary stability at \(D=I\) from orbit-level D-stability and shows why the all-\(D\) theorem is not merely a restatement of fractional stabilization of one matrix.

### W18 — mixed-sign ecological example

\[
\alpha=0.7,\qquad
A=
\begin{pmatrix}
-1&-3&-1/2\\
0&-1&-2\\
-3/2&1/2&-1
\end{pmatrix}.
\]

- \(\beta=(1,1/4,2)\);
- \(\kappa=41/4=10.25\);
- \(T_1\approx8.4926406871\);
- \(T_\alpha\approx4991.73914301\) (HP);
- loop coordinates
  \[
  g=(0,3/4,-1),
  \qquad
  L_3=-9;
  \]
- direct orbit checks agree with C-10.

Role: best compact ecological feedback example; the reciprocal products include zero, positive and negative signs.

### W28 — generic near the exact fractional boundary

\[
\alpha=0.9,\qquad
A=
\begin{pmatrix}
-1&-3&0\\
1/2&-1&-3\\
-3&0&-1
\end{pmatrix}.
\]

- \(\beta=(5/2,1,1)\);
- \(\kappa=59/2=29.5\);
- \(T_1\approx12.8245553203\);
- \(T_\alpha\approx29.6498305102\) (HP);
- fractional margin
  \[
  T_\alpha-\kappa\approx0.1498305102;
  \]
- normalized band position \(\approx0.991095\);
- direct worst-orbit Matignon margin is positive and very small.

Role: demonstrates a genuinely generic matrix close to the exact C-10 boundary, where the theorem is most numerically delicate.

## Recommended main-table choice

If limited to four rows:

1. W03 — symmetric analytic reference;
2. W22 — Hurwitz at identity but not D-stable;
3. W18 — mixed ecological feedback;
4. W28 — close to the exact fractional boundary.

If five rows are affordable, add W10 as an interval-certified nonsymmetric matrix.

## Before insertion into the paper

Wait for Wave 2 P3/P4/P5 and the final report. Then:

- replace HP labels by CERTIFIED where P1/P3 can certify the exact beta point;
- add final robustness columns from P3;
- choose only quantities necessary to support the narrative;
- move full matrices/precision metadata for the remaining witnesses to supplementary material.
