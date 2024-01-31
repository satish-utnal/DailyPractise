# 2- write a program to find all orders in furniture category with sales amount between 1000 and 1200

import pandas as pd

pd.options.display.width = None
pd.options.display.max_columns = None
pd.set_option('display.max_rows', 5000)
pd.set_option('display.max_columns', 5000)

df = pd.read_csv("orders.txt")
# print(df.dtypes)
print(df[(df["category"] == 'Furniture') & (df["sales"].between(1000, 1200))].sort_values("sales"))
