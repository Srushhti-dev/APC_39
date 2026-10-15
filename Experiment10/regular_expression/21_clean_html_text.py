import re
import html

text = input("Paste text containing HTML: ")
text = re.sub(r"(?is)<script\b.*?>.*?</script\s*>", " ", text)
text = re.sub(r"(?is)<style\b.*?>.*?</style\s*>", " ", text)
text = re.sub(r"<[^>]+>", " ", text)
text = html.unescape(text)
text = re.sub(r"\s+", " ", text).strip()
# Keep letters, numbers, whitespace, and common sentence punctuation.
text = re.sub(r"[^\w\s.,!?;:'()-]", "", text)
print("Cleaned text:", text)
