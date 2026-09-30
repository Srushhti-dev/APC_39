import pandas as pd

data = {
    "Order_ID": [1, 2, 3, 4, 5],
    "Customer": ["Amit", "Priya", "Rahul", "Sneha", "Neha"],
    "Product": ["Laptop", "Mobile", "Tablet", "Headphones", "Monitor"],
    "Quantity": [1, 2, 3, 5, 2],
    "Price": [60000, 25000, 15000, 2000, 12000],
    "Discount": [5000, 3000, 2000, 500, 1000]
}

df = pd.DataFrame(data)

df["Final_Amount"] = df["Quantity"] * df["Price"] - df["Discount"]

print("All orders:")
print(df)

print("\nOrders above 5000:")
print(df[df["Final_Amount"] > 5000])

print("\nHighest-value order:")
print(df.loc[df["Final_Amount"].idxmax()])

print("\nAverage order value:", df["Final_Amount"].mean())
