# 4- consider the below list of list conatins following information :
from typing import List

# 1. The name of a university
# 2. The total number of enrolled students
# 3. The annual tuition fees

universities: list[list[str | int]] = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]
#
# write a program to print follwoing information :
# 1- a list of all the universitites  : ['California Institute of Technology','Harvard',..so on]
# 2- total number of student entrolled in all the unversities together
# 3- mean of tuition fees

uname = []
totalstudents = 0
totalfees = 0
print(len(universities[0]))
for i in range(0, len(universities)):
    for j in range(len(universities[i])):
        if j == 0:
            uname.append(universities[i][j])
        elif j == 1:
            totalstudents = totalstudents+universities[i][j]
        elif j == 2:
            totalfees = totalfees+universities[i][j]

print(f'list of all the universities  : {uname}')
print(f'Total number of student entrolled in all the unversities : {totalstudents}')
print(f"mean of tuition fees: {totalfees / len(universities)} ")