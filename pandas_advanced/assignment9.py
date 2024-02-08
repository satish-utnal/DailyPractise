"""
9- write a program to find top 3 cities by sales
"""

import pandas as pd

pd.options.display.width = None
pd.options.display.max_rows = None

orders_raw = pd.read_csv("../data/orders.txt")
orders_city = orders_raw.groupby('city')['sales'].sum().reset_index(name='total_sale')

print(orders_city.sort_values(by='total_sale', ascending=False).head(3))
