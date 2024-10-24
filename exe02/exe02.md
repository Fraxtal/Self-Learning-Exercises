Problem:

    You have been hired to develop a library system for a local library. The library has books, each with a title, author, genre, and availability status.
    The library also has members who can borrow books from the library. Each member has a name, address, and a list of borrowed books.
    
    Your task is to implement a library system using Object-Oriented Programming (OOP) and read and write concepts in Python. Create the following classes:
    
    1. Book:
    - Attributes: title (string), author (string), genre (string), is_available (bool)
    - Methods:
      - `__init__(self, title, author, genre)`: Initializes a book object with the given title, author, genre, and sets availability status to True.
      - `display_info(self)`: Displays information about the book, including title, author, genre, and availability status.
      - `setAvailable(self)`: Marks the book as unavailable (sets is_available to False) if is_available is True and vice versa.
    
    2. Member:
    - Attributes: name (string), address (string), borrowed_books (list)
    - Methods:
      - `__init__(self, name, address)`: Initializes a member object with the given name, address, and an empty list for borrowed books.
      - `display_info(self)`: Displays information about the member, including name, address, and the list of borrowed books.
      - `borrow_book(self, book)`: Allows the member to borrow a book by adding it to the list of borrowed books.
      - `return_book(self, book)`: Allows the member to return a book by removing it from the list of borrowed books.
    
    3. Library:
    - Attributes: books (list), members (list)
    - Methods:
      - `__init__(self)`: Initializes a library object with empty lists for books and members.
      - `add_book(self, title, author, genre)`: Adds a book to the library's list of books.
      - `add_member(self, name, address)`: Adds a member to the library's list of members.
      - `display_books(self)`: Displays information about all the books in the library.
      - `display_members(self)`: Displays information about all the members in the library.
      - `borrow_book(self, book_title, member_name)`: Allows a member to borrow a book from the library by updating the book's availability status and adding it to the member's list of borrowed books.
      - `return_book(self, book_title, member_name)`: Allows a member to return a book to the library by updating the book's availability status and removing it from the member's list of borrowed books.
    
    IMPORTANT: All of these datas must be written in the text file named 'data.txt' and your program should be able to access data just by reading the file.
    
    Your solution should demonstrate the use of classes, objects, attributes, methods, encapsulation, and other OOP principles.
    Test your solution with sample scenarios, such as adding books and members, displaying book and member information, borrowing and returning books, and
    handling cases where books are not available or members try to borrow or return books that do not exist.