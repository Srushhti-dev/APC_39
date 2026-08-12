cart = []

while True:
    print("\n1. Add item")
    print("2. Remove item")
    print("3. Search item")
    print("4. Display cart")
    print("5. Count total items")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        item = input("Enter item to add: ")
        cart.append(item)
        print("Item added.")

    elif choice == 2:
        item = input("Enter item to remove: ")
        if item in cart:
            cart.remove(item)
            print("Item removed.")
        else:
            print("Item not found.")

    elif choice == 3:
        item = input("Enter item to search: ")
        if item in cart:
            print("Item is available.")
        else:
            print("Item not found.")

    elif choice == 4:
        print("Shopping Cart:", cart)

    elif choice == 5:
        print("Total items:", len(cart))

    elif choice == 6:
        break

    else:
        print("Invalid choice.")