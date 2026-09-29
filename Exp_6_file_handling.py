
# FILE HANDLING 

# 1. Create student.txt and write student details.

with open("student.txt", "w") as file:
    file.write("Name: Rahul\n")
    file.write("Roll Number: 101\n")
    file.write("Branch: Computer Science\n")
    file.write("Semester: 3\n")


# 2. Open a text file and display complete contents.

with open("student.txt", "r") as file:
    print(file.read())


# 3. Append additional student information.

with open("student.txt", "a") as file:
    file.write("College: ABC College\n")


# 4. Read a text file line by line.

with open("student.txt", "r") as file:
    for line in file:
        print(line.strip())


# 5. Count total number of lines.

with open("student.txt", "r") as file:
    lines = file.readlines()

print("Total Lines:", len(lines))


# 6. Count total number of words.

with open("student.txt", "r") as file:
    text = file.read()

words = text.split()
print("Total Words:", len(words))


# 7. Count total number of characters including spaces.

with open("student.txt", "r") as file:
    text = file.read()

print("Total Characters:", len(text))


# 8. Read a text file and display lines in reverse order.

with open("student.txt", "r") as file:
    lines = file.readlines()

for line in reversed(lines):
    print(line.strip())


# 9. Count vowels and consonants.

with open("student.txt", "r") as file:
    text = file.read().lower()

vowels = 0
consonants = 0

for ch in text:
    if ch.isalpha():
        if ch in "aeiou":
            vowels += 1
        else:
            consonants += 1

print("Vowels:", vowels)
print("Consonants:", consonants)


# 10. Count alphabets, digits, spaces and special characters.

with open("student.txt", "r") as file:
    text = file.read()

alphabets = digits = spaces = special = 0

for ch in text:
    if ch.isalpha():
        alphabets += 1
    elif ch.isdigit():
        digits += 1
    elif ch.isspace():
        spaces += 1
    else:
        special += 1

print("Alphabets:", alphabets)
print("Digits:", digits)
print("Spaces:", spaces)
print("Special Characters:", special)


# 11. Find the longest word.

with open("student.txt", "r") as file:
    words = file.read().split()

longest = max(words, key=len)
print("Longest Word:", longest)


# 12. Count frequency of each word using dictionary.

with open("student.txt", "r") as file:
    words = file.read().lower().split()

frequency = {}

for word in words:
    word = word.strip(".,!?")
    frequency[word] = frequency.get(word, 0) + 1

print(frequency)


# 13. Search for a word and display occurrences and line numbers.

search_word = input("Enter word to search: ").lower()
count = 0
line_numbers = []

with open("student.txt", "r") as file:
    for line_no, line in enumerate(file, 1):
        words = line.lower().split()
        occurrences = words.count(search_word)

        if occurrences > 0:
            count += occurrences
            line_numbers.append(line_no)

print("Occurrences:", count)
print("Line Numbers:", line_numbers)


# 14. Replace a word with another word.

old_word = input("Enter word to replace: ")
new_word = input("Enter new word: ")

with open("student.txt", "r") as file:
    text = file.read()

text = text.replace(old_word, new_word)

with open("student_new.txt", "w") as file:
    file.write(text)

print("Modified file created.")


# 15. Remove single-line comments from Python source file.

with open("program.py", "r") as source:
    lines = source.readlines()

with open("program_without_comments.py", "w") as target:
    for line in lines:
        stripped = line.lstrip()

        if not stripped.startswith("#"):
            target.write(line)

print("Comments removed.")


# 16. Create another file containing text in uppercase.

with open("student.txt", "r") as file:
    text = file.read()

with open("uppercase.txt", "w") as file:
    file.write(text.upper())

print("Uppercase file created.")


# 17. Student records.

with open("students.csv", "w") as file:
    file.write("RollNo,Name,Marks\n")
    file.write("101,Amit,85\n")
    file.write("102,Priya,92\n")
    file.write("103,Rahul,78\n")

students = []

with open("students.csv", "r") as file:
    next(file)

    for line in file:
        roll, name, marks = line.strip().split(",")
        students.append((int(roll), name, float(marks)))

print("All Records:")
for student in students:
    print(student)

highest = max(students, key=lambda x: x[2])
average = sum(x[2] for x in students) / len(students)

print("Highest Marks:", highest)
print("Average Marks:", average)

