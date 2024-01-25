
# 10- Write a function called capitalize_odd_letters that takes a string as input and returns the same string with the odd-indexed letters capitalized.
# eg: input : ankit . output : aNkIt


def capitalize(str):
    finalstr=""
    for i in range(len(str)):
        if i == 0 or i % 2 == 0:
            finalstr = finalstr+str[i].lower()
        else:
            finalstr = finalstr+str[i].upper()
    print(finalstr)


capitalize(input("Enter STring to capitalize : "))