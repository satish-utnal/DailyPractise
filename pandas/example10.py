# 10 - write the result of previous question into a csv file in your local machine

import readcsv as o

o.df.set_index("order_id",inplace=True)
df = o.df.sort_index(ascending=False)
df.to_csv("orders_sorted.csv")