import re

code = input("Enter product code (ABC-1234-XY): ").strip()
pattern = r"[A-Za-z]{3}-\d{4}-[A-Za-z]{2}"
print("Valid product code" if re.fullmatch(pattern, code) else "Invalid product code")
