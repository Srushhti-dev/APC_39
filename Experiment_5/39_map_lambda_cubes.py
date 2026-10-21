numbers = list(map(int, input("Enter numbers: ").split()))
cubes = list(map(lambda x: x ** 3, numbers))
print("Cubes =", cubes)
