#
universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]
#
# 5- write a program to convert above universities list to a dictionary. the keys should be the name of the university
dict = {}
for i in range(0, len(universities)):
    dict.update({universities[i][0]: {"total students": universities[i][1], "fees": universities[i][2]}})
print(f'{dict}')
