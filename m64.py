class Book:
    def __init__(self, book_id, title, author, quantity):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.quantity = quantity

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} | Quantity: {self.quantity}"


class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        self.borrowed_books.append(book.title)

    def return_book(self, book):
        if book.title in self.borrowed_books:
            self.borrowed_books.remove(book.title)


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def find_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def borrow_book(self, member_id, title):
        member = None
        for m in self.members:
            if m.member_id == member_id:
                member = m
                break

        if member is None:
            return "Member not found."

        book = self.find_book(title)
        if book is None:
            return "Book not found."

        if book.quantity <= 0:
            return "Book is not available."

        book.quantity -= 1
        member.borrow_book(book)
        return f"{member.name} borrowed '{book.title}' successfully."

    def return_book(self, member_id, title):
        member = None
        for m in self.members:
            if m.member_id == member_id:
                member = m
                break

        if member is None:
            return "Member not found."

        book = self.find_book(title)
        if book is None:
            return "Book not found."

        if title not in member.borrowed_books:
            return "This book was not borrowed by the member."

        book.quantity += 1
        member.return_book(book)
        return f"{member.name} returned '{book.title}' successfully."

    def display_books(self):
        if not self.books:
            print("No books in library.")
            return
        for book in self.books:
            print(book)


# Example usage
library = Library()

b1 = Book(1, "Python Crash Course", "Eric Matthes", 3)
b2 = Book(2, "Clean Code", "Robert C. Martin", 2)
b3 = Book(3, "Introduction to Algorithms", "CLRS", 1)

library.add_book(b1)
library.add_book(b2)
library.add_book(b3)

m1 = Member(101, "Rahul")
m2 = Member(102, "Anita")

library.add_member(m1)
library.add_member(m2)

library.display_books()

print(library.borrow_book(101, "Python Crash Course"))
print(library.borrow_book(102, "Clean Code"))
print(library.return_book(101, "Python Crash Course"))

print("\nUpdated book list:")
library.display_books()