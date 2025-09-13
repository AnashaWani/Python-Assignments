### PRACTICAL - WEATHER DATASET ###


import pandas as pd

weather = pd.read_csv("weather.csv")
print(f"DataSet :\n{weather}")

temp = weather['Temp']
avg_temp = temp.mean()
print("Average temperature :\n",avg_temp)

rainfall = weather['Rainfall']
max_day = rainfall.idxmax()                             # calcuting index of max value of rainfall   #
max_rainfall = weather.loc[max_day, 'Day']              # calcuting the day on index of max rainfall #
print("Day with maximum rainfall :\n",max_rainfall)

days = weather[weather['Temp']>30]
print(f"Days where temperature >30 :\n{days}")
