class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)

r = Rectangle(10, 5)
print("Length:", r.length)
print("Breadth:", r.breadth)
print("Area:", r.area())
print("Perimeter:", r.perimeter())
