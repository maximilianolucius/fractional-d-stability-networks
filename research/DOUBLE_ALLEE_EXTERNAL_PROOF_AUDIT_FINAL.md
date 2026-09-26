# External independent proof audit — Double-Allee theorem core

**Date:** 2026-09-26  
**Audited branch:** `agent/external-proof-double-allee-20260926`  
**Audited input SHA:** `f3bd34b0482e3709939de00cdbfb9e836aa7893b`  
**Overall status:** `EXTERNAL_AUDIT_PASS_WITH_FIXES`

## 0. Eligibility and scope

This is a different session from the sessions that produced
`research/DOUBLE_ALLEE_PROOF_AUDIT_FINAL.md` and
`research/DOUBLE_ALLEE_PROOF_AUDIT2_FINAL.md`. The eligibility gate is
therefore satisfied.

I independently reconstructed the logical core from the current theorem
files. I did not modify `paper/`, any Chief theorem/report, novelty material,
or either prior audit. Numerical experiments below are used only as
falsification searches; all verdicts rest on analytic arguments.

## 1. Verdicts

| Item | Verdict | Decisive reason |
|---|---|---|
| EXT-01 invariant realization | **PASS** | The displayed construction is a global right inverse on the open set `beta_ij>1`, `kappa>sum(beta)-2`; all parameters are positive, all efficiencies lie in `(0,1)`, and `e1 e3>e2`. |
| EXT-02 biological embedding | **PASS** | `H_A>0`, the mortality bounds, the `K-X` bound, all equilibrium equations, and the finite `K->X+` limit of `r` are mutually compatible and quantified. |
| EXT-03 full-dimensional openness | **PASS** | A base point exists for every fixed `0<alpha<1`; the full state Jacobian is `diag(X,Y,Z)B`, is nonsingular, and the IFT continues the equilibrium under independent perturbations of all 14 biological coordinates. |
| EXT-04 strict-P / nondegeneracy | **PASS** | `-det B=Delta(s+chi)` exactly. Moreover `q=0` is a genuine nondegenerate fold boundary in the `m` direction, not merely an IFT failure. |
| EXT-05 Allee sensitivity | **PASS WITH FIX** | `dX/dm<0` is correct. The current `chi>=0` condition for `ds/dm<0` is sufficient but unnecessary: strict-P alone already forces `ds/dm<0`. The exact strengthening is proved below. |
| EXT-06 unique/transverse Cain crossing | **PASS** | The formula, strict convexity, iff crossing condition, uniqueness, and the stated positive transversality bound all follow exactly. |
| EXT-07 prescribed-`m0` transition | **PASS** | The one-time joint realization fixes every parameter other than `m`; the local branch crosses in the correct direction, and the high-order step uses exact C-10, not C-11. |
| EXT-08 dependency/circularity | **PASS** | The dependency graph is acyclic. C-07 and C-11 are not load-bearing for this core; C-15 is useful for smooth threshold dependence but is not needed to create the ecological realization. |

No load-bearing implication fails. The sole requested fix is a theorem
strengthening in EXT-05, not a repair of a false conclusion used later.

## 2. EXT-01 — invariant realization

Put

~~~text
A = beta12-1,  B = beta13-1,  C = beta23-1,
R = kappa-(beta12+beta13+beta23-2).
~~~

All four are positive. With

~~~text
rho = R/sqrt(ABC),
tau = (rho+sqrt(rho^2+4))/2,
~~~

one has `tau>1` and `tau-1/tau=rho`. For any `eta in (0,1)`,

~~~text
e1=e3=eta,       e2=eta^2/tau^2
~~~

gives `0<e_i<1` and `e1 e3/e2=tau^2>1`. For arbitrary positive
`s,c1,c2`, the positive square-root definitions of `q1,q2,h` reproduce
the three prescribed beta coordinates. Their remaining contribution is

~~~text
sqrt(ABC)(tau-1/tau)=R,
~~~

so the prescribed kappa is also exact. There is no additional algebraic
constraint.

This is stronger than a local rank calculation: it is an explicit right
inverse onto the entire open four-dimensional set

~~~text
{beta_ij>1, kappa>beta12+beta13+beta23-2}.
~~~

Consequently the image contains the desired open four-dimensional
fractional band. Since each `beta_ij>1`, the lower bound on kappa also
implies `kappa>0`, hence `q=kappa*s*c1*c2>0`.

## 3. EXT-02 — quantified biological embedding

Let

~~~text
d=X-m,  u=X+a,  ell=K-X.
~~~

Then `d,u,ell>0`, `u-d=m+a>0`, and

~~~text
C_A=(m+a)/(du)>0,
H_A=1/ell-C_A.
~~~

