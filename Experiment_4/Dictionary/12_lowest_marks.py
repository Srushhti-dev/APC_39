marks = {"Amit": 75, "Rahul": 90, "Sneha": 85, "Priya": 65}
student = min(marks, key=marks.get)
print("Lowest marks:", student)
print("Marks:", marks[student])
