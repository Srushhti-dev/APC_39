def count_vowels(text):
    count = 0
    for ch in text.lower():
        if ch in "aeiou":
            count += 1
    return count

text = input("Enter a string: ")
print("Number of vowels =", count_vowels(text))
