def calculate(marks):
    total = sum(marks)
    percentage = total / 5

    if percentage >= 90:
        grade = "A"
    elif percentage >= 75:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 40:
        grade = "D"
    else:
        grade = "F"

    return total, percentage, grade

students = []
n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter name: ")
    roll = input("Enter roll number: ")
    marks = list(map(int, input("Enter 5 marks: ").split()))
    total, percentage, grade = calculate(marks)

    students.append({
        "name": name,
        "roll": roll,
        "marks": marks,
        "total": total,
        "percentage": percentage,
        "grade": grade
    })

class_average = sum(s["percentage"] for s in students) / n
highest = max(students, key=lambda x: x["percentage"])
lowest = min(students, key=lambda x: x["percentage"])

for s in students:
    print("\nName:", s["name"])
    print("Roll:", s["roll"])
    print("Total:", s["total"])
    print("Percentage:", s["percentage"])
    print("Grade:", s["grade"])

print("\nClass Average =", class_average)
print("Highest Scorer =", highest["name"])
print("Lowest Scorer =", lowest["name"])
