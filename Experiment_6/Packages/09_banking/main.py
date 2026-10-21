from banking.account import Account
from banking.transaction import deposit, withdraw
from banking.loan import calculate_loan
a=Account(101,"Amit",10000)
a.display()
a.balance=deposit(a.balance,5000)
a.balance=withdraw(a.balance,2000)
print("Balance:",a.balance)
print("Loan:",calculate_loan(100000,8,5))
