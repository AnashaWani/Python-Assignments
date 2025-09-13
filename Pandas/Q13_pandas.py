### PRACTICAL - STUDENT MARKS ###


import pandas as pd

marks = pd.read_csv("markss.csv")
print(f"DataSet :\n{marks}")

mark = marks[['Math','Science','English']]
average = mark.mean()                                # calculating the average marks for each column #

print(f"Average marks for each subject :\n{average}")
