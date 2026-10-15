import re

text = input("Enter a string: ")
vowels = re.findall(r"[aeiou]", text, flags=re.IGNORECASE)
print("Vowels:", vowels)
print("Vowel count:", len(vowels))
