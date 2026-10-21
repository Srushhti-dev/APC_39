class Account:
    def __init__(self, account_no, name, balance):
        self.account_no=account_no; self.name=name; self.balance=balance
    def display(self):
        print("Account:",self.account_no)
        print("Name:",self.name)
        print("Balance:",self.balance)
