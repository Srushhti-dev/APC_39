employees = [
    ("Rahul", 50000),
    ("Amit", 70000),
    ("Sneha", 45000),
    ("Riya", 60000)
]

employees.sort(key=lambda x: x[1])
print(employees)
