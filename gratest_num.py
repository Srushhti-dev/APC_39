#3.	Define a function that accepts two numbers and returns the greater number.
def grater_number(n1,n2):
    if n1 > n2:
        return "grater number:"
    return n2
n1 = int(input("enter number1:"))
n2 = int(input("enter number2:"))
print("grater number is:",grater_number(n1,n2))