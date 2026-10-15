# File Handling , Exception , Modules and Basic OOP

# File Handling

# Syntax
from fileinput import close

# f=open("filename", "mode")
# f.close()

# File opening modes
print("File opening modes")

f = open("demofile.txt", "r")
print(f.read())

# using with statement to open a file
print("\nUsing with statement to open a file")

with open("data.txt", "r") as file:
    content = file.read()
    print(content)
   
   
# Reading specific number of characters from a file
print("Reading specific number of characters from a file") 
   
with open("data.txt", "r") as file:
    print(file.read(5))


# Reading a single line from a file
print("Reading a single line from a file")  
  
with open("data.txt", "r") as file:
    print(file.readline())


# Reading all lines from a file
print("Reading all lines from a file") 
   
with open("data.txt", "r") as file:
    lines = file.readlines()
    print(lines)
    

# Writing to a file
print("Writing to a file")

with open("data.txt", "w") as file:
    file.write("Learning Python")
    print("Written to the file successfully.")
 
# Writing multiple lines to a file
print("Writing multiple lines to a file") 
   
with open("data.txt", "w") as file:
    file.write("Python\n")
    file.write("Java\n")
    file.write("C++\n")    
    print("Written multiple lines to the file successfully.")

# Appending to a file
print("Appending to a file")
    
with open("data.txt", "a") as file:
    file.write("JavaScript\n")    
    print("Appended to the file successfully.")
    
    
    
# Exception Handling

print("\n--- Exception Handling ---")
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a / b

except ValueError:
    print("Enter numbers only.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

else:
    print("Result:", result)

finally:
    print("Program finished.")
    
    
# Modules
print("\n--- Built-in Modules ---")

# Math
print("\n--- Math Module ---")
import math

print(math.sqrt(25))
print(math.factorial(5))
print(math.pi)    


# Random
print("\n--- Random Module ---")
import random

number = random.randint(1, 100)
print(number)    


# Datetime
print("\n--- Datetime Module ---")
import datetime

today = datetime.date.today()
print(today)


# Basic OOP
print("\n--- Basic OOP ---")

# without init method
print("\n--- Without init method ---")
class Person:
    name = "Rajput"
    
p=Person()
print(p.name)    


# with init method
print("\n--- With init method ---")
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Linus", 28)

print(p1.name)
print(p1.age)



# Class with methods
print("\n--- Class with methods ---")

class Person:
  def __init__(self, name):
    self.name = name

  def greet(self):
    print("Hello, my name is " + self.name)

p1 = Person("Emil")
p1.greet()


# Methods with parameters
print("\n--- Methods with parameters ---")

class Calculator:
  def add(self, a, b):
    return a + b

  def multiply(self, a, b):
    return a * b

calc = Calculator()
print(calc.add(5, 3))
print(calc.multiply(4, 7))


# Modify object properties
print("\n--- Modify object properties ---")

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def celebrate_birthday(self):
    self.age += 1
    print(f"Happy birthday! You are now {self.age}")

p1 = Person("Linus", 25)
p1.celebrate_birthday()
p1.celebrate_birthday()


# Inheritance
print("\n--- Inheritance ---")

class Animal:
    def eat(self):
        print("This animal eats food")


class Dog(Animal):
    def bark(self):
        print("Dog is barking")


d1 = Dog()

d1.eat()   # Inherited from Animal
d1.bark()  # Defined in Dog


# Polymorphism
print("\n--- Polymorphism ---")

class Dog:
    def sound(self):
        print("Dog barks")


class Cat:
    def sound(self):
        print("Cat meows")


d1 = Dog()
c1 = Cat()

d1.sound()
c1.sound()


# Encapsulation
print("\n--- Encapsulation ---")

# private attribute 
class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age # Private property

p1 = Person("Emil", 25)
print(p1.name)
print(p1.__age) # This will cause an error beacuse Private properties cannot be accessed directly from outside the class.


# Accessing private attribute using getter method
print("\n--- Accessing private attribute using getter method ---")
class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age

  def get_age(self):
    return self.__age

p1 = Person("Tobias", 25)
print(p1.get_age())


# full example public , private and protected attributes
print("\n--- Full example public , private and protected attributes ---")

class Parent:
    def __init__(self):
        self.name = "Public"
        self._age = 25
        self.__salary = 50000

    def show(self):
        print(self.name)
        print(self._age)
        print(self.__salary)


class Child(Parent):
    def display(self):
        print(self.name)  # Public: works
        print(self._age)  # Protected convention: works
        # print(self.__salary)  # Does not access Parent's private-style attribute


p = Parent()
p.show()

print(p.name)   # Works
print(p._age)   # Works, but intended for internal use
# print(p.__salary)  # AttributeError