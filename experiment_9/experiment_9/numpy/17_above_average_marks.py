import numpy as np

marks = np.array([65, 78, 82, 55, 90, 72, 88, 60, 95, 68,
                  75, 84, 59, 91, 73, 80, 62, 87, 70, 96])

average = np.mean(marks)
above_average = marks[marks > average]

print("Marks:", marks)
print("Class average:", average)
print("Students' marks above average:", above_average)
