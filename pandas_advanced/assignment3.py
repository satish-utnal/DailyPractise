"""
3- delete column profit_category from the dataframe

"""

import assignment2 as a1

print(a1.orders_raw)

a1.orders_raw.drop(columns=['profit_category','profit_category1'], inplace=True)
print(a1.orders_raw)
