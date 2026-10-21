paragraph = input("Enter a paragraph: ")

words = paragraph.split()
result = {}

for word in words:
    length = len(word)
    if length in result:
        result[length] += 1
    else:
        result[length] = 1

print(result)
