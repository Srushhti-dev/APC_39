#4.	Create a function simple_interest(p, r, t) to calculate simple interest.
def simple_interest(p, r, t):
    return (p * r * t) / 100

p = float(input("Principal: "))
r = float(input("Rate: "))
t = float(input("Time: "))

print("Simple Interest:", simple_interest(p, r, t))


#5.	Write a function is_prime(n) that returns True if a number is prime; otherwise, returns False.
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input("Enter number: "))
print(is_prime(n))


#6.	Define a function to calculate the area of a circle using its radius.
def circle_area(r):
    return 3.142*r*r
r = int(input("enter a radius:"))
print("area of circle is:",circle_area(r))


#7.	Write a function that accepts n and returns the sum of the first n natural numbers.
def natural_numbers(n):
    return n *(n+1) /2
n = int(input("enter a number:"))
print("sum is:",natural_numbers(n))


#8.	Create a function power(base, exponent) to calculate the value of base raised to exponent.
def power(base, exponent):
    return base ** exponent

b = int(input("Enter base: "))
e = int(input("Enter exponent: "))

print("Result:", power(b, e))


#9.	Write a function that accepts a list of numbers and returns the largest element without using the built-in max() function.
def largest(lst):
    large = lst[0]

    for x in lst:
        if x > large:
            large = x

    return large

lst = list(map(int, input("Enter numbers: ").split()))
print("Largest:", largest(lst))


#10.	Define a function that accepts a string and returns the number of vowels present in it.
def count_vowels(s):
    count = 0

    for ch in s.lower():
        if ch in "aeiou":
            count += 1

    return count

s = input("Enter string: ")
print("Vowels:", count_vowels(s))


#11.	Write a function that accepts a string and returns its reverse.
def reverse_string(s):
    return s[::-1]

s = input("Enter string: ")
print("Reverse:", reverse_string(s))


#12.	Create a function that checks whether a given string or number is a palindrome.
def palindrome(s):
    
    s = str(s)
    return s == s[::-1]

x = input("Enter string or number: ")

if palindrome(s):
    print("Palindrome")
else:
    print("Not Palindrome")


#13.	Write a function that accepts a list of numbers and returns their average.
def average(lst):
    return sum(lst) / len(lst)

lst = list(map(float, input("Enter numbers: ").split()))
print("Average:", average(lst))

#14.	Define a function that accepts a list and an element and returns the number of times that element occurs.
def count_occurrences(lst, element):
    count = 0

    for x in lst:
        if x == element:
            count += 1

    return count

lst = list(map(int, input("Enter numbers: ").split()))
element = int(input("Enter element: "))

print("Occurrences:", count_occurrences(lst, element))


# #15.	Write a function that accepts a list and returns a new list containing only unique elements.
def unique_elements(lst):
    result = []

    for x in lst:
        if x not in result:
            result.append(x)

    return result

lst = list(map(int, input("Enter numbers: ").split()))
print("Unique:", unique_elements(lst))


# 16.	Create a function to find the second-largest number in a list.
def second_largest(lst):
    unique = list(set(lst))
    unique.sort()

    return unique[-2]

lst = list(map(int, input("Enter numbers: ").split()))

print("Second Largest:", second_largest(lst))


# 17.	Write a function that accepts n and returns the first n Fibonacci numbers.
def fibonacci(n):
    a, b = 0, 1
    result = []

    for i in range(n):
        result.append(a)
        a, b = b, a + b

    return result

n = int(input("Enter n: "))
print(fibonacci(n))


# 18.	Create a function that accepts marks in five subjects and returns the student's percentage and grade.
def result(marks):
    total = sum(marks)
    percentage = total / 5

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    return percentage, grade

marks = []

for i in range(5):
    marks.append(float(input("Enter marks: ")))

percentage, grade = result(marks)

print("Percentage:", percentage)
print("Grade:", grade)


# 19.	Write a function that accepts the number of units consumed and calculates the electricity bill according to predefined slabs.
def electricity_bill(units):
    if units <= 100:
        bill = units * 5
    elif units <= 200:
        bill = 100 * 5 + (units - 100) * 7
    elif units <= 300:
        bill = 100 * 5 + 100 * 7 + (units - 200) * 10
    else:
        bill = 100 * 5 + 100 * 7 + 100 * 10 + (units - 300) * 12

    return bill

