def second_largest(lst):
    unique = list(set(lst))
    unique.sort()
    return unique[-2]

lst = list(map(int, input("Enter numbers: ").split()))
print("Second largest =", second_largest(lst))
