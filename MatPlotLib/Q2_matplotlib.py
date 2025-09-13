### ADDING LABELS AND TITLE ###


import matplotlib.pyplot as plt

weeks = [1,2,3,4,5]
height = [5,9,14,20,27]

plt.xlabel("Weeks")                                  # labelling x-axis                   #
plt.ylabel("Height (cm)")                            # labelling y-axis                   #
plt.title("Plant Growth Over 5 Weeks")               # setting a title for the graph/plot #

plt.plot(weeks, height)
plt.show()