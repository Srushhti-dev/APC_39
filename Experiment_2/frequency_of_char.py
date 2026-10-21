# •	Find the number of times a specified character appears in a string. 


string = input("Enter String: ")
ch = input("Enter Character to Find: ")

count = 0

for char in string:
    if char == ch:
        count += 1

print("Frequency of", ch, "is", count)