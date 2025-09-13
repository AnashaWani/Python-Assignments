### BOOLEAN MASKING ###


import numpy as np

arr = np.array([3,6,9,12,15])
selected = arr[arr>8]                             # selcting elements satisfying the condition #

print("Numbers in array greater than 8 :\n",selected)