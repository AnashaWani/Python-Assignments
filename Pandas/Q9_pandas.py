### HANDLING MISSING VALUES ###


import pandas as pd

marks = pd.read_csv("marks.csv")

fill_mm = marks.fillna(0)              # filling missing marks/values of dataframe with 0 #

print(f"Marks DataFrame :\n{marks}")
print(f"Marks DataFrame after filling missing marks :\n{fill_mm}")