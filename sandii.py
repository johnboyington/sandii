import numpy as np
import matplotlib.pyplot as plt

def iterate(n, f_i, N, sig, R):
    '''
    One iteration of the sand ii algorithm
    '''
    l_f = len(f_i)
    l_k = len(N)
    for iteration in range(n):
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
    return f_i


n = 100
R = np.array([[1, 2, 3, 2], [3, 2, 1, 1]], dtype=np.float64)
f_i = np.array([1, 1, 1, 1], dtype=np.float64)
N = np.array([2, 2.5], dtype=np.float64)
sig = np.array([0.5, 0.5], dtype=np.float64)

sol = iterate(n, f_i, N, sig, R)
print(sol)
print(R.dot(sol))
    