numbers = [10, 20, 10, 30, 20, 10, 40]

frequency = {}

for n in numbers:
    if n in frequency:
        frequency[n] += 1
    else:
        frequency[n] = 1

print("Frequency of elements:")

for key, value in frequency.items():
    print(key, ":", value)