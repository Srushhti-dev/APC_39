import re

text = input("Paste research references: ")
dois = re.findall(r"\b10\.\d{4,9}/[-._;()/:A-Z0-9]+\b", text, flags=re.IGNORECASE)
years = re.findall(r"\b(?:19|20)\d{2}\b", text)
emails = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b", text)
urls = re.findall(r"https?://[^\s<>\"']+", text)
print("DOIs:", dois)
print("Publication-year candidates:", years)
print("Email addresses:", emails)
print("URLs:", urls)
