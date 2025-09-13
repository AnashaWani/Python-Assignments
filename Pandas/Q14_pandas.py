### PRACTICAL - SALES DATASET ###


import pandas as pd

sales = pd.read_csv("sales.csv")
print(f"DataSet :\n{sales}")

product = sales.groupby('Product')

# adding grouped products #
grouped_products = product.sum()

# calculating total sales per product #
grouped_products['Total'] = grouped_products['Quantity'] * grouped_products['Price']

total_sales = grouped_products.reset_index()[['Product','Total']]

print(f"Total sales per product :\n{total_sales}")

