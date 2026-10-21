import pandas as pd

df = pd.read_csv("employees.csv")

print("CSE employees:\n", df[df["Department"] == "CSE"])
print("\nAverage salary:", df["Salary"].mean())
print("\nHighest salary:", df["Salary"].max())
print("Lowest salary:", df["Salary"].min())
print("\nEmployees with salary greater than ₹50,000:\n", df[df["Salary"] > 50000])
print("\nDepartment-wise average salary:\n", df.groupby("Department")["Salary"].mean())
