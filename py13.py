my_tuple = ("apple", "banana", "cherry")
temp_list = list(my_tuple)
temp_list[1] = "kiwi"
my_tuple = tuple(temp_list)
print(my_tuple)
