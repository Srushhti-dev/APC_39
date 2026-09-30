# Accept 10 numbers from the user and store them in a list. Calculate:Sum ,Average 
numbers = []

for i in range(10):
    num = int(input("Enter number: "))
    numbers.append(num)

total = sum(numbers)

average = total / 10

print("Sum:", total)
print("Average:", average)