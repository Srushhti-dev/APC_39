from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, balance=0):
        self.balance = balance

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass


class SavingsAccount(BankAccount):
    def deposit(self, amount):
        self.balance += amount
        print("Savings deposit:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Savings withdrawal:", amount)
        else:
            print("Insufficient balance.")


class CurrentAccount(BankAccount):
    def deposit(self, amount):
        self.balance += amount
        print("Current deposit:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Current withdrawal:", amount)
        else:
            print("Insufficient balance.")


account = SavingsAccount(10000)
account.deposit(2000)
account.withdraw(3000)
print("Balance:", account.balance)

account = CurrentAccount(15000)
account.deposit(5000)
account.withdraw(4000)
print("Balance:", account.balance)
