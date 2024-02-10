"""
11- write a program to fill unknown(nan) return reason to a default value 'unknown'
"""

import pandas as pd

pd.options.display.width = None
pd.options.display.max_rows = 100

orders_raw = pd.read_csv("../data/orders.txt")
returns_raw = pd.read_csv("../data/returns.txt")

orders_returns = pd.merge(left=orders_raw, right=returns_raw, left_on="order_id", right_on="Order Id", how='left')
orders_returns.drop(columns="Order Id", inplace=True)

orders_returns.fillna('unknown')
