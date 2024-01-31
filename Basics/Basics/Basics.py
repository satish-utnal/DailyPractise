# variable name like 'a' in below stored in stack memory and the values '5' with below example stored in heap memory

# 'a' is references (like pointers in c) to 5 the
a = 5
print(a)

b = 6

print(b)

# id is the function to check memory address where the value stored in heap memory
print(id(a))

# after assigning different value to variable a the memory address will change

a = 20

print(id(a))

# print multiple values

print("vivek", "utnal", 5)

# print multiple values with seperator
print("seperator as ',' :vivek", "utnal", 5, 10, sep=",")
print("vivek", "utnal", 5, 10, sep=",")
print("seperator as 'new line' :vivek", "utnal", 5, 10, sep="\n")
print("using end function:vivek", "utnal", 5, 10, end=" ")
print("vrinda", "utnal", 5, 10)