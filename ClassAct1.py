# Bank Account Management System
# Demonstration of Inheritance

# Parent Class
class Account:

    account_number = 100001

    def __init__(self, name, balance):
        self.name = name
        self.account_no = Account.account_number
        self.balance = balance

        # Generate next account number
        Account.account_number += 1

    def deposit(self, amount):
        self.balance += amount
        print("Amount deposited:", amount)
        print("Deposit successful.")

    def display(self):
        print("\n----- Account Details -----")
        print("Account Holder :", self.name)
        print("Account Number :", self.account_no)
        print("Balance        :", self.balance)


# Child Class - Savings Account
class SavingsAccount(Account):

    def calculate_interest(self):
        interest = self.balance * 0.05
        self.balance += interest

        print("\nInterest Rate:", "5%")
        print("Interest Added:", interest)
        print("Interest calculation successful.")


# Child Class - Current Account
class CurrentAccount(Account):

    def withdraw(self, amount):

        if amount <= self.balance:
            self.balance -= amount
            print("\nAmount withdrawn:", amount)
            print("Withdrawal successful.")
        else:
            print("\nInsufficient balance.")
            print("Withdrawal failed.")


# ------------------------------------------------
# MAIN PROGRAM
# ------------------------------------------------

print("======================================")
print("     BANK ACCOUNT MANAGEMENT SYSTEM")
print("======================================")


# Create Savings Account
print("\n### SAVINGS ACCOUNT ###")

savings = SavingsAccount("John", 5000)

savings.display()

# Deposit money
savings.deposit(1000)

# Calculate 5% interest
savings.calculate_interest()

# Display updated details
savings.display()


# Create Current Account
print("\n### CURRENT ACCOUNT ###")

current = CurrentAccount("Marina", 10000)

current.display()

# Deposit money
current.deposit(2000)

# Withdraw money
current.withdraw(3000)

# Try withdrawal with insufficient balance
current.withdraw(20000)

# Display updated details
current.display()