Therefore

~~~text
H_A>0  iff  0<ell<1/C_A,
K_max=X+1/C_A.
~~~

For `Q=s/H_A`, the split

~~~text
Y=xi Q/q1,  Z=(1-xi)Q/q2
~~~

is positive and gives `q1Y+q2Z=Q`. The formula for `mu1` has a strictly
positive intercept and a strictly negative `Q` coefficient, so `Q<Q1`
is exact and `Q1>0`. For `mu2`, no bound is needed when its displayed
`Q` coefficient is nonnegative; otherwise its denominator is positive
and `Q<Q2` is exact. Thus `Qbar` is always positive.

The bound

~~~text
0<K-X<1/(C_A+s/Qbar)
~~~

is nonempty, implies `H_A>s/Qbar`, hence `Q<Qbar`, and is automatically
contained in `(0,1/C_A)`. There is no incompatibility between mortality
positivity and `H_A>0`.

Finally,

~~~text
r = Q(X+a)/[(1-X/K)(X-m)]
~~~

is positive, realizes `g_DA(X)=Q`, and gives `g_DA'(X)=-QH_A=-s`.
Although `Q,Y,Z` tend to zero as `K->X+`, the growth parameter does not
blow up:

~~~text
lim_(K->X+) r = s X(X+a)/(X-m) in (0,infinity).
~~~

All three coexistence equations then hold by the definitions of
`mu1,mu2`.

## 4. EXT-03 — full-dimensional biological openness

An explicit base-point recipe exists for every fixed alpha:

- take `beta=(2,2,2)`, for which `T1=18`;
- if `2/3<alpha<1`, take
  `kappa=(18+T_alpha(2,2,2))/2`; C-10 gives `T_alpha>18`;
- if `0<alpha<=2/3`, take `kappa=19`;
- apply EXT-01 and then EXT-02.

This produces a feasible positive equilibrium with the required strict
invariant inequalities. At coexistence the per-capita Jacobian is `B`,
whereas the full state Jacobian is

~~~text
J=diag(X,Y,Z)B.
~~~

The distinction causes no gap because

~~~text
det B=-kappa*s*c1*c2 != 0,
det J=XYZ det B != 0.
~~~

Apply the IFT to the three state equations and the state variables
`(X,Y,Z)`, with all 14 biological parameters

~~~text
(r,a,K,m,q1,q2,e1,e2,e3,mu1,mu2,c1,c2,h)
~~~

free. It produces a smooth local equilibrium branch over a neighborhood
in the full 14-dimensional parameter space. Positivity, `m<X<K`, the
efficiency inequalities, strict-P, and the strict C-10/Cain inequalities
all persist after shrinking the neighborhood. Thus this is not openness
inside a constrained construction manifold.

For `2/3<alpha<1`, continuity (indeed smoothness, by C-15) of
`T_alpha(beta)` preserves the upper inequality. For low order, strict-P
and `kappa>T1` are open conditions. The Kolmogorov orbit lemma then
transfers the classification from `B` to `J`.

The argument is pointwise in alpha. As `alpha->1-` the available band
shrinks but remains nonempty for every fixed `alpha<1`; as
`alpha->2/3+`, C-15 shows that the upper threshold diverges. There is no
endpoint discontinuity that defeats the existence or openness claim.

## 5. EXT-04 — strict-P identity and fold boundary

Direct determinant expansion gives

~~~text
q=-det B
 =s(c1c2+e3h^2)
  +c1e2q2^2+c2e1q1^2+hq1q2(e1e3-e2)
 =Delta(s+chi).
~~~

When `s>0`, all order-one and order-two principal minors of `-B` are
strictly positive. Since `Delta>0`, strict-P is therefore equivalent to

~~~text
s>0 and s+chi>0.
~~~

For the scalar coexistence equation

~~~text
F(X,m)=g_DA(X;m)-chi X+nu,
~~~

one has

~~~text
F_X=-(s+chi)=-q/Delta.
~~~

The phrase "fold boundary" can be made fully nondegenerate. With the
notation of EXT-02,

~~~text
H_X=1/ell^2+1/d^2-1/u^2,
H_X-H^2=2(u-d)(ell+u)/(d ell u^2)>0.
~~~

At `q=0`, `F_X=0`, while

~~~text
F_m=-Q/d != 0,
F_XX=g_DA''(X)=-Q(H_X-H^2)<0.
~~~

Hence `q=0` is a genuine nondegenerate saddle-node/fold with `m` as the
unfolding parameter (whenever the remaining positive-coexistence
conditions hold).

## 6. EXT-05 — exact Allee sensitivity and required fix

