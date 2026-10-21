class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    def percentage(self):
        return sum(self.marks) / len(self.marks)

    def display(self):
        print("Roll No:", self.roll_no)
        print("Name:", self.name)
        print("Marks:", self.marks)
        print("Percentage:", self.percentage(), "%")
        print()

student1 = Student(101, "Amit", [80, 75, 90, 85, 70])
student2 = Student(102, "Priya", [90, 85, 95, 88, 92])
student3 = Student(103, "Rahul", [70, 65, 80, 75, 72])

student1.display()
student2.display()
student3.display()
