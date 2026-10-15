import pandas as pd
import numpy as np


data = {
    "Product": [
        "Laptop", "Mobile", "Headphones", "Laptop",
        "Mobile", "Keyboard", "Mouse", 
    ],
    "Category": [
        "Electronics", "Electronics", "Accessories", "Electronics",
        "Electronics", "Accessories", "Accessories"
    ],
    "Quantity": [2, 5, 10, 3, 8, 6, 12,],
    "Price": [60000, 25000, 2000, 60000, 25000, 1500, 800]
}

df = pd.DataFrame(data)

df["Sales"] = df["Quantity"] * df["Price"]

print(" SALES DATA:")
print(df)


total_sales = np.sum(df["Sales"])
print("\nTotal Sales:", total_sales)


average_sales = np.mean(df["Sales"])
print("Average Sales:", average_sales)


product_sales = df.groupby("Product")["Quantity"].sum()

best_selling_product = product_sales.idxmax()
best_selling_quantity = product_sales.max()

print("\nBest-Selling Product:", best_selling_product)
print("Quantity Sold:", best_selling_quantity)


category_sales = df.groupby("Category")["Sales"].sum()

print("\n CATEGORY-WISE SALES: ")
print(category_sales)






