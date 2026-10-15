import re

sentence = input("Enter a sentence: ")
print("Five-character words:", re.findall(r"\b[A-Za-z]{5}\b", sentence))
