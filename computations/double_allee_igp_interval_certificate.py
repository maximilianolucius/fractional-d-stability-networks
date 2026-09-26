#!/usr/bin/env python3
"""Interval certificate for the double-Allee IGP example.

Requires mpmath.  This is an independent certified check of one interior
fractional-only point.  The theorem itself remains analytic.

Certificate logic at alpha=0.9, m=0.21:
  1. X,Y,Z intervals are strictly positive.
  2. kappa-T1 > 0, hence the reduced matrix is not Hurwitz D-stable.
  3. Phi-rho_alpha > 0, where Phi=T1/kappa and
     rho_alpha=(1-2 cos(alpha*pi/2))^2.
     By C-11 this is a sufficient all-positive-diagonal Matignon certificate.
"""

from mpmath import iv

iv.dps = 50

alpha = iv.mpf("0.9")
lam = iv.mpf("0.05")
eta = iv.mpf("0.5")
E_norm = iv.mpf("14")

tau = (E_norm + iv.sqrt(E_norm**2 + 4)) / 2

e1 = eta
e3 = eta
e2 = eta**2 / tau**2

c1 = lam
c2 = lam
s0 = lam

q1 = lam * iv.sqrt(1 / e1)
q2 = lam * iv.sqrt(1 / e2)
h = lam * iv.sqrt(1 / e3)

X0 = iv.mpf("1")
m0 = iv.mpf("0.2")
a = iv.mpf("0.5")
K = iv.mpf("1.1")

H0 = 1 / (K - X0) - 1 / (X0 - m0) + 1 / (X0 + a)
Q0 = s0 / H0

Y0 = Q0 / (2 * q1)
Z0 = Q0 / (2 * q2)

mu1 = e1 * q1 * X0 - c1 * Y0 - h * Z0
mu2 = e2 * q2 * X0 + e3 * h * Y0 - c2 * Z0

r = Q0 * (X0 + a) / ((1 - X0 / K) * (X0 - m0))

Delta = c1 * c2 + e3 * h**2

chi = (
    e1 * c2 * q1**2
    + e2 * c1 * q2**2
    + h * q1 * q2 * (e1 * e3 - e2)
) / Delta

nu = (
    mu1 * (q1 * c2 + q2 * e3 * h)
    + mu2 * (q2 * c1 - q1 * h)
) / Delta

m = iv.mpf("0.21")

Aq = r + K * chi
Bq = r * (K + m) - K * chi * a + K * nu
Cq = r * K * m - K * nu * a

disc = Bq**2 - 4 * Aq * Cq
X = (Bq + iv.sqrt(disc)) / (2 * Aq)

A1 = e1 * q1 * X - mu1
A2 = e2 * q2 * X - mu2
Y = (c2 * A1 - h * A2) / Delta
Z = (e3 * h * A1 + c1 * A2) / Delta

g = r / (X + a) * (1 - X / K) * (X - m)
gp = g * (-1 / (K - X) + 1 / (X - m) - 1 / (X + a))
s = -gp

beta12 = 1 + e1 * q1**2 / (s * c1)
beta13 = 1 + e2 * q2**2 / (s * c2)
beta23 = 1 + e3 * h**2 / (c1 * c2)

kappa = (
    beta12
    + beta13
    + beta23
    - 2
    + h * q1 * q2 * (e1 * e3 - e2) / (s * c1 * c2)
)

T1 = (iv.sqrt(beta12) + iv.sqrt(beta13) + iv.sqrt(beta23)) ** 2

Phi = T1 / kappa
theta = alpha * iv.pi / 2
rho_alpha = (1 - 2 * iv.cos(theta)) ** 2

print("X =", X)
print("Y =", Y)
print("Z =", Z)
print("s =", s)
print("beta12 =", beta12)
print("beta13 =", beta13)
print("beta23 =", beta23)
print("kappa =", kappa)
print("T1 =", T1)
print("kappa-T1 =", kappa - T1)
print("Phi =", Phi)
print("rho_alpha =", rho_alpha)
print("Phi-rho_alpha =", Phi - rho_alpha)
