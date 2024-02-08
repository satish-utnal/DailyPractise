"""
7- write a program to print cities where we have all 3 kinds of returns (others,bad quality,wrong items)
"""

import pandas as pd

pd.options.display.width = None
pd.options.display.max_rows = None

orders_raw = pd.read_csv("../data/orders.txt")
returns_raw = pd.read_csv("../data/returns.txt")

orders_returns = pd.merge(left=orders_raw, right=returns_raw, left_on="order_id", right_on="Order Id", how='left')
orders_returns.drop(columns="Order Id", inplace=True)
orders_returns = orders_returns[orders_returns['Return Reason'].notna()]
orders_city = orders_returns.groupby('city')['Return Reason'].apply(set).reset_index(name='reason')
orders_city['rlist'] = orders_city['reason'].apply(lambda x: len(x))
orders_city = orders_city[orders_city['rlist'] > 2]
orders_city.drop(columns='rlist', inplace=True)
print(orders_city)





