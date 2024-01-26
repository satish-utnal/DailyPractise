# Assignment 3: Building a Bank Account Class
# Create a class named BankAccount with the following attributes:
#
# account_holder (string)
# balance (float)
# Include methods:
#
# deposit to add funds to the account.
# withdraw to deduct funds from the account.
#
# Tasks:
#
# Create an instance of the BankAccount class.
# Set values for the account_holder and balance attributes.
# Call the deposit and withdraw methods to perform transactions.
# Display the final balance.


class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, dp_amount):
        self.balance = self.balance + dp_amount

    def withdraw(self, wd_amount):
        self.balance = self.balance - wd_amount


bank_details = BankAccount('Vrinda', balance=float(2704.55))
print(f'Account holder name : {bank_details.account_holder}')
print(f'Balance for {bank_details.account_holder} is : {bank_details.balance}')
print(f'Depositing amount 13000.45 to {bank_details.account_holder} account')
bank_details.deposit(float(13000.45))
print(f'Balance after deposit is : {bank_details.balance}')
bank_details.withdraw(float(1300))
print(f'Transferred rent of 1300 and balance is : {bank_details.balance}')