print("Students scoring more than 80:")
for student in students:
    if student[2] > 80:
        print(student)


# 18. Employee records.

with open("employees.csv", "w") as file:
    file.write("101,Rahul,IT,60000\n")
    file.write("102,Priya,HR,55000\n")
    file.write("103,Amit,Finance,75000\n")

employees = []

with open("employees.csv", "r") as file:
    for line in file:
        emp_id, name, department, salary = line.strip().split(",")
        employees.append(
            (int(emp_id), name, department, float(salary))
        )

def display_employees():
    for employee in employees:
        print(employee)

def highest_paid():
    return max(employees, key=lambda x: x[3])

def average_salary():
    return sum(x[3] for x in employees) / len(employees)

def above_salary(amount):
    for employee in employees:
        if employee[3] > amount:
            print(employee)

display_employees()
print("Highest Paid:", highest_paid())
print("Average Salary:", average_salary())
print("Employees above 60000:")
above_salary(60000)


# 19. Student attendance.

with open("attendance.txt", "w") as file:
    file.write("101,Rahul,80,100\n")
    file.write("102,Priya,70,100\n")
    file.write("103,Amit,90,100\n")

with open("attendance.txt", "r") as file:
    for line in file:
        roll, name, present, total = line.strip().split(",")

        percentage = (int(present) / int(total)) * 100

        print(name, "Attendance:", percentage, "%")

        if percentage < 75:
            print(name, "has attendance below 75%")


# 20. Deposits and withdrawals.

with open("transactions.txt", "w") as file:
    file.write("deposit,5000\n")
    file.write("withdrawal,1000\n")
    file.write("deposit,3000\n")
    file.write("withdrawal,500\n")

total_deposits = 0
total_withdrawals = 0
transactions = []

with open("transactions.txt", "r") as file:
    for line in file:
        transaction, amount = line.strip().split(",")
        amount = float(amount)

        transactions.append(amount)

        if transaction == "deposit":
            total_deposits += amount
        else:
            total_withdrawals += amount

final_balance = total_deposits - total_withdrawals
largest_transaction = max(transactions)

print("Total Deposits:", total_deposits)
print("Total Withdrawals:", total_withdrawals)
print("Final Balance:", final_balance)
print("Largest Transaction:", largest_transaction)


# 21. Book management.

books = {}

def add_book(book_id, title, author):
    books[book_id] = {
        "title": title,
        "author": author,
        "available": True
    }

def search_book(book_id):
    if book_id in books:
        print(books[book_id])
    else:
        print("Book not found.")

def issue_book(book_id):
    if book_id in books and books[book_id]["available"]:
        books[book_id]["available"] = False
        print("Book issued.")
    else:
        print("Book unavailable.")

def return_book(book_id):
    if book_id in books:
        books[book_id]["available"] = True
        print("Book returned.")

def available_books():
    for book_id, book in books.items():
        if book["available"]:
            print(book_id, book)

add_book(101, "Python", "John")
add_book(102, "Java", "David")

search_book(101)
issue_book(101)
return_book(101)
available_books()


# 22. Combine two text files into a third file.

with open("file1.txt", "r") as file:
    text1 = file.read()

with open("file2.txt", "r") as file:
    text2 = file.read()

with open("file3.txt", "w") as file:
    file.write(text1)
    file.write("\n")
    file.write(text2)

print("Files combined.")


# 23. Compare two text files.

with open("file1.txt", "r") as file:
    lines1 = file.readlines()

with open("file2.txt", "r") as file:
    lines2 = file.readlines()

if lines1 == lines2:
    print("Files are identical.")
else:
    print("Files are different.")

    for i in range(min(len(lines1), len(lines2))):
        if lines1[i] != lines2[i]:
            print("First difference at line:", i + 1)
            break

# MODULE PROGRAMS


# 1. calculator.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    return "Cannot divide by zero"


# main.py

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Addition:", add(a, b))
print("Subtraction:", subtract(a, b))
print("Multiplication:", multiply(a, b))
print("Division:", divide(a, b))


# 2. student.py

def total_marks(marks):
    return sum(marks)

def percentage(marks):
    return sum(marks) / len(marks)

def grade(marks):
    p = percentage(marks)

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
    return "F"


# main.py

marks = [85, 90, 78, 88, 92]

