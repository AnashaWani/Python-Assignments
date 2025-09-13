### STACKING ARRAYS ###


import numpy as np

arr1 = np.array([1,2])
arr2 = np.array([3,4])
print("First array :\n", arr1, "\nSecond array :\n", arr2)

# creating new array by vertically stacking other two #
new = np.vstack([arr1,arr2])

print("Array after stacking vertically :\n", new)