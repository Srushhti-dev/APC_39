# Store 15 integers in a list. Count how many numbers are:Even ,Odd
numbers = []

# Accept 15 integers
for i in range(15):
    num = int(input("Enter number: "))
    numbers.append(num)

even_count = 0
odd_count = 0

# Count even and odd numbers
for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Even numbers:", even_count)
print("Odd numbers:", odd_count)