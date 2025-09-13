### RESHAPING ARRAY ###


import numpy as np

arr = np.array([1,2,3,4,5,6])
print("Original array :\n", arr)

# reshaping array in new order #
new = arr.reshape(2,3)
print("Reshaped array :\n", new)