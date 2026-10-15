# Python Array Module 

from array import array

# 1. append()
a = array('i', [1, 2, 3])
a.append(4)
print("append():", a)

# 2. buffer_info()
print("buffer_info():", a.buffer_info())

# 3. byteswap()
b = array('i', [1, 2, 3])
b.byteswap()
print("byteswap():", b)

# 4. count()
a = array('i', [1, 2, 2, 3])
print("count(2):", a.count(2))

# 5. extend()
a = array('i', [1, 2])
a.extend([3, 4])
print("extend():", a)

# 6. frombytes()
a = array('i')
source = array('i', [10, 20])
a.frombytes(source.tobytes())
print("frombytes():", a)

# 7. fromfile()
a = array('i', [10, 20, 30])
filename = "array_data.bin"
with open(filename, "wb") as f:
    a.tofile(f)

b = array('i')
with open(filename, "rb") as f:
    b.fromfile(f, 3)
print("fromfile():", b)
os.remove(filename)

# 8. fromlist()
a = array('i')
a.fromlist([5, 10, 15])
print("fromlist():", a)

# 9. fromunicode()
a = array('u')
a.fromunicode("Hello")
print("fromunicode():", a)

# 10. index()
a = array('i', [10, 20, 30])
print("index(20):", a.index(20))

# 11. insert()
a = array('i', [1, 3, 4])
a.insert(1, 2)
print("insert():", a)

# 12. pop()
a = array('i', [1, 2, 3])
print("pop():", a.pop())

# 13. remove()
a = array('i', [1, 2, 3])
a.remove(2)
print("remove():", a)

# 14. reverse()
a = array('i', [1, 2, 3])
a.reverse()
print("reverse():", a)

# 15. tobytes()
a = array('i', [1, 2, 3])
data = a.tobytes()
print("tobytes():", data)

# 16. tofile()
import os
a = array('i', [100, 200, 300])
filename = "array_output.bin"
with open(filename, "wb") as f:
    a.tofile(f)
print("tofile(): Data written to", filename)
os.remove(filename)

# 17. tolist()
a = array('i', [1, 2, 3])
print("tolist():", a.tolist())

# 18. tounicode()
a = array('u', "Hello")
print("tounicode():", a.tounicode())
