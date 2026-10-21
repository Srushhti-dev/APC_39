class ATM:
    def __init__(self, account_no, name, balance):
        self.account_no = account_no
        self.name = name
        self.balance = balance

    def check_balance(self):
        print("Current Balance:", self.balance)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Amount deposited:", amount)
            print("New Balance:", self.balance)
        else:
            print("Invalid amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print("Amount withdrawn:", amount)
            print("Remaining Balance:", self.balance)

    def display_account(self):
        print("\nAccount Number:", self.account_no)
        print("Account Holder:", self.name)
        print("Balance:", self.balance)

atm = ATM(1001, "Amit", 10000)

while True:
    print("\n----- ATM MENU -----")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Display Account Details")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        atm.check_balance()
    elif choice == "2":
        amount = float(input("Enter deposit amount: "))
        atm.deposit(amount)
    elif choice == "3":
        amount = float(input("Enter withdrawal amount: "))
        atm.withdraw(amount)
    elif choice == "4":
        atm.display_account()
    elif choice == "5":
        print("Thank you for using ATM.")
        break
    else:
        print("Invalid choice.")
