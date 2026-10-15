import pandas as pd

data = {
    "Student_ID": [101, 102, 103, 104, 105],
    "Student_Name": ["Amit", "Sneha", "Rahul", "Priya", "Neha"],
    "Python": [80, 72, 90, 65, 85],
    "DBMS": [75, 80, 88, 70, 82],
    "Mathematics": [85, 78, 92, 68, 80]
}

df = pd.DataFrame(data)

print("DataFrame:")
print(df)

df["Total"] = df["Python"] + df["DBMS"] + df["Mathematics"]
df["Average"] = df["Total"] / 3

print("\nTotal and Average:")
print(df[["Student_ID", "Student_Name", "Total", "Average"]])

print("\nStudents with average greater than 75:")
print(df[df["Average"] > 75])
