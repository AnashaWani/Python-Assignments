### PRACTICAL - TEMPERATURE ANALYSIS ###


import numpy as np

array = np.array([30,32,29,35,28,33,31])

highest = np.max(array)
lowest = np.min(array)

new = array.reshape(7,1)

print("Highest temperature of the week :\n", highest)
print("Lowest temperature of the week :\n", lowest)
print("Original array :\n", array, "\nReshaped array :\n", new)