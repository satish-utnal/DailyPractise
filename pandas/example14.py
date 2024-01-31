# 14- create a column as profit_category . sets it value as below:
#
# if profit < 0 then 'loss'
# if profit between 0 and 100 then 'low profit'
# if profit between 100 and 500 then 'medium profit'
# else high profit

import pandas as pd

pd.options.display.width = None

df = pd.read_csv("orders.txt")
df["profit_category"] = df["profit"].apply(lambda x: 'loss' if x < 0 else 'low profit' if (x <= 0) | (x < 100) else 'medium profit' if (x <= 100) | (x < 500) else 'high profit')
print(df.head(100))
