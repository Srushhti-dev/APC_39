class Book:
    def __init__(self, book_id, title, author, price):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print("Book ID:", self.book_id)
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)
        print()

book1 = Book(101, "Python Programming", "John", 500)
book2 = Book(102, "Java Programming", "James", 600)
book3 = Book(103, "C Programming", "Dennis", 450)

book1.display()
book2.display()
book3.display()
