"""
2- create a column as profit_category(use apply method) . sets it value as below:

if profit < 0 then 'loss'
if profit between 0 and 100 then 'low profit'
if profit between 100 and 500 then 'medium profit'
else high profit

"""

import pandas as pd

pd.options.display.width = None

orders_raw = pd.read_csv("../data/orders.txt")

print("----------approach 1 with creating function------")


def get_profit_category(profit):
    if profit < 0:
        return 'loss'
    elif 0.0 <= profit < 100.0:
        return 'low profit'
    elif 100.0 <= profit < 500.0:
        return 'medium profit'
    else:
        return 'high profit'


orders_raw['profit_category'] = orders_raw['profit'].apply(get_profit_category)
print(orders_raw)
print("----------approach 2 with lambda function------")

orders_raw['profit_category1'] = orders_raw['profit'].apply(lambda x: 'loss' if x < 0 else 'low profit' if 0 <= x < 100
                                                            else 'medium profit' if 100 <= x < 500 else 'high profit')
print(orders_raw)
