# 3- Write a Python function that accepts a string and counts the number of upper and lower case letters.
# Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Upper case characters : 3
# No. of Lower case Characters : 12


def CountUpperLower(x):
    Ucount = 0
    Lcount = 0
    for chr in x:
        if chr.isupper():
            Ucount = Ucount + 1
        else:
            Lcount = Lcount + 1

    return Ucount, Lcount


Getstr = input("Enter String to get its count of Upper and lower characters : ")
print(f'No. of Upper case characters : {CountUpperLower(Getstr)[0]}')
print(f'No. of Lower case characters : {CountUpperLower(Getstr)[1]}')
