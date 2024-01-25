# from a list of numbers create 2 list , one containing only the even numbers and other only the odd numbers
GivenList = input("Enter list of numbers to list with \",\" separated: ")
Templist = GivenList.split(",")
Mylist = [int(num.strip(" ")) for num in Templist]  # Convert given list to int from string
Evenlist =[]
Oddlist =[]
for num in Mylist:
    if num % 2 == 0 :
        Evenlist.append(num)
    else:
        Oddlist.append(num)
print(f'Even number list: {Evenlist}')
print(f'Odd number list: {Oddlist}')