def add_book():
    book_id = input("Book ID: ")
    title = input("Title: ")
    author = input("Author: ")
    with open("books.txt", "a") as file:
        file.write(f"{book_id},{title},{author},Available\n")
    print("Book added.")

def search_book():
    book_id = input("Enter book ID: ")
    with open("books.txt", "r") as file:
        for line in file:
            data = line.strip().split(",")
            if data[0] == book_id:
                print(data)
                return
    print("Book not found.")

def issue_book():
    book_id = input("Enter book ID: ")
    with open("books.txt", "r") as file:
        lines = file.readlines()
    with open("books.txt", "w") as file:
        for line in lines:
            data = line.strip().split(",")
            if data[0] == book_id:
                if data[3] == "Available":
                    data[3] = "Issued"
                    print("Book issued.")
                else:
                    print("Book already issued.")
            file.write(",".join(data) + "\n")

def return_book():
    book_id = input("Enter book ID: ")
    with open("books.txt", "r") as file:
        lines = file.readlines()
    with open("books.txt", "w") as file:
        for line in lines:
            data = line.strip().split(",")
            if data[0] == book_id:
                data[3] = "Available"
                print("Book returned.")
            file.write(",".join(data) + "\n")

def display_available():
    with open("books.txt", "r") as file:
        for line in file:
            data = line.strip().split(",")
            if data[3] == "Available":
                print(data)

while True:
    print("\n1. Add Book\n2. Search Book\n3. Issue Book")
    print("4. Return Book\n5. Display Available Books\n6. Exit")
    choice = input("Enter choice: ")
    if choice == "1": add_book()
    elif choice == "2": search_book()
    elif choice == "3": issue_book()
    elif choice == "4": return_book()
    elif choice == "5": display_available()
    elif choice == "6": break
    else: print("Invalid choice")
