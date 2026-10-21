import pandas as pd

products = {
    "Laptop": 55000,
    "Mouse": 800,
    "Keyboard": 1500,
    "Monitor": 12000,
    "Printer": 9000
}

s = pd.Series(products)

print("Products and prices:\n", s)

increased = s * 1.10
print("\nPrices after 10% increase:\n", increased)

print("\nMost expensive product:")
print(s.idxmax(), "₹", s.max())

print("\nProducts costing more than ₹1,000:\n", s[s > 1000])
