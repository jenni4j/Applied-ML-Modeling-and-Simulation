import numpy as np
import matplotlib.pyplot as plt


N = 200

h = 2*pi/N
x = linspace(0,2*pi,N+1)'
u = sin(x)

A = zeros(N,N)

for i in range(1,N):
    A[i,i] = 1/h

A(1,N) = -1/h

for i in range(1,N):
    A(i,i-1) = -1/h

spy(A(1:10,1:10))

dudx = A*u




