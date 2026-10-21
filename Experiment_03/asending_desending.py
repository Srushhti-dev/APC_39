numbers = []

for i in range(10):
    n = int(input("Enter number: "))
    numbers.append(n)

numbers.sort()

print("Ascending:", numbers)

numbers.sort(reverse=True)

print("Descending:", numbers)