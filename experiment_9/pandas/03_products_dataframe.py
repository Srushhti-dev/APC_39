import pandas as pd

data = {
    "Product_ID": [101, 102, 103, 104, 105],
    "Product_Name": ["Laptop", "Mouse", "Keyboard", "Monitor", "Printer"],
    "Category": ["Electronics", "Accessories", "Accessories", "Electronics", "Electronics"],
    "Price": [55000, 800, 1500, 12000, 9000],
    "Quantity": [3, 20, 15, 5, 4]
}

df = pd.DataFrame(data)
df["Total_Amount"] = df["Price"] * df["Quantity"]

print(df)
print("\nProduct with highest total sales:")
print(df.loc[df["Total_Amount"].idxmax()])
