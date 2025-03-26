class Account:
    def __init__(self, acc_num, holder, balance=0):
        self._acc_num, self._holder, self._balance = acc_num, holder, balance

    def deposit(self, amount):
        if amount > 0: self._balance += amount; print(f"Deposited ${amount}. Balance: ${self._balance}")
        else: print("Invalid deposit.")

    def withdraw(self, amount):
        if 0 < amount <= self._balance: self._balance -= amount; print(f"Withdrew ${amount}. Balance: ${self._balance}")
        else: print("Invalid withdrawal.")

    def check_balance(self): print(f"Balance for {self._holder}: ${self._balance}")


class SavingsAccount(Account):
    def __init__(self, acc_num, holder, balance=0, interest_rate=0.02):
        super().__init__(acc_num, holder, balance)
        self._interest_rate = interest_rate

    def add_interest(self):
        interest = self._balance * self._interest_rate
        self.deposit(interest); print(f"Interest added: ${interest}")


class CurrentAccount(Account):
    def __init__(self, acc_num, holder, balance=0, overdraft_limit=500):
        super().__init__(acc_num, holder, balance)
        self._overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if 0 < amount <= (self._balance + self._overdraft_limit): self._balance -= amount; print(f"Withdrew ${amount}. Balance: ${self._balance}")
        else: print("Exceeds overdraft limit.")


# Example
if __name__ == "__main__":
    savings = SavingsAccount("SA001", "Alice", 1000)
    savings.deposit(500); savings.add_interest(); savings.check_balance()

    current = CurrentAccount("CA001", "Bob", 500)
    current.withdraw(700); current.check_balance()