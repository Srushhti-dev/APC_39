numbers = list(map(int, input("Enter numbers: ").split()))
even = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers =", even)
