employees = [
    ("Rahul", "IT", 60000),
    ("Amit", "HR", 45000),
    ("Sneha", "IT", 75000),
    ("Riya", "Sales", 55000)
]

high_salary = list(filter(lambda x: x[2] > 50000, employees))

increased_salary = list(
    map(lambda x: (x[0], x[1], x[2] * 1.10), employees)
)

sorted_employees = sorted(employees, key=lambda x: x[2])

print("Salary > 50000:", high_salary)
print("10% Increased Salary:", increased_salary)
print("Sorted:", sorted_employees)
