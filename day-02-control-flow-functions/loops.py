# 1. Conditions 
print("\n--- Conditions (if,else) ---")
age = 20

if age >= 18:
    print("You are an adult")
else:
    print("You are under 18")


print("\n--- Grade Evaluation (if,elif,else) ---")

marks = 75
if marks >= 80:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
else:
    print("Grade C")
    
    
# 2. Loops
print("\n--- Loops (for) ---")
for i in range(5):
    print(i)
    
    
print("\n--- Loops (while) ---")
count = 1

while count <= 5:
    print(count)
    count += 1    
    
# 3. Loops with break and continue
print("\n--- Loops with break and continue ---")

for i in range(1, 6):
    if i == 3:
        break
    print(i)    

for i in range(1, 6):
    if i == 3:
        continue
    print(i)
    
# 4. Range
print("\n--- Range ---")

for i in range(5):
    print(i)

print("\n--- Range with start and end ---")
for i in range(2, 7):
    print(i)
    
print("\n--- Range with step ---")    
for i in range(2, 11, 2):
    print(i)

print("\n--- Range in reverse order ---")    
for i in range(5, 0, -1):
    print(i)
    
    
            
# 5. Functions
print("\n--- Functions ---")

# simple function without parameters
print("\n--- Simple Function ---")
def greet():
    print("Hello, Python!")

greet()

# fun with parameter
print("\n--- Function with Parameters ---")
def greet(name):
    print("Hello", name)

greet("Ali")
greet("Sara")    


# function with return value
print("\n--- Function with Return Value ---")
def add(a, b):
    return a + b

result = add(10, 5)
print(result)



# 6. Combine Conditions, Loops, and Functions
print("\n--- Combine Conditions, Loops, and Functions ---")
def check_even(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

for i in range(1, 6):
    print(i, check_even(i))