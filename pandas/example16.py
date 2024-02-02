# 16- find all the orders where customer name starts with 'D' and ends with 'e'

import pandas as pd
import re

pd.options.display.width = None

df = pd.read_csv("orders.txt")
print(df[(df["customer_name"].str.lower().str.endswith('e')) & (df["customer_name"].str.lower().str.startswith('d'))])
#print(df[df["customer_name"].apply(lambda x: (x[0] == 'D') & (x[-1] == 'e'))])
