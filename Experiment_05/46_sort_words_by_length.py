words = input("Enter words: ").split()
words.sort(key=lambda word: len(word))
print("Sorted words =", words)
