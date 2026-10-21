def binary_search(lst, low, high, target):
    if low > high:
        return -1

    mid = (low + high) // 2

    if lst[mid] == target:
        return mid
    elif target < lst[mid]:
        return binary_search(lst, low, mid - 1, target)
    else:
        return binary_search(lst, mid + 1, high, target)

lst = [10, 20, 30, 40, 50]
target = int(input("Enter element: "))

result = binary_search(lst, 0, len(lst) - 1, target)

if result != -1:
    print("Element found at index", result)
else:
    print("Element not found")
