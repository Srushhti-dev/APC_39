import pandas as pd

data = {
    "Employee_ID": [1, 2, 3, 4, 5],
    "Employee_Name": ["Amit", "Neha", "Rahul", "Pooja", "Karan"],
    "Department": ["CSE", "IT", "HR", "CSE", "Finance"],
    "Salary": [60000, 48000, 55000, 75000, 52000],
    "Experience": [5, 3, 7, 10, 4]
}

df = pd.DataFrame(data)
print("DataFrame:\n", df)

print("\nSalary greater than ₹50,000:\n", df[df["Salary"] > 50000])
print("\nAverage salary:", df["Salary"].mean())
print("\nHighest salary:", df["Salary"].max())
print("\nEmployee with highest experience:\n", df.loc[df["Experience"].idxmax()])
