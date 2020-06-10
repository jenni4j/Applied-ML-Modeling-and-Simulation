import numpy as np
import matplotlib.pyplot as plt


N = 200
#set up grid and compute state vector
h = 2*np.pi/N
x = np.transpose(np.linspace(0,2*np.pi,N))
u = np.sin(x)

A = np.zeros((N,N))

#loop through and replace appropriate entries with -1/h
for i in range(0,N):
    A[i,i] = 1/h

A[1,N-1] = -1/h

for i in range(1,N):
    A[i,i-1] = -1/h

#compute derivative
dudx = A*u

plt.plot(x,np.cos(x),'k')
plt.plot(x,dudx)
plt.legend(loc='best')
plt.show()





