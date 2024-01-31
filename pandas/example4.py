# 4- create a new column in the orders dataframe with name profit_flag. Set its value as 1 if profit is greater than
# 0 else set 0.

import pandas as pd

pd.options.display.width = None
pd.options.display.max_columns = 5000
pd.options.display.max_rows = 5000

df = pd.read_csv("orders.txt")

df["profit_flag"] = df["profit"].apply(lambda x: 1 if x > 0 else 0)
print(df)
