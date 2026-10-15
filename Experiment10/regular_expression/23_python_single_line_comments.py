import re

source = input("Enter one line of Python source code: ")
# This simple pattern finds # and the text after it, but can misidentify # inside strings.
comments = re.findall(r"#.*", source)
print("Possible single-line comments:", comments or "None found")

print("\\nLimitation: regex alone cannot reliably parse Python syntax. For example:")
print('message = "not a # comment"  # actual comment')
print("For robust comment detection, tokenize source using Python's tokenize module.")
