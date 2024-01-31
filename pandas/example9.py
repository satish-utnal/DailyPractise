# 9- sort the index (order id) in descending order for the dataframe

import readcsv as o

o.df.set_index("order_id",inplace=True)
df = o.df.sort_index(ascending=False)
print(df)