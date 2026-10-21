class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, roll_no):
        super().__init__(name, age)
        self.roll_no = roll_no


class Faculty(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject


class TeachingAssistant(Student, Faculty):
    def __init__(self, name, age, roll_no, subject):
        Person.__init__(self, name, age)
        self.roll_no = roll_no
        self.subject = subject

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Roll No:", self.roll_no)
        print("Subject:", self.subject)
        print("Role: Teaching Assistant")


ta = TeachingAssistant("Amit", 24, 101, "Python")
ta.display()
