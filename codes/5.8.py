#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
from sklearn.impute import SimpleImputer

# Sample data with missing values
data = {
    'Age': [25, 30, None, 40],
    'Blood Pressure': [120, 130, None, 140]
}
df = pd.DataFrame(data)

# Create imputer to fill missing values with the mean
imputer = SimpleImputer(strategy='mean')

# Fit and transform all columns at once
df[:] = imputer.fit_transform(df)

print(df)


# In[ ]:




