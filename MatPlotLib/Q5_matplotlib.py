### PLOTTING HORIZONTAL BAR CHART ###


import matplotlib.pyplot as plt

students = ["A","B","C","D","E"]
marks = [78,55,89,92,66]

# plotting horizontal bar chart as (x,y) on corresponding axis #
plt.barh(students,marks)

plt.xlabel("Marks")
plt.ylabel("Students")
plt.title("Marks of 5 Students")

plt.show()