words = input("Enter words: ").split()

lengths = list(map(lambda word: len(word), words))

long_words = list(
    filter(lambda word: len(word) > 5, words)
)

sorted_words = sorted(words, key=lambda word: len(word))

print("Lengths =", lengths)
print("Words > 5 characters =", long_words)
print("Sorted words =", sorted_words)
