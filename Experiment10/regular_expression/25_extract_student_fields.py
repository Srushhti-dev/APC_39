import re

text = input("Enter student record, e.g. Name: Asha, Roll No: 123, Marks: 87.5: ")
pattern = r"Name\s*:\s*([A-Za-z ]+?)\s*,\s*Roll\s*(?:No\.?|Number)\s*:\s*(\d+)\s*,\s*Marks\s*:\s*(\d+(?:\.\d+)?)"
match = re.search(pattern, text, flags=re.IGNORECASE)
if match:
    name, roll_number, marks = match.groups()
    print("Name:", name.strip())
    print("Roll number:", roll_number)
    print("Marks:", marks)
else:
    print("Record not found. Use: Name: Asha, Roll No: 123, Marks: 87.5")
