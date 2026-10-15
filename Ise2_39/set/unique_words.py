#18.	Accept a sentence from the user and use a set to display all unique words.
sentence = input("Enter a sentence: ")

words = sentence.split()

unique_words = set(words)

print("Unique words:", unique_words)