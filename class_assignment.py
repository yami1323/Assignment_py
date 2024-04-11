##1##
# class StringManipulator:
#   def get_input(self):
#       self.input_string = input("Enter a string: ")

#   def print_uppercase(self):
#       if hasattr(self, 'input_string'):
#           print(self.input_string.upper())
#       else:
#           print("No string input yet.")
# manipulator = StringManipulator()
# manipulator.get_input()
# manipulator.print_uppercase()


##2##
# class Example:
#   class_param = "Class Parameter"   

#   def __init__(self, instance_param):
#       self.instance_param = instance_param    

#   def simple_method(self):
#       print("This is a simple method.")

# example_instance = Example("Instance Parameter")
# example_instance.simple_method()


##3##
# import math

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return math.pi * self.radius**2
# circle = Circle(5)

# print("Area of the circle:", circle.area()) 


##4##
# class BankAccount:
#   def __init__(self, initial_balance=0):
#       self.balance = initial_balance

#   def deposit(self, amount):
#       self.balance += amount
#       return self.balance

#   def withdraw(self, amount):
#       if amount <= self.balance:
#           self.balance -= amount
#           return self.balance
#       else:
#           print("Insufficient funds")
#           return self.balance
# account = BankAccount(1000) 
# print("Current balance:", account.balance) 

# account.deposit(500)  
# print("Current balance after deposit:", account.balance)  

# account.withdraw(200)  
# print("Current balance after withdrawal:", account.balance)  

# account.withdraw(2000)  


##5##
# class Shape:
#   def __init__(self):
#       pass

#   def area(self):
#       return 0


# class Square(Shape):
#   def __init__(self, length):
#       super().__init__()
#       self.length = length

#   def area(self):
#       return self.length ** 2
# square = Square(5)
# print("Area of square:", square.area()) 


##6##
# class Car:
#   def __init__(self, make, model, year):
#       self.make = make
#       self.model = model
#       self.year = year

#   def display_details(self):
#       print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}")
# my_car = Car("Audi", "Q6 e-tron", 2023)
# my_car.display_details() 


##7##
# class Student:
#   total_students = 0

#   def __init__(self, name, age, grade):
#       self.name = name
#       self.age = age
#       self.grade = grade
#       Student.total_students += 1

#   def display_details(self):
#       print("Name:", self.name)
#       print("Age:", self.age)
#       print("Grade:", self.grade)

#   @classmethod
#   def display_total_students(cls):
#       print("Total number of students:", cls.total_students)


# student1 = Student("Aasiya", 15, "A")
# student2 = Student("Farhan", 16, "B")

# student1.display_details()
# print() 
# student2.display_details()

# print() 
# Student.display_total_students()   


##8##
# import random

# class BankAccount:
#     def __init__(self):
#         self.__balance = 0.0
#         self.__account_number = random.randint(10000000, 99999999)

#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             print(f"Deposit of ${amount} successful.")
#         else:
#             print("Invalid amount for deposit.")

#     def withdraw(self, amount):
#         if 0 < amount <= self.__balance:
#             self.__balance -= amount
#             print(f"Withdrawal of ${amount} successful.")
#         else:
#             print("Insufficient funds for withdrawal.")

#     def display_balance(self):
#         print(f"Account Number: {self.__account_number}")
#         print(f"Current Balance: ${self.__balance:.2f}")
# account = BankAccount()
# account.deposit(1000)
# account.withdraw(500)
# account.withdraw(700)


##9##
# class Author:
#   def __init__(self, name, birth_year):
#       self.name = name
#       self.birth_year = birth_year
# class Book:
#   def __init__(self, title, year, author):
#       self.title = title
#       self.year = year
#       self.author = author
#   def display_details(self):
#       print("Title:", self.title)
#       print("Year:", self.year)
#       print("Author:", self.author.name)
#       print("Author's Birth Year:", self.author.birth_year)
# author1 = Author("Harper Lee", 1926)
# book1 = Book("To Kill A Mockingbird", 1960, author1)
# book1.display_details() 




