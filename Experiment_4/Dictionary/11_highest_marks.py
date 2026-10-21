marks = {"Amit": 75, "Rahul": 90, "Sneha": 85, "Priya": 95}
student = max(marks, key=marks.get)
print("Highest marks:", student)
print("Marks:", marks[student])
