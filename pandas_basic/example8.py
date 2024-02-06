# 8- for the previous(6th) question display all the columns from order_date to city (as per the order in dataset)

print("--------- Result for assignment no 6 --------------")

import example6 as e6

print("--------- Result for assignment no 8 --------------")
e6.df.reset_index("order_id", inplace=True)
print(e6.df.iloc[0:, 1:])
