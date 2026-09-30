numbers = (10, 15, 22, 31, 40, 55, 60, 73, 82, 91, 100, 25, 36, 47, 58)

even = 0
odd = 0

for n in numbers:
    if n % 2 == 0:
        even += 1
    else:
        odd += 1

print("Tuple:", numbers)
print("Even numbers:", even)
print("Odd numbers:", odd)