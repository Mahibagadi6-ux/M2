class Book:
    def __init__(self, isbn: str, title: str, author: str):
        self.isbn = isbn
        self.title = title
        self.author = author
        self._is_borrowed = False  # Protected attribute (Encapsulation)

    def borrow_book(self) -> bool:
        if not self._is_borrowed:
            self._is_borrowed = True
            return True
        return False

    def return_book(self):
        self._is_borrowed = False

    def is_available(self) -> bool:
        return not self._is_borrowed


class Member:
    def __init__(self, member_id: str, name: str):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []  # List of Book objects

    def borrow(self, book: Book):
        if book.borrow_book():
            self.borrowed_books.append(book)
            print(f"📚 {self.name} successfully borrowed '{book.title}'.")
        else:
            print(f"❌ Sorry, '{book.title}' is currently unavailable.")

    def return_item(self, book: Book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            print(f"✅ {self.name} returned '{book.title}'.")
        else:
            print(f"❌ {self.name} does not have this book.")


class Library:
    def __init__(self):
        self.books = {}    # ISBN -> Book object
        self.members = {}  # Member ID -> Member object

    def add_book(self, book: Book):
        self.books[book.isbn] = book

    def register_member(self, member: Member):
        self.members[member.member_id] = member


# --- Execution ---
lib = Library()
book1 = Book("111", "Python OOP Guide", "Jane Doe")
member1 = Member("M01", "Alice")

lib.add_book(book1)
lib.register_member(member1)

# Try borrowing
member1.borrow(book1)
# Try borrowing the same book again
