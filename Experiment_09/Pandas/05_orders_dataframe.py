import pandas as pd

data = {
    "Order_ID": [1, 2, 3, 4, 5],
    "Customer": ["Amit", "Neha", "Ravi", "Pooja", "Kiran"],
    "Product": ["Laptop", "Phone", "Chair", "Tablet", "Printer"],
    "Quantity": [1, 2, 5, 2, 3],
    "Price": [60000, 25000, 3000, 18000, 8000],
    "Discount": [5000, 3000, 1000, 2000, 1500]
}

df = pd.DataFrame(data)
df["Final_Amount"] = df["Quantity"] * df["Price"] - df["Discount"]

print("All orders:\n", df)
print("\nOrders above ₹5,000:\n", df[df["Final_Amount"] > 5000])
print("\nHighest-value order:\n", df.loc[df["Final_Amount"].idxmax()])
print("\nAverage order value:", df["Final_Amount"].mean())
