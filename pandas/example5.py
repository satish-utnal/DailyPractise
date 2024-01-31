# 5- a) in the orders data frame rename column names to upper case ..eg order_id should be ORDER_ID
#   b)again change the column names back to lower case

import pandas as pd
pd.options.display.width = None
pd.options.display.max_columns = 5000
pd.options.display.max_rows = 5000

df = pd.read_csv("orders.txt")
print("-----original columns ----")
print(df.columns)
print("-----converting to upper-----")
df.columns = [col.upper() for col in df.columns]
print(df.head(10))
print("-----converting to lower-----")
df.columns = [col.lower() for col in df.columns]
print(df.head(10))
