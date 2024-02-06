import pandas as pd
emp = {"name": ["Satish", "poornima", "vivek", "vrinda"], "gender": ["male", "female", "male", "female"], "email": [
    "satish@gmail.com", "poornima@gmail.com", "vivek@gmail.com", "vrinda@gmail.com"]}

Schema = ["emp_name","Gender", "Email_Address"]
df = pd.DataFrame(emp)
print("-------------filtering only male records--------------------")
print(df[df["gender"] == "male"])
print("------------selecting columns ---------------------")
print(df.columns)
print("-------------filtering based on wild card search --------------------")
print(df[df["name"].str.contains("v")])
print("------------converting to upper---------------------")
print(df["name"].str.upper())
print("------------selecting only required columns---------------------")
print(df.loc[[1,2],["email"]])
print("------------ original dataframe---------------------")
print(df)
print("----------- altering column names ----------------------")
schema_original = df.columns
df.columns = Schema
print(df)
print("---------------reverting back to original state ------------------")
df.columns = schema_original
print(df)
print("---------------turning index off------------------")
df.set_index("name", inplace=True)
print(df)
print("--------------reverting index-------------------")
df.reset_index(inplace=True)
print(df)
print("---------- selecting required columns without loc-----------------------")
print(df[["email", "name"]])
print("---------------------------------")
df.index = [1,2,3,4]





