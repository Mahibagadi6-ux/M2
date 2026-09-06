class Book:
    def __init__(self, book_id, title, author, quantity):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.quantity = quantity

    def __str__(self):
        return f"ID: {self.book_id} | {self.title} by {self.author} | Quantity: {self.quantity}"


class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book_title):
        self.borrowed_books.append(book_title)

    def return_book(self, book_title):
        if book_title in self.borrowed_books:
            self.borrowed_books.remove(book_title)


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

    def find_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None

    def display_books(self):
        if not self.books:
            print("No books in library.")
            return
        for book in self.books:
            print(book)

    def display_members(self):
        if not self.members:
            print("No members registered.")
            return
        for member in self.members:
            print(f"Member ID: {member.member_id} | Name: {member.name} | Borrowed: {member.borrowed_books}")

    def borrow_book(self, member_id, title):
        member = self.find_member(member_id)
        if member is None:
            print("Member not found.")
            return

        book = self.find_book(title)
        if book is None:
            print("Book not found.")
            return

        if book.quantity <= 0:
            print("Book is not available.")
            return

        book.quantity -= 1
        member.borrow_book(book.title)
        print(f"{member.name} borrowed '{book.title}' successfully.")

    def return_book(self, member_id, title):
        member = self.find_member(member_id)
        if member is None:
            print("Member not found.")
            return

        book = self.find_book(title)
        if book is None:
            print("Book not found.")
            return

        if title not in member.borrowed_books:
            print("This book was not borrowed by this member.")
            return

        book.quantity += 1
        member.return_book(title)
        print(f"{member.name} returned '{book.title}' successfully.")


library = Library()

library.add_book(Book(1, "Python Crash Course", "Eric Matthes", 3))
library.add_book(Book(2, "Clean Code", "Robert C. Martin", 2))
library.add_book(Book(3, "Introduction to Algorithms", "CLRS", 1))

library.add_member(Member(101, "Rahul"))
library.add_member(Member(102, "Anita"))

while True:
    print("\n===== Library Management System =====")
    print("1. Display all books")
    print("2. Add a new book")
    print("3. Register a new member")
    print("4. Display all members")
    print("5. Borrow a book")
    print("6. Return a book")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        library.display_books()

    elif choice == "2":
        book_id = int(input("Enter book ID: "))
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        quantity = int(input("Enter quantity: "))
        library.add_book(Book(book_id, title, author, quantity))
        print("Book added successfully.")

    elif choice == "3":
        member_id = int(input("Enter member ID: "))
        name = input("Enter member name: ")
        library.add_member(Member(member_id, name))
        print("Member registered successfully.")

    elif choice == "4":
        library.display_members()

    elif choice == "5":
        member_id = int(input("Enter member ID: "))
        title = input("Enter book title to borrow: ")
        library.borrow_book(member_id, title)

    elif choice == "6":
        member_id = int(input("Enter member ID: "))
        title = input("Enter book title to return: ")
        library.return_book(member_id, title)

    elif choice == "7":
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")