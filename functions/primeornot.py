# 8- write a function called is_prime that takes an integer as an argument and returns True if it is a prime number, and False otherwise.

def validateprime(x):
    pr = False
    if x <= 1:
        print("Enter positive number greater than 1 to validate prime or not : ")
    else:
        for i in range(2, int(x/2)):
            if x % i == 0:
                pr = True
                break
            else:
                pass
    return pr

prime = int(input("Enter a number to check whether its prime or not : "))
print(validateprime(prime))
