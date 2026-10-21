# •	Count the number of vowels, consonants, digits, spaces, and special characters in a given string. 

char=str(input("Enter a Text:"))

vowels=0
consonants=0
digits=0
spaces=0
special=0

for ch in char:
    if char in "aeiou":
        vowels=+1
    elif 'a'>= char <= 'z':
        consonants=+1
    elif '1'>= char <= '9':
        digits=+1
    elif char==" ":
        spaces=+1
    else:
        special=+1

print("vowels",vowels)
print("consonant",consonants)
print("digits",digits)
print("spaces",spaces)
print("special",special)

        
