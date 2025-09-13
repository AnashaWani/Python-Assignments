### IMPORTING PANDAS AND READING CSV FILE ###


# importing 'pandas' library (for data analysis and data manipulation) #
import pandas as pd

# reading data from CSV file into dataframe #
students = pd.read_csv("students.csv")

# printing the dataframe #
print(f"Students DataFrame :\n{students}")