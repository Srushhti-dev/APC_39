products = {"Laptop": 15, "Mouse": 8, "Keyboard": 20}

name = input("Enter product to add: ")
quantity = int(input("Enter quantity: "))
products[name] = quantity

name = input("Enter product to update: ")
if name in products:
    quantity = int(input("Enter new quantity: "))
    products[name] = quantity

name = input("Enter product to delete: ")
if name in products:
    del products[name]

name = input("Enter product to search: ")
if name in products:
    print("Quantity:", products[name])
else:
    print("Product not found")

print("Products with quantity below 10:")
for name, quantity in products.items():
    if quantity < 10:
        print(name, quantity)
