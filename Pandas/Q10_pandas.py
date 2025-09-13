### BASICS OF GROUPBY ###


import pandas as pd

students = pd.read_csv("students.csv")

grade = students.groupby('Grade')            # grouping values by grade                    #
size = grade.size()                          # .size calculates size of each row of column #

print(f"Number of students in each grade :\n{size}")