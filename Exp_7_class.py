# Create a Student class to store student details and calculate percentage.

class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    def display(self):
        total = sum(self.marks)
        percentage = total / len(self.marks)
        print("Roll No:", self.roll_no)
        print("Name:", self.name)
        print("Marks:", self.marks)
        print("Percentage:", percentage)


students = [
    Student(1, "Rahul", [80, 75, 85, 90, 88]),
    Student(2, "Priya", [90, 85, 92, 88, 95]),
    Student(3, "Amit", [70, 75, 80, 72, 78])
]

for student in students:
    student.display()
    print()


# Create an Employee class to calculate HRA, DA, and gross salary.

class Employee:
    def __init__(self, emp_id, name, basic_salary):
        self.emp_id = emp_id
        self.name = name
        self.basic_salary = basic_salary

    def calculate_hra(self):
        return self.basic_salary * 0.20

    def calculate_da(self):
        return self.basic_salary * 0.10

    def gross_salary(self):
        return self.basic_salary + self.calculate_hra() + self.calculate_da()

    def display(self):
        print("Employee ID:", self.emp_id)
        print("Name:", self.name)
        print("Basic Salary:", self.basic_salary)
        print("HRA:", self.calculate_hra())
        print("DA:", self.calculate_da())
        print("Gross Salary:", self.gross_salary())


employee = Employee(101, "Rahul", 50000)
employee.display()


# Create a Rectangle class to calculate area and perimeter.

class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)


rectangle = Rectangle(10, 5)
print("Area:", rectangle.area())
print("Perimeter:", rectangle.perimeter())


# Create a Circle class to calculate area and circumference.

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

    def circumference(self):
        return 2 * math.pi * self.radius


circle = Circle(7)
print("Area:", circle.area())
print("Circumference:", circle.circumference())


# Create a Book class and display information of three books.

class Book:
    def __init__(self, book_id, title, author, price):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print("Book ID:", self.book_id)
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)


books = [
    Book(1, "Python Basics", "John Smith", 500),
    Book(2, "Data Structures", "Robert Brown", 650),
    Book(3, "Object Oriented Programming", "David Lee", 700)
]

for book in books:
    book.display()
    print()


# Create an ElectricityBill class to calculate the bill according to unit slabs.

class ElectricityBill:
    def __init__(self, consumer_number, consumer_name, units):
        self.consumer_number = consumer_number
        self.consumer_name = consumer_name
        self.units = units

    def calculate_bill(self):
        if self.units <= 100:
            bill = self.units * 2
        elif self.units <= 200:
            bill = 100 * 2 + (self.units - 100) * 3
        elif self.units <= 300:
            bill = 100 * 2 + 100 * 3 + (self.units - 200) * 5
        else:
            bill = 100 * 2 + 100 * 3 + 100 * 5 + (self.units - 300) * 7
        return bill

    def display(self):
        print("Consumer Number:", self.consumer_number)
        print("Consumer Name:", self.consumer_name)
        print("Units Consumed:", self.units)
        print("Electricity Bill:", self.calculate_bill())


bill = ElectricityBill(1001, "Rahul", 250)
bill.display()


# Create a MobilePhone class to display specifications and calculate discounted price.

class MobilePhone:
    def __init__(self, brand, model, storage, price):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.price = price

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Storage:", self.storage)
        print("Price:", self.price)

    def discounted_price(self, discount):
        return self.price - (self.price * discount / 100)


phone = MobilePhone("Samsung", "Galaxy S24", "256 GB", 80000)
phone.display()
print("Price after discount:", phone.discounted_price(10))


# Create a Patient class to display patient information and calculate the total bill.

