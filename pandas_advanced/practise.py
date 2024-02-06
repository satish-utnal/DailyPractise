"""

this py is basically for practising the functionalities what I have learnt in this week

"""

import pandas as pd

pd.options.display.width = None

df = pd.read_csv("../data/orders.txt")
returns = pd.read_csv("../data/returns.txt")

df["flag"] = 1

print("-----Added new column flag ----")
print(df)
print("-----drop column flag ----")
df.drop(columns=["flag"], inplace=True)
print(df)
print("-----delete one record where order_id='CA-2018-100006'----")
f = df[df["order_id"] == "CA-2018-100006"]
df.drop(f.index, inplace=True)
print(df)
print("-----reset index after deletion'----")
df.reset_index(inplace=True)
df.drop(columns="index", inplace=True)
print(df)
print("-----max , min sum sales, ----")
print(df["sales"].max(), 'max')
print(df["sales"].min(), 'min')
print(df["sales"].mean(), 'mean')
print(df["sales"].count(), 'count')
print(df["sales"].sum(), 'sum')
print("-----distinct category count----")
print(df["category"].value_counts())
print("-----using group by ----")
print(df.groupby("category")["sales"].sum())
print(df.groupby(["city", "category"])["sales"].sum())
print("-----using group by with sorting ----")
print(df.groupby('city').agg({'sales':'sum','profit':'mean'}).sort_values(by='sales').tail(5))
print("-----using group by with sorting multi index records ----")
print(df.groupby('city').agg({'sales': ['sum', 'mean'], 'profit': 'mean'}).sort_values([('sales', 'sum'),
                                                                                        ('sales', 'mean')]).tail(5))
print("-----left join two df----")
print(pd.merge(left=df, right=returns, left_on='order_id', right_on="Order Id", how='left'))

print("-----right join two df----")
print(pd.merge(left=df, right=returns, left_on="order_id", right_on="Order Id", how='right'))

print("-----inner join----")
print(pd.merge(left=df, right=returns, left_on="order_id", right_on="Order Id", how="inner"))

print("-----inner join----")

print(df["city"].unique())



