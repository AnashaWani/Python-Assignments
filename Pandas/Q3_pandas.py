### SELECTING COLUMNS ###


import pandas as pd

students = pd.read_csv("students.csv")

name_column = students['Name']          # df_name[column_name] will return the mentioned column #

print(f"Name Column of the Students DataFrame :\n{name_column}")