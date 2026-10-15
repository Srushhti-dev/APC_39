import re

text = input("Enter text: ")
print("Result:", re.sub(r" {2,}", " ", text).strip())
