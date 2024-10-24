import random

class Book:
    def __init__(self, title, author, genre, __is_available):
        self.title = title
        self.author = author
        self.genre = genre
        self.__is_available = __is_available
        self.id = random.randrange(100000,999999)
    
    def display_info(self):
        print(f"Book Title : {self.title}\n"
              f"Book Author : {self.author}\n"
              f"Genre : {self.genre}\n"
              f"Book ID : {self.id}")
        
        if self.__is_available:
            print(f"Availability : Available")
        else:
            print(f"Availability : Not available")

    def set_ava(self):
        self.__is_available = not(self.__is_available)

    def is_ava(self):
        return self.__is_available

    def reset_id(self):
        self.id = random.randrange(100000,999999)