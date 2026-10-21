import pandas as pd

data = {
    "Product_ID": [1, 2, 3, 4, 5],
    "Product_Name": ["Laptop", "Mobile", "Headphones", "Monitor", "Printer"],
    "Category": ["Electronics", "Electronics", "Accessories", "Electronics", "Electronics"],
    "Price": [55000, 20000, 2500, 12000, 9000],
    "Quantity": [3, 4, 10, 5, 2]
}

df = pd.DataFrame(data)
df["Total_Sales"] = df["Price"] * df["Quantity"]

print("DataFrame:\n", df)
print("\nProducts with sales greater than ₹10,000:\n",
      df[df["Total_Sales"] > 10000])
print("\nProduct with maximum sales:\n", df.loc[df["Total_Sales"].idxmax()])
print("\nAverage sales:", df["Total_Sales"].mean())
