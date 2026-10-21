def read_employees():
    employees = []
    with open("employees.txt", "r") as file:
        for line in file:
            emp_id, name, department, salary = line.strip().split(",")
            employees.append({
                "id": emp_id, "name": name,
                "department": department, "salary": float(salary)
            })
    return employees

def display_employees(employees):
    for emp in employees:
        print(emp)

def highest_paid(employees):
    return max(employees, key=lambda x: x["salary"])

def average_salary(employees):
    return sum(e["salary"] for e in employees) / len(employees)

def above_salary(employees, amount):
    for emp in employees:
        if emp["salary"] > amount:
            print(emp)

employees = read_employees()
print("All Employees:")
display_employees(employees)

print("\nHighest Paid:", highest_paid(employees))
print("\nAverage Salary:", average_salary(employees))

amount = float(input("\nEnter salary limit: "))
print("Employees earning above", amount)
above_salary(employees, amount)
