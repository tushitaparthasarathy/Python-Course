# ── BOOK CLASS ─────────────────────────────────────────────────
# TODO: Define a class called Book
class Book:

    # TODO: Define __init__(self, title, author)
    #   Set up three attributes:
    #     self.title   = title
    #     self.author  = author
    #     self.is_borrowed = False   ← starts as not borrowed
    def __init__(self, title, author):
        pass  # replace pass with your attribute assignments

    # TODO: Define borrow(self)
    #   If self.is_borrowed is already True → print that it's already borrowed
    #   Otherwise → set self.is_borrowed = True and print a borrow message
    def borrow(self):
        pass

    # TODO: Define return_book(self)
    #   If self.is_borrowed is False → print that it wasn't borrowed
    #   Otherwise → set self.is_borrowed = False and print a return message
    def return_book(self):
        pass

    # TODO: Define __str__(self)
    #   Return a string like:  "Title by Author [Available]"
    #   or                     "Title by Author [Borrowed]"
    def __str__(self):
        pass


# ── LIBRARY ────────────────────────────────────────────────────
# TODO: Create at least 3 Book objects with different titles and authors
# Example: book1 = Book("Python Crash Course", "Eric Matthes")

print("=" * 42)
print("         📚  LIBRARY SYSTEM")
print("=" * 42)

# TODO: Print each book (uses __str__ automatically)

# TODO: Borrow some books using .borrow()
# TODO: Try to borrow the same book twice to test the guard message

# TODO: Return a book using .return_book()
# TODO: Try to return a book that was never borrowed to test that guard

# TODO: Print each book again to show updated status