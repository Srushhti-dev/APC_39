import pandas as pd

df = pd.read_csv("students.csv")

print("First 5 records:\n", df.head())
print("\nLast 5 records:\n", df.tail())

subjects = ["Python", "DBMS", "Maths"]
df["Total"] = df[subjects].sum(axis=1)
df["Average"] = df[subjects].mean(axis=1)

print("\nTotal and average marks:\n", df[["Student_ID", "Name", "Total", "Average"]])
print("\nStudents with average greater than 75:\n", df[df["Average"] > 75])
print("\nStudent with highest average:\n", df.loc[df["Average"].idxmax()])
print("\nAverage marks for each subject:\n", df[subjects].mean())
