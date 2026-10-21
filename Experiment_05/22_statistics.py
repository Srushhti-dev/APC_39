def statistics(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return min(numbers), max(numbers), total, average

numbers = list(map(int, input("Enter numbers: ").split()))
minimum, maximum, total, avg = statistics(numbers)

print("Minimum =", minimum)
print("Maximum =", maximum)
print("Sum =", total)
print("Average =", avg)
