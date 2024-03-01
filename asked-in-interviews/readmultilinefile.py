import pandas as pd

df = pd.read_csv("../data/emp_multiline.txt", escapechar='\n')
df['address'] = df['address'].str.replace('\r', ' ')
print(df)
