class Vehicle:
    def __init__(self, vehicle_no, model, rental_rate, availability=True):
        self.vehicle_no = vehicle_no
        self.model = model
        self.rental_rate = rental_rate
        self.availability = availability

    def rent(self):
        if self.availability:
            self.availability = False
            print("Vehicle rented successfully.")
        else:
            print("Vehicle is not available.")

    def return_vehicle(self):
        if not self.availability:
            self.availability = True
            print("Vehicle returned successfully.")
        else:
            print("Vehicle was not rented.")

    def calculate_charges(self, days):
        return self.rental_rate * days

    def display(self):
        print("Vehicle Number:", self.vehicle_no)
        print("Model:", self.model)
        print("Rental Rate:", self.rental_rate)
        print("Available:", self.availability)

vehicle = Vehicle("MH12AB1234", "Honda City", 2000)
vehicle.display()
vehicle.rent()
days = 3
print("Rental Charges:", vehicle.calculate_charges(days))
vehicle.return_vehicle()
vehicle.display()
