students = [
    ("Rahul", 80),
    ("Amit", 65),
    ("Sneha", 90),
    ("Riya", 76)
]

def average_marks(students):
    marks = list(map(lambda x: x[1], students))
    return sum(marks) / len(marks)

above_75 = list(filter(lambda x: x[1] > 75, students))
sorted_students = sorted(students, key=lambda x: x[1])

print("Average Marks =", average_marks(students))
print("Above 75 =", above_75)
print("Sorted Students =", sorted_students)
