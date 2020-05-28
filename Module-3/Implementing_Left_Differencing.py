N = 200

h = 2*pi/N
x = linspace(0,2*pi,N+1)'
u = sin(x)

A = zeros(N,N)

for i in range(1,N):
    A[i,i] = 1/h

