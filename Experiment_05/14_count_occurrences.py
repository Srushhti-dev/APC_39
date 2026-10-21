def count_occurrences(lst, element):
    count = 0
    for item in lst:
        if item == element:
            count += 1
    return count

lst = list(map(int, input("Enter numbers: ").split()))
element = int(input("Enter element: "))
print("Occurrences =", count_occurrences(lst, element))
