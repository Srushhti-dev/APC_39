class FoodOrder:
    def __init__(self, order_id, customer_name, food_item, quantity, price):
        self.order_id = order_id
        self.customer_name = customer_name
        self.food_item = food_item
        self.quantity = quantity
        self.price = price

    def total_bill(self):
        subtotal = self.quantity * self.price
        tax = subtotal * 0.05
        return subtotal + tax

    def display(self):
        print("Order ID:", self.order_id)
        print("Customer Name:", self.customer_name)
        print("Food Item:", self.food_item)
        print("Quantity:", self.quantity)
        print("Price per item:", self.price)
        print("Total Bill including 5% tax:", self.total_bill())

    def __del__(self):
        print("Order completed. FoodOrder object destroyed.")

order = FoodOrder(101, "Amit", "Pizza", 2, 300)
order.display()
