import re

sentence = input("Enter a sentence: ")
print("Words beginning with A/a:", re.findall(r"\b[aA]\w*\b", sentence))
