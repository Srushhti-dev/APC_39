import re

email = input("Enter an email address: ").strip()
pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
print("Valid email format" if re.fullmatch(pattern, email) else "Invalid email format")
