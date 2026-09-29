# Create Employee and Manager classes to display employee/manager details and calculate the manager's annual salary.

class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def display(self):
        print("Employee ID:", self.emp_id)
        print("Name:", self.name)
        print("Salary:", self.salary)


class Manager(Employee):
    def __init__(self, emp_id, name, salary, department):
        super().__init__(emp_id, name, salary)
        self.department = department

    def display(self):
        super().display()
        print("Department:", self.department)

    def annual_salary(self):
        return self.salary * 12


manager = Manager(101, "Rahul", 50000, "IT")
manager.display()
print("Annual Salary:", manager.annual_salary())


# Create Vehicle and Car classes to display vehicle details and calculate the car's discounted price.

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)


class Car(Vehicle):
    def __init__(self, brand, model, fuel_type, price):
        super().__init__(brand, model)
        self.fuel_type = fuel_type
        self.price = price

    def display(self):
        super().display()
        print("Fuel Type:", self.fuel_type)
        print("Price:", self.price)

    def discounted_price(self, discount):
        return self.price - (self.price * discount / 100)


car = Car("Toyota", "Fortuner", "Diesel", 4000000)
car.display()
print("Discounted Price:", car.discounted_price(10))


# Create Academic, Sports, and Student classes using multiple inheritance to calculate the student's overall performance.

class Academic:
    def __init__(self, marks):
        self.marks = marks


class Sports:
    def __init__(self, sports_points):
        self.sports_points = sports_points


class Student(Academic, Sports):
    def __init__(self, marks, sports_points):
        Academic.__init__(self, marks)
        Sports.__init__(self, sports_points)

    def overall_performance(self):
        return self.marks + self.sports_points


student = Student(85, 15)
print("Academic Marks:", student.marks)
print("Sports Points:", student.sports_points)
print("Overall Performance:", student.overall_performance())

## Create PersonalDetails, ProfessionalDetails, and Employee classes using multiple inheritance to display complete employee information.

class PersonalDetails:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class ProfessionalDetails:
    def __init__(self, emp_id, designation, salary):
        self.emp_id = emp_id
        self.designation = designation
        self.salary = salary


class Employee(PersonalDetails, ProfessionalDetails):
    def __init__(self, name, age, emp_id, designation, salary):
        PersonalDetails.__init__(self, name, age)
        ProfessionalDetails.__init__(self, emp_id, designation, salary)

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.emp_id)
        print("Designation:", self.designation)
        print("Salary:", self.salary)


employee = Employee("Rahul", 25, 101, "Software Engineer", 50000)
employee.display()


# Create Person, Student, and ResearchStudent classes using multilevel inheritance to display complete details.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, roll_no, course):
        super().__init__(name, age)
        self.roll_no = roll_no
        self.course = course


class ResearchStudent(Student):
    def __init__(self, name, age, roll_no, course, research_topic, guide_name):
        super().__init__(name, age, roll_no, course)
        self.research_topic = research_topic
        self.guide_name = guide_name

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Roll Number:", self.roll_no)
        print("Course:", self.course)
        print("Research Topic:", self.research_topic)
        print("Guide Name:", self.guide_name)


research_student = ResearchStudent(
    "Priya",
    24,
    102,
    "M.Sc Computer Science",
    "Artificial Intelligence",
    "Dr. Sharma"
)

research_student.display()


# Create BankAccount, SavingsAccount, and PremiumSavingsAccount classes using multilevel inheritance to calculate interest and display account details.

class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance


class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        return self.balance * self.interest_rate / 100


class PremiumSavingsAccount(SavingsAccount):
    def __init__(self, account_number, balance, interest_rate, benefits):
        super().__init__(account_number, balance, interest_rate)
        self.benefits = benefits

    def display(self):
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)
        print("Interest Rate:", self.interest_rate, "%")
        print("Interest:", self.calculate_interest())
        print("Benefits:", self.benefits)


account = PremiumSavingsAccount(
    123456,
    100000,
    6,
    "Free ATM transactions and priority banking"
)

account.display()


# Create a Shape base class and derived Circle, Rectangle, and Triangle classes to calculate their respective areas.

import math

