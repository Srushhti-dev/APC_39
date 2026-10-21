old_word = input("Enter word to replace: ")
new_word = input("Enter new word: ")

with open("student.txt", "r") as file:
    content = file.read()

content = content.replace(old_word, new_word)

with open("student.txt", "w") as file:
    file.write(content)

print("Word replaced successfully.")
