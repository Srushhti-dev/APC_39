from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):
    def start(self):
        print("Car started.")

    def stop(self):
        print("Car stopped.")


class Bike(Vehicle):
    def start(self):
        print("Bike started.")

    def stop(self):
        print("Bike stopped.")


class Bus(Vehicle):
    def start(self):
        print("Bus started.")

    def stop(self):
        print("Bus stopped.")


for vehicle in [Car(), Bike(), Bus()]:
    vehicle.start()
    vehicle.stop()
