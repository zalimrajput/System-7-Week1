# Day 1: Python Basics

# 1. Variables and Data Types
name = "Rajput"          # String
age = 20                 # Integer
height = 5.8             # Float
is_student = True        # Boolean

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is Student:", is_student)

# Check data types
print("\n--- Data Types ---")
print(type(name))
print(type(age))
print(type(height))
print(type(is_student))

# 2. Operators
print("\n--- Operators ---")
a = 10
b = 3

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Power:", a ** b)

# 3. User Input and Output
print("\n--- User Input ---")
user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))

print("Hello,", user_name)
print("Next year, you will be", user_age + 1)

# 4. Simple Calculation
print("\n--- Simple Calculator ---")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Sum:", num1 + num2)
print("Product:", num1 * num2)