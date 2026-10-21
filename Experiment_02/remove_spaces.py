# 	Remove all spaces from the input string. 

string = input("Enter String: ")

new_string = ""

for ch in string:
    if ch != " ":
        new_string = new_string + ch

print("String without spaces:", new_string)