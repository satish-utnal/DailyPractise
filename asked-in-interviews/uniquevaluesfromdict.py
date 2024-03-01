"""
find_unique_values(dictionary) -> [3,4]
"""


def find_unique_values(dictionary):
    list = [value for key, value in dictionary.items()]
    unique_list = [i for i in list if list.count(i)==1]
    return unique_list


dictionary = {"key1": 1, "key2": 1, "key3": 7, "key4": 3, "key5": 4, "key6": 7}
print(find_unique_values(dictionary))
