list1 = [10, 20, 30, 40, 50]
list2 = [30, 40, 50, 60, 70]

common = []

for element in list1:
    if element in list2:
        common.append(element)

print("Common elements:", common)