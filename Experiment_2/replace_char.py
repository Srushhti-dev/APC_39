#Replace all occurrences of a given character with another character. 
char ="Harsh"



old_word=input("Enter Char to replace:")
new_word=input("Enter new Char to replace:")

replace=""

for char in char:
    if char==old_word:
        replace=replace+new_word
    else:
        replace=replace+char

print("Repalced String: ",replace)
