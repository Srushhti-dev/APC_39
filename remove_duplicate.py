numbers = [10, 20, 10, 30, 20, 40, 30, 50]

unique = []

for n in numbers:
    if n not in unique:
        unique.append(n)

print("Original list:", numbers)
print("After removing duplicates:", unique)