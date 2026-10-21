num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1 >= num2 and num1 >= num3:
    print("Largest =", num1)
elif num2 >= num1 and num2 >= num3:
    print("Largest =", num2)
else:
    print("Largest =", num3)

if num1 <= num2 and num1 <= num3:
    print("Smallest =", num1)
elif num2 <= num1 and num2 <= num3:
    print("Smallest =", num2)
else:
    print("Smallest =", num3)