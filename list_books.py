books = ["Python", "Java", "C++", "HTML"]


new_book = input("Enter new book: ")
books.append(new_book)


search_book = input("Enter book to search: ")

if search_book in books:
    print("Book found.")
else:
    print("Book not found.")


remove_book = input("Enter book to remove: ")

if remove_book in books:
    books.remove(remove_book)
    print("Book removed.")
else:
    print("Book not found.")

print("All books:", books)

# Count books
print("Total books:", len(books))