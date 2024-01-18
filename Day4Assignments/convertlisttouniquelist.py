# 4- Write a Python function that takes a list and returns a new list with distinct elements from the first list.
# Sample List : [1,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]

def getUnique(instr):
    uList = []
    for i in instr:
        if i not in uList:
            uList.append(i)
    return uList

myList = [1,2,3,3,3,3,4,5]

print(f'Sample List : {myList}')
print(f'Unique List : {getUnique(myList)}')

