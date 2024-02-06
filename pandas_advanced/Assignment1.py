"""

1- write a program to find unique list of cities where orders are placed for Office Supplies category.


"""

import pandas as pd

pd.options.display.width = None

orders_raw = pd.read_csv("../data/orders.txt")
returns_raw = pd.read_csv("../data/returns.txt")


print("------------Approach 1-----------")

orders_office_supplies = orders_raw[orders_raw['category'] == 'Office Supplies']
print(orders_office_supplies['city'].unique())
# print(len(orders_office_supplies['city'].unique()))

print("------------Approach 2-----------")

print(orders_raw[orders_raw['category'] == 'Office Supplies'].groupby('city').count())
