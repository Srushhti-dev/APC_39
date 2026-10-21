from abc import ABC, abstractmethod

class FoodOrder(ABC):
    @abstractmethod
    def calculate_bill(self):
        pass

    @abstractmethod
    def delivery_charge(self):
        pass


class RestaurantOrder(FoodOrder):
    def __init__(self, food_price):
        self.food_price = food_price

    def calculate_bill(self):
        return self.food_price

    def delivery_charge(self):
        return 0


class HomeDeliveryOrder(FoodOrder):
    def __init__(self, food_price):
        self.food_price = food_price

    def calculate_bill(self):
        return self.food_price

    def delivery_charge(self):
        return 50


for order in [RestaurantOrder(500), HomeDeliveryOrder(500)]:
    print("Food Bill:", order.calculate_bill())
    print("Delivery Charge:", order.delivery_charge())
    print("Total:", order.calculate_bill() + order.delivery_charge())