Implicit differentiation gives, without any assumption on the sign of
chi beyond strict-P,

~~~text
dX/dm=-Q/[d(s+chi)]<0.
~~~

The current theorem proves `ds/dm<0` from the sufficient condition
`chi>=0`. That condition is not needed. Since `s=QH`, exact
differentiation gives

~~~text
ds/dm
=-Q/[d(s+chi)]
  * [Q H_X+s/d+chi(H+1/d)].
~~~

This formula also gives the unrestricted exact sign criterion:

~~~text
ds/dm<0
iff
(s+chi)[Q H_X+s/d+chi(H+1/d)]>0.
~~~

On the positive strict-P stratum, `chi>-s`. Since `H+1/d>0`,

~~~text
Q H_X+s/d+chi(H+1/d)
>
Q H_X+s/d-s(H+1/d)
=Q(H_X-H^2)
>0.
~~~

Therefore the exact strengthened conclusion is

~~~text
Q>0, s>0, s+chi>0, m>-a, 0<m<X<K
  ==> dX/dm<0 and ds/dm<0.
~~~

In particular, the sign persists for negative chi. A fully biological
exact witness is

~~~text
a=m=1, X=2, K=21/10, r=54,
q1=q2=h=1,
c1=c2=e1=e3=1/10, e2=9/10,
Y=57/70, Z=3/70,
mu1=53/700, mu2=657/350.
~~~

Here

~~~text
Q=6/7, H=28/3, s=8, chi=-79/11,
s+chi=9/11>0,
dX/dm=-22/21,
ds/dm=-9362/441<0.
~~~

This is not a counterexample to the theorem; it is a counterexample to
the necessity of its extra sufficient hypothesis. Recommended fix:
replace the `chi>=0` proof in Section 9 with the strict-P argument above.

## 7. EXT-06 — unique and transverse Cain crossing

Expanding

~~~text
T1=(sqrt(1+A0t)+sqrt(1+B0t)+sqrt(C0))^2
~~~

gives exactly the displayed `G1(t)`. Its endpoint data are

~~~text
G1(0)=-4-4sqrt(C0)<0,
lim_(t->infinity) G1(t)/t=E0-2sqrt(A0B0).
~~~

Moreover,

~~~text
d^2/dt^2 sqrt[(1+A0t)(1+B0t)]
=-(A0-B0)^2/
  [4(1+A0t)^(3/2)(1+B0t)^(3/2)],
~~~

and each individual square-root term is strictly concave. Hence `G1`
is strictly convex for all positive `A0,B0,C0` (also when `A0=B0`).

If `E0<=2sqrt(A0B0)`, the derivative of the convex function cannot
become positive enough to produce a positive root; at equality the
negative `sqrt(t)` terms force `G1(t)->-infinity`. If
`E0>2sqrt(A0B0)`, the positive asymptotic slope and negative initial
value give one root, and strict convexity gives uniqueness. At that root,

~~~text
G1'(t_H)
>= [G1(t_H)-G1(0)]/t_H
= (4+4sqrt(C0))/t_H>0.
~~~

Thus the crossing condition is iff and the stated transversality bound
is correct.

## 8. EXT-07 — prescribed-`m0` fractional-only transition

For prescribed `t0>0`, the displayed definition of `E0` makes
`G1(t0)=0` identically. It also satisfies

~~~text
E0>2sqrt(A0B0),
~~~

because
`sqrt[(1+A0t0)(1+B0t0)]>sqrt(A0B0)t0` and all remaining numerator
terms are positive.

At `s0=1/t0`, the EXT-01 target has

~~~text
beta12=1+A0t0,
beta13=1+B0t0,
beta23=C0,
R=E0t0.
~~~

Thus the joint EXT-01 choice (not a variation of one efficiency in
isolation) realizes exactly the desired path constants. EXT-02 then sets
`s=s0` at any selected `m0`. After this one-time construction,
`r,a,K,q1,q2,e_i,mu_i,c_i,h` are all fixed; only `m` varies.

EXT-05 gives `dt/dm>0`, and EXT-06 gives the unique transverse Cain
crossing. Positivity and strict-P persist locally by the IFT. On the
`m>m0` side, `kappa>T1` immediately, so classical D-stability is lost.
At `m0`:

- if `alpha>2/3`, exact C-10 gives
  `T1(beta)<T_alpha(beta)`; continuity preserves
  `kappa<T_alpha(beta)` on a sufficiently short right interval;
- if `alpha<=2/3`, strict-P plus Kellogg gives fractional D-stability on
  that interval.

C-11 is not used in either implication. Near `alpha=1` the right
interval may become small but remains nonempty for every fixed
`alpha<1`; near `2/3` there is no hidden gap, and at `2/3` the Kellogg
case applies.

