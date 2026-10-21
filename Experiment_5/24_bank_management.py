balance = 0
transactions = []

def deposit(amount):
    global balance
    balance += amount
    transactions.append("Deposited: " + str(amount))

def withdraw(amount):
    global balance
    if amount <= balance:
        balance -= amount
        transactions.append("Withdrawn: " + str(amount))
        print("Withdrawal successful")
    else:
        print("Insufficient balance")

def balance_enquiry():
    print("Balance =", balance)

def transaction_history():
    print("\nTransaction History:")
    for t in transactions:
        print(t)

deposit(5000)
withdraw(2000)
balance_enquiry()
transaction_history()
