my_tuple = ("apple", "banana", "cherry")
print("Before deletion:", my_tuple)
del my_tuple
try:
    print(my_tuple)
except NameError as e:
    print("Verification:", e)