units = float(input("Enter units: "))
print("Electricity Bill:", electricity_bill(units))


# 20.	Write a function that accepts basic salary and calculates gross salary after adding HRA and DA.
def gross_salary(basic):
    hra = basic * 0.20
    da = basic * 0.10
    return basic + hra + da

basic = float(input("Enter basic salary: "))
print("Gross Salary:", gross_salary(basic))


# 21.	Create a function that accepts item prices and quantities and returns the total bill after applying a discount.
def total_bill(prices, quantities):
    total = 0

    for i in range(len(prices)):
        total += prices[i] * quantities[i]

    if total >= 5000:
        discount = total * 0.20
    elif total >= 2000:
        discount = total * 0.10
    else:
        discount = 0

    return total - discount

prices = list(map(float, input("Enter prices: ").split()))
quantities = list(map(int, input("Enter quantities: ").split()))

print("Final Bill:", total_bill(prices, quantities))


# 22.	Write a function that accepts a list of numbers and returns the minimum, maximum, sum, and average.

def statistics(lst):
    minimum = min(lst)
    maximum = max(lst)
    total = sum(lst)
    avg = total / len(lst)

    return minimum, maximum, total, avg

lst = list(map(float, input("Enter numbers: ").split()))

a, b, c, d = statistics(lst)

print("Minimum:", a)
print("Maximum:", b)
print("Sum:", c)
print("Average:", d)


# 23.	Write a program using separate functions to process student records containing name, roll number, and marks in five subjects. Calculate total, percentage, grade, class average, highest scorer, and lowest scorer.
def total(marks):
    return sum(marks)

def percentage(marks):
    return sum(marks) / 5

def grade(p):
    if p >= 90:
        return "A+"
    elif p >= 80:
        return "A"
    elif p >= 70:
        return "B"
    elif p >= 60:
        return "C"
    elif p >= 50:
        return "D"
    else:
        return "F"


students = []

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter name: ")
    roll = input("Enter roll number: ")

    marks = []
    for j in range(5):
        marks.append(float(input("Enter marks: ")))

    t = total(marks)
    p = percentage(marks)
    g = grade(p)

    students.append({
        "name": name,
        "roll": roll,
        "marks": marks,
        "total": t,
        "percentage": p,
        "grade": g
    })


class_average = sum(s["percentage"] for s in students) / n

# Find highest and lowest without lambda
highest = students[0]
lowest = students[0]

for s in students:
    if s["percentage"] > highest["percentage"]:
        highest = s

    if s["percentage"] < lowest["percentage"]:
        lowest = s


for s in students:
    print("\nName:", s["name"])
    print("Roll:", s["roll"])
    print("Total:", s["total"])
    print("Percentage:", s["percentage"])
    print("Grade:", s["grade"])

print("\nClass Average:", class_average)
print("Highest Scorer:", highest["name"])
print("Lowest Scorer:", lowest["name"])


# 24.	Create functions for deposit, withdrawal, balance enquiry, and transaction history. Prevent withdrawal when the balance is insufficient and maintain a transaction record.

balance = 0
transactions = []


def deposit(amount):
    global balance
    balance += amount
    transactions.append("Deposited: " + str(amount))


def withdrawal(amount):
    global balance

    if amount <= balance:
        balance -= amount
        transactions.append("Withdrawn: " + str(amount))
        print("Withdrawal successful")
    else:
        print("Insufficient balance")


def balance_enquiry():
    print("Balance:", balance)


def transaction_history():
    print("\nTransaction History:")
    for t in transactions:
        print(t)


while True:
    print("\n1. Deposit")
    print("2. Withdrawal")
    print("3. Balance Enquiry")
    print("4. Transaction History")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        amount = float(input("Enter amount: "))
        deposit(amount)

    elif choice == 2:
        amount = float(input("Enter amount: "))
        withdrawal(amount)

    elif choice == 3:
        balance_enquiry()

    elif choice == 4:
        transaction_history()

    elif choice == 5:
        break

    else:
        print("Invalid choice")


# 25.	Create functions to add books, issue books, return books, search books, and display available books. Maintain book availability using dictionaries.
books = {}


def add_book(book):
    books[book] = True
    print("Book added")


