from Books.books import add_book, display_books
from Books.search import search_book
from Members.registration import register_member
from Members.members import add_member, display_members
from Transactions.issue import issue_book
from Transactions.return_book import return_book

book={"id":101,"title":"Python","available":True}
add_book(book)
member=register_member("Amit",1)
add_member(member)
display_books()
display_members()
print("Search:",search_book([book],"Python"))
print("Issued:",issue_book(book))
return_book(book)
print("Returned:",book)
