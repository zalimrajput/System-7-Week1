# List , Tuples, Sets , Dictionaries

# 1. List with Methods & Operations

print("\n--- List with Methods ---")
numbers = [10, 20, 30, 20]

# Append
print("\n--- Append ---")
a = [10, 20]
a.append(30)
print(a)

# Extend
print("\n--- Extend ---")
a = [10, 20]
a.extend([30, 40])
print(a)


# Insert
print("\n--- Insert ---")
a = [10, 30]
a.insert(1, 20)
print(a)

# Remove
print("\n--- Remove ---")
a = [10, 20, 20]
a.remove(20)
print(a)

# Pop
print("\n--- Pop ---")
a = [10, 20, 30]
x = a.pop()
print(a)

# Clear
print("\n--- Clear ---")
a = [10, 20]
a.clear()
print(a)

# Index
print("\n--- Index ---")
a = [10, 20, 30]
print(a.index(20))


# Count
print("\n--- Count ---")    
a = [10, 20, 20, 30]
print(a.count(20))

# Sort (by default acsending order)
print("\n--- Sort ---")
a = [30, 10, 20]
a.sort()
print(a)

print("\n--- Sort in Reverse Order ---")
a.sort(reverse=True)
print(a)

# Reverse
print("\n--- Reverse ---")
a = [10, 20, 30]
a.reverse()
print(a)

# Copy
print("\n--- Copy ---")
a = [10, 20]
b = a.copy()
print(b)



print("\n--- List Operations ---")
a = [10, 20, 30]

print(len(a))       
print(max(a))       
print(min(a))       
print(sum(a))       
print(sorted(a))    
print(20 in a)      
print(a[0])         
print(a[0:2])       



# Tuples
print("\n--- Tuples With Methods ---")
numbers = (10, 20, 20, 30)

print("\n--- Count ---")
a = (10, 20, 20, 30)
print(a.count(20))


print("\n--- Index ---")
a = (10, 20, 30)
print(a.index(30))


# Tuples wuth Operations
print("\n--- Tuple Operations ---")
a = (10, 20, 30)

print(len(a))       # 3
print(max(a))       # 30
print(min(a))       # 10
print(sum(a))       # 60
print(a[0])         # 10
print(a[0:2])       # (10, 20)
print(20 in a)      # True



# Dictionaries
print("\n--- Dictionaries With Methods ---")

student = {
    "name": "Ali",
    "age": 20,
    "marks": 85
}


# Keys
print("\n--- Keys ---")
print(student.keys())


# Values
print("\n--- Values ---")
print(student.values())


# Items
print("\n--- Items ---")
print(student.items())


# Get
print("\n--- Get ---")
print(student.get("name"))      
print(student.get("grade"))      
print(student.get("grade", 0))  


# Update
print("\n--- Update ---")
student.update({"age": 21, "city": "Lahore"})
print(student)

# Pop
print("\n--- Pop ---")
age = student.pop("age")
print(age)  

# Popitem
print("\n--- Popitem ---")
print(student.popitem())


# Set Default
print("\n--- Set Default ---")
student.setdefault("city", "Lahore")
print(student)


# Copy
print("\n--- Copy ---")
student_copy = student.copy()
print(student_copy)


# Clear
print("\n--- Clear ---")
student.clear()
print(student)


# Format Keys
print("\n--- Format Keys ---")
stu= dict.fromkeys(["a", "b", "c"], 0)
print(stu)

print("\n--- Dictionary Operations ---")
student = {"name": "Ali", "age": 20}

print(student["name"])    # Ali
print("age" in student)   # True
print(len(student))       # 2

student["marks"] = 85     # Add
student["age"] = 21       # Update
del student["marks"]      # Delete a key


# Sets
print("\n--- Sets With Methods ---")

a = {10, 20, 30}
b = {20, 30, 40}

# Add
print("\n--- Add ---")
a = {10, 20}
a.add(30)
print(a)

# Update
print("\n--- Update ---")
a = {10, 20}
a.update([30, 40])
print(a)

# Remove
print("\n--- Remove ---")
a = {10, 20, 30}
a.remove(20)
print(a)


# Discard
print("\n--- Discard ---")
a = {10, 20, 30}
a.discard(50)
print(a)


# Pop
print("\n--- Pop ---")
a = {10, 20, 30}
x = a.pop()
print(x)


# Clear
print("\n--- Clear ---")
a = {10, 20}
a.clear()
print(a)


# Sets with Math Operations
print("\n--- Sets with Math Operations ---")

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# Union
print("\n--- Union ---")
print(a.union(b))

# Intersection
print("\n--- Intersection ---")
print(a.intersection(b))


# Difference
print("\n--- Difference ---")
print(a.difference(b))


# Symmetric Difference
print("\n--- Symmetric Difference ---")
print(a.symmetric_difference(b))

# Set comparison and in place methods
a = {1, 2}
b = {1, 2, 3}

print(a.issubset(b))      # True
print(b.issuperset(a))    # True
print(a.isdisjoint({5, 6}))  # True

a = {1, 2, 3}
a.intersection_update({2, 3, 4})
print(a)                  


# Set Operations
print("\n--- Set Operations ---")

a = {10, 20, 30}

print(len(a))       # 3
print(20 in a)      # True
print(50 not in a)  # True
print(sorted(a))    # [10, 20, 30]