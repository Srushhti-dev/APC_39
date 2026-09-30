#Find the second largest element
numbers = [10, 25, 50, 40, 60, 30]

unique = list(set(numbers))
unique.sort()

print("Second largest element:", unique[-2])