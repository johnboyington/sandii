from sandii import iterate
import numpy as np
import matplotlib.pyplot as plt


test = 1

if test == 0:
    R = np.array([[1, 2, 3, 2], [3, 2, 1, 1]], dtype=np.float64)
    f_i = np.array([1, 1, 1, 1], dtype=np.float64)
    N = np.array([2, 2.5], dtype=np.float64)
    sig = np.array([0.5, 0.5], dtype=np.float64)
    
    sol = iterate(f_i, N, sig, R)
    print(sol)
    print(R.dot(sol))

if test == 1:
    solutions = []
    
    R = np.array([[1, 2, 3, 2], [3, 2, 1, 1]], dtype=np.float64)
    f_i = np.array([1, 1, 1, 1], dtype=np.float64)
    N = np.array([2, 2.5], dtype=np.float64)
    sig = np.array([0.5, 0.5], dtype=np.float64)
    
    ns = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 20, 25, 50, 100]
    
    for i, it in enumerate(ns):
        solutions.append((iterate(f_i, N, sig, R, max_iter=it), str(1 - i/len(ns))))
    
    plt.figure(0)
    for sol in solutions:
        plt.plot(sol[0], color=sol[1])
    