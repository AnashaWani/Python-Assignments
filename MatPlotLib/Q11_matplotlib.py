### READING CSV FILE AND PLOTTING BAR CHART ###


import pandas as pd
import matplotlib.pyplot as plt

students = pd.read_csv("studentss.csv")
name = students['Name']
marks = students['Marks']

plt.bar(name,marks)
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Marks Obtained by Students")

plt.show()