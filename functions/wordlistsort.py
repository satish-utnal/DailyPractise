# 6- Write a Python function that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.
# Sample Items : green-red-yellow-black-white
# Expected Result : black-green-red-white-yellow


def wordlist(SampleItems):
    print(SampleItems)
    ExpectedResultList = SampleItems.split("-")
    ExpectedResultList.sort(reverse=True)
    ExpectedResult = ""
    for str in ExpectedResultList:
        ExpectedResult=str+"-"+ExpectedResult
    print(ExpectedResult.strip("-")) # strip added to remove hypen from end, we can add if condition in loop aswell to avoid adding hypen at end


SampleItems = "green-red-yellow-black-white"  # input("Enter hyper separated string to sort : ")
wordlist(SampleItems)

