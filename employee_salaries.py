salaries = [25000, 35000, 55000, 60000, 28000, 75000, 45000]

highest = max(salaries)
lowest = min(salaries)
average = sum(salaries) / len(salaries)

above_50000 = 0
below_30000 = 0

for salary in salaries:
    if salary > 50000:
        above_50000 += 1

    if salary < 30000:
        below_30000 += 1

print("Highest salary: rs", highest)
print("Lowest salary: rs", lowest)
print("Average salary: rs", average)
print("Employees earning above rs50,000:", above_50000)
print("Employees earning below rs30,000:", below_30000)