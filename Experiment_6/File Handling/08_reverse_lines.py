with open("student.txt", "r") as file:
    lines = file.readlines()
for line in reversed(lines):
    print(line.strip())
