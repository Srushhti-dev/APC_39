import pandas as pd

salaries = {
    "Amit": 55000,
    "Priya": 48000,
    "Rahul": 65000,
    "Sneha": 75000,
    "Neha": 52000
}

series = pd.Series(salaries)

print("Employee Salary Series:")
print(series)

print("\nHighest salary:", series.max())
print("Lowest salary:", series.min())
print("Average salary:", series.mean())

print("\nEmployees earning more than 50000:")
print(series[series > 50000])
