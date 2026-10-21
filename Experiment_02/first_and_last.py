# Print the first and last character of a string

string = input("Enter String: ")

first = ""
last = ""

for char in string:
    if first == "":
        first = char
    last = char

print("First Character:", first)
print("Last Character:", last)