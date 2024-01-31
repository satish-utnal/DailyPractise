# 12- sort the dataframe column by sales in ascending order , in case of a tie it should be sorted by profit in
# descending order

import readcsv as r

df = r.df
print(df.sort_values(["sales", "profit"], ascending=[True, True]))
