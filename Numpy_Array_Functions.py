import numpy as np

# Define a Numpy array
numpy_array = np.array([1, 2, 3, 4, 5])
print('-'*50)
# Print the original array
print("Original Array: ", numpy_array)

# Create a new Numpy array
new_numpy_array = np.array([6, 7, 8, 9, 10])

# Print the new array
print("New Array: ", new_numpy_array)

# Add the two Numpy arrays
resulting_array = numpy_array + new_numpy_array

# Print the resulting array
print("Resulting Array: ", resulting_array)
print('-'*50)


# Define a Numpy array
numpy_array = np.array([4, 2, 9, 1, 5])

# Print the original array
print("Original Array: ", numpy_array)

# Sort the Numpy array in ascending order
sorted_array = np.sort(numpy_array)

# Print the sorted array
print("Sorted Array: ", sorted_array)
print('-'*50)

#NumPy array of random numbers

# Set the random seed for reproducibility
np.random.seed(0)

# Create a NumPy array of 5 random numbers between 0 and 1
random_array = np.random.rand(5)

# Print the random array
print("Random Array: ", random_array)
print('-'*50)