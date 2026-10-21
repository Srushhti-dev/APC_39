import string_utils
text = input("Enter a string: ")
print("Vowels:", string_utils.count_vowels(text))
print("Reverse:", string_utils.reverse_string(text))
print("Palindrome:", string_utils.is_palindrome(text))
print("Words:", string_utils.count_words(text))
print("Without spaces:", string_utils.remove_spaces(text))
