class Employee:
    def __init__(self, emp_id, name, basic_salary):
        self.emp_id = emp_id
        self.name = name
        self.basic_salary = basic_salary

    def calculate_salary(self):
        return self.basic_salary


class Manager(Employee):
    def calculate_salary(self):
        return self.basic_salary + self.basic_salary * 0.30


class Developer(Employee):
    def calculate_salary(self):
        return self.basic_salary + self.basic_salary * 0.20


class Tester(Employee):
    def calculate_salary(self):
        return self.basic_salary + self.basic_salary * 0.15


employees = [
    Manager(101, "Amit", 50000),
    Developer(102, "Priya", 45000),
    Tester(103, "Rahul", 40000)
]

for emp in employees:
    print(emp.name, "-", emp.__class__.__name__, "-", emp.calculate_salary())
