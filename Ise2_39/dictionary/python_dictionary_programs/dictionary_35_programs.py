# PYTHON DICTIONARY PROGRAMS 

# 1. Student details
student={'roll_no':101,'name':'Srushhti','department':'CSE','marks':85}
print(student)

# 2. Employee information - value for specified key
employee = {
    "id": 101,
    "name": "Srushhti",
    "department": "CSE",
    "salary": 50000
}

key = input("Enter key: ")

if key in employee:
    print(employee[key])
else:
    print("Key not found")

# 3. Five products, add new product
products={'Pen':10,'Notebook':50,'Bag':800,'Bottle':300,'Pencil':5}
products['Eraser']=8
print(products)

 # 4. Update student marks
marks = {
    "Amit": 75,
    "Neha": 88,
    "Riya": 92
}

name = input("Enter student name: ")
new_marks = int(input("Enter new marks: "))

if name in marks:
    marks[name] = new_marks

print(marks)

# 5. Remove city
cities={'Mumbai':20000000,'Pune':7000000,'Delhi':32000000,'Nashik':2000000}
city=input(' City to remove: ')
if city in cities: 
  del cities[city]
else: 
  print('City not found')
print(cities)

# # 6. Check employee ID
employees={101:'Amit',102:'Neha',103:'Riya',104:'Srushhti'}
emp_id = int(input("Enter employee ID: "))

if emp_id in employees:
    print("Employee exists")
else:
    print("Employee does not exist")

 # 7. Number of key-value pairs
records={'Amit':80,'Neha':90,'Riya':85,'Srushhti':75}
print('Total pairs:',len(records))

# 8. Keys, values, pairs
data={'name':'Srushhti','age':20,'course':'CSE','city':'Kolhapur'}
print('Keys:',list(data.keys()))
print('Values:',list(data.values()))
print('Pairs:',list(data.items()))

# # 9. Languages and creators
languages={'Python':'Guido van Rossum','Java':'James Gosling','C':'Dennis Ritchie','JavaScript':'Brendan Eich'}
for key, value in languages.items():
    print(key, ":", value)


# 10. Five students and marks
students = {}

for i in range(5):
    name = input("Enter name: ")
    marks = int(input("Enter marks: "))
    students[name] = marks

print(students)

# 11. Highest marks
marks={'Amit':75,'Neha':88,'Riya':95,'Srushhti':82}
student = max(marks, key=marks.get)
print("Highest:", student)
print("Marks:", marks[student])

#  12. Lowest marks
student = min(marks, key=marks.get)

print("Lowest:", student)
print("Marks:", marks[student])

#  13. Average marks
average = sum(marks.values()) / len(marks)
print("Average:", average)

# 14. Character frequency
text = input("Enter string: ")

frequency = {}
for ch in text:
    frequency[ch] = frequency.get(ch, 0) + 1
print(frequency)

#  15. Word frequency
sentence = input("Enter sentence: ")

frequency = {}

for word in sentence.split():
    frequency[word] = frequency.get(word, 0) + 1

print(frequency)

#  16. Merge dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

merged = {**dict1, **dict2}

print(merged)

#  17. Common keys
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 20, "c": 30, "d": 40}

common = dict1.keys() & dict2.keys()
print(common)

# 18. Common values
dict1 = {"a": 10, "b": 20, "c": 30}
dict2 = {"x": 20, "y": 30, "z": 40}

common = set(dict1.values()) & set(dict2.values())
print(common)

# # 19. Remove duplicate values, retain first key
d={'A':10,'B':20,'C':10,'D':30,'E':20}; unique={}

result = {}

for key, value in data.items():
    if value not in result.values():
        result[key] = value

print(result)

# 20. Ascending order of keys
data={'d':4,'b':2,'a':1,'c':3}
result = dict(sorted(data.items()))

print(result)

# 21. 1 to 10 and squares
squares = {}

for i in range(1, 11):
    squares[i] = i ** 2

print(squares)

#  22. Even numbers 1 to 20 and squares
squares = {}

for i in range(1, 21):
    if i % 2 == 0:
        squares[i] = i ** 2

print(squares)

# 23. Unique numbers and frequency
numbers = [1, 2, 2, 3, 4, 4, 4, 5, 1, 3]

frequency = {}

for num in numbers:
    frequency[num] = frequency.get(num, 0) + 1

print(frequency)

# # 24. 1 to 10 and cubes
cubes = {}

for i in range(1, 11):
    cubes[i] = i ** 3

