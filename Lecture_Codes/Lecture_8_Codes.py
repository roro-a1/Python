# OOP in Python - To map with real world scenarios, we started using objects in code. This is called Object-Oriented Programming.
# Class & Object in Python -
# Class is a blueprint for creating objects. Object is an instance of that class.
# Constructor(__init__ Function) - All classes haver a function called __init__(), which is always executed when the class is being initiated.

"""
class Student:
    name = "Chitra"
    def __init__(self): # Default constructors
        print("Adding new student in database...")

s1 = Student()
print(s1.name)
"""
"""
class Student:
    name = "Chitra"
    def __init__(self, student_name, mark):
        self.name = student_name
        self.mark = mark
        print("Adding new student in database...")

s1 = Student("Chitra", 97)
print(s1.name)
print(s1.mark)

s2 = Student("Shraddha", 78)
print(s2.name)
print(s2.mark)
"""

# Class & Instance Attributes - class.attr or object.attr.
# Methods - Methods are functions that belong to objects.
"""
class Student:
    name = "Chitra"
    def __init__(self, student_name, mark):
        self.name = student_name
        self.mark = mark
        print("Adding new student in database...")

    def welcome(self):
        print("Welcome student,", self.name)

    def get_marks(self):
        return self.mark

s1 = Student("Chitra", 97)
s1.welcome()
print(s1.get_marks())
"""

# Practice
# Create student class that takes name & marks of 3 subjects as arguments in constructor. Then create a method to print the average.
"""
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0

        for i in self.marks:
            sum += i
        print("Hi", self.name, "your average score is:", sum/3)

s1 = Student("Nora", [55, 78, 91])
s1.get_avg()
"""

# Static Methods - Methods that don't use the self parameter(work at class level)
"""
class Student:
    name = "Chitra"
    def __init__(self, student_name, mark):
        self.name = student_name
        self.mark = mark
        print("Adding new student in database...")

    @staticmethod
    def welcome():
        print("Welcome student!")

    def get_marks(self):
        return self.mark

s1 = Student("Chitra", 97)
s1.welcome()
print("Your score is", s1.get_marks())
"""

# 4 pillars - Abstraction, Encapsulation, Inheritance, Polymorphism.
# Abstraction - Hiding the implementation details of the class and only showing the essential features to the user.
"""
class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.clutch = True
        self.acc = True
        print("car started...")

car1 = Car()
car1.start()
"""

# Encapsulation - Wrapping data and functions into a single unit(object).

# Practice
# Create Account class with 2 attributes - balance & account no. Create methods for debit, credit & printing the balance.
"""
class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account = acc

    # Debit method
    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "was debited.")
        print("Current balance is", self.get_balance())

    # Credit method
    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "was credited.")
        print("Current balance is", self.get_balance())

    def get_balance(self):
        return self.balance

acc1 = Account(10000, 99666555554)
print("Your account number is", acc1.account)
acc1.debit(1000)
acc1.credit(6500)
acc1.credit(50000)
"""

# del keyword - Used to delete objects properties or object itself.
"""
class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("Chitra")
print(s1.name)
del s1.name
print(s1.name) # Throws error
"""

# Private(like) attributes & methods - Conceptual implementation in Python
# Private attributes & methods are meant to be used only within the class and are not accessible from outside the class.

"""
class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass

acc1 = Account("98765", "squert")

print(acc1.acc_no)
print(acc1.__acc_pass) # Throws error "'Account' object has no attribute '__acc_pass'"
"""

# Inheritance - When one class(child/derived) derives the properties and methods of another class(parent/base)
"""
class Car:
    @staticmethod
    def start():
        print("Car started...")

    @staticmethod
    def stop():
        print("Car stopped...")

class ToyotaCar(Car):
    def __init(self, name):
        self.name = name

car1 = ToyotaCar()
print(car1.start())
"""

# Inheritance types - 1. Single Inheritance, 2. Multi-level Inheritance, 3. Multiple Inheritance.
"""
class Car:
    @staticmethod
    def start():
        print("Car started...")

    @staticmethod
    def stop():
        print("Car stopped...")

class ToyotaCar(Car):
    def __init__(self, brand):
        self.brand = brand
        
class Fortuner(ToyotaCar): # Multi level Inheritance
    def __init__(self, name):
        self.name = name

car1 = ToyotaCar("Fortuner")
print(car1.start())
"""
"""
class Car:
    @staticmethod
    def start():
        print("Car started...")

    @staticmethod
    def stop():
        print("Car stopped...")


class ToyotaCar(Car):
    def __init__(self, brand):
        self.brand = brand


class Fortuner(ToyotaCar, Car):  # Multiple Inheritance
    def __init__(self, name):
        self.name = name

car1 = ToyotaCar()
print(car1.start())
"""

# Super Method - super() method is used to inherit the properties of parent class.

# Class Method - A class method is bound to the class & receives the class as an implicit first argument
# Note - static method can't access or modify class state & generally for utility.
"""
class Person:
    name = "Anonymous"

    def changeName(self, name):
        self.name = name

    def change_Name(self, name):
        self.__class__.name = "Apex"

p1 = Person()
p1.changeName("Chitra")
print(p1.name)
print(Person.name)
p2 = Person()
p2.changeName("Chitra")
print(p2.name)
"""

# Here my head went blank, this topic can only be understood by practice for me.
# Polymorphism is remaining, hopefully Angela Yu will take care of the rest for me in 100 days of coding bootcamp.