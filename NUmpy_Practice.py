import numpy as np

# Creating Numpy Arrays
print("Creating Numpy Arrays")
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("Array 'a':", a)
print("Array 'b':", b)

# Basic Operations
print("\nBasic Operations")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

# Dot Product
print("\nDot Product")
print("Dot Product of 'a' and 'b':", np.dot(a, b))

# Cross Product
print("\nCross Product")
print("Cross Product of 'a' and 'b':", np.cross(a, b))

# Reshaping
print("\nReshaping..")
print("Original Shape of 'a':", a.shape)
a = a.reshape(3, 1)
print("Reshaped 'a':", a)

# Slicing
print("\nSlicing")
print("Slicing first 2 elements of 'a':", a[:2])

# Sorting
print("\nSorting")
print("Sorted 'a':", np.sort(a))

# Finding Unique Elements
print("\nFinding Unique Elements")
a = np.array([1, 2, 2, 3, 3, 3])
print("Unique elements of 'a':", np.unique(a))