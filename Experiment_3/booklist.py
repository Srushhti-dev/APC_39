books = ["Python", "Java", "C++"]

books.append("HTML")

book = input("Search book: ")

if book in books:
    print("Book found")
else:
    print("Book not found")

books.remove("Java")

print("Books:", books)
print("Total books:", len(books))