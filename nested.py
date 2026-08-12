#Nested list storing student details
students = [
    ["srushhti", 39, 85],
    ["neha", 102, 90],
    ["arya", 44, 78],
    ["aditi", 26, 92]
]

print("Student Details:")

for student in students:
    print("Name:", student[0])
    print("Roll Number:", student[1])
    print("Marks:", student[2])
    print()