print(cubes)

# # 25. Student management
students = {}

while True:
    print("\n1.Add")
    print("2.Update")
    print("3.Delete")
    print("4.Search")
    print("5.Display")
    print("6.Highest")
    print("7.Average")
    print("8.Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        name = input("Enter name: ")
        marks = int(input("Enter marks: "))
        students[name] = marks

    elif choice == 2:
        name = input("Enter name: ")
        if name in students:
            students[name] = int(input("Enter new marks: "))
        else:
            print("Student not found")

    elif choice == 3:
        name = input("Enter name: ")
        if name in students:
            del students[name]
        else:
            print("Student not found")

    elif choice == 4:
        name = input("Enter name: ")
        if name in students:
            print(students[name])
        else:
            print("Student not found")

    elif choice == 5:
        print(students)

    elif choice == 6:
        if students:
            name = max(students, key=students.get)
            print(name, students[name])

    elif choice == 7:
        if students:
            print(sum(students.values()) / len(students))

    elif choice == 8:
        break

#  26. Employee salaries
employees = {
    "Amit": 45000,
    "Neha": 65000,
    "Riya": 75000,
    "Rahul": 50000
}

highest = max(employees, key=employees.get)
lowest = min(employees, key=employees.get)
average = sum(employees.values()) / len(employees)

print("Highest:", highest, employees[highest])
print("Lowest:", lowest, employees[lowest])
print("Average:", average)

print("Salary above 50000:")
for name, salary in employees.items():
    if salary > 50000:
        print(name, salary)

 # 27. Product quantity management
products = {
    "Pen": 25,
    "Notebook": 8,
    "Bag": 15,
    "Pencil": 5
}

name = input("Add product: ")
quantity = int(input("Enter quantity: "))
products[name] = quantity

name = input("Update product: ")
if name in products:
    products[name] = int(input("Enter new quantity: "))

name = input("Delete product: ")
if name in products:
    del products[name]

name = input("Search product: ")
if name in products:
    print("Quantity:", products[name])

print("Products below 10:")
for name, quantity in products.items():
    if quantity < 10:
        print(name, quantity)

 # 28. Contact management
contacts = {}

name = input("Enter contact name: ")
phone = input("Enter phone: ")
contacts[name] = phone

name = input("Search contact: ")
if name in contacts:
    print(contacts[name])

name = input("Update contact: ")
if name in contacts:
    contacts[name] = input("Enter new phone: ")

name = input("Delete contact: ")
if name in contacts:
    del contacts[name]

print("All contacts:")
print(contacts)

 # 29. Book management
books = {}

book_id = int(input("Enter book ID: "))
book_name = input("Enter book name: ")
books[book_id] = book_name

book_id = int(input("Search book ID: "))
if book_id in books:
    print(books[book_id])

book_id = int(input("Remove book ID: "))
if book_id in books:
    del books[book_id]

print("All books:", books)
print("Total books:", len(books))


# # 30. Group students by department
students={'Amit':'CSE','Neha':'IT','Riya':'CSE','Srushhti':'ENTC','Sneha':'IT'}; grouped={}
result = {}

for name, department in students.items():
    if department not in result:
        result[department] = []
    result[department].append(name)

print(result)

 # 31. Group words by word length
words = ["cat", "dog", "apple", "banana", "book", "pen"]

result = {}

for word in words:
    length = len(word)

    if length not in result:
        result[length] = []

    result[length].append(word)

print(result)

# 32. Two numbers with target sum using dictionary
numbers = [2, 7, 11, 15, 3, 6]
target = 9

seen = {}

for num in numbers:
    complement = target - num

    if complement in seen:
        print(complement, num)
        break

    seen[num] = True

# 33. First character occurring only once
text = input("Enter string: ")

frequency = {}

for ch in text:
    frequency[ch] = frequency.get(ch, 0) + 1

for ch in text:
    if frequency[ch] == 1:
        print("First unique character:", ch)
        break

# 34. First character occurring more than once
text = input("Enter string: ")

frequency = {}

for ch in text:
    frequency[ch] = frequency.get(ch, 0) + 1

for ch in text:
    if frequency[ch] == 1:
        print("First unique character:", ch)
        break

# 35. Paragraph: word length -> number of words
paragraph = input("Enter paragraph: ")

result = {}

for word in paragraph.split():
    word = word.strip(".,!?;:'\"()[]{}")

    if word:
        length = len(word)
        result[length] = result.get(length, 0) + 1

print(result)