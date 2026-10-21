words = input("Enter words: ").split()
result = list(filter(lambda word: len(word) > 5, words))
print(result)
