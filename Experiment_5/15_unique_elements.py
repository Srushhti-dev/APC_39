def unique_elements(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result

lst = list(map(int, input("Enter numbers: ").split()))
print("Unique elements =", unique_elements(lst))
