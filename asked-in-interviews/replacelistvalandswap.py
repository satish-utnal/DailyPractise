"""
given list
[1,2,3,4,5,2]

output -- replace given number in below example its 2 

[1,3,4,5,_,_]


"""


my_list = [1,2,3,4,5,2]


VAL = 2
L1 = len(my_list)
print(my_list, L1)
my_list = [i for i in my_list if i != VAL]
l2 = len(my_list)
print(my_list,l2)
for i in range(0, L1 - l2):
    my_list.append('-')
print(my_list, len(my_list))
