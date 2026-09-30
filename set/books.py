#23.	Create a set containing available books and another set containing requested books. Determine which requested books are available.
available_books = {"Python", "Java", "C++", "DBMS","Machine learning"}
requested_books = {"Python", "DMS", "AI"}

available_requested = available_books & requested_books

print("Requested books that are available:", available_requested)