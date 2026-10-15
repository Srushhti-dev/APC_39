import re

sentence = input("Enter a sentence: ")
pattern = r"\b([A-Za-z]+)\s+\1\b"
matches = re.findall(pattern, sentence, flags=re.IGNORECASE)
print("Consecutive repeated words:", matches)
