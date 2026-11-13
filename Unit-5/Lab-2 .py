class Book:

  def __init__(self, title, author):
    self.title = title
    self.author = author
    self.is_available = True


class Library:

  def __init__(self):
    self.books = []

  def add_book(self, book):
    self.books.append(book)
    return f"Added '{book.title}' to the library."

  def borrow_book(self, title):
    for book in self.books:
      if book.title.lower() == title.lower():
        if book.is_available:
          book.is_available = False
          return f"Successfully borrowed '{title}'."
        return f"'{title}' is currently checked out."
    return f"Book '{title}' not found."

  def return_book(self, title):
    for book in self.books:
      if book.title.lower() == title.lower():
        if not book.is_available:
          book.is_available = True
          return f"Successfully returned '{title}'."
        return f"'{title}' was not checked out."
    return f"Book '{title}' not found."