class Patient:
    def __init__(self, patient_id, name, age, disease, consultation_fee):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.disease = disease
        self.consultation_fee = consultation_fee

    def total_bill(self):
        return self.consultation_fee

    def display(self):
        print("Patient ID:", self.patient_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Disease:", self.disease)
        print("Consultation Fee:", self.consultation_fee)
        print("Total Bill:", self.total_bill())


patient = Patient(101, "Amit", 35, "Fever", 500)
patient.display()


# Create an ATM class to check balance, deposit, withdraw, and display account details using a menu-driven program.

class ATM:
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def check_balance(self):
        print("Balance:", self.balance)

    def deposit(self, amount):
        self.balance += amount
        print("Amount deposited successfully.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn successfully.")
        else:
            print("Insufficient balance.")

    def display_account(self):
        print("Account Number:", self.account_number)
        print("Name:", self.name)
        print("Balance:", self.balance)


atm = ATM(123456, "Rahul", 10000)

while True:
    print("\n1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Display Account Details")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        atm.check_balance()
    elif choice == 2:
        amount = float(input("Enter amount: "))
        atm.deposit(amount)
    elif choice == 3:
        amount = float(input("Enter amount: "))
        atm.withdraw(amount)
    elif choice == 4:
        atm.display_account()
    elif choice == 5:
        print("Thank you.")
        break
    else:
        print("Invalid choice.")


# Create a Vehicle class to rent and return vehicles and calculate rental charges based on the number of days.

class Vehicle:
    def __init__(self, vehicle_number, model, rental_rate, availability=True):
        self.vehicle_number = vehicle_number
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
        self.availability = True
        print("Vehicle returned successfully.")

    def rental_charges(self, days):
        return self.rental_rate * days


vehicle = Vehicle("MH12AB1234", "Swift", 1500)

vehicle.rent()
print("Rental Charges:", vehicle.rental_charges(3))
vehicle.return_vehicle()


# Create a ShoppingCart class to add and remove products, calculate the total bill, and display a destructor message.

class ShoppingCart:
    def __init__(self, customer_name, cart_id):
        self.customer_name = customer_name
        self.cart_id = cart_id
        self.products = {}

    def add_product(self, name, price):
        self.products[name] = price
        print("Product added.")

    def remove_product(self, name):
        if name in self.products:
            del self.products[name]
            print("Product removed.")
        else:
            print("Product not found.")

    def total_bill(self):
        return sum(self.products.values())

    def __del__(self):
        print("Shopping cart object destroyed.")


cart = ShoppingCart("Rahul", 101)

cart.add_product("Laptop", 50000)
cart.add_product("Mouse", 1000)
cart.add_product("Keyboard", 2000)

print("Total Bill:", cart.total_bill())

cart.remove_product("Mouse")
print("Total Bill:", cart.total_bill())


# Create a FoodOrder class to calculate the total bill including tax and display an order completion message using a destructor.

class FoodOrder:
    def __init__(self, order_id, customer_name, food_item, quantity, price):
        self.order_id = order_id
        self.customer_name = customer_name
        self.food_item = food_item
        self.quantity = quantity
        self.price = price

    def total_bill(self):
        amount = self.quantity * self.price
        tax = amount * 0.05
        return amount + tax

    def display(self):
        print("Order ID:", self.order_id)
        print("Customer Name:", self.customer_name)
        print("Food Item:", self.food_item)
        print("Quantity:", self.quantity)
        print("Price:", self.price)
        print("Total Bill:", self.total_bill())

    def __del__(self):
        print("Order completed successfully.")


order = FoodOrder(101, "Priya", "Pizza", 2, 300)
order.display()


# Create a StudentResult class to calculate total, percentage, and grade and display a message using a destructor.

class StudentResult:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def total(self):
        return sum(self.marks)

    def percentage(self):
        return self.total() / 5

    def grade(self):
        percentage = self.percentage()

        if percentage >= 90:
            return "A+"
        elif percentage >= 80:
            return "A"
        elif percentage >= 70:
            return "B"
        elif percentage >= 60:
            return "C"
        elif percentage >= 50:
            return "D"
        else:
            return "F"

    def display(self):
        print("Student Name:", self.name)
        print("Marks:", self.marks)
        print("Total:", self.total())
        print("Percentage:", self.percentage())
        print("Grade:", self.grade())

    def __del__(self):
        print("Student result object destroyed.")


student = StudentResult("Rahul", [85, 90, 78, 88, 92])
student.display()