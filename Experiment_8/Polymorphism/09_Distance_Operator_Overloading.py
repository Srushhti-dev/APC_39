class Distance:
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches
        self.normalize()

    def normalize(self):
        self.feet += self.inches // 12
        self.inches %= 12

    def __add__(self, other):
        return Distance(self.feet + other.feet, self.inches + other.inches)

    def display(self):
        print(self.feet, "feet", self.inches, "inches")


d1 = Distance(5, 8)
d2 = Distance(3, 7)
d3 = d1 + d2
d3.display()
