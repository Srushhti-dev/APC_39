products = [
    ("Laptop", 50000, 2),
    ("Mouse", 800, 3),
    ("Keyboard", 1500, 2),
    ("Monitor", 12000, 1)
]

total_values = list(
    map(lambda x: (x[0], x[1], x[2], x[1] * x[2]), products)
)

expensive = list(filter(lambda x: x[1] > 1000, products))

sorted_products = sorted(total_values, key=lambda x: x[3])

print("Total Values:", total_values)
print("Products > 1000:", expensive)
print("Sorted by Total Value:", sorted_products)
