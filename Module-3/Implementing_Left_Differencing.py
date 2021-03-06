import numpy as np
import matplotlib.pyplot as plt

#set up grid and compute state vector
N = 200
h = 2*np.pi/N
x = np.transpose(np.linspace(0,2*np.pi,N+1))
x = x[0:N]
u = np.sin(x)

A = np.zeros((N,N))

#loop through and replace appropriate entries with -1/h
for i in range(0,N):
    A[i,i] = 1/h

A[0,N-1] = -1/h

for i in range(1,N):
    A[i,i-1] = -1/h

#compute derivative
dudx = np.dot(A,u)

plt.plot(x,np.cos(x),label = 'Truth')
plt.plot(x,dudx,label = 'Approximation')
plt.legend(loc='best')
plt.xlabel('x')
plt.ylabel('dudx')
plt.show()





