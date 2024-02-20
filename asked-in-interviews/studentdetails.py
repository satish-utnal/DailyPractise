import pandas as pd

input_data = "John 2020 89, John 2021 94, John 2022 97, " + \
             "James 2019 34, James 2020 32, James 2021 99, " + \
             "John 2029 45, John 2023 66, John 2019 78, " + \
             "Peter 2020 78, Peter 2021 98, Peter 2022 45, " + \
             "Eloise 2019 88, Eloise 2020 99, Eloise 2021 66, " + \
             "James 2022 89, James 2023 58, Jonathan 2022 100, " + \
             "Sarah 2019 65, Sarah 2020 66, Sarah 2021 66"
# Instructions #
# input_data contains information about some students' test scores over some years.
# For example, the first few entries in the data say:
#   - John did a test in 2020 and got 89 marks.
#   - John did a test in 2021 and got 94 marks.
#   - John did a test in 2022 and got 97 marks.
#   - James did a test in 2019 and got 34 marks.
#    etc.
# Write some code to process input_data and query the following information:
#   (1) For a given student, what scores did he/she receive?
#   (2) For a given student, what was his/her best score?
#   (3) For a given student, what was his/her worst score?
#   (4) For a given student, what was his/her average score?
"""
for i in range(len(students)):
    row = students[i].split()
    data.append(row)

df = pd.DataFrame(columns=columns, data=data)
"""
columns = ['name', 'year', 'score']
df = pd.DataFrame(columns=columns)
print(df.columns)
students = input_data.split(',')
for i in range(len(students)):
    row = students[i].split()
    df.loc[i] = row
df['score'] = df['score'].astype('int')
print(df)
choose = input('Enter student name to get his details: ')
df_choose = df[df.name == choose]
print(df_choose)
print(f"max score for {choose} is : {df_choose['score'].max()}")
print(f"min score for {choose} is : {df_choose['score'].min()}")
print(f"Average score for {choose} is : {df_choose['score'].mean()}")