## 9. Two-equilibrium adversarial check

Two positive coexistence equilibria are possible in this model. A random
falsification search found, for example (rounded),

~~~text
a=.114338, m=.241808, K=5.382673, r=.308763,
q1=.413841, q2=.165336,
c1=.714772, c2=2.485513, h=.120101,
e1=.120616, e2=.317749, e3=.609917,
mu1=.006071, mu2=.001283,
~~~

two feasible positive equilibria with prey coordinates approximately
`0.246823` and `3.400173`. The first has `s<0`; the second has `s>0` and
`s+chi>0`.

This does not invalidate any audited theorem. EXT-02 constructs a
specified equilibrium, while EXT-03 and EXT-07 explicitly use its local
smooth branch. Neither theorem asserts global uniqueness. Manuscript
wording must continue to say "a positive coexistence equilibrium" or
"the constructed branch", not "the unique equilibrium".

## 10. EXT-08 — dependency and circularity graph

~~~text
elementary determinant/minor algebra
  |--> EXT-01 invariant realization
  |--> EXT-04 strict-P identity/fold
  |--> EXT-06 path formula/convex crossing
  |
double-Allee calculus
  |--> EXT-02 quantified embedding
  |--> EXT-05 sensitivity
  |
EXT-01 + EXT-02
  |--> constructed biological base point
          |
          + C-10 exact high-order classification
          + Cain classical threshold
          + Kellogg low-order wedge
          + C-15 threshold smoothness/continuity
          + IFT in the state variables
          |
          |--> EXT-03 full-dimensional open region
          |
EXT-01 + EXT-02 + EXT-05 + EXT-06
  + C-10/Cain (high order)
  + Kellogg (low order)
  + IFT/local continuity
  |--> EXT-07 prescribed-m0 transition

Kolmogorov orbit lemma
  |--> transfer B <-> J in EXT-03 and EXT-07
~~~

Precise external-result roles:

- **C-10:** necessary-and-sufficient high-order fractional threshold and
  the exact fractional-only band; it is load-bearing in EXT-03/07.
- **C-15:** supplies unique-optimizer smoothness of `T_alpha`; useful for
  the openness/continuity statement. Its matrix realizability theorem is
  not used because EXT-01 supplies a direct ecological realization.
- **Cain:** exact classical `T1` boundary and therefore the meaning of
  `kappa>T1` and of the crossing in EXT-03/06/07.
- **Kellogg:** the low-order (`alpha<=2/3`) implication strict-P implies
  robust Matignon stability in EXT-03/07.
- **IFT:** continues the full biological equilibrium in EXT-03 and the
  local `m` branch in EXT-05/07.
- **C-07:** used only in the separate two-dimensional consistency check,
  not in EXT-01--EXT-07.
- **C-11:** not load-bearing here and never replaces exact C-10.

There is no circularity. C-10 and C-15 are matrix results established
without the Double-Allee construction; EXT-01/02 then realize points to
which those results are applied. C-15 depends on the C-10 objective, but
no argument sends an ecological conclusion back into C-10 or C-15.

## 11. Required adversarial conclusions

1. **EXT-03 openness:** no counterexample. The nonsingular full state
   Jacobian and independent 14-coordinate IFT eliminate the
   lower-dimensional-family objection.
2. **EXT-05 with `chi<0`:** no strict-P counterexample exists; the exact
   inequality proves both sensitivities remain negative. The rational
   biological witness above confirms that the strengthened regime is
   nonempty.
3. **Embedding bounds:** `Q1/Q2` and `H_A>0` are always compatible because
   `H_A->infinity` as `K->X+` and every active `Qbar` is positive.
4. **Efficiencies:** `e1=e3=eta`, `e2=eta^2/tau^2` proves compatibility of
   `e1e3>e2` with all `e_i in (0,1)`.
5. **Multiple equilibria:** possible, but harmless because every theorem
   is branch-local and asserts existence rather than uniqueness.
6. **Order endpoints:** no hidden discontinuity; the high-order band is
   positive for each `alpha<1`, diverges on approach to `2/3+`, and joins
   the Kellogg regime at and below `2/3`.

## 12. Verification record

Independent SymPy reductions returned zero residual for
`q-Delta(s+chi)`, derived the displayed exact `ds/dm` factorization and
`H_X-H^2`, recovered the finite limit of `r`, and recovered both the
second derivative and asymptotic slope used in EXT-06. The repository
suite passes with the local package exposed as intended:

~~~text
PYTHONPATH=src pytest -q
39 passed
~~~

`EXTERNAL_AUDIT_PASS_WITH_FIXES`
