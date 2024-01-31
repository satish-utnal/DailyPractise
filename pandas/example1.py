# 1- write a program to fetch all the orders with indexes  multiple of 100 eg : 100,200,300,400..... . Display
# order_id , category and sales columns
import pandas as pd

df = pd.read_csv("orders.txt")
pd.options.display.width = None
pd.options.display.max_columns = None
pd.set_option('display.max_rows', 5000)
pd.set_option('display.max_columns', 5000)
# print(df.count("index"))
# use this if you need to re-index from existing with multiples of 100
# df.index = [i*100 for i in range(1,df.shape[0]+1)]
# test code
# mylist = [i for i in range(1, 5000) if i%100 == 0 ]
# print(mylist)
print(df.loc[[i for i in range(1, df.shape[0]+1) if i % 100 == 0], ["order_id", "category", "sales"]])




