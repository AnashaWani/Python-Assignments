### SORTING VALUES ###


import pandas as pd

students = pd.read_csv("students.csv")

# sorting values in descending order by age #
age_d_order = students.sort_values(by="Age", ascending=False)

print(f"Sorting by descending value of age :\n{age_d_order}")