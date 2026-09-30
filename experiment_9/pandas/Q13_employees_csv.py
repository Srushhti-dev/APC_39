import pandas as pd

df = pd.read_csv("employees.csv")

print("Employees from CSE department:")
print(df[df["Department"] == "CSE"])

print("\nAverage salary:", df["Salary"].mean())
print("Highest salary:", df["Salary"].max())
print("Lowest salary:", df["Salary"].min())

print("\nEmployees with salary greater than 50000:")
print(df[df["Salary"] > 50000])

print("\nDepartment-wise average salary:")
print(df.groupby("Department")["Salary"].mean())
