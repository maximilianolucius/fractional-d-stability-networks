#!/usr/bin/env python3
"""Round-1 nonlinear Caputo order sweep for Mathematics manuscript 4633263.

Reproduces Table "Additional nonlinear Caputo simulations" using the submitted
W2-A table entries and selected row-response rates, with Adams--Bashforth--
Moulton PECE discretization. Requirements: numpy, scipy, numba.
Output: relative distance to coexistence at t=180, two time steps.
Finite-time numerical experiment only; not a spectral stability certificate.
"""
import math
import numpy as np
from numba import njit

# Decimal values as reported in the submitted W2-A table:
p = np.array([
  0.229, 1.4913425743, 7.8104480113, 0.511,
  0.5121684678, 3.2338213736, 0.1404219270,
  0.065, 0.0509, 0.773, 0.01404592165, 0.773,
  0.3178535346, 0.1209173583
], dtype=np.float64)
rate = np.array([0.1810024, 2.6060229, 14.0412352])
a,K,r,m,q1,q2,h,c1,c2,e1,e2,e3,mu1,mu2=p
delta=c1*c2+e3*h*h
Y=(c2*(e1*q1-mu1)-h*(e2*q2-mu2))/delta
Z=(e3*h*(e1*q1-mu1)+c1*(e2*q2-mu2))/delta
ustar=np.array([1.0,Y,Z])
initial=ustar*np.array([1.001,0.999,1.001])

@njit
def rhs(u,p,rate):
    a,K,r,m,q1,q2,h,c1,c2,e1,e2,e3,mu1,mu2=p
    x,y,z=u
    g=r/(x+a)*(1-x/K)*(x-m)
    return rate*np.array([
        x*(g-q1*y-q2*z),
        y*(e1*q1*x-mu1-c1*y-h*z),
        z*(e2*q2*x+e3*h*y-mu2-c2*z)
    ])

@njit
def pece(alpha,step,N,x0,p,rate):
    U=np.zeros((N+1,3)); FF=np.zeros((N+1,3))
    U[0]=x0; FF[0]=rhs(x0,p,rate)
    predc=step**alpha/math.gamma(alpha+1.0)
    corr=step**alpha/math.gamma(alpha+2.0)
    w=np.empty(N+1); ac=np.empty(N+1)
    for k in range(N+1):
        w[k]=(k+1)**alpha-k**alpha
        if k>0:
            ac[k]=(k+1)**(alpha+1)+(k-1)**(alpha+1)-2*k**(alpha+1)
    for n in range(N):
        pp=x0.copy()
        for j in range(n+1):
            pp+=predc*w[n-j]*FF[j]
        val=x0+corr*rhs(pp,p,rate)
        val+=corr*(n**(alpha+1)-(n-alpha)*(n+1)**alpha)*FF[0]
        for j in range(1,n+1):
            val+=corr*ac[n+1-j]*FF[j]
        U[n+1]=val
        FF[n+1]=rhs(val,p,rate)
    return U

if __name__ == "__main__":
    print("Equilibrium:",ustar)
    print("Initial relative perturbation:",initial/ustar-1)
    for alpha in (0.900,0.930,0.945,0.950,0.955,0.965):
        for step in (0.04,0.02):
            sol=pece(alpha,step,int(round(180/step)),initial,p,rate)
            dist=np.linalg.norm(sol[-1]/ustar-1)
            print(f"alpha={alpha:.3f}, step={step:.2f}, d(180)={dist:.9g}")
