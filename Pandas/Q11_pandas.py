### COUNTING VALUES ###


import pandas as pd

students = pd.read_csv("students.csv")

# calculating number of occurances of each row of the column #
g = students['Grade'].value_counts()

print(f"Number of times each grade occurs :\n{g}")