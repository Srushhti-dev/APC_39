#Accept 10 numbers and sort in ascending and descending order
numbers = []

for i in range(10):
    n = int(input("Enter number: "))
    numbers.append(n)

print("Original list:", numbers)

ascending = sorted(numbers)
descending = sorted(numbers, reverse=True)

print("Ascending order:", ascending)
print("Descending order:", descending)