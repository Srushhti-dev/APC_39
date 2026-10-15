import re

text = input("Enter a string: ")
print("Uppercase letters:", re.findall(r"[A-Z]", text))