class Shape:
    def display_name(self):
        print("Shape:", self.__class__.__name__)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius


class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


circle = Circle(7)
rectangle = Rectangle(10, 5)
triangle = Triangle(8, 6)

circle.display_name()
print("Area:", circle.area())

rectangle.display_name()
print("Area:", rectangle.area())

triangle.display_name()
print("Area:", triangle.area())

## Create Employee as a base class and Manager, Developer, and Tester as derived classes to calculate salaries using different allowances.

class Employee:
    def __init__(self, emp_id, name, basic_salary):
        self.emp_id = emp_id
        self.name = name
        self.basic_salary = basic_salary

    def display(self):
        print("Employee ID:", self.emp_id)
        print("Name:", self.name)
        print("Basic Salary:", self.basic_salary)


class Manager(Employee):
    def calculate_salary(self):
        allowance = self.basic_salary * 0.40
        return self.basic_salary + allowance

    def display(self):
        super().display()
        print("Manager Allowance: 40%")
        print("Total Salary:", self.calculate_salary())


class Developer(Employee):
    def calculate_salary(self):
        allowance = self.basic_salary * 0.30
        return self.basic_salary + allowance

    def display(self):
        super().display()
        print("Developer Allowance: 30%")
        print("Total Salary:", self.calculate_salary())


class Tester(Employee):
    def calculate_salary(self):
        allowance = self.basic_salary * 0.20
        return self.basic_salary + allowance

    def display(self):
        super().display()
        print("Tester Allowance: 20%")
        print("Total Salary:", self.calculate_salary())


manager = Manager(101, "Rahul", 50000)
developer = Developer(102, "Priya", 45000)
tester = Tester(103, "Amit", 40000)

manager.display()
print()

developer.display()
print()

tester.display()


# Create Person as a base class with Student and Faculty derived from it and TeachingAssistant inheriting from both Student and Faculty.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, roll_no, course):
        super().__init__(name, age)
        self.roll_no = roll_no
        self.course = course


class Faculty(Person):
    def __init__(self, name, age, faculty_id, department):
        super().__init__(name, age)
        self.faculty_id = faculty_id
        self.department = department


class TeachingAssistant(Student, Faculty):
    def __init__(self, name, age, roll_no, course, faculty_id, department):
        Person.__init__(self, name, age)
        self.roll_no = roll_no
        self.course = course
        self.faculty_id = faculty_id
        self.department = department

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Roll Number:", self.roll_no)
        print("Course:", self.course)
        print("Faculty ID:", self.faculty_id)
        print("Department:", self.department)


student = Student("Amit", 21, 101, "Computer Science")
faculty = Faculty("Dr. Sharma", 45, 501, "Computer Science")

teaching_assistant = TeachingAssistant(
    "Rahul",
    24,
    102,
    "MCA",
    502,
    "Computer Science"
)

print("Student Details:")
print(student.name, student.age, student.roll_no, student.course)

print("\nFaculty Details:")
print(faculty.name, faculty.age, faculty.faculty_id, faculty.department)

print("\nTeaching Assistant Details:")
teaching_assistant.display()


# Create Vehicle as a base class with Car and Bike derived from it and SportsCar and ElectricBike further derived from Car and Bike.

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)


class Car(Vehicle):
    def __init__(self, brand, model, fuel_type):
        super().__init__(brand, model)
        self.fuel_type = fuel_type

    def car_info(self):
        print("Fuel Type:", self.fuel_type)


class Bike(Vehicle):
    def __init__(self, brand, model, engine_cc):
        super().__init__(brand, model)
        self.engine_cc = engine_cc

    def bike_info(self):
        print("Engine:", self.engine_cc, "cc")


class SportsCar(Car):
    def __init__(self, brand, model, fuel_type, top_speed):
        super().__init__(brand, model, fuel_type)
        self.top_speed = top_speed

    def display_sports_car(self):
        self.display()
        self.car_info()
        print("Top Speed:", self.top_speed, "km/h")


class ElectricBike(Bike):
    def __init__(self, brand, model, engine_cc, battery_capacity):
        super().__init__(brand, model, engine_cc)
        self.battery_capacity = battery_capacity

    def display_electric_bike(self):
        self.display()
        self.bike_info()
        print("Battery Capacity:", self.battery_capacity, "kWh")