def issue_book(book):
    if book in books and books[book]:
        books[book] = False
        print("Book issued")
    else:
        print("Book unavailable")


def return_book(book):
    if book in books:
        books[book] = True
        print("Book returned")
    else:
        print("Book not found")


def search_book(book):
    if book in books:
        print("Book found")
    else:
        print("Book not found")


def display_books():
    print("\nAvailable Books:")
    for book, available in books.items():
        if available:
            print(book)


add_book("Python")
add_book("Java")
add_book("C++")

issue_book("Python")
return_book("Python")
search_book("Java")
display_books()

# 26.	Develop a modular program using functions to calculate electricity bills using different consumption slabs. Include fixed charges, taxes, and discounts.

def calculate_units(units):
    if units <= 100:
        return units * 5
    elif units <= 200:
        return 500 + (units - 100) * 7
    elif units <= 300:
        return 1200 + (units - 200) * 10
    else:
        return 2200 + (units - 300) * 12


def fixed_charge():
    return 100


def calculate_tax(amount):
    return amount * 0.05


def discount(amount):
    if amount > 5000:
        return amount * 0.10
    return 0


def final_bill(units):
    energy = calculate_units(units)
    fixed = fixed_charge()
    subtotal = energy + fixed
    tax = calculate_tax(subtotal)
    disc = discount(subtotal)

    return subtotal + tax - disc


units = float(input("Enter units consumed: "))

print("Final Electricity Bill:", final_bill(units))


# 27.	Create functions to calculate consultation charges, laboratory charges, medicine charges, room charges, and final bill. Apply discounts based on patient category.

def consultation(category):
    return 500 if category == "general" else 300


def laboratory():
    return 1000


def medicine():
    return 1500


def room():
    return 2000


def final_bill(category):
    total = consultation(category) + laboratory() + medicine() + room()

    if category == "senior":
        discount = total * 0.20
    elif category == "general":
        discount = total * 0.10
    else:
        discount = 0

    return total - discount


category = input("Enter category (general/senior): ").lower()

print("Final Hospital Bill:", final_bill(category))


# 28.	Implement functions to add/remove products, calculate subtotal, apply coupon discounts, calculate GST, and generate the final invoice.
products = {}


def add_product(name, price, quantity):
    products[name] = [price, quantity]


def remove_product(name):
    if name in products:
        del products[name]


def subtotal():
    total = 0

    for price, quantity in products.values():
        total += price * quantity

    return total


def coupon_discount(amount, coupon):
    if coupon == "SAVE10":
        return amount * 0.10
    return 0


def gst(amount):
    return amount * 0.18


def invoice(coupon):
    sub = subtotal()
    discount = coupon_discount(sub, coupon)
    taxable = sub - discount
    tax = gst(taxable)

    return taxable + tax


add_product("Laptop", 50000, 1)
add_product("Mouse", 1000, 2)

coupon = input("Enter coupon: ")

print("Final Invoice:", invoice(coupon))


# 29.	Write a recursive function to search for an element in a sorted list using binary search.

# 30.	Convert a decimal number into binary using recursion without using Python's built-in conversion functions.

# 31.	Check whether a string is a palindrome using recursion.
products = {}


def add_product(name, price, quantity):
    products[name] = [price, quantity]


def remove_product(name):
    if name in products:
        del products[name]


def subtotal():
    total = 0

    for price, quantity in products.values():
        total += price * quantity

    return total


def coupon_discount(amount, coupon):
    if coupon == "SAVE10":
        return amount * 0.10
    return 0


def gst(amount):
    return amount * 0.18


def invoice(coupon):
    sub = subtotal()
    discount = coupon_discount(sub, coupon)
    taxable = sub - discount
    tax = gst(taxable)

    return taxable + tax


add_product("Laptop", 50000, 1)
add_product("Mouse", 1000, 2)

coupon = input("Enter coupon: ")

print("Final Invoice:", invoice(coupon))


# 32.	Create separate functions for addition, subtraction, multiplication, and division. Pass these functions as arguments to another function called calculate().
def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    return a / b


def calculate(operation, a, b):
    return operation(a, b)


a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Addition:", calculate(addition, a, b))
print("Subtraction:", calculate(subtraction, a, b))
print("Multiplication:", calculate(multiplication, a, b))
print("Division:", calculate(division, a, b))
