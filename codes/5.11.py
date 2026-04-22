#!/usr/bin/env python
# coding: utf-8

# In[11]:


import tensorflow as tf

# Load CIFAR-10 dataset (small color images)
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.cifar10.load_data()

# Pick one image
image_array = x_train[0] / 255.0  # normalize
print(image_array.shape)


# In[ ]:





# In[ ]:




