students = (
    (101, "Alice Smith", "Computer Science", 3.8),
    (102, "Bob Jones", "Data Science", 3.5),
    (103, "Charlie Brown", "Mathematics", 3.9),
    (104, "Diana Prince", "Physics", 3.7)
)
print("--- Student Records ---")
for student in students:
    student_id, name, major, gpa = student
    print(f"ID: {student_id} | Name: {name} | Major: {major} | GPA: {gpa}")
