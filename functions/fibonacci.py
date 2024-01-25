
# 8- write a function called is_prime that takes an integer as an argument and returns True if it is a prime number, and False otherwise.

def getfibonacci(n):
    FibonacciList = []
    if n == 1:
        FibonacciList.append(0)
    elif n == 2:
        FibonacciList.append(0)
        FibonacciList.append(1)
    elif n >= 3:
        FibonacciList.append(0)
        FibonacciList.append(1)
        for i in range(2, n):
            FibonacciList.append(FibonacciList[i-2]+FibonacciList[i-1])
    return FibonacciList

num=int(input("Enter range to get fibonacci series : "))
fiblist = getfibonacci(num)
print(fiblist)