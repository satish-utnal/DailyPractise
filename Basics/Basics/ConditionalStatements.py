print("Enter Age")
age = int(input())
if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")
print("Enter No to verify nested if")
try:
    age1 = int(input())
except:
    print("Enter integer entry only")

if age1>18:
    if age1>65:
        print("Take care")
    else:
        print("Eligible")
else:
    print("Not eligible")


print("Enter a number to test elif")
x = int(input())

if x > 0:
    print("positive")
elif x == 0:
    print("Zero")
else:
    print("Negative")
