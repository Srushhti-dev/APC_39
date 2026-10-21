class Vehicle:
    def start(self):
        pass


class Car(Vehicle):
    def start(self):
        print("Car starts with a key/button.")


class Bike(Vehicle):
    def start(self):
        print("Bike starts with self-start/kick.")


class Bus(Vehicle):
    def start(self):
        print("Bus starts with a heavy diesel engine.")


for vehicle in [Car(), Bike(), Bus()]:
    vehicle.start()
