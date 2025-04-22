# 37. Class BankAccount
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def display(self):
        print(f"Account Holder: {self.account_holder}, Balance: {self.balance}")

account1 = BankAccount("Emma", 10000)
account1.display()