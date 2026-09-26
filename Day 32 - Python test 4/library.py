class Book:
    def __init__(self, author, title):
        self.title=title
        self.author=author
        self.is_borrowed= False
    def borrow(self):
        self.is_borrowed=True
        print("Book has been borrowed")
    def return_book(self):
        self.is_borrowed=False
        print("Book has been returned")
book1=Book("book_1","author1")
book2=Book("book_2", "author2")
book3=Book("book_3", "author2")
book1.borrow()
book1.return_book()
book2.borrow()
book2.return_book()
book3.borrow()
book3.return_book()