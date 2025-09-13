### PLOTTING MULTIPLE LINES IN ONE GRAPH ###


import matplotlib.pyplot as plt

weeks = [1,2,3,4,5]
plant_A = [5,9,14,20,27]
plant_B = [4,8,12,18,25]

# setting individual labels for lines #
plt.plot(weeks, plant_A, label="Plant A")
plt.plot(weeks, plant_B, label="Plant B")

plt.xlabel("Weeks")
plt.ylabel("Height (cm)")
plt.title("Growth of Plants A & B over 5 Weeks")

plt.legend()                                          # displays the individual labels in plot #

plt.show()
