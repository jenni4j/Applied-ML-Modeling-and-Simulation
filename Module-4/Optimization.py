def grad(x):
    g1 = 1/(1-x(1)-x(2))-1/x(1)
    g2 = 1/(1-x(1)-x(2))-1/x(2)
    g = [g1,g2]
    return g

