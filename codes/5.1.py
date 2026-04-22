#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np 
# Normalization 
data = np.array([1, 2, 3, 4, 5]) 
normalized_data = (data - np.min(data)) / (np.max(data) - np.min(data)) 
print(normalized_data)


# In[ ]:




