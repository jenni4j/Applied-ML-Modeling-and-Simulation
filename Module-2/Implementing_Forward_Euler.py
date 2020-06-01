# Script for checking implementation of ODE RHS and forward Euler
import numpy as np
import matplotlib.pyplot as plt


##Functions to implement
def ode_rhs(u,beta,kappa):
    s = u[0]
    i = u[1]
    r = u[2]
    dsdt = -beta*s*i
    didt = beta*s*i - kappa*i
    drdt = kappa*i
    dudt = [dsdt,didt,drdt]
    return dudt

def forwardEulerUpdate(u,dt,beta,kappa):
    u_next = u + ode_rhs(u,beta,kappa)*dt
    return u_next

##For checking implementation of ODE RHS and Forward Euler
i = 0.01
s = 1 - i
r = 0
u0 = [s,i,r]

beta = 0.5
kappa = 0.33

dudt = ode_rhs(u0, beta, kappa)


dsdt = dudt[0]
didt = dudt[1]
drdt = dudt[2]

dt = 1
u_check = np.zeros([3,3])
u_check[0,:] = u0

for t in range(1,2):
    u_now = u_check[t-1,:]
    u_next = forwardEulerUpdate(u_now,dt,beta,kappa)
    u_check[t,:] = u_next

##Generating plots for answering the multiple choice questions
i = 0.0001
s = 1 - i
r = 0
u0 = [s,i,r]

beta = 0.5
kappa = 0.33

dt = 1
T = np.arange(0,100,dt)

u = np.zeros([3,len(T)])
u[:,0] = u0

for t in range(1,len(T)):
    u[:,t] = forwardEulerUpdate(u[:,t-1],dt,beta,kappa)

plt.plot(T,u[0,:], label = 's(t) Approx')
plt.plot(T,u[1,:], label = 'i(t) Approx')
plt.plot(T,u[2,:], label = 'r(t) Approx')
plt.legend(loc='best')
plt.show()

