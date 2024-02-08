"""
4- delete all the rows where profit is negative
"""

import pandas as pd

pd.options.display.width = None

orders_raw = pd.read_csv("../data/orders.txt")
orders_raw_copy = orders_raw.copy()
print("------------Approach 1-----------")
orders_raw = orders_raw[orders_raw["profit"] >= 0]
print(orders_raw)

print("------------Approach 2-----------")
orders_in_loss = orders_raw_copy['profit'] < 0
orders_raw_copy.drop(index=orders_raw_copy[orders_in_loss].index, inplace=True)
print(orders_raw_copy)

print(orders_raw.shape)
print(orders_raw_copy.shape)
print('-----test if both approach are resulting same result---------')
df = pd.merge(left=orders_raw, right=orders_raw_copy, on='order_id', how='right')
print(df[df['customer_name_x'].isna()])
df = pd.merge(left=orders_raw, right=orders_raw_copy, on='order_id', how='left')
print(df[df['customer_name_y'].isna()])



