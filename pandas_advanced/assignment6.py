"""
6- write a program to get city wise count of return orders
"""

import pandas as pd

pd.options.display.width = None

orders_raw = pd.read_csv("../data/orders.txt")
returns_raw = pd.read_csv("../data/returns.txt")

orders_returns = pd.merge(left=orders_raw, right=returns_raw, left_on="order_id", right_on="Order Id", how='left')
orders_returns.drop(columns="Order Id", inplace=True)
orders_quality = orders_returns.groupby('city')['Return Reason'].value_counts()
print(orders_quality)
