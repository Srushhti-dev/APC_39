from student.marks import total, percentage
from student.grade import grade
from student.attendance import eligible
marks=[80,75,90,85,70]
p=percentage(marks)
print("Total:",total(marks))
print("Percentage:",p)
print("Grade:",grade(p))
print("Attendance Eligible:",eligible(80,100))
