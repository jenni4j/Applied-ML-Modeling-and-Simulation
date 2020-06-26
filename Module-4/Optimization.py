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


def f(x1, x2):
    return -1*log(1-x1-x2)-log(x1)-log(x2)

g1 = x1
g2 = x2

xt = [0.25,0.25]
g1_xt = g1(xt(1),xt(2))
g2_xt = g2(xt(1),xt(2))

grad = [g1(x1,x2),g2(x1,x2)]

#initial condition
x0 = [0.85,0.05]
alpha = 0.05

#run gradient descent
[x_gd,] = grad_descent(grad,alpha,x0)