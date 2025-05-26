
In Python, arrays can be implemented using either:

Lists – Built-in and very flexible.

array module – More memory-efficient for uniform data types.

NumPy arrays – Powerful for numerical computations (if you're using NumPy).


1. Using Python Lists


# List implementation
arr = [10, 20, 30, 40]

# Accessing elements
print(arr[1])  # Output: 20

# Adding elements
arr.append(50)

# Removing elements
arr.remove(30)

# Iterating through the array
for item in arr:
    print(item)

2. Using array Module


import array

# Creating an integer array
arr = array.array('i', [10, 20, 30, 40])

# Accessing elements
print(arr[2])  # Output: 30

# Adding elements
arr.append(50)

# Removing elements
arr.remove(20)

# Iterating
for item in arr:
    print(item)




3. Using NumPy (optional, for scientific tasks)


import numpy as np

# Creating a NumPy array
arr = np.array([10, 20, 30, 40])

# Accessing and manipulating
print(arr[0])      # 10
print(arr + 5)     # Add 5 to each element
print(arr.mean())  # Calculate mean



