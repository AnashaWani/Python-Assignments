### PRACTICAL - STUDENT MARKS ###


import numpy as np

marks = np.array([45, 67, 89, 32, 76])

mean = np.mean(marks)
print("Average marks of the 5 students :\n", mean)

above_avg = marks[marks>mean]                      # selecting marks according to the condition #
print("Above average marks:\n",above_avg)