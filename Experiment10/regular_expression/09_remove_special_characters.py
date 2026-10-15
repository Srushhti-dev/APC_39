import re

text = input("Enter a string: ")
print("Cleaned text:", re.sub(r"[^A-Za-z0-9 ]", "", text))
