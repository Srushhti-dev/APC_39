import matplotlib.pyplot as plt

students = ["A", "B", "C", "D"]
marks = [80, 70, 90, 60]

plt.bar(students, marks)
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Bar Plot")
plt.show()
