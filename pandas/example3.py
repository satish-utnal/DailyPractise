# 3- write a program to find all the orders where there was a loss (profit<0) in the city of new york , Los Angeles and Seattle

import pandas as pd

pd.options.display.width = None
pd.options.display.max_columns = None
pd.options.display.max_rows = 5000
# pd.set_option('display.max_rows' , 5000)

df = pd.read_csv("orders.txt")

print(df[df["city"].isin(["Seattle", "Los Angeles", "New York City"]) & (df["profit"] < 0)].
      sort_values(["profit"], ascending=False))
