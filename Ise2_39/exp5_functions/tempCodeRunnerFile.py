def statistics(lst):
    minimum = min(lst)
    maximum = max(lst)
    total = sum(lst)
    avg = total / len(lst)

    return minimum, maximum, total, avg

lst = list(map(float, input("Enter numbers: ").split()))

a, b, c, d = statistics(lst)

print("Minimum:", a)
print("Maximum:", b)
print("Sum:", c)
print("Average:", d)