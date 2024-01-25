# 7- write a program that finds the largest number in a list(unsorted) of integers without using sort/sorted or max/min method.

GivenList = input("Enter list of numbers to list with \",\" separated: ")
Templist = GivenList.split(",")
Mylist = [int(num.strip(" ")) for num in Templist]  # Convert given list to int from string

maxnum = 0
minnum = Mylist[0]
for num in Mylist:

    if num > maxnum:
        maxnum=num
    if num < minnum:
        minnum=num
print(f"Larget number of list is : {maxnum}")
print(f"Larget number of list is : {minnum}")
