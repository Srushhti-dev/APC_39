numbers = [2, 7, 11, 15]
target = 9

seen = {}
for number in numbers:
    required = target - number
    if required in seen:
        print("Numbers:", required, number)
        break
    seen[number] = True
