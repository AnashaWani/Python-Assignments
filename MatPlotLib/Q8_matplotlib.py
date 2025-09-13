### CUSTOMIZING COLORS AND STYLES ###


import matplotlib.pyplot as plt

weeks = [1,2,3,4,5]

# creating lists for quadratic and cubic functions of dataset #
x_2 = [x**2 for x in weeks]
x_3 = [x**3 for x in weeks]

plt.plot(weeks, x_2, 'r--', label="x²")                # r-- creates red dashed line  #
plt.plot(weeks, x_3, 'g:', label="x³")                 # g: creates green dotted line #

plt.xlabel("weeks")
plt.ylabel("x")
plt.title("Recreating Q3 with x² and x³")

plt.legend()
plt.show()