sports_car = SportsCar("Ferrari", "488", "Petrol", 340)
electric_bike = ElectricBike("Revolt", "RV400", 5, 4.5)

print("Sports Car Details:")
sports_car.display_sports_car()

print("\nElectric Bike Details:")
electric_bike.display_electric_bike()


# Create Student as a base class and Result as a derived class to calculate total marks, percentage, and grade.

class Student:
    def __init__(self, roll_no, name, course):
        self.roll_no = roll_no
        self.name = name
        self.course = course


class Result(Student):
    def __init__(self, roll_no, name, course, marks):
        super().__init__(roll_no, name, course)
        self.marks = marks

    def total_marks(self):
        return sum(self.marks)

    def percentage(self):
        return self.total_marks() / len(self.marks)

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
        print("Roll Number:", self.roll_no)
        print("Name:", self.name)
        print("Course:", self.course)
        print("Marks:", self.marks)
        print("Total Marks:", self.total_marks())
        print("Percentage:", self.percentage())
        print("Grade:", self.grade())


result = Result(
    101,
    "Rahul",
    "BCA",
    [85, 90, 78]
)

result.display()

# Create Product and ElectronicProduct classes to calculate the final price after applying a discount.

class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price


class ElectronicProduct(Product):
    def __init__(self, product_id, name, price, brand, warranty):
        super().__init__(product_id, name, price)
        self.brand = brand
        self.warranty = warranty

    def final_price(self, discount):
        return self.price - (self.price * discount / 100)

    def display(self, discount):
        print("Product ID:", self.product_id)
        print("Name:", self.name)
        print("Price:", self.price)
        print("Brand:", self.brand)
        print("Warranty:", self.warranty)
        print("Final Price:", self.final_price(discount))


product = ElectronicProduct(101, "Laptop", 60000, "Dell", "2 Years")
product.display(10)


# Create Printer and Scanner classes and a MultifunctionDevice class using multiple inheritance.

class Printer:
    def print_document(self):
        print("Printing document...")


class Scanner:
    def scan_document(self):
        print("Scanning document...")


class MultifunctionDevice(Printer, Scanner):
    def display(self):
        print("Multifunction device supports printing and scanning.")


device = MultifunctionDevice()
device.display()
device.print_document()
device.scan_document()


# Create Camera and Phone classes and a Smartphone class using multiple inheritance.

class Camera:
    def take_photo(self):
        print("Photograph taken.")


class Phone:
    def make_call(self, number):
        print("Calling:", number)


class Smartphone(Camera, Phone):
    def display(self):
        print("Smartphone supports camera and calling features.")


smartphone = Smartphone()
smartphone.display()
smartphone.take_photo()
smartphone.make_call("9876543210")


# Create Person, Student, and ResearchStudent classes using multilevel inheritance.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, roll_no, course):
        super().__init__(name, age)
        self.roll_no = roll_no
        self.course = course


class ResearchStudent(Student):
    def __init__(self, name, age, roll_no, course, research_topic, guide_name):
        super().__init__(name, age, roll_no, course)
        self.research_topic = research_topic
        self.guide_name = guide_name

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Roll Number:", self.roll_no)
        print("Course:", self.course)
        print("Research Topic:", self.research_topic)
        print("Guide Name:", self.guide_name)


research_student = ResearchStudent(
    "Rahul", 24, 101, "MCA",
    "Artificial Intelligence", "Dr. Sharma"
)

research_student.display()


# Create Animal as a base class and Dog, Cat, and Cow classes with specific sounds and behaviors.

class Animal:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Animal Name:", self.name)


class Dog(Animal):
    def sound(self):
        print("Dog says: Woof Woof")

    def behavior(self):
        print("Dog is loyal.")


class Cat(Animal):
    def sound(self):
        print("Cat says: Meow")

    def behavior(self):
        print("Cat is independent.")


class Cow(Animal):
    def sound(self):
        print("Cow says: Moo")

    def behavior(self):
        print("Cow gives milk.")


dog = Dog("Tommy")
cat = Cat("Kitty")
cow = Cow("Ganga")

