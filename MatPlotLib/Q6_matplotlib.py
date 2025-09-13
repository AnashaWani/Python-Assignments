### PLOTTING PIE CHART ###


import matplotlib.pyplot as plt

companies = ["Apple","Samsung","Xiaomi","Others"]
share = [30,25,20,25]

# plotting pie chart with labels as companies #
plt.pie(share, labels=companies, autopct="%1.1f%%")

plt.title("Market Share of 4 Companies")
plt.show()