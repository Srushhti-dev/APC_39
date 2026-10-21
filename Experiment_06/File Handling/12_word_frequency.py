with open("student.txt", "r") as file:
    words = file.read().lower().split()

frequency = {}
for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print(frequency)
