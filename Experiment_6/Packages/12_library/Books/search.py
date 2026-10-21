def search_book(books,title):
    for book in books:
        if book["title"].lower()==title.lower(): return book
    return None
