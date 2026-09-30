import pandas as pd

# Part A: Retail sales
data = {
    "Product_ID": [101, 102, 103, 104, 105],
    "Product_Name": ["Laptop", "Mobile", "Printer", "Monitor", "Tablet"],
    "Category": ["Electronics", "Electronics", "Electronics", "Electronics", "Electronics"],
    "Price": [50000, 30000, 12000, 15000, 20000],
    "Quantity": [2, 3, 1, 2, 4]
}

df = pd.DataFrame(data)
df["Total_Sales"] = df["Price"] * df["Quantity"]

print("Retail Sales DataFrame:")
print(df)

print("\nProducts with sales greater than 10000:")
print(df[df["Total_Sales"] > 10000])

print("\nProduct with maximum sales:")
print(df.loc[df["Total_Sales"].idxmax()])

print("\nAverage sales:", df["Total_Sales"].mean())

# Part B: Student Series
marks = {
    "Amit": 80,
    "Sneha": 72,
    "Rahul": 90,
    "Priya": 65,
    "Neha": 85
}

series = pd.Series(marks)

print("\nStudent Marks Series:")
print(series)

print("\nMarks of Rahul:", series["Rahul"])
print("Maximum marks:", series.max())
print("Minimum marks:", series.min())
print("Average marks:", series.mean())

print("\nStudents scoring more than 75:")
print(series[series > 75])
