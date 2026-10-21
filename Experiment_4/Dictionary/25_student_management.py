students = {"Amit": 80, "Rahul": 75, "Sneha": 90}

name = input("Enter student name to add: ")
marks = int(input("Enter marks: "))
students[name] = marks

name = input("Enter student name to update: ")
if name in students:
    marks = int(input("Enter new marks: "))
    students[name] = marks

name = input("Enter student name to delete: ")
if name in students:
    del students[name]

name = input("Enter student name to search: ")
if name in students:
    print("Marks:", students[name])
else:
    print("Student not found")

print("All students:")
for name, marks in students.items():
    print(name, ":", marks)

if len(students) > 0:
    highest = max(students, key=students.get)
    print("Highest marks:", highest, students[highest])
    average = sum(students.values()) / len(students)
    print("Average:", average)
