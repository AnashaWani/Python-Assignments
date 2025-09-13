### PLOTTING A SIMPLE LINE CHART ###


# importing 'matplotlib' library ( for visualization ) #
import matplotlib.pyplot as plt

# datasets as lists #
weeks = [1,2,3,4,5]
height = [5,9,14,20,27]

# plotting line chart as (x,y) on corresponding axis #
plt.plot(weeks, height)

# displaying the plot/graph #
plt.show()