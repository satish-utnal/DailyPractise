# 15- create a new column sales_profit_ratio and set its value as (profit/sales)*100

import pandas as pd

pd.options.display.width = None

df = pd.read_csv("../data/orders.txt")

df["sales_profit_ratio"] = (df["profit"]/df["sales"]) * 100

print(df)
