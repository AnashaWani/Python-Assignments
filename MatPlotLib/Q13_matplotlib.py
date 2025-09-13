### VISUALIZING MONTHLY SALES WITH A BAR CHART ###


import matplotlib.pyplot as plt

months = ["Jan","Feb","Mar","Apr","May"]
sales = [1000,1200,900,1500,1100]

plt.bar(months,sales)
plt.xlabel("Months")
plt.ylabel("Sales")
plt.title("Monthly Sales")

plt.show()