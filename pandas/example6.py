# 6- set the index of orders dataframe to order_id and fetch order details(all columns) of following list of orders :
# CA-2019-115742
# CA-2020-111682
# CA-2019-149587
# US-2020-150147
# CA-2020-138520

import pandas as pd


def display(id_list):
    print(df.loc[id_list])


pd.options.display.width = None
# pd.options.display.max_Columns = 5000


df = pd.read_csv("orders.txt")
# print(df)
df.set_index("order_id", inplace=True)
id_list = ['CA-2019-115742', 'CA-2020-111682', 'CA-2019-149587', 'US-2020-150147', 'CA-2020-138520']
display(id_list)
