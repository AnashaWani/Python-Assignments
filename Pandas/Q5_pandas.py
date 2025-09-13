### FILTERING ROWS ###


import pandas as pd

students = pd.read_csv("students.csv")

select_g7 = students[students['Grade']>7]      # selecting data from dataframe satisfying the condition #

print(f"Students with Grade>7 :\n{select_g7['Name']}")