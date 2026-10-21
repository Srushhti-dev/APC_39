from array import array

a = array('i', [10, 20, 30])

with open("data.bin", "wb") as file:
    a.tofile(file)

print("Array data saved to data.bin")
