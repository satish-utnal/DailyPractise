import pandas as pd

pd.options.display.width = None
pd.options.display.max_columns = None
pd.set_option('display.max_rows', 5000)
pd.set_option('display.max_columns', 5000)

df = pd.read_csv("orders.txt")