dog.display()
dog.sound()
dog.behavior()

cat.display()
cat.sound()
cat.behavior()

cow.display()
cow.sound()
cow.behavior()


# Create Person, Doctor, Patient, Surgeon, and MedicalResearcher classes to demonstrate multiple and hierarchical inheritance.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Doctor(Person):
    def __init__(self, name, age, specialization):
        super().__init__(name, age)
        self.specialization = specialization

    def doctor_details(self):
        print("Doctor:", self.name)
        print("Specialization:", self.specialization)


class Patient(Person):
    def __init__(self, name, age, disease):
        super().__init__(name, age)
        self.disease = disease

    def patient_details(self):
        print("Patient:", self.name)
        print("Disease:", self.disease)


class Surgeon(Doctor, Patient):
    def __init__(self, name, age, specialization, disease):
        Person.__init__(self, name, age)
        self.specialization = specialization
        self.disease = disease

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Specialization:", self.specialization)
        print("Disease:", self.disease)


class MedicalResearcher(Doctor):
    def research(self):
        print(self.name, "is conducting medical research.")


surgeon = Surgeon("Dr. Rahul", 40, "General Surgery", "Appendicitis")
surgeon.display()

researcher = MedicalResearcher("Dr. Priya", 38, "Cardiology")
researcher.doctor_details()
researcher.research()


# Create Shape and derived classes to demonstrate runtime polymorphism using the area() method.

import math

class Shape:
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


shapes = [
    Circle(7),
    Rectangle(10, 5),
    Triangle(8, 6)
]

for shape in shapes:
    print("Area:", shape.area())


# Create Employee and derived classes to calculate salary according to different roles.

class Employee:
    def __init__(self, basic_salary):
        self.basic_salary = basic_salary

    def calculate_salary(self):
        pass


class Manager(Employee):
    def calculate_salary(self):
        return self.basic_salary + self.basic_salary * 0.40


class Developer(Employee):
    def calculate_salary(self):
        return self.basic_salary + self.basic_salary * 0.30


class Tester(Employee):
    def calculate_salary(self):
        return self.basic_salary + self.basic_salary * 0.20


employees = [
    Manager(50000),
    Developer(45000),
    Tester(40000)
]

for employee in employees:
    print("Salary:", employee.calculate_salary())


# Create Vehicle and derived classes to demonstrate different starting behaviors.

class Vehicle:
    def start(self):
        pass


class Car(Vehicle):
    def start(self):
        print("Car starts with a key or push button.")


class Bike(Vehicle):
    def start(self):
        print("Bike starts with a self-start or kick.")


class Bus(Vehicle):
    def start(self):
        print("Bus starts with an ignition key.")


vehicles = [Car(), Bike(), Bus()]

for vehicle in vehicles:
    vehicle.start()


# Create Animal and subclasses to demonstrate polymorphic sound() methods.

class Animal:
    def sound(self):
        pass


class Dog(Animal):
    def sound(self):
        print("Dog: Woof")


class Cat(Animal):
    def sound(self):
        print("Cat: Meow")


class Cow(Animal):
    def sound(self):
        print("Cow: Moo")


class Lion(Animal):
    def sound(self):
        print("Lion: Roar")


animals = [Dog(), Cat(), Cow(), Lion()]

for animal in animals:
    animal.sound()


# Create Notification and derived classes to demonstrate different notification methods.

class Notification:
    def send(self):
        pass


class EmailNotification(Notification):
    def send(self):
        print("Sending notification through Email.")


class SMSNotification(Notification):
    def send(self):
        print("Sending notification through SMS.")


class PushNotification(Notification):
    def send(self):
        print("Sending Push Notification.")


notifications = [
    EmailNotification(),
    SMSNotification(),
    PushNotification()
]

for notification in notifications:
    notification.send()


# Create Student and derived classes to calculate grades using different grading criteria.

class Student:
    def calculate_grade(self, marks):
        pass


class EngineeringStudent(Student):
    def calculate_grade(self, marks):
        if marks >= 90:
            return "A"
        elif marks >= 75:
            return "B"
        elif marks >= 60:
            return "C"
        return "F"


