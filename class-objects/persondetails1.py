# Assignment 1: Creating a Simple Class
# Create a class named Person with the following attributes:
#
# name (string)
# age (integer)
# Include a method display_info that prints the person's name and age.


class Person():

    def __init__(self, name, age):
        self.name = name
        self.age = age

display_info = Person('Vivek Utnal', 6)
print(f'name: {display_info.name}')
print(f'age : {display_info.age}')



