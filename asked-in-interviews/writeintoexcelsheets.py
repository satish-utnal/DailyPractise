import pandas as pd

df = pd.read_csv("../data/orders.txt")
with pd.ExcelWriter("../data/orders.xlsx", mode='a', engine="openpyxl") as writer:
    df.to_excel(writer,  index=False, sheet_name="order12")
