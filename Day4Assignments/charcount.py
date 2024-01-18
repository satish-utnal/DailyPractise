# 7- write a python function that accepts a string and prints the count of occurence of each characters
# sample string: aabccda
# expected result:
# a -> 3
# b-> 1
# c-> 2
# d -> 1


def charcount(str):
    dict = {}
    for char in str:
        if char in dict.keys():
            dict[char] = dict[char] + 1
        else:
            dict.update({char: 1})
    for key,value in dict.items():
        print(f'{key} -> {value}')



charcount(input('Enter string to get each char occurrence : '))
