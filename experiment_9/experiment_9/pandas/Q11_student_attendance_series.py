import pandas as pd

attendance = {
    "Amit": 92,
    "Sneha": 70,
    "Rahul": 88,
    "Priya": 95,
    "Neha": 65
}

series = pd.Series(attendance)

print("Average attendance:", series.mean())

print("\nStudents below 75%:")
print(series[series < 75])

print("\nStudents above 90%:")
print(series[series > 90])

print("\nHighest attendance:", series.max())
