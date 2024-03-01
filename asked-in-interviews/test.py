import pandas as pd

dictionary = {"key1": 1, "key2": 1, "key3": 7, "key4": 3, "key5": 4, "key6": 7}

list = [[key, value] for key, value in dictionary.items()]
columns = ['col1', 'col2']
df = pd.DataFrame(data=list, columns=columns)
df=df.groupby('col2').count().reset_index()
print(df)
list = [value for key, value in dictionary.items()]
unique_elements = [x for x in list if list.count(x) == 1]
print(unique_elements)
