import pandas as pd

data = {
    "Student_ID": [101, 102, 103, 104, 105],
    "Name": ["Amit", "Sneha", "Rahul", "Priya", "Neha"],
    "Department": ["CSE", "IT", "CSE", "IT", "CSE"],
    "Total_Classes": [100, 100, 120, 80, 90],
    "Classes_Attended": [90, 70, 85, 75, 60]
}

df = pd.DataFrame(data)

df["Attendance_Percentage"] = (
    df["Classes_Attended"] / df["Total_Classes"]
) * 100

print("Attendance:")
print(df)

print("\nStudents with attendance below 75%:")
print(df[df["Attendance_Percentage"] < 75])
