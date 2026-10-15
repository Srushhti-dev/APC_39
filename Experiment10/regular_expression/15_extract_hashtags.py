import re

post = input("Enter a social media post: ")
print("Hashtags:", re.findall(r"(?<!\w)#[A-Za-z0-9_]+", post))
