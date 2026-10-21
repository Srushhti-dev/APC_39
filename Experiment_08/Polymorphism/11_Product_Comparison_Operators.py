class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        return self.price == other.price

    def __gt__(self, other):
        return self.price > other.price


p1 = Product("Laptop", 60000)
p2 = Product("Phone", 60000)
p3 = Product("Tablet", 30000)

print("Laptop == Phone:", p1 == p2)
print("Laptop > Tablet:", p1 > p3)
