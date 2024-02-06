"""
This py is just to read the csv file into data frame which can be used across different scripts
"""

import pandas as pd

pd.options.display.width = None

df = pd.read_csv("../data/orders.txt")
df_returns = pd.read_csv("../data/returns.txt")
print(df_returns)


