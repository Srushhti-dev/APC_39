class Student:
    def __init__(self, name, total_marks):
        self.name = name
        self.total_marks = total_marks

    def __gt__(self, other):
        return self.total_marks > other.total_marks

    def __lt__(self, other):
        return self.total_marks < other.total_marks


s1 = Student("Amit", 450)
s2 = Student("Priya", 420)

print("Amit > Priya:", s1 > s2)
print("Amit < Priya:", s1 < s2)
