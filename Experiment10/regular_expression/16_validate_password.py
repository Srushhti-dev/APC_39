import re

password = input("Enter a password: ")
checks = [
    (r".{8,}", "at least 8 characters"),
    (r"[A-Z]", "one uppercase letter"),
    (r"[a-z]", "one lowercase letter"),
    (r"\d", "one digit"),
    (r"[^A-Za-z0-9\s]", "one special character"),
]
missing = [description for pattern, description in checks if not re.search(pattern, password)]
if not missing:
    print("Password meets all requirements")
else:
    print("Password does not meet requirements. Missing:", ", ".join(missing))
