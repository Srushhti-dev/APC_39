students = ["srushhti", "Priya", "harsh", "rushi"]

print("Total students:", len(students))

name = input("Enter student name to search: ")

if name in students:
    print(name, "is present.")
else:
    print(name, "is absent.")

new_student = input("Enter new student name: ")
students.append(new_student)

absent_student = input("Enter absent student name to remove: ")

if absent_student in students:
    students.remove(absent_student)
    print("Student removed.")
else:
    print("Student not found.")

print("Updated student list:", students)