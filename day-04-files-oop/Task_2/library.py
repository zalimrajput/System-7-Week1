
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f'"{book}" added to the library.')

    def show_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print("\nBooks in the library:")
            for book in self.books:
                print(book)

    def borrow_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f'You borrowed "{book}".')
        else:
            print(f'"{book}" is not available.')

    def return_book(self, book):
        self.books.append(book)
        print(f'You returned "{book}".')


# Create a library object
library1 = Library()

# Add books
library1.add_book("Python Basics")
library1.add_book("Learn OOP")
library1.add_book("Data Science")

# Display books
library1.show_books()

# Borrow a book
library1.borrow_book("Python Basics")

# Display remaining books
library1.show_books()

# Return the book
library1.return_book("Python Basics")

# Display books again
library1.show_books()
