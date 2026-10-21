with open("students.txt", "r") as file:
    lines = file.readlines()

students = []
for line in lines[1:]:
    roll, name, marks = line.strip().split(",")
    students.append({"roll": roll, "name": name, "marks": int(marks)})

print("All Records:")
for student in students:
    print(student)

highest = max(students, key=lambda x: x["marks"])
print("\nStudent with highest marks:", highest["name"], highest["marks"])

average = sum(s["marks"] for s in students) / len(students)
print("Average marks:", average)

print("\nStudents scoring more than 80:")
for student in students:
    if student["marks"] > 80:
        print(student["name"])
