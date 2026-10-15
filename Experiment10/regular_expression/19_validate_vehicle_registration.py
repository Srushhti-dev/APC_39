import re

registration = input("Enter vehicle registration (e.g., MH12AB1234): ").strip().upper()
pattern = r"[A-Z]{2}\d{2}[A-Z]{1,3}\d{4}"
print("Valid common registration format" if re.fullmatch(pattern, registration) else "Invalid registration format")
# This checks a common format only; it does not verify registration against government records.
