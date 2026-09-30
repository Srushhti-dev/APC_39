numbers = (50, 20, 80, 10, 40, 30)

ascending = tuple(sorted(numbers))
descending = tuple(sorted(numbers, reverse=True))

print("Original tuple:", numbers)
print("Ascending order:", ascending)
print("Descending order:", descending)