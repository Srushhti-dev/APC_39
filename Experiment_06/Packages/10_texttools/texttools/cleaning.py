import string
def remove_punctuation(text): return text.translate(str.maketrans("","",string.punctuation))
def remove_extra_spaces(text): return " ".join(text.split())
