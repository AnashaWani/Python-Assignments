### MERGING DATAFRAMES ###


import pandas as pd

# creating and printing first df #
df1 = pd.DataFrame({"ID":[1,2], "Name":["Amit","Sara"]})
print(f"First DataFrame :\n{df1}")

# creating and printing second df#
df2 = pd.DataFrame({"ID":[1,2], "Marks":[85,90]}) 
print(f"Second DataFrame :\n{df2}")

# merging the two dataframes #
merged = pd.merge(df1, df2, on="ID")

print(f"DataFrame after merging :\n{merged}")