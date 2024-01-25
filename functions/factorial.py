#2- write a Python function which takes a positive number as input and return the factorial of the number.

#eg: factorial of 5 is -> 5*4*3*2*1 = 120

def factorial(x):
    fact = 1
    for num in range(1, x+1):
        fact = fact * num
    return fact


inpt = int(input("Enter any positive number to get factorial of it : "))
f = factorial(inpt)
print(f"Factorial of number is : {f}")
