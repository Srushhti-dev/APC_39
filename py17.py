my_tuple = ("apple", "banana", "cherry")
print("Tuple before deletion:", my_tuple)
del my_tuple
try:
    print(my_tuple)
except NameError as e:
    print("\nSuccess: The tuple has been completely deleted.")
    print("Error message:", e)
