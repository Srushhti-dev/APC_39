with open("student.txt", "r") as file:
    content = file.read()
print("Total characters including spaces:", len(content))
