# Library Management System
# 1. Create a class Author
# Attribute: name
# Method: get_author_info()

# Returns:

# Author: J.K. Rowling
# 2. Create a class Book
# Attributes
# title
# author (an Author object)
# Class Attribute
# total_books
# Increase by 1 whenever a new book is created.
# Methods
# get_details()
# Returns title and author information.
# Static Method
# get_category()

# Returns:

# General Book
# Class Method
# get_total_books()

# Returns the total number of books created.

# 3. Add Property and Setter

# Create a property:

# price

# Requirements:

# Price cannot be negative.
# Raise a ValueError if a negative value is assigned.

# Example:

# book.price = 500     # Valid
# book.price = -50     # Error
# 4. Create a class EBook that inherits from Book
# Additional Attribute
# file_size

# (in MB)

# Override
# get_details()

# Use super() to include the base details and append:

# File Size: 25 MB

class Author:
    
    def __init__(self, name):
        self.name = name

    def get_author_info(self):
        return f"Author: {self.name}"


class Book:
    total_books = 0

    def __init__(self, title, author, price=0):
        self.title = title
        self.author = author      # Author object
        self.price = price        # Uses setter

        Book.total_books += 1

    def get_details(self):
        return (
            f"Title: {self.title}\n"
            f"{self.author.get_author_info()}"
        )

    @staticmethod
    def get_category():
        return "General Book"

    @classmethod
    def get_total_books(cls):
        return cls.total_books

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value


class EBook(Book):

    def __init__(self, title, author, file_size, price=0):
        super().__init__(title, author, price)
        self.file_size = file_size

    def get_details(self):
        return (
            f"{super().get_details()}\n"
            f"File Size: {self.file_size} MB"
        )


# Creating Author object
author1 = Author("J.K. Rowling")

# Creating EBook object
ebook1 = EBook(
    "Harry Potter",
    author1,
    25,
    499
)

print(ebook1.get_details())

print("\nCategory:")
print(Book.get_category())

print("\nTotal Books:")
print(Book.get_total_books())

print("\nPrice:")
print(ebook1.price)