class MedicalStudent(Student):
    def calculate_grade(self, marks):
        if marks >= 85:
            return "A"
        elif marks >= 70:
            return "B"
        elif marks >= 55:
            return "C"
        return "F"


class ManagementStudent(Student):
    def calculate_grade(self, marks):
        if marks >= 80:
            return "A"
        elif marks >= 65:
            return "B"
        elif marks >= 50:
            return "C"
        return "F"


students = [
    EngineeringStudent(),
    MedicalStudent(),
    ManagementStudent()
]

for student in students:
    print(student.calculate_grade(82))


# Create BankAccount and derived classes to calculate interest differently.

class BankAccount:
    def calculate_interest(self, balance):
        pass


class SavingsAccount(BankAccount):
    def calculate_interest(self, balance):
        return balance * 0.06


class CurrentAccount(BankAccount):
    def calculate_interest(self, balance):
        return balance * 0.02


class FixedDepositAccount(BankAccount):
    def calculate_interest(self, balance):
        return balance * 0.08


accounts = [
    SavingsAccount(),
    CurrentAccount(),
    FixedDepositAccount()
]

for account in accounts:
    print("Interest:", account.calculate_interest(100000))


# Create Report and derived classes to demonstrate polymorphic report generation.

class Report:
    def generate(self):
        pass


class PDFReport(Report):
    def generate(self):
        print("Generating PDF report.")


class ExcelReport(Report):
    def generate(self):
        print("Generating Excel report.")


class HTMLReport(Report):
    def generate(self):
        print("Generating HTML report.")


def generate_report(report):
    report.generate()


generate_report(PDFReport())
generate_report(ExcelReport())
generate_report(HTMLReport())


# Create Distance class and overload the + operator to add distances in normalized form.

class Distance:
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches

    def __add__(self, other):
        total_inches = self.feet * 12 + self.inches
        total_inches += other.feet * 12 + other.inches

        feet = total_inches // 12
        inches = total_inches % 12

        return Distance(feet, inches)

    def display(self):
        print(self.feet, "feet", self.inches, "inches")


d1 = Distance(5, 8)
d2 = Distance(4, 10)

d3 = d1 + d2
d3.display()


# Create Student class and overload > and < operators to compare total marks.

class Student:
    def __init__(self, name, total_marks):
        self.name = name
        self.total_marks = total_marks

    def __gt__(self, other):
        return self.total_marks > other.total_marks

    def __lt__(self, other):
        return self.total_marks < other.total_marks


student1 = Student("Rahul", 450)
student2 = Student("Priya", 470)

print("Student 1 has greater marks:", student1 > student2)
print("Student 1 has fewer marks:", student1 < student2)


# Create Product class and overload == and > operators to compare prices.

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        return self.price == other.price

    def __gt__(self, other):
        return self.price > other.price


product1 = Product("Laptop", 60000)
product2 = Product("Mobile", 60000)

print("Prices are equal:", product1 == product2)
print("Product 1 is more expensive:", product1 > product2)


# Create Payment and derived payment classes to demonstrate polymorphism in an online shopping payment system.

class Payment:
    def make_payment(self, amount):
        pass


class UPIPayment(Payment):
    def make_payment(self, amount):
        print("Paid", amount, "using UPI.")


class CardPayment(Payment):
    def make_payment(self, amount):
        print("Paid", amount, "using Card.")


class WalletPayment(Payment):
    def make_payment(self, amount):
        print("Paid", amount, "using Wallet.")


def process_payment(payment, amount):
    payment.make_payment(amount)


process_payment(UPIPayment(), 5000)
process_payment(CardPayment(), 5000)
process_payment(WalletPayment(), 5000)


# Create Person and derived role classes and demonstrate polymorphism using a list of objects.

class Person:
    def display_role(self):
        pass


class Student(Person):
    def display_role(self):
        print("Role: Student")


class Faculty(Person):
    def display_role(self):
        print("Role: Faculty")


class Administrator(Person):
    def display_role(self):
        print("Role: Administrator")


people = [
    Student(),
    Faculty(),
    Administrator()
]

for person in people:
    person.display_role()


# Create Media and derived classes to demonstrate different media playback methods.

class Media:
    def play(self):
        pass


