def count_vowels(s): return sum(ch.lower() in "aeiou" for ch in s)
def reverse_string(s): return s[::-1]
def is_palindrome(s): return s == s[::-1]
def count_words(s): return len(s.split())
def remove_spaces(s): return s.replace(" ", "")
