import re

paragraph = input("Enter a paragraph: ")
# Indian PIN codes start with digits 1-9 and contain six digits.
pins = re.findall(r"(?<!\d)[1-9]\d{5}(?!\d)", paragraph)
print("PIN codes:", pins)
