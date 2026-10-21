students = {"Amit": "CSE", "Rahul": "IT", "Sneha": "CSE", "Priya": "ENTC", "Rohan": "IT"}

groups = {}
for student, department in students.items():
    if department not in groups:
        groups[department] = []
    groups[department].append(student)

print(groups)
