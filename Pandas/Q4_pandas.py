### SELECTING ROWS ###


import pandas as pd

students = pd.read_csv("students.csv")

first_row = students.head(1)        # df_name.head(row_number) will return mentioned row from top #

print(f"First row of the Students DataFrame :\n{first_row}")