### GENERATING RANDOM NUMBERS ###


import numpy as np

np.random.seed(42)                           # for reproducibility : same sequence of random numbers #
array = np.random.randint(1,21,size=5)       # generating random numbers of (low,high-1,size)        #

print("5 random numbers between 1 and 20 :\n", array)
