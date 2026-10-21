numbers = []

for i in range(10):
    n = int(input("Enter number: "))
    numbers.append(n)

total = sum(numbers)
average = total / 10

print("Sum:", total)
print("Average:", average)