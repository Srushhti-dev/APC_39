import re

number = input("Enter a 10-digit Indian mobile number: ").strip()
pattern = r"[6-9]\d{9}"
if re.fullmatch(pattern, number):
    print("Valid mobile number")
else:
    print("Invalid mobile number")
