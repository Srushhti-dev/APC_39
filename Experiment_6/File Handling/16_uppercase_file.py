with open("student.txt", "r") as file:
    content = file.read()

with open("uppercase.txt", "w") as file:
    file.write(content.upper())

print("Uppercase file created.")
