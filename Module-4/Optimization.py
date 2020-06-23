def grad(x):
    g1 = 1/(1-x(1)-x(2))-1/x(1)
    g2 = 1/(1-x(1)-x(2))-1/x(2)
    g = [g1,g2]
    return g

def grad_descent(g, alpha, x0, max_iter, grad_tol):
    x = x0
    grad = g(x)

    x_iter = x0
    g_iter = norm(grad)

    counter = 1

    