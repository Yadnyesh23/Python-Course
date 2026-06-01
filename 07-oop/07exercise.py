# Library Book Tracker

# Create a class called Book.

# Requirements

# Create a class attribute:

# category = "General"
# The constructor should accept:
# title
# author
# is_available (True or False)

# Inside the constructor, shadow the class attribute by setting:

# self.category = "Programming"

# Create a method book_info() that returns:

# "Python Crash Course by Eric Matthes - Available - Programming"
# "Atomic Habits by James Clear - Not Available - Programming"

# depending on the value of is_available.

# Create two book objects and print their information.

class Book:
    category = "General"
    
    def __init__(self, title, author, is_available):
        self.title = title
        self.author = author
        self.is_available = is_available
        self.category = "Programming"
    
    def book_info(self):
        avaibility = "Available" if self.is_available else "Not Available"
        return f"{self.title} by {self.author} - {avaibility} - {self.category}"
    
book1 = Book("Python Crash Course", "Eric Matthes", True)
book2 = Book("Atomic Habits", "James Clear", False)

print(book1.book_info())
print(book2.book_info())