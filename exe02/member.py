class Member:
    def __init__(self, name, address, __borrowed_books):
        self.name = name
        self.address = address
        self.__borrowed_books = __borrowed_books
    
    def display_info(self):
        print(f"Name: {self.name}"
              f"Address: {self.address}"
              f"Borrowed Books: ")
        if (len(self.__borrowed_books) > 0):
            for i,book in enumerate(self.__borrowed_books):
                print(f"{i+1}. {book}")
        else:
            print(f" (-- empty --)")
        
    def borrow_book(self, book):
        self.__borrowed_books.append(book)
        i = self.__borrowed_books.index(book)
        print(f"{self.name} borrowed the book '{self.__borrowed_books[i]}'!")

    def return_book(self, book):
        if (self.__borrowed_books.count(book) == 0):
            print(f"This book does not belong to us!")
        else:
            i = self.__borrowed_books.index(book)
            print(f"{self.name} returned the book '{self.__borrowed_books[i]}'!")
            self.__borrowed_books.remove(book)
