import pandas as pd

marks = {
    "Aarav": 85,
    "Priya": 72,
    "Rohan": 91,
    "Sneha": 68,
    "Vikram": 78
}

s = pd.Series(marks)

print("Series:\n", s)
print("\nMarks of Priya:", s["Priya"])
print("\nMaximum marks:", s.max())
print("Minimum marks:", s.min())
print("Average marks:", s.mean())
print("\nStudents scoring more than 75:\n", s[s > 75])
