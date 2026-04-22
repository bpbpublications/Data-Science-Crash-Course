#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
from sklearn.preprocessing import StandardScaler

# Sample numeric data
data = pd.DataFrame({
    "age": [25, 32, 47, 51],
    "income": [50000, 60000, 80000, 90000]
})

# Initialize scaler
scaler = StandardScaler()

# Fit and transform the data
scaled_data = scaler.fit_transform(data)

# Convert back to DataFrame to keep column names
scaled_df = pd.DataFrame(scaled_data, columns=data.columns)

print(scaled_df)


# In[ ]:




