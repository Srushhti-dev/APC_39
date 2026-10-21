cart = ["Milk", "Bread", "Rice"]

cart.append("Apple")

cart.remove("Bread")

item = input("Search item: ")

if item in cart:
    print("Item found")
else:
    print("Item not found")

print("Cart:", cart)
print("Total items:", len(cart))