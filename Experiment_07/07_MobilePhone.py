class MobilePhone:
    def __init__(self, brand, model, storage, price):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.price = price

    def display_specs(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Storage:", self.storage)
        print("Price:", self.price)

    def discounted_price(self, discount):
        return self.price - (self.price * discount / 100)

phone = MobilePhone("Samsung", "Galaxy S24", "256 GB", 70000)
phone.display_specs()
discount = 10
print("Discount:", discount, "%")
print("Price after discount:", phone.discounted_price(discount))
