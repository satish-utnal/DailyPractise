"""
12- write a program to find avg sales and avg profit for each category
"""

import pandas as pd

pd.options.display.width = None
pd.options.display.max_rows = 100

orders_raw = pd.read_csv("../data/orders.txt")
returns_raw = pd.read_csv("../data/returns.txt")

orders_returns = pd.merge(left=orders_raw, right=returns_raw, left_on="order_id", right_on="Order Id", how='left')
orders_returns.drop(columns="Order Id", inplace=True)
print(orders_returns.groupby('category').agg({'sales': ['sum', 'mean'], 'profit': 'mean'}))
