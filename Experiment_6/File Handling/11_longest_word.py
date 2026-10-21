with open("student.txt", "r") as file:
    words = file.read().split()

if words:
    print("Longest word:", max(words, key=len))
else:
    print("File is empty.")
