marks = [
    75, 82, 65, 90, 55,
    88, 72, 95, 60, 78,
    85, 69, 91, 73, 80,
    67, 89, 76, 92, 58
]

highest = max(marks)
lowest = min(marks)
average = sum(marks) / len(marks)

above_average = 0
below_average = 0

for mark in marks:
    if mark > average:
        above_average += 1
    elif mark < average:
        below_average += 1

print("Highest marks:", highest)
print("Lowest marks:", lowest)
print("Average marks:", average)
print("Students above average:", above_average)
print("Students below average:", below_average)