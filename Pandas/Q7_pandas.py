### FINDING DISCRIPTIVE STATISTICS ###


import pandas as pd

students = pd.read_csv("students.csv")

# selecting age column and calculating its mean value #
age = students['Age']
mean_age = age.mean()

# selecting grade column and looking for its maximum value #
grade = students['Grade']
max_grade = grade.max()

print("Mean age in Students DataFrame :\n",mean_age)
print("Maximum grade in Students DataFrame :\n",max_grade)