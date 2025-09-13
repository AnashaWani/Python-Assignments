### STUDENTS MARKS DATASET AS LINE CHART ###


import matplotlib.pyplot as plt

subjects = ["Math","Science","English","History","Comptuter"]
marks = [78,85,66,74,90]

plt.plot(subjects,marks)
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.title("Student's Marks across Subjects")

plt.show()