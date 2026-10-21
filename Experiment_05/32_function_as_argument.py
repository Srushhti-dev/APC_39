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

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Addition =", calculate(addition, a, b))
print("Subtraction =", calculate(subtraction, a, b))
print("Multiplication =", calculate(multiplication, a, b))
print("Division =", calculate(division, a, b))
