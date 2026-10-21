numbers = list(map(int, input("Enter numbers: ").split()))
squares = list(map(lambda x: x * x, numbers))
print("Squares =", squares)
