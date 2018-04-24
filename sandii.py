import numpy as np
from numpy.linalg import norm


def iterate(f_i, N, sig, R, max_iter=1000, tol=1E-4):
    '''
    One iteration of the sand ii algorithm
    '''
    l_f = len(f_i)
    l_k = len(N)
    iteration = 0
    N0 = np.sum(R * f_i, axis=1)
    error = norm(N0 - N, ord=2)
    while iteration < max_iter and error > tol:
        f_i_new = f_i * 0
        for i in range(l_f):
            bot = 0
            top = 0
            for k in range(l_k):
                # bot
                c = (N[k]**2 / sig[k]**2)
                a = (R[k][i] * f_i[i])
                b = np.sum(R[k] * f_i)
                bot += (a / b) * c
                # top
                log_term = np.log(N[k] / b)
                top += ((a / b) * c) * log_term
            coef = np.exp(top / bot)
            f_i_new[i] = f_i[i] * coef
        f_i = f_i_new
        N0 = np.sum(R * f_i, axis=1)
        error = norm(N0 - N, ord=2)
        iteration += 1
    return f_i
