import numpy as np

def combinations(n, r):
    return (np.math.factorial(n)/np.math.factorial(n-r))

a = combinations(13, 4)
b = combinations(52, 4)
p = round(a*100/b,2)
print('The probability that all cards are cross ',p, '%')