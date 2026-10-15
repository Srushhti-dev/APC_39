#Display only unique elements from a list
numbers = [10, 20, 10, 30, 20, 40, 50, 30]

unique = []

for n in numbers:
    if n not in unique:
        unique.append(n)

print("Original list:", numbers)
print("Unique elements:", unique)