

nSpace = 100
nTime = 100

ux_scheme = 'left'
timestepper = 'fe'

x = linspace(0,1,nSpace+1)
dx = 1/nSpace
u0 = init(x)

c = 0.5
k = 0.00005

A = getMatrix(nSpace,ux_scheme)

tic
[u,cost] = integrate(u0,A,timestepper,nTime)
toc

calcErr = getError(x,u)