print("Total:", total_marks(marks))
print("Percentage:", percentage(marks))
print("Grade:", grade(marks))


# 3. number_utils.py

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


def is_palindrome(n):
    return str(n) == str(n)[::-1]


def is_armstrong(n):
    digits = str(n)
    total = sum(int(d) ** len(digits) for d in digits)
    return total == n


def is_perfect(n):
    total = 0

    for i in range(1, n):
        if n % i == 0:
            total += i

    return total == n


# main.py

n = int(input("Enter number: "))

print("Prime:", is_prime(n))
print("Palindrome:", is_palindrome(n))
print("Armstrong:", is_armstrong(n))
print("Perfect:", is_perfect(n))


# 4. string_utils.py

def count_vowels(text):
    return sum(1 for ch in text.lower() if ch in "aeiou")

def reverse_string(text):
    return text[::-1]

def is_palindrome(text):
    return text == text[::-1]

def count_words(text):
    return len(text.split())

def remove_spaces(text):
    return text.replace(" ", "")


# main.py

text = input("Enter string: ")

print("Vowels:", count_vowels(text))
print("Reverse:", reverse_string(text))
print("Palindrome:", is_palindrome(text))
print("Words:", count_words(text))
print("Without Spaces:", remove_spaces(text))


# 5. salary.py

def gross_salary(basic):
    hra = basic * 0.20
    da = basic * 0.10
    return basic + hra + da

def deductions(basic):
    return basic * 0.05

def net_salary(basic):
    return gross_salary(basic) - deductions(basic)


# main.py

basic = float(input("Enter basic salary: "))

print("Gross Salary:", gross_salary(basic))
print("Deductions:", deductions(basic))
print("Net Salary:", net_salary(basic))


