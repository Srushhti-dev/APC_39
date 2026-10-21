class Employee:
    def calculate_salary(self):
        pass


class Manager(Employee):
    def __init__(self, basic):
        self.basic = basic

    def calculate_salary(self):
        return self.basic + self.basic * 0.30


class Developer(Employee):
    def __init__(self, basic):
        self.basic = basic

    def calculate_salary(self):
        return self.basic + self.basic * 0.20


class Tester(Employee):
    def __init__(self, basic):
        self.basic = basic

    def calculate_salary(self):
        return self.basic + self.basic * 0.15


for employee in [Manager(50000), Developer(45000), Tester(40000)]:
    print(employee.__class__.__name__, "Salary:", employee.calculate_salary())
