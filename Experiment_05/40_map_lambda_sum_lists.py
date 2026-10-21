a = list(map(int, input("Enter first list: ").split()))
b = list(map(int, input("Enter second list: ").split()))

result = list(map(lambda x, y: x + y, a, b))
print("Sum =", result)
