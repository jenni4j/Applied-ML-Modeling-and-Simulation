import numpy as np
nSpace = 100 # of spatial grid points
nTime = 100 # of time steps

ux_scheme = 'left' #choose 'left' or 'right' for type of discretiztion stencil

#timestepper so we know which integrator to use
# fe (forward Euler), be (backward Euler), rk2 (two stage Runge-Kutta), rk4 (four stage Runge-Kutta)

timestepper = 'fe'
x = np.linspace(0,1,nSpace+1)
dx = 1/nSpace
u0 = init(x)