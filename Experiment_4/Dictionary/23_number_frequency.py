numbers = [1, 2, 2, 3, 3, 3, 4, 4, 5]
frequency = {}
for number in numbers:
    if number in frequency:
        frequency[number] += 1
    else:
        frequency[number] = 1
print(frequency)
