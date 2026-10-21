info = input("Enter additional information: ")
with open("student.txt", "a") as file:
    file.write("\n" + info)
print("Information appended successfully.")
