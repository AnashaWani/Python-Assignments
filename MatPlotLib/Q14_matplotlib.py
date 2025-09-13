### PLOTTING WEATHER DATASET AS GRAPH ###


import matplotlib.pyplot as plt

days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
temp = [22,24,20,23,25,27,26]

plt.plot(days,temp)
plt.xlabel("Days")
plt.ylabel("Temperature (°C)")
plt.title("Temperature across 7 Days")

plt.show()