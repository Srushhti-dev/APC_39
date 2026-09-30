#12.	Create two sets of numbers and find the elements that are present in either set but not in both.
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

result = set1.symmetric_difference(set2)

print("Elements in either but not both:", result)