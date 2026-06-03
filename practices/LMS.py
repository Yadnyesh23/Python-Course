# Library management system

class Book:
    
    def __init__(self, title, author, isbn ):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False
    
    def borrow_book(self):
        if self.is_borrowed:
            return f"Book is already borrowed"
        self.is_borrowed = True
        return f"Book borrwed succesfully"
    
    def return_book(self):
        if not self.is_borrowed:
            return f"Book is already returned"
        self.is_borrowed = False
        return f"Book returned succesfully"

class BookNotFoundError(Exception):
    pass

class BookAlreadyBorrowedError(Exception):
    pass

class BookNotBorrowedError(Exception):
    pass

class Library:
    
    def __init__(self):
        self.books = []
        
    def add_book(self, book):
       self.books.append(book)
    
    def display_books(self):
        books_list = []
        for book in self.books:
            books_list.append({"Title" : book.title, "Author" : book.author, "isbn" : book.isbn, "Is Borrowed" : book.is_borrowed})
        
        return books_list
    
    def remove_book(self, isbn):
        for book in self.books:
            if isbn == book.isbn:
                self.books.remove(book)
                return "Book returned succesfully"
        raise BookNotFoundError("Book Not Found")
    
    def search_book(self, keyword):
        for book in self.books:
            if keyword == book.title or keyword == book.author or keyword == book.isbn:
                return book
            
        raise BookNotFoundError("Book Not Found")
        
    
library = Library()


book1 = Book(
    "Atomic Habits",
    "James Clear",
    "12345"
)

book2 = Book(
    "Deep Work",
    "Cal Newport",
    "12346"
)

book3 = Book(
    "The Psychology of Money",
    "Morgan Housel",
    "12347"
)

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
book_list = library.display_books()
print(book_list)
