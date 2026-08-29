class book:
    def __init__(self,isbn,title,auther):
        self.isbn = isbn
        self.title = title
        self.auther = auther
        self._is_borrowed = False
    def borrow_book(self):
        if not self._is_borrowed:
            self._is_borrowed = True
            return True
        return False
    def return_book(self):
        self._is_borrowed = False
    def is_avilable_book(self):
        return  not self._is_borrowed
class member:
    def __init__(self,member_id,name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []
    def borrow(self,book:book):
        if book in self.borrowed_books:
            self.borrowed_books.append(book)
            print(f" {self.name} successfully borrowed {book.title}")
        else:
            print(f"{book.title} is not avilable at sorry")
    def return_ithem(self,book:book):
        if book.borrow_book():
            book.return_book()
            self.borrowed_books.remove(book)
            print(f" {self.name} successfully borrowed {book.title}")
        else:
            print(f"{self.name} is not avilable at sorry")
    def is_avilable(self):
        return not self._is_borrowed
class library:
    def __init__(self):
        self.books = {}
        self.members = {}
    def add_book(self,book:book):
        self.books[book.isbn] = book
    def register_member(self,member:member):
        self.members[member.member_id] = member
lib = library()
book1 = book("111","python","mahesh")
member1 = member(1,"vishwa")
lib.add_book(book1)
lib.register_member(member1)






