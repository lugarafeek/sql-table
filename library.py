from datetime import datetime, timedelta

class Book:
    def __init__(self, title, author):
        self.title = title  
        self.author = author  
        self.is_lended = False  
        self.due_date = None  


    def display_info(self):
        status = "Lended" if self.is_lended else "Available"
        due_date = f"Due date: {self.due_date.strftime('%Y-%m-%d')}" if self.due_date else "No due date"
        print(f"Title: {self.title}, Author: {self.author}, Status: {status}, {due_date}")

    def is_overdue(self):
        if self.due_date:
            return datetime.now() > self.due_date
        return False


class Library:
    def __init__(self):
        self.books = []  

  
    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")

    
    def lend_book(self, title, days_for_return=14):
        for book in self.books:
            if book.title == title and not book.is_lended:
                book.is_lended = True
                book.due_date = datetime.now() + timedelta(days=days_for_return)
                print(f"Book '{title}' has been lent out. It is due to be returned on {book.due_date.strftime('%Y-%m-%d')}.")
                return
        print(f"Book '{title}' is either not available or already lent out.")


    def return_book(self, title):
        for book in self.books:
            if book.title == title and book.is_lended:
                if book.is_overdue():
                    print(f"Book '{title}' is overdue! It was due on {book.due_date.strftime('%Y-%m-%d')}.")
                book.is_lended = False
                book.due_date = None
                print(f"Book '{title}' has been returned to the library.")
                return
        print(f"Book '{title}' was not lent out.")

   
    def display_books(self):
        print("\nBooks in the library:")
        for book in self.books:
            book.display_info()


# Create an instance of the Library class
library = Library()

# Create some books
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
book3 = Book("1984", "George Orwell")

# Add books to the library
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Display all books
library.display_books()

# Lend a book with a due date of 7 days
library.lend_book("The Great Gatsby", days_for_return=7)

# Try lending the same book again (should show it's already lent out)
library.lend_book("The Great Gatsby")

# Display all books after lending
library.display_books()

# Simulate waiting for a few days
# You can manually test it by changing your computer's date/time or waiting for a real-time pass

# Let's assume the user returns the book after a few days
library.return_book("The Great Gatsby")

# Display all books after returning
library.display_books()
