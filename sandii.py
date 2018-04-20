import numpy as np
import matplotlib.pyplot as plt

def iterate(n, f_i, N, sig, R):
    '''
    One iteration of the sand ii algorithm
    '''
    
    for i in range(n):
        b = (N**2 / sig**2)
        a = ((R * f_i) / np.sum(R * f_i))
        W = a.T * b
        c = np.sum(W * np.log(N / np.sum(R * f_i)), axis=1) / np.sum(W, axis=1)
        f_i = f_i * np.exp(c)
    return f_i


n = 1000
R = np.array([[1, 2, 3, 2], [3, 2, 1, 1]])
f_i = np.array([1, 1, 1, 1])
N = np.array([2, 2.5])
sig = np.array([0.5, 0.5])

sol = iterate(n, f_i, N, sig, R)
print(sol)
print(R.dot(sol))
    