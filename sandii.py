import numpy as np
import matplotlib.pyplot as plt

def iterate(n, f_i, N, sig, R):
    '''
    One iteration of the sand ii algorithm
    '''
    l_f = len(f_i)
    l_k = len(N)
    for iteration in range(n):
        for i in range(l_f):
            bot = 0
            top = 0
            for k in range(l_k):
                # bot
                c = (N[k]**2 / sig[k]**2)
                a = (R[k] * f_i)
                b = np.sum(R[k] * f_i)
                bot += (a[k] / b) * c
                # top
                log_term = np.log(N[k] / b)
                top += ((a[k] / b) * c) * log_term
            c = np.exp(top / bot)
            print(c)
            f_i[i] *= c
    return f_i


n = 10
R = np.array([[1, 2, 3, 2], [3, 2, 1, 1]])
f_i = np.array([1, 1, 1, 1])
N = np.array([2, 2.5])
sig = np.array([0.5, 0.5])

sol = iterate(n, f_i, N, sig, R)
print(sol)
print(R.dot(sol))
    