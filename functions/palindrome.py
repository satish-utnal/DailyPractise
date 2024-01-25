# 5- Write a Python function that checks whether a passed string is a palindrome or not.
# Note: A palindrome is a word, phrase, or sequence that reads the same backward as forward, e.g., madam.

def palidrome(instr):
    pl=""
    for cr in instr:
        pl = cr + pl
    if pl == instr:
        return True
    else:
        return False


getStr = input("Enter a string to check whether its palindrome or not : ")
print(palidrome(getStr))

