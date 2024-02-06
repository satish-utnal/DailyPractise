# 13- reset the index to original state

import readcsv as r

df = r.df
df.set_index("order_id", inplace=True)
print(df)
df.reset_index("order_id", inplace=True)
print(df)