class Audio(Media):
    def play(self):
        print("Playing audio.")


class Video(Media):
    def play(self):
        print("Playing video.")


class Podcast(Media):
    def play(self):
        print("Playing podcast.")


media = [
    Audio(),
    Video(),
    Podcast()
]

for item in media:
    item.play()


# Create SmartDevice and derived device classes with different turn_on and turn_off behaviors.

class SmartDevice:
    def turn_on(self):
        pass

    def turn_off(self):
        pass


class Light(SmartDevice):
    def turn_on(self):
        print("Light turned ON.")

    def turn_off(self):
        print("Light turned OFF.")


class Fan(SmartDevice):
    def turn_on(self):
        print("Fan turned ON.")

    def turn_off(self):
        print("Fan turned OFF.")


class AC(SmartDevice):
    def turn_on(self):
        print("AC turned ON.")

    def turn_off(self):
        print("AC turned OFF.")


class TV(SmartDevice):
    def turn_on(self):
        print("TV turned ON.")

    def turn_off(self):
        print("TV turned OFF.")


devices = [Light(), Fan(), AC(), TV()]

for device in devices:
    device.turn_on()
    device.turn_off()


# Create an abstract Shape class and derived classes that implement the area() method.

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


shapes = [
    Circle(7),
    Rectangle(10, 5),
    Triangle(8, 6)
]

for shape in shapes:
    print("Area:", shape.area())


# Create an abstract Vehicle class with start() and stop() methods and implement them in Car, Bike, and Bus.

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


vehicles = [Car(), Bike(), Bus()]

for vehicle in vehicles:
    vehicle.start()
    vehicle.stop()


# Create an abstract BankAccount class with deposit and withdraw operations.

class BankAccount(ABC):
    def __init__(self, balance=0):
        self.balance = balance

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass


class SavingsAccount(BankAccount):
    def deposit(self, amount):
        self.balance += amount
        print("Savings deposit:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Savings withdrawal:", amount)
        else:
            print("Insufficient balance.")


class CurrentAccount(BankAccount):
    def deposit(self, amount):
        self.balance += amount
        print("Current deposit:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Current withdrawal:", amount)
        else:
            print("Insufficient balance.")


savings = SavingsAccount(10000)
current = CurrentAccount(20000)

savings.deposit(5000)
savings.withdraw(2000)

current.deposit(5000)
current.withdraw(3000)


# Create an abstract FoodOrder class with bill and delivery charge methods and implement different order types.

class FoodOrder(ABC):
    @abstractmethod
    def calculate_bill(self):
        pass

    @abstractmethod
    def delivery_charge(self):
        pass


class RestaurantOrder(FoodOrder):
    def __init__(self, amount):
        self.amount = amount

    def calculate_bill(self):
        return self.amount

    def delivery_charge(self):
        return 0


class HomeDeliveryOrder(FoodOrder):
    def __init__(self, amount):
        self.amount = amount

    def calculate_bill(self):
        return self.amount

    def delivery_charge(self):
        return 50


orders = [
    RestaurantOrder(500),
    HomeDeliveryOrder(500)
]

for order in orders:
    print("Bill:", order.calculate_bill())
    print("Delivery Charge:", order.delivery_charge())


# Create an abstract Patient class and implement billing and treatment methods for different patient types.

class Patient(ABC):
    @abstractmethod
    def calculate_bill(self):
        pass

    @abstractmethod
    def treatment(self):
        pass


class InPatient(Patient):
    def calculate_bill(self):
        return 5000

    def treatment(self):
        print("In-patient receives hospital treatment.")


class OutPatient(Patient):
    def calculate_bill(self):
        return 1000

    def treatment(self):
        print("Out-patient receives consultation.")


class EmergencyPatient(Patient):
    def calculate_bill(self):
        return 10000

    def treatment(self):
        print("Emergency patient receives immediate treatment.")


patients = [
    InPatient(),
    OutPatient(),
    EmergencyPatient()
]

for patient in patients:
    patient.treatment()
    print("Bill:", patient.calculate_bill())


# Create an abstract Transport class and calculate fares for Bus, Train, Taxi, and Flight.

