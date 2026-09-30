import pandas as pd

data = {
    "Product_ID": [101, 102, 103, 104, 105],
    "Product_Name": ["Laptop", "Mouse", "Keyboard", "Monitor", "Printer"],
    "Category": ["Electronics", "Accessories", "Accessories", "Electronics", "Electronics"],
    "Price": [50000, 800, 1500, 12000, 8000],
    "Quantity": [2, 10, 8, 5, 3]
}

df = pd.DataFrame(data)

df["Total_Amount"] = df["Price"] * df["Quantity"]

print("DataFrame:")
print(df)

print("\nProduct with highest total sales:")
print(df.loc[df["Total_Amount"].idxmax()])
