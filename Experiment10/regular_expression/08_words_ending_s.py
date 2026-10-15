import re

sentence = input("Enter a sentence: ")
print("Words ending in s:", re.findall(r"\b\w+s\b", sentence, flags=re.IGNORECASE))
