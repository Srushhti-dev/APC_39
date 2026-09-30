import pandas as pd

data = {
    "Employee_ID": [1, 2, 3, 4, 5],
    "Employee_Name": ["Raj", "Priya", "Amit", "Sneha", "Rohan"],
    "Department": ["CSE", "IT", "HR", "CSE", "Finance"],
    "Salary": [55000, 48000, 62000, 75000, 52000],
    "Experience": [3, 5, 7, 10, 4]
}

df = pd.DataFrame(data)

print("Employees with salary greater than 50000:")
print(df[df["Salary"] > 50000])

print("\nAverage Salary:", df["Salary"].mean())
print("Highest Salary:", df["Salary"].max())

print("\nEmployee with highest experience:")
print(df.loc[df["Experience"].idxmax()])
