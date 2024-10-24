import random

class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
        
    def display_information(self):
        print(f"{self.name} {self.age} {self.address}")
        print(self.name)
    
    def set_name(self, name):
        self.name = name
    
    def set_age(self, age):
        self.age = age
        
    def set_address(self, address):
        self.address = address

class Student(Person):
    def __init__(self, name, age, address, major, gpa):
        super().__init__(name, age, address)
        self.studentid = random.randrange(1000000, 9999999)
        self.major = major
        self.gpa = gpa
    
    def set_major(self, major):
        self.major = major
    
    def set_gpa(self, gpa):
        self.gpa = gpa
    
    def display_information(self):
        print(f"Name: {self.name}"
              f"Age: {self.age}"
              f"Address: {self.address}"
              f"Major: {self.major}"
              f"GPA : {self.gpa}")
    
class BankAccount:
    def __init__(self, __acc_id, __holder_name, __balance):
        self.__acc_id = __acc_id
        self.__holder_name = __holder_name
        self.__balance = __balance
    
    def top_up(self, amount):
        self.__balance += amount
    
    def deduct(self, amount):
        self.__balance -= amount
    
    def check_balance(self): 
        print(f"Bank Account Name : {self.__holder_name}\n"
              f"Bank Account ID : {self.__acc_id}\n"
              f"Your current balance : RM {self.__balance}")
        
bankaccount = BankAccount(11230, "Nicholas", 87132)
bankaccount.top_up(1000)
bankaccount.check_balance()
