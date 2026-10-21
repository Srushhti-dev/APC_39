def deposit(balance,amount): return balance+amount
def withdraw(balance,amount):
    if amount>balance:
        print("Insufficient balance"); return balance
    return balance-amount
