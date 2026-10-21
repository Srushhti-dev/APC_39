total_deposit = total_withdrawal = largest = 0

with open("transactions.txt", "r") as file:
    for line in file:
        transaction, amount = line.strip().split(",")
        amount = float(amount)
        largest = max(largest, amount)
        if transaction.lower() == "deposit":
            total_deposit += amount
        elif transaction.lower() == "withdrawal":
            total_withdrawal += amount

print("Total Deposits:", total_deposit)
print("Total Withdrawals:", total_withdrawal)
print("Final Balance:", total_deposit - total_withdrawal)
print("Largest Transaction:", largest)