class Transport(ABC):
    @abstractmethod
    def calculate_fare(self, distance):
        pass


class Bus(Transport):
    def calculate_fare(self, distance):
        return distance * 2


class Train(Transport):
    def calculate_fare(self, distance):
        return distance * 1.5


class Taxi(Transport):
    def calculate_fare(self, distance):
        return distance * 10


class Flight(Transport):
    def calculate_fare(self, distance):
        return distance * 15


transports = [
    Bus(),
    Train(),
    Taxi(),
    Flight()
]

for transport in transports:
    print("Fare:", transport.calculate_fare(100))


# Create an abstract Question class and implement answer evaluation for different question types.

class Question(ABC):
    @abstractmethod
    def evaluate_answer(self, answer):
        pass


class MCQQuestion(Question):
    def __init__(self, correct_answer):
        self.correct_answer = correct_answer

    def evaluate_answer(self, answer):
        return answer == self.correct_answer


class TrueFalseQuestion(Question):
    def __init__(self, correct_answer):
        self.correct_answer = correct_answer

    def evaluate_answer(self, answer):
        return answer == self.correct_answer


class DescriptiveQuestion(Question):
    def __init__(self, correct_answer):
        self.correct_answer = correct_answer

    def evaluate_answer(self, answer):
        return answer.lower() == self.correct_answer.lower()


questions = [
    MCQQuestion("B"),
    TrueFalseQuestion(True),
    DescriptiveQuestion("Python")
]

answers = ["B", True, "Python"]

for question, answer in zip(questions, answers):
    print("Correct:", question.evaluate_answer(answer))


# Create an abstract Authentication class and implement password, OTP, and biometric authentication.

class Authentication(ABC):
    @abstractmethod
    def authenticate(self):
        pass


class PasswordAuthentication(Authentication):
    def authenticate(self):
        print("Authenticated using password.")


class OTPAuthentication(Authentication):
    def authenticate(self):
        print("Authenticated using OTP.")


class BiometricAuthentication(Authentication):
    def authenticate(self):
        print("Authenticated using biometric verification.")


authentications = [
    PasswordAuthentication(),
    OTPAuthentication(),
    BiometricAuthentication()
]

for authentication in authentications:
    authentication.authenticate()


# Create an abstract CloudStorage class and implement upload, download, and delete operations.

class CloudStorage(ABC):
    @abstractmethod
    def upload_file(self, filename):
        pass

    @abstractmethod
    def download_file(self, filename):
        pass

    @abstractmethod
    def delete_file(self, filename):
        pass


class GoogleDrive(CloudStorage):
    def upload_file(self, filename):
        print("Uploaded", filename, "to Google Drive.")

    def download_file(self, filename):
        print("Downloaded", filename, "from Google Drive.")

    def delete_file(self, filename):
        print("Deleted", filename, "from Google Drive.")


class Dropbox(CloudStorage):
    def upload_file(self, filename):
        print("Uploaded", filename, "to Dropbox.")

    def download_file(self, filename):
        print("Downloaded", filename, "from Dropbox.")

    def delete_file(self, filename):
        print("Deleted", filename, "from Dropbox.")


storage = [
    GoogleDrive(),
    Dropbox()
]

for service in storage:
    service.upload_file("document.pdf")
    service.download_file("document.pdf")
    service.delete_file("document.pdf")


# Create an abstract Appointment class and implement booking and fee calculation for different appointment types.

class Appointment(ABC):
    @abstractmethod
    def book_appointment(self):
        pass

    @abstractmethod
    def calculate_fee(self):
        pass


class GeneralAppointment(Appointment):
    def book_appointment(self):
        print("General appointment booked.")

    def calculate_fee(self):
        return 500


class SpecialistAppointment(Appointment):
    def book_appointment(self):
        print("Specialist appointment booked.")

    def calculate_fee(self):
        return 1000


class EmergencyAppointment(Appointment):
    def book_appointment(self):
        print("Emergency appointment booked.")

    def calculate_fee(self):
        return 2000


appointments = [
    GeneralAppointment(),
    SpecialistAppointment(),
    EmergencyAppointment()
]

for appointment in appointments:
    appointment.book_appointment()
    print("Fee:", appointment.calculate_fee())