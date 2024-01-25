# given a list of numbers unsorted, write a program to find the median of the numbers in list
from typing import List

GivenList = input("Enter list of numbers to list with \",\" separated: ")
Templist = GivenList.split(",")
Mylist = [int(num.strip(" ")) for num in Templist]  # Convert given list to int from string
Mylist.sort()
if len(Mylist) % 2 != 0:
    print(f'Given list is odd and Median of List is : {Mylist[int((len(Mylist)) / 2)]}')
else:
    mid = int(len(Mylist)/2)
    print(f'Given list is even and Median of List is : {int(Mylist[mid-1] + Mylist[mid]) / 2}')