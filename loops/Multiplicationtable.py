#
# 10- write program to take a input(number) from the user  and print the multiplication table (up to 10) of that number.
#
# for example user input = 9 then you need to print
#
# 1*9=9
# 2*9=18
# --
# so on till
# 10*9=90

st = int(input("Enter number for it multiplication table : "))
for i in range(1,11):
    print(f'{i}*{st}={i*st}')