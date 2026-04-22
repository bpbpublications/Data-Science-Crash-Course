#!/usr/bin/env python
# coding: utf-8

# In[6]:


`


# In[7]:


import tensorflow as tf
import numpy as np

# Example data (2D: samples x features)
data = np.array([[1, 2, 3, 4, 5]])

# Normalize along axis 1 (features axis)
normalized_data = tf.keras.utils.normalize(data, axis=1)

print(normalized_data)


# In[ ]:





# In[ ]:




