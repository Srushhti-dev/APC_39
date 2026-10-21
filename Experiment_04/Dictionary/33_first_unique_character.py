text = input("Enter a string: ")

frequency = {}
for char in text:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

for char in text:
    if frequency[char] == 1:
        print("First unique character:", char)
        break
