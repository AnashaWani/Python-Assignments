### PLOTTING HISTOGRAM ###


import matplotlib.pyplot as plt

ages = [12,13,14,15,16,15,14,13,16,12,15,14,13]

# plotting histogram of dataset #
plt.hist(ages)

plt.xlabel("Ages")
plt.ylabel("No. of entries of each age")
plt.title("Histogram of Ages")

plt.show()