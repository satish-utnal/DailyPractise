# 6-  write a program that reverses a given string. For example, if the input is "Hello" from user, the output should be "olleH" without using step size trick.

MyString = input("Enter string to reverse :")
print(len(MyString))
reversestr = ""
for i in range(len(MyString)): # without using step size
    reversestr = MyString[i] + reversestr
print(reversestr)

print(MyString[::-1]) # with using step size