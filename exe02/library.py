from book import Book
from member import Member

class Library(Book, Member):
    def __init__(self):
        self.lib_member = []
        self.lib_book = []
    
    def add_book(self, title, author, genre):
        for book_object in self.lib_book:
            if book_object.title == title:
                print(f"\n '{title}' has already been registered in the library's database.")
                break
            else:
                self.lib_book.append(Book(title, author, genre, True))
                print(f"\n '{title}' has been successfully added to our library's database.")
                break
        
        if len(self.lib_book) == 0:
                self.lib_book.append(Book(title, author, genre, True))
                print(f"\n '{title}' has been successfully added to our library's database.")
                
    def add_member(self, name, address):
        for member_obj in self.lib_member:
            if member_obj.name == name:
                print(f"\n '{name}' has already been registered in the library's database.")
                break
            else:
                self.lib_member.append(Member(name, address, []))
                print(f"\n '{name}' has been successfully added to our library's database.")
                break
        
        if len(self.lib_member) == 0:
                self.lib_member.append(Member(name, address, []))
                print(f"\n '{name}' has been successfully added to our library's database.")
    
    def display_books(self):
        print(f"Book list of library :")
        if (len(self.lib_book) > 0):
            for i, book in enumerate(self.lib_book):
                print(f"\n<<<BOOK {i + 1}>>>")
                book.display_info()
        else:
            print(f"(This library has no book!)\n")

    def display_members(self):
        print(f"Member list of library :")
        if (len(self.lib_member) > 0):
            for i, member_ in enumerate(self.lib_member):
                print(f"\n<<<Member {i + 1}>>>")
                member_.display_info()
        else:
            print(f"(No member data exist in our library's database!)\n")

    def borrow_book(self, book_title, member_name):
        member_available = 1
        i = 0
        book_available = 1
        j = 0
        for member_index, member_object in enumerate(self.lib_member):
            if member_object.name == member_name:
                member_available = 0
                i = member_index

        for book_index, book_object in enumerate(self.lib_book):
            if book_object.title == book_title:
                book_available = 0
                j = book_index

        if member_available == 0 and book_available == 0:
            if (self.lib_book[j].is_ava() == True):
                self.lib_member[i].borrow_book(book_title)
                self.lib_book[j].set_ava()
            else:
                print(f"This book is unavailable at the moment!")

        else:
            print(f"This member/book does not exist in our library's database")


    def return_book(self, book_title, member_name):
        member_available = 1
        i = 0
        book_available = 1
        j = 0
        for member_index, member_object in enumerate(self.lib_member):
            if member_object.name == member_name:
                member_available = 0
                i = member_index

        for book_index, book_object in enumerate(self.lib_book):
            if book_object.title == book_title:
                book_available = 0
                j = book_index

        if member_available == 0 and book_available == 0:
            if (self.lib_book[j].is_ava() == False):
                self.lib_member[i].return_book(book_title)
                self.lib_book[j].set_ava()
            else:
                print(f"You are returning a book that is not being borrowed!")

        else:
            print(f"This member or book doesn't belong to our library's database!")
