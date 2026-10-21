word = input("Enter word to search: ")
count = 0

with open("student.txt", "r") as file:
    for line_no, line in enumerate(file, start=1):
        for w in line.split():
            if w.lower() == word.lower():
                count += 1
                print("Found at line:", line_no)

print("Total occurrences:", count)
