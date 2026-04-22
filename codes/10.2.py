#!/usr/bin/env python
# coding: utf-8

# In[57]:


import numpy as np
# From a list
arr = np.array([1, 2, 3, 4])
# 2D Array
matrix = np.array([[1, 2], [3, 4]])
# Using functions
zeros = np.zeros((2, 3)) 
print(zeros)# 2x3 array of zeros
ones = np.ones((3, 2)) 
print(ones)# 3x2 array of ones
range_array = np.arange(0, 10, 2)
print(range_array)# Array: [0, 2, 4, 6, 8]
linspace_array = np.linspace(0, 1, 5)
print(linspace_array)# 5 evenly spaced values between 0 and 1
print(arr.shape)       # Returns the shape of the array
print(arr.ndim)        # Number of dimensions
print(arr.size)        # Total number of elements
print(arr.dtype)


# In[ ]:





# In[ ]:




