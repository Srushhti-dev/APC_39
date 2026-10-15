import matplotlib.pyplot as plt

students = ["A", "B", "C", "D"]
marks = [80, 70, 90, 60]

plt.barh(students, marks)
plt.xlabel("Marks")
plt.ylabel("Students")
plt.title("Horizontal Bar Plot")
plt.show()
