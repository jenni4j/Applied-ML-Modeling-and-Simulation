import numpy as np

def grad(x):
    g1 = 1/(1-x(1)-x(2))-1/x(1)
    g2 = 1/(1-x(1)-x(2))-1/x(2)
    g = [g1,g2]
    return g

def grad_descent(g, alpha, x0, max_iter, grad_tol):
    x = x0
    grad = g(x)

    x_iter = x0
    g_iter = np.linalg.norm(grad)

    counter = 1

    while(np.linalg.norm(grad) > grad_tol && counter < max_iter):
        x = x - alpha*grad
        x_iter = [x_iter, x]
        grad = g(x)
        g_iter = [g_iter, np.linalg.norm(grad)]
        counter = counter + 1
        