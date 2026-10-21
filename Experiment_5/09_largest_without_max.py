def largest(numbers):
    large = numbers[0]
    for n in numbers:
        if n > large:
            large = n
    return large

numbers = list(map(int, input("Enter numbers: ").split()))
print("Largest =", largest(numbers))
