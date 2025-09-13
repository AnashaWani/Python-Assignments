### ADDING NEW COLUMN ###


import pandas as pd

students = pd.read_csv("students.csv")

# generating new column while applying condition for data #
students['Passed'] = students['Grade'].apply(lambda grade : "Yes" if grade>=8 else "No")

print(f"Students DataFrame with Passed column :\n{students}")