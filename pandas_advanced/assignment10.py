"""
10- write a program to get order ids and sales of return orders who's return reason is not known (nan)
"""

import pandas as pd

pd.options.display.width = None
pd.options.display.max_rows = 100

orders_raw = pd.read_csv("../data/orders.txt")
returns_raw = pd.read_csv("../data/returns.txt")

orders_returns = pd.merge(left=orders_raw, right=returns_raw, left_on="order_id", right_on="Order Id", how='left')
orders_returns.drop(columns="Order Id", inplace=True)
orders_nan = orders_returns[orders_returns['Return Reason'].notna()]
print(orders_nan)
