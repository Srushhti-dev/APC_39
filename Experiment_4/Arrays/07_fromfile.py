from array import array

a = array('i', [10, 20, 30])

with open("data.bin", "wb") as file:
    a.tofile(file)

b = array('i')

with open("data.bin", "rb") as file:
    b.fromfile(file, 3)

print(b)
