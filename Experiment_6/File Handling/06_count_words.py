with open("student.txt", "r") as file:
    content = file.read()
print("Total number of words:", len(content.split()))
