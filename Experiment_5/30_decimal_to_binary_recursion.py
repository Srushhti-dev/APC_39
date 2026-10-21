def decimal_to_binary(n):
    if n == 0:
        return ""
    return decimal_to_binary(n // 2) + str(n % 2)

n = int(input("Enter decimal number: "))

if n == 0:
    print("Binary = 0")
else:
    print("Binary =", decimal_to_binary(n))
