books = {}

def add_book(book, author):
    books[book] = {"author": author, "available": True}

def issue_book(book):
    if book in books and books[book]["available"]:
        books[book]["available"] = False
        print("Book issued")
    else:
        print("Book not available")

def return_book(book):
    if book in books:
        books[book]["available"] = True
        print("Book returned")

def search_book(book):
    if book in books:
        print("Book found:", books[book])
    else:
        print("Book not found")

def display_books():
    for book, details in books.items():
        if details["available"]:
            print(book, "-", details["author"])

add_book("Python", "Guido")
add_book("Java", "James Gosling")
issue_book("Python")
return_book("Python")
search_book("Java")

print("\nAvailable Books:")
display_books()
