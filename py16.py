original_tuple = ("apple", "banana", "cherry")
temp_list = list(original_tuple)
temp_list[1] = "kiwi"         
temp_list.append("orange")  
modified_tuple = tuple(temp_list)
print(modified_tuple)
