class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def display(self):
        print("Brand:", self.brand)


class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def drive(self):
        print("Car is driving.")


class Bike(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def ride(self):
        print("Bike is riding.")


class SportsCar(Car):
    def __init__(self, brand, model, top_speed):
        super().__init__(brand, model)
        self.top_speed = top_speed

    def show_speed(self):
        print("Sports Car Top Speed:", self.top_speed, "km/h")


class ElectricBike(Bike):
    def __init__(self, brand, model, battery):
        super().__init__(brand, model)
        self.battery = battery

    def show_battery(self):
        print("Battery:", self.battery, "kWh")


sports_car = SportsCar("Ferrari", "F8", 340)
sports_car.display()
sports_car.drive()
sports_car.show_speed()

print()
bike = ElectricBike("Ather", "450X", 3.7)
bike.display()
bike.ride()
bike.show_battery()
