# Assignment 4: Enhancing the Bank Account Class Modify the BankAccount class from bankdetail1.py file 3 to include a
# method display_balance that prints the current balance. Tasks:
#
# Modify the BankAccount class to include the display_balance method.
# Create an instance of the modified class.
# Perform deposit and withdrawal transactions.
# Call the display_balance method to print the final balance.

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, dp_amount):
        self.balance = self.balance + dp_amount

    def withdraw(self, wd_amount):
        self.balance = self.balance - wd_amount

    def display_balance(self):
        print(f'Current balance : {self.balance}')


bank_details1 = BankAccount('Vivek', float(750.55))
bank_details1.display_balance()
bank_details1.deposit(float(2707.55))
bank_details1.display_balance()
bank_details1.withdraw(float(150))
bank_details1.display_balance()
