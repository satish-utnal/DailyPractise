# Assignment 5: Creating a Library Book Class
# Create a class named Book with the following attributes:
#
# title (string)
# author (string)
# is_available (boolean)
# Include a method checkout that sets the is_available attribute to False when a book is borrowed.
#
# Tasks:
#
# Create an instance of the Book class.
# Set values for the title, author, and is_available attributes.
# Call the checkout method to simulate borrowing the book.
# Display the book's information, including its availability.

def display():
    print(f'\tBook Details')
    print(f'Title : {book_detail.title}')
    print(f'Author : {book_detail.author}')
    print(f'Availability : {book_detail.is_available}')


class Book():
    def __init__(self, title, author, is_available):
        self.title = title
        self.author = author
        self.is_available = is_available

    def checkout(self):
        self.is_available = False

    def checkin(self):
        self.is_available = True


book_detail = Book('Advanced Python', 'Ankit', True)
display()
book_detail.checkout()
display()
book_detail.checkin()
display()
book_detail.checkout()
display()