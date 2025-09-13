### PLOTTING BAR CHART ###


import matplotlib.pyplot as plt

students = ["A","B","C","D","E"]
marks = [78,55,89,92,66]

# plotting bar chart as (x,y) on corresponding axis #
plt.bar(students,marks)

plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Marks of 5 Students")

plt.show()