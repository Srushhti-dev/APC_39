import re

text = input("Enter text (you can type \\n as two characters, or edit this code for multiline input): ")
matches = re.findall(r" ", text), re.findall(r"\t", text), re.findall(r"\n", text)
print("Spaces:", len(matches[0]))
print("Tabs:", len(matches[1]))
print("Newlines:", len(matches[2]))
print("Whitespace matches (space/tab/newline):", re.findall(r"[ \t\n]", text))
