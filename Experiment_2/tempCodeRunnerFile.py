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

