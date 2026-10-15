import pandas as pd

prices = {
    "Laptop": 50000,
    "Mouse": 800,
    "Keyboard": 1500,
    "Monitor": 12000,
    "Headphones": 2000
}

series = pd.Series(prices)

print("Products and prices:")
print(series)

series = series * 1.10

print("\nPrices after 10% increase:")
print(series)

print("\nMost expensive product:")
print(series.idxmax(), "=", series.max())

print("\nProducts costing more than 1000:")
print(series[series > 1000])
