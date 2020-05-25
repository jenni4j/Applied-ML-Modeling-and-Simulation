# Script for checking implementation of ODE RHS and forward Euler
import numpy as np


##Functions to implement
def ode_rhs(u,beta,kappa):
    s = u[0]
    i = u[1]
    r = u[2]
    dsdt = 0
    didt = 0
    drdt = 0
    dudt = [dsdt,didt,drdt]
    return dudt

def forwardEulerUpdate(u,dt,beta,kappa):
    u_next = 0
    return u_next

##For checking implementation of ODE RHS and Forward Euler
i = 0.01
s = 1 - i
r = 0
u0 = [s,i,r]

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

##Generating plots for answering the multiple choice questions
i = 0.01
s = 1 - i
r = 0
u0 = [s,i,r]

beta = 1/2
kappa = 1/3

dt = 1
T = range(0,100,dt)

u = np.zeros(3,len(t))
u[:,0] = u0

for t = 1:len(T)
    u[:,t] = forwardEulerUpdate(u[:,t-1],dt,beta,kappa)


