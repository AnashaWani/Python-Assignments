### MINI-PROJECT : COMBINING CHARTS ###


import matplotlib.pyplot as plt

months = ["Jan","Feb","Mar","Apr","May"]
sales = [1000,1200,900,1500,1100]
companies = ["Apple","Samsung","Xiaomi","Others"]
share = [30,25,20,25]

# setting canvas size to fit graphs #
plt.figure(figsize=(12,8))

# showing sales trend over months with line chart #
plt.subplot(3,1,1)
plt.plot(months, sales, color="green")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.title("Sales Trend Over Months")

# showing percentage contribution with pie charts #
plt.subplot(3,1,2)
plt.pie(share, labels=companies, autopct="%1.1f%%")
plt.title("Percentage Contribution of Mobile Market Shares")
plt.axis("equal")

# comparing product sales with bar chart #
plt.subplot(3,1,3)
plt.bar(months, sales, color="purple")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.title("Comparison of Product Sales across Months")

plt.tight_layout()

plt.show()