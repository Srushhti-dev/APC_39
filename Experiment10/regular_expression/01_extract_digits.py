import re

text = input("Enter a string: ")
print("Digits:", re.findall(r"\d", text))
