import re

text = input("Enter text containing filenames: ")
extensions = re.findall(r"\b[\w-]+\.(\w{1,10})\b", text)
print("File extensions:", extensions)
