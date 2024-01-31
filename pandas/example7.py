# 7- for the previous question display columns order id, order date , sales and category columns in the given order

print("--------- Result for assignment no 6 --------------")
import example6 as e6


print("--------- Result for assignment no 7 --------------")

#print(e6.df.loc[[e6.id_list], ["order_date","sales","category"]])
print(e6.df.loc[e6.id_list, ["order_date", "sales", "category"]])
