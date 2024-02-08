"""
5- write a program to get category wise sales of orders that were not returned
"""
import pandas as pd

pd.options.display.width = None

orders_raw = pd.read_csv("../data/orders.txt")
returns_raw = pd.read_csv("../data/returns.txt")

orders_returns = pd.merge(left=orders_raw, right=returns_raw, left_on="order_id", right_on="Order Id", how='left')
orders_returns.drop(columns="Order Id", inplace=True)
orders_quality = orders_returns[orders_returns['Return Reason'].isna()]
print(orders_returns.groupby('category')['sales'].sum())

