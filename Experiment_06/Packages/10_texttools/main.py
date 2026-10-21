from texttools.cleaning import remove_punctuation, remove_extra_spaces
from texttools.tokenization import tokenize
from texttools.frequency import word_frequency
text=input("Enter text: ")
text=remove_extra_spaces(remove_punctuation(text))
print("Clean:",text)
print("Tokens:",tokenize(text))
print("Frequency:",word_frequency(text))
