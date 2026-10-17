# Numpy Array , Indexing & Mathematical Operations


# NumPy 

import numpy as np

# Python list
print("Python List")
numbers = [10, 20, 30, 40]

# NumPy array
print("NumPy Array")
arr = np.array([10, 20, 30, 40])

print(numbers)
print(arr)



# TYpe of array
print("Type of array")

# Zero Dimension Array
print("Zero Dimensional Array")
a = np.array(54)
print(a)

# One Dimension Array
print("One Dimensional Array")
b = np.array([10, 20, 30])
print(b)


# Two Dimensional Array
print("Two Dimensional Array")
c = np.array([[1, 2, 3],
              [4, 5, 6]])
print(c)


# Three dimension Array
print("Three Dimensional Array")

d= np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])
print(d.shape)



# Useful Array Properties
print("Array Properties")
import numpy as np

arr = np.array([[10, 20, 30],
                [40, 50, 60]])

print(arr.ndim)   # Number of dimensions: 2
print(arr.shape)  # Rows and columns: (2, 3)
print(arr.size)   # Total elements: 6
print(arr.dtype)  # Data type of elements


# Array Indexing
print("Array Indexing")


# One Dimensional Array Indexing
print("One Dimensional Array Indexing")
arr = np.array([1, 2, 3, 4])
print(arr[0])



# One Dimensional Array Indexing &  Addition
print("One Dimensional Array Indexing &  Addition")
arr = np.array([1, 2, 3, 4])
print(arr[2] + arr[3])


# Two Dimensional Array Indexing
print("Two Dimensional Array Indexing")

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('2nd element on 1st row: ', arr[0, 1])


# Three Dimensional Array Indexing
print("Three Dimensional Array Indexing")
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr[0, 1, 2])



# Negative Indexing
print("Negative Indexing")
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('Last element from 2nd dim: ', arr[1, -1])


# Array Slicing
print("Array Slicing")

# 1 to 5 elements
print("1 to 5 elements")
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5])

# 4 to end
print("4 to end")
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[4:])


# 0 to 4 elements
print("0 to 4 elements")
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[:4])


# Array with Data Type
print("Array with Data Type")

print("Converting to String")
arr = np.array([1, 2, 3, 4], dtype='S')
print(arr)
print(arr.dtype)


print("Converting to Integer")
arr = np.array([1, 2, 3, 4], dtype='i4')
print(arr)
print(arr.dtype)

# Array Copy & View
print("Array Copy & View")

print("Array Copy")
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42
print(arr)
print(x)

print("Array View")
arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42
print(arr)
print(x)


# Array Reshaping
print("Array Reshaping")
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)
print(newarr)


# Array Iterating
print("Array Iterating")
print("Iterating 1D Array")
arr = np.array([1, 2, 3])
for x in arr:
  print(x)
  
print("Iterating 2D Array")  
arr = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr:
  print(x)  
  
  
# Array Joining
print("Array Joining")
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2))
print(arr)
  
  
# Array Joining 2D
print("Array Joining 2D")
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.concatenate((arr1, arr2), axis=1)
print(arr)  
  
 
 
# Array Joining by Axis  
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.concatenate((arr1, arr2), axis=1)
print(arr)  


# Array Splitting
print("Array Splitting")
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)
print(newarr)


# Array Searching
print("Array Searching")
arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)
print(x)


# Array Sorting
print("Array Sorting")
arr = np.array([3, 2, 0, 1])
print(np.sort(arr))


# Array Filtering
print("Array Filtering")
arr = np.array([41, 42, 43, 44])
x = [True, False, True, False]
newarr = arr[x]
print(newarr)