class BankAccount:
    def __init__(self, holder, balance=0):
        self.holder = holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ₹{amount}. New balance: ₹{self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ₹{amount}. New balance: ₹{self.balance}")
        else:
            print("Invalid withdrawal or insufficient funds.")

    def check_balance(self):
        print(f"Balance for {self.holder}: ₹{self.balance}")


class SavingsAccount(BankAccount):
    def __init__(self, holder, balance=0, interest_rate=0.01):
        super().__init__(holder, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.deposit(interest)
        print(f"Interest added: ₹{interest}")


class CurrentAccount(BankAccount):
    def __init__(self, holder, balance=0, overdraft_limit=5000):
        super().__init__(holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):  # Override withdraw method
        if amount > 0 and (self.balance - amount) >= -self.overdraft_limit:
            self.balance -= amount
            print(f"Withdrew ₹{amount}. New balance: ₹{self.balance}")
        else:
            print("Invalid withdrawal or exceeds overdraft limit.")


# Example usage
savings = SavingsAccount("Alice", 10000)
savings.deposit(5000)
savings.withdraw(2000)
savings.add_interest()
savings.check_balance()

current = CurrentAccount("Bob", 5000)
current.deposit(3000)
current.withdraw(12000)  # Within overdraft limit
current.withdraw(2000)   # Exceeds overdraft limit
current.check_balance()