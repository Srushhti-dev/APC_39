class Student:
    def __init__(self, marks):
        self.marks = marks

    def calculate_grade(self):
        pass


class EngineeringStudent(Student):
    def calculate_grade(self):
        if self.marks >= 85:
            return "A"
        elif self.marks >= 70:
            return "B"
        elif self.marks >= 55:
            return "C"
        return "D"


class MedicalStudent(Student):
    def calculate_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 60:
            return "C"
        return "D"


class ManagementStudent(Student):
    def calculate_grade(self):
        if self.marks >= 80:
            return "A"
        elif self.marks >= 65:
            return "B"
        elif self.marks >= 50:
            return "C"
        return "D"


for student in [EngineeringStudent(82), MedicalStudent(88), ManagementStudent(78)]:
    print(student.__class__.__name__, "Grade:", student.calculate_grade())
