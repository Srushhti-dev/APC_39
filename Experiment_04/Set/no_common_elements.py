#15.	Write a program to determine whether two sets have no elements in common.
set1 = {1,2,3,4,5,6}
set2 = {5,6}


if set1.isdisjoint(set2):
    print("Sets have no elements in common")
else:
    print("Sets have common elements")