import matplotlib.pyplot as plt

subjects = ["Python", "Java", "C++", "SQL"]
values = [40, 30, 20, 10]

plt.pie(values, labels=subjects, autopct="%1.1f%%")
plt.title("Pie Chart")
plt.show()