# 6. recursive.py

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def sum_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_digits(n // 10)


def binary(n):
    if n == 0:
        return ""
    return binary(n // 2) + str(n % 2)


# main.py

n = int(input("Enter number: "))

print("Factorial:", factorial(n))
print("Fibonacci:", fibonacci(n))
print("Sum of Digits:", sum_digits(n))
print("Binary:", binary(n))


# PACKAGE PROGRAMS




# mathutils/basic.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b


# mathutils/number.py

def prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


def armstrong(n):
    digits = str(n)
    return sum(int(d) ** len(digits) for d in digits) == n


def palindrome(n):
    return str(n) == str(n)[::-1]


# mathutils/statistics.py

def mean(numbers):
    return sum(numbers) / len(numbers)

def maximum(numbers):
    return max(numbers)

def minimum(numbers):
    return min(numbers)


# main.py

from mathutils.basic import add
from mathutils.number import prime, armstrong, palindrome
from mathutils.statistics import mean, maximum, minimum

numbers = [10, 20, 30, 40, 50]

print("Addition:", add(10, 20))
print("Prime:", prime(17))
print("Armstrong:", armstrong(153))
print("Palindrome:", palindrome(121))
print("Mean:", mean(numbers))
print("Maximum:", maximum(numbers))
print("Minimum:", minimum(numbers))


# 8. student package



# student/marks.py

def total(marks):
    return sum(marks)

def percentage(marks):
    return sum(marks) / len(marks)


# student/grade.py

def grade(percentage):
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
    return "F"


# student/attendance.py

def eligible(present, total):
    percentage = present / total * 100
    return percentage >= 75


# main.py

from student.marks import total, percentage
from student.grade import grade
from student.attendance import eligible

marks = [80, 85, 90, 75, 88]

p = percentage(marks)

print("Total:", total(marks))
print("Percentage:", p)
print("Grade:", grade(p))
print("Attendance Eligible:", eligible(80, 100))


# 9. banking package

# banking/account.py

class Account:
    def __init__(self, account_no, name, balance):
        self.account_no = account_no
        self.name = name
        self.balance = balance

    def display(self):
        print(self.account_no, self.name, self.balance)


# banking/transaction.py

def deposit(balance, amount):
    return balance + amount

def withdrawal(balance, amount):
    if amount <= balance:
        return balance - amount
    return balance


# banking/loan.py

def loan_amount(principal, rate, years):
    interest = principal * rate * years / 100
    return principal + interest


# main.py

from banking.account import Account
from banking.transaction import deposit, withdrawal
from banking.loan import loan_amount

account = Account(101, "Rahul", 10000)

account.balance = deposit(account.balance, 5000)
account.balance = withdrawal(account.balance, 2000)

account.display()

print("Loan Amount:", loan_amount(100000, 8, 2))


# 10. texttools package



# texttools/cleaning.py

import string

def remove_punctuation(text):
    return text.translate(str.maketrans("", "", string.punctuation))

def remove_extra_spaces(text):
    return " ".join(text.split())


# texttools/tokenization.py

def tokenize(text):
    return text.split()


# texttools/frequency.py

def word_frequency(text):
    frequency = {}

    for word in text.split():
        frequency[word] = frequency.get(word, 0) + 1

    return frequency


# main.py

from texttools.cleaning import remove_punctuation, remove_extra_spaces
from texttools.tokenization import tokenize
from texttools.frequency import word_frequency

text = "Python, is easy. Python is powerful."

text = remove_punctuation(text)
text = remove_extra_spaces(text)

print("Cleaned:", text)
print("Tokens:", tokenize(text))
print("Frequency:", word_frequency(text))


# 11. college_project directory



# student/details.py

def student_details():
    print("Student Name: Rahul")
    print("Roll Number: 101")


# student/marks.py

def student_marks():
    print("Marks: 85")


# faculty/details.py

def faculty_details():
    print("Faculty Name: Professor Sharma")
    print("Department: Computer Science")


# main.py

from student.details import student_details
from student.marks import student_marks
from faculty.details import faculty_details

student_details()
student_marks()
faculty_details()


# 12. Library application


# books/book.py

def add_book(book_id, title):
    return {
        "id": book_id,
        "title": title
    }


# members/member.py

def add_member(member_id, name):
    return {
        "id": member_id,
        "name": name
    }


# transactions/transaction.py

def issue_book(book, member):
    print(book["title"], "issued to", member["name"])


# main.py

from books.book import add_book
from members.member import add_member
from transactions.transaction import issue_book

book = add_book(101, "Python Programming")
member = add_member(1, "Rahul")

issue_book(book, member)


# 13. Ecommerce directory


# products/product.py

def product(name, price):
    return {
        "name": name,
        "price": price
    }


# products/category.py

def category(name):
    return name


# customers/customer.py

def customer(name, email):
    return {
        "name": name,
        "email": email
    }


# customers/address.py

def address(city):
    return city


# orders/order.py

def create_order(product, customer):
    return {
        "product": product,
        "customer": customer
    }


# orders/status.py

def order_status():
    return "Order Confirmed"


# payments/payment.py

def payment(amount):
    print("Payment of", amount, "successful.")


# payments/method.py

def payment_method():
    return "UPI"


# main.py

from products.product import product
from customers.customer import customer
from orders.order import create_order
from orders.status import order_status
from payments.payment import payment
from payments.method import payment_method

p = product("Laptop", 50000)
c = customer("Rahul", "rahul@example.com")

order = create_order(p, c)

print(order)
print(order_status())
print("Payment Method:", payment_method())
payment(p["price"])


# 14. Medical project
#
# medical_project/
#     main.py
#     patient/
#         __init__.py
#         patient.py
#     doctor/
#         __init__.py
#         doctor.py
#     billing/
#         __init__.py
#         bill.py
#     records/
#         __init__.py
#         record.py


# patient/patient.py

def patient_details(patient_id, name, age):
    return {
        "id": patient_id,
        "name": name,
        "age": age
    }


# doctor/doctor.py

def doctor_details(doctor_id, name, department):
    return {
        "id": doctor_id,
        "name": name,
        "department": department
    }


# billing/bill.py

def calculate_bill(consultation_fee, medicine_fee):
    return consultation_fee + medicine_fee


# records/record.py

def medical_record(patient_name, disease, treatment):
    return {
        "patient": patient_name,
        "disease": disease,
        "treatment": treatment
    }


# main.py

from patient.patient import patient_details
from doctor.doctor import doctor_details
from billing.bill import calculate_bill
from records.record import medical_record

patient = patient_details(101, "Rahul", 25)

doctor = doctor_details(
    501,
    "Dr. Sharma",
    "Cardiology"
)

record = medical_record(
    patient["name"],
    "Fever",
    "Medicine"
)

bill = calculate_bill(500, 1000)

print("Patient:", patient)
print("Doctor:", doctor)
print("Medical Record:", record)
print("Total Bill:", bill)