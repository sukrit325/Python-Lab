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
        print("Book added successfully.")

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if book.is_available:
                    book.is_available = False
                    print("Book borrowed successfully.")
                else:
                    print("Book is already borrowed.")
                return
        print("Book not found.")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if not book.is_available:
                    book.is_available = True
                    print("Book returned successfully.")
                else:
                    print("Book was not borrowed.")
                return
        print("Book not found.")

    def display_books(self):
        print("\n--- LIBRARY BOOKS ---")
        for book in self.books:
            status = "Available" if book.is_available else "Borrowed"
            print(book.title, "-", book.author, "-", status)


library = Library()

while True:
    print("\n--- LIBRARY MENU ---")
    print("1. Add Book")
    print("2. Borrow Book")
    print("3. Return Book")
    print("4. Display Books")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")
        library.add_book(Book(title, author))

    elif choice == "2":
        title = input("Enter Book Title to Borrow: ")
        library.borrow_book(title)

    elif choice == "3":
        title = input("Enter Book Title to Return: ")
        library.return_book(title)

    elif choice == "4":
        library.display_books()

    elif choice == "5":
        print("Exiting Library System...")
        break

    else:
        print("Invalid choice.")