#1.Create a class Student with attributes such as roll_no, name, and marks. Create objects for multiple students and display their details and percentage.
class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    def calculate_percentage(self):
        return sum(self.marks) / len(self.marks)

    def display_details(self):
        print("Roll No:", self.roll_no)
        print("Name:", self.name)
        print("Marks:", self.marks)
        print("Percentage:", self.calculate_percentage(), "%")
        print()

student1 = Student(101, "Amit", [85, 78, 90, 88, 92])
student2 = Student(102, "Sneha", [90, 85, 80, 95, 88])

student1.display_details()
student2.display_details()