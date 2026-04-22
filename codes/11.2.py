#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "Order_ID": [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010],
    "Product_Name": [" Laptop ", "Smartphone", "Headphones", " laptop", "Tablet ", "Smartphone", "Camera", " Headphones ", "Smartwatch", "Laptop"],
    "Category": ["Electronics", "Electronics", "Accessories", "Electronics", "Electronics", "Electronics", "Electronics", "Accessories", "Accessories", "Electronics"],
    "Revenue": [75000, 50000, np.nan, 75000, 30000, 50000, np.nan, 2000, 15000, 75000],
    "Quantity": [2, 1, 3, 2, 1, 1, 1, 2, 1, 2]
}

df = pd.DataFrame(data)

# Pairplot using a valid column
sns.pairplot(df, hue="Category")

plt.show()


# In[ ]:




