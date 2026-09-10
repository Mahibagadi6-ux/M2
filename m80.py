class book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
        self.is_available = True

    def borrow(self):
        if self.is_available:
            self.is_available = False
            print(f"{self.title} borrowed successfully ")
        else:
            print(f"{self.title} already borrowed ")
    def return_book(self):
        self.is_available = True
        print(f"{self.title} returned successfully")
class library:
    def __init__(self,id,name_of_taken):
        self.id = id
        self.name_of_taken = name_of_taken
        self.books = []
    def add_book(self,book_name):
        if book_name in self.books:
            print(f"{self.book_name} alredy  exits ")
        else:
            self.books.append(book_name)
            print(f"book {book_name} added successfully")
    def remove_book(self,book_name):
        if book_name in self.books:
            self.books.remove(book_name)
            print(f"book {book_name} removed successfully")
        else:
            print(f"book {book_name} not found ")
    def search_book(self,book_name):
        if book_name in self.books:
            print(f"book {book_name} found successfully")
        else:
            print(f"book {book_name} not found ")
    def return_books(self,book_name):
        if book_name in self.books:
            print(f" book {book_name} returned successfully")
        else:
            print(f"book {book_name} not in the library ")
li = library(1234,"mahesh")
li.add_book("python")
li.add_book("mahesh")
li.search_book("python")
li.remove_book("mahesh")
li.return_books("mahesh")

