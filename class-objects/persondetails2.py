# Assignment 2: Working with Methods and Parameters
# Extend the Person class from Assignment 1 by adding a method celebrate_birthday that increments the person's age by 1.
#
# Tasks:
#
# Modify the Person class to include the celebrate_birthday method.
#
# Create an instance of the Person class and set initial values for name and age.
# Call the celebrate_birthday method and then use the display_info method to print the updated information.

class Person():

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def celebrate_birthday(self):
        self.age = self.age + 1

display_info = Person('Vivek Utnal', 6)
print(f'name: {display_info.name}')
print(f'age : {display_info.age}')
display_info.celebrate_birthday()
print(f'Hi {display_info.name} you are turning {display_info.age} years wish you happy birthday')


