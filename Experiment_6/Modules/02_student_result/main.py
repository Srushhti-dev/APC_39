import student
marks = [float(input(f"Enter marks {i+1}: ")) for i in range(5)]
p = student.percentage(marks)
print("Total:", student.total_marks(marks))
print("Percentage:", p)
print("Grade:", student.grade(p))
