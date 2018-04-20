import numpy as np

def iterate(f_i, N, sig, R):
    '''
    One iteration of the sand ii algorithm
    '''
    
    W = ((R * f_i) / np.sum(R * f_i)) * (N**2 / sig**2)
    c = np.sum(W * np.log(N / np.sum(R * f_i))) / np.sum(W)
    return f_i * np.exp(c)
    