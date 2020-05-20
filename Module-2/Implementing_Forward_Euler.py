# Script for checking implementation of ODE RHS and forward Euler
import numpy as np

i = 0.01
s = 1 - i
r = 0
u0 = [s;i;r]

beta = 1/2 
kappa = 1/3

dudt = ode_rhs(u0, beta, kappa)

dsdt = dudt(1)
didt = dudt(2)
drdt = dudt(3)

dt = 1
u_check = np.zeros([3,51])
u_check[:,0] = u0

for t in range(1,51):
    u_now = u_check[:,t-1]
    u_next = forwardEulerUpdate(u_now,dt,beta,kappa)
    u_check[:,t] = u_next


