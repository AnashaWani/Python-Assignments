### PLOTTING SUBPLOTS ###


import matplotlib.pyplot as plt

students = ["A","B","C","D","E"]
math = [78,55,89,92,66]
science = [88,62,79,95,70]

# subplot : (rows,columns,position) #
plt.subplot(1,2,1)

plt.bar(students, math, color="yellow")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Math Marks")

plt.subplot(1,2,2)

plt.bar(students, science, color="pink")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Science Marks")

plt.tight_layout()                                   # to make sure the charts don't overlap #

plt.show()