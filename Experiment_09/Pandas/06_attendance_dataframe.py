import pandas as pd

data = {
    "Student_ID": [101, 102, 103, 104, 105],
    "Name": ["Aarav", "Priya", "Rohan", "Sneha", "Vikram"],
    "Department": ["CSE", "IT", "CSE", "ECE", "IT"],
    "Total_Classes": [100, 90, 80, 100, 120],
    "Classes_Attended": [80, 60, 75, 92, 85]
}

df = pd.DataFrame(data)
df["Attendance_Percentage"] = (
    df["Classes_Attended"] / df["Total_Classes"] * 100
)

print(df)
print("\nStudents with attendance below 75%:\n",
      df[df["Attendance_Percentage"] < 75])
