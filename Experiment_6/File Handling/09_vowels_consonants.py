with open("student.txt", "r") as file:
    content = file.read()

vowels = consonants = 0
for ch in content.lower():
    if ch.isalpha():
        if ch in "aeiou":
            vowels += 1
        else:
            consonants += 1

print("Vowels:", vowels)
print("Consonants:", consonants)
