#Count the number of uppercase and lowercase letters in a string. 
string=input("Enter Strings:")

uppercase=0
lowercase=0

for char in string:
    if "A"<= char <="Z":
        uppercase+=1
    elif "a"<= char <="z":
        lowercase+=1


print("Uppercase",uppercase)
print("Lowercase",lowercase)

<<<<<<< HEAD

=======
>>>>>>> 37dd3c0888632f277afb3853624d6ef7ca906fb8
