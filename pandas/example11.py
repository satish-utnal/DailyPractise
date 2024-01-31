# 11- sort the dataframe column by profit in descending order

import readcsv as o

df = o.df
df = df.sort_values("profit", ascending=False)
print(df)
