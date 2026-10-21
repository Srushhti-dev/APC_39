import pandas as pd

data = {
    "Student_ID": [101, 102, 103, 104, 105],
    "Student_Name": ["Aarav", "Priya", "Rohan", "Sneha", "Vikram"],
    "Python": [85, 72, 91, 68, 78],
    "DBMS": [80, 75, 88, 70, 82],
    "Mathematics": [90, 70, 84, 76, 79]
}

df = pd.DataFrame(data)
print("DataFrame:\n", df)

df["Total"] = df[["Python", "DBMS", "Mathematics"]].sum(axis=1)
df["Average"] = df[["Python", "DBMS", "Mathematics"]].mean(axis=1)

print("\nWith Total and Average:\n", df)
print("\nStudents with average greater than 75%:\n", df[df["Average"] > 75])
