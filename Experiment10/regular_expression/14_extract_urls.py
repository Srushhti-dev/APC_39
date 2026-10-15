import re

text = input("Enter text containing web addresses: ")
urls = re.findall(r"https?://[^\s<>\"']+", text)
print("URLs:", urls)
