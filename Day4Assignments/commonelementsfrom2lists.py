# 11- write a function called find_common_elements that takes two lists as input and returns a new list containing the common elements between the two lists.

def commonelements(list1,list2):
    list3=[]
    for i in list1:
        if i in list2:
            list3.append(i)
    return list3

givenlist1=input("Enter first list with \',' seperated :")
givenlist2=input("Enter second list with \',' seperated :")
list1=givenlist1.split(",")
list2=givenlist2.split(",")
list3=commonelements(list1,list2)
print(f'Common list is : {list3}')