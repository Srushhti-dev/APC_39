import re

text = input("Paste invoice text: ")
invoice_numbers = re.findall(r"\b(?:Invoice\s*(?:No\.?|Number|#)\s*[:\-]?\s*)([A-Z0-9/-]+)", text, flags=re.IGNORECASE)
dates = re.findall(r"\b(?:0[1-9]|[12]\d|3[01])[-/](?:0[1-9]|1[0-2])[-/]\d{4}\b", text)
amounts = re.findall(r"(?:₹|Rs\.?|INR|\$|€)\s?\d[\d,]*(?:\.\d{2})?", text, flags=re.IGNORECASE)
print("Invoice numbers:", invoice_numbers)
print("Dates:", dates)
print("Monetary amounts:", amounts)
