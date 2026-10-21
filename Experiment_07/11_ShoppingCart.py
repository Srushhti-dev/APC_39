class ShoppingCart:
    def __init__(self, customer_name, cart_id):
        self.customer_name = customer_name
        self.cart_id = cart_id
        self.products = []

    def add_product(self, name, price, quantity):
        product = {"name": name, "price": price, "quantity": quantity}
        self.products.append(product)
        print(name, "added to cart.")

    def remove_product(self, name):
        for product in self.products:
            if product["name"] == name:
                self.products.remove(product)
                print(name, "removed from cart.")
                return
        print("Product not found.")

    def total_bill(self):
        total = 0
        for product in self.products:
            total += product["price"] * product["quantity"]
        return total

    def display(self):
        print("Customer:", self.customer_name)
        print("Cart ID:", self.cart_id)
        for product in self.products:
            print(product)
        print("Total Bill:", self.total_bill())

    def __del__(self):
        print("Shopping cart object destroyed.")

cart = ShoppingCart("Amit", 101)
cart.add_product("Laptop", 50000, 1)
cart.add_product("Mouse", 1000, 2)
cart.add_product("Keyboard", 2000, 1)
cart.display()
cart.remove_product("Mouse")
cart.display()
