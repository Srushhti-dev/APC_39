class BankAccount:
    def calculate_interest(self):
        pass


class SavingsAccount(BankAccount):
    def __init__(self, balance):
        self.balance = balance

    def calculate_interest(self):
        return self.balance * 0.06


class CurrentAccount(BankAccount):
    def __init__(self, balance):
        self.balance = balance

    def calculate_interest(self):
        return self.balance * 0.02


class FixedDepositAccount(BankAccount):
    def __init__(self, balance):
        self.balance = balance

    def calculate_interest(self):
        return self.balance * 0.08


for account in [SavingsAccount(50000), CurrentAccount(50000), FixedDepositAccount(50000)]:
    print(account.__class__.__name__, "Interest:", account.calculate_interest())
