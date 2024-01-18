# 1-  create a simple calculator in Python. The calculator should be able to perform basic arithmetic operations such as addition, subtraction, multiplication, and division.
# Here are the detailed requirements:
# Implement a function add(x, y) that takes two numbers as input and returns their sum.
# Implement a function subtract(x, y) that takes two numbers as input and returns their difference.
# Implement a function multiply(x, y) that takes two numbers as input and returns their product.
# Implement a function divide(x, y) that takes two numbers as input and returns their quotient. Ensure that the function handles the case of division by zero appropriately.
# Create a main function called calculator() that interacts with the user to perform calculations. The main function should:
# Display a menu with options for addition, subtraction, multiplication, and division.
# Prompt the user to enter their choice and the numbers on which the operation should be performed.
# Call the corresponding function based on the user's choice and display the result.
# Ensure the program continues to run until the user chooses to exit.
# Feel free to add additional features or improvements to enhance the calculator's functionality. Test your program with various input scenarios to ensure it works correctly.


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def quotient(x, y):
    return x / y


def Calculator(ch, x, y):
    if ch == 1:
        print(f' Addition of {x, y} is {add(int(x), int(y))}')
    elif ch == 2:
        print(f' Subtraction of {x, y} is {subtract(int(x), int(y))}')
    elif ch == 3:
        print(f' Multiplication of {x, y} is {multiply(int(x), int(y))}')
    elif ch == 4:
        print(f' Division of {x, y} is {quotient(int(x), int(y))}')


st=0
while True:
    if st == 5:
        break
    else:
        print(f'Choose below menu to continue to perform operations')
        print(f'\t 1 : Addition \n\t 2 : Subtraction \n\t 3 : Multiplication \n\t 4 : Division \n\t 5 : Exit')
        st = int(input('Enter your option : '))
        if st != 5:
            inpt = input(" Enter two numbers to perform the operation : ")
            x, y = inpt.split(",")
            Calculator(st, x, y)
        else:
            pass
