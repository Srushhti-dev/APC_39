
# 33.	Write a lambda function to calculate the square of a given number.
square = lambda x: x * x

n = int(input("Enter number: "))
print("Square:", square(n))

# 34.	Create a lambda function that returns the cube of a number.
cube = lambda x: x ** 3

n = int(input("Enter number: "))
print("Cube:", cube(n))


# 35.	Write a lambda function that returns True if a number is even and False otherwise.
even = lambda x: x % 2 == 0

n = int(input("Enter number: "))
print(even(n))

# 36.	Use a lambda function to find the maximum of two numbers.
maximum = lambda a, b: a if a > b else b

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Maximum:", maximum(a, b))


# 37.	Create a lambda function to calculate simple interest using principal, rate, and time.
simple_interest = lambda p, r, t: (p * r * t) / 100

p = float(input("Enter principal: "))
r = float(input("Enter rate: "))
t = float(input("Enter time: "))

print("Simple Interest:", simple_interest(p, r, t))


# 38.	Take a list of numbers, use map() and a lambda function to generate a list containing their squares.
numbers = list(map(int, input("Enter numbers: ").split()))

squares = list(map(lambda x: x * x, numbers))

print("Squares:", squares)

# 39.	Use map() with lambda to calculate the cube of every element in a list.
numbers = list(map(int, input("Enter numbers: ").split()))

cubes = list(map(lambda x: x ** 3, numbers))

print("Cubes:", cubes)

# 40.	Take two lists of numbers, use map() and lambda to create a third list containing the sum of corresponding elements.
list1 = list(map(int, input("Enter first list: ").split()))
list2 = list(map(int, input("Enter second list: ").split()))

list3 = list(map(lambda x, y: x + y, list1, list2))

print("Third list:", list3)


# # 41.	Take a list of integers, use filter() and lambda to extract all even numbers.list1 = list(map(int, input("Enter first list: ").split()))
list1 = list(map(int, input("Enter first list: ").split()))
list2 = list(map(int, input("Enter second list: ").split()))

list3 = list(map(lambda x, y: x + y, list1, list2))

print("Third list:", list3)

# # 42.	Take a list of integers, use filter() with an appropriate lambda expression to identify prime numbers.
# def is_prime(n):
#     if n < 2:
#         return False

#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False

#     return True


# numbers = list(map(int, input("Enter numbers: ").split()))

# primes = list(filter(lambda x: is_prime(x), numbers))

# print("Prime numbers:", primes)


# 43.	Use filter() and lambda to extract positive numbers from a list.
numbers = list(map(int, input("Enter numbers: ").split()))

positive = list(filter(lambda x: x > 0, numbers))

print("Positive numbers:", positive)


# 44.	Take a list of numbers, use filter() and lambda to find numbers greater than 50.
numbers = list(map(int, input("Enter numbers: ").split()))

result = list(filter(lambda x: x > 50, numbers))

print("Numbers greater than 50:", result)


# 45.	Take a list of words, use filter() and lambda to find words having more than five characters.
words = input("Enter words: ").split()

result = list(filter(lambda x: len(x) > 5, words))

print("Words:", result)


# 46.	Take a list of words; sort them according to their length using lambda.
words = input("Enter words: ").split()

words.sort(key=lambda x: len(x))

print("Sorted words:", words)


# 47.	Take a list of tuples containing student names and marks, sort the students according to their marks using lambda.
students = [
    ("srushhti ", 75),
    ("rushi", 90),
    ("sid", 68),
    ("arya", 82)
]

students.sort(key=lambda x: x[1])

print("Students sorted according to marks:")
print(students)


# 48.	Take employee records containing name and salary, sort them according to salary using lambda.
students = [
    ("rushi", 75),
    ("srushhti", 90),
    ("sid", 68),
    ("Priya", 82)
]

students.sort(key=lambda x: x[1])

print("Students sorted according to marks:")
print(students)


# 49.	Take a list containing student names and marks, use functions and lambda expressions to:
# a)	Calculate average marks. 
# b)	Filter students scoring above 75. 
# c)	Sort students according to marks.

students = [
    ("srushhti", 80),
    ("arya", 92),
    ("rushi", 70),
    ("harsh", 85)
]


def average(students):
    marks = list(map(lambda x: x[1], students))
    return sum(marks) / len(marks)


avg = average(students)


above_75 = list(filter(lambda x: x[1] > 75, students))


sorted_students = sorted(students, key=lambda x: x[1])


print("Average marks:", avg)
print("Students above 75:", above_75)
print("Students sorted according to marks:", sorted_students)


# 50.	Take employee records containing name, department, and salary, use filter(), map(), and sorted() with lambda functions to:
# a)	Find employees earning more than ₹50,000. 
# b)	Increase salaries by 10%. 
# c)	Sort employees according to salary.
employees = [
    ("rushi", "IT", 60000),
    ("arya", "HR", 45000),
    ("aditi", "IT", 75000),
    ("vedika", "Sales", 55000)
]



high_salary = list(
    filter(lambda x: x[2] > 50000, employees)
)

increased_salary = list(
    map(lambda x: (x[0], x[1], x[2] * 1.10), employees)
)


sorted_employees = sorted(
    employees,
    key=lambda x: x[2]
)


print("Employees earning more than 50000:")
print(high_salary)

print("\nAfter 10% salary increase:")
print(increased_salary)

print("\nEmployees sorted according to salary:")
print(sorted_employees)

# 51.	Take a list of products with names, prices, and quantities, use functions and lambda expressions to:
# a)	Calculate total value of each product. 
# b)	Filter products costing more than ₹1,000. 
# c)	Sort products according to total value.
products = [
    ("Laptop", 50000, 2),
    ("Mouse", 500, 3),
    ("Phone", 30000, 2),
    ("Keyboard", 1500, 1)
]


# Function to calculate total value
def total_value(product):
    return product[1] * product[2]



values = list(
    map(lambda x: (x[0], total_value(x)), products)
)

expensive = list(
    filter(lambda x: x[1] > 1000, products)
)

sorted_products = sorted(
    values,
    key=lambda x: x[1]
)


print("Total value of products:")
print(values)

print("\nProducts costing more than 1000:")
print(expensive)

print("\nProducts sorted according to total value:")
print(sorted_products)


# 52.	Write a program using functions, map(), filter(), and lambda expressions to process a list of words and:
# a)	Find the length of every word. 
# b)	Extract words having more than five characters. 
# c)	Sort words according to their length.

words = input("Enter words: ").split()

lengths = list(map(lambda x: len(x), words))

long_words = list(filter(lambda x: len(x) > 5, words))

sorted_words = sorted(
    words,
    key=lambda x: len(x)
)


print("Length of every word:", lengths)
print("Words having more than 5 characters:", long_words)
print("Words sorted according to length:", sorted_words)