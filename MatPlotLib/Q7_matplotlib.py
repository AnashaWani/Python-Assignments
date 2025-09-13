### PLOTTING HEIGHT VS WEIGHT OF STUDENTS ###


import matplotlib.pyplot as plt

height = [150,155,160,165,170]
weight = [45,50,55,65,70]

plt.xlabel("Height")
plt.ylabel("Weight")
plt.title("Height VS Weight of Students ")

plt.plot(height,weight)
plt.show()