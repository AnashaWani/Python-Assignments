### CHECKING BASIC INFO OF DATAFRAME ###


import pandas as pd

students = pd.read_csv("students.csv")

shape = students.shape              # .shape returns (rows,columns)         #
columns = students.columns          # .columns returns list of column names #

print("Shape of the Students DataFrame :\n",shape)
print("Columns of the Students DataFrame :\n",columns)