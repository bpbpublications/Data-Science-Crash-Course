#!/usr/bin/env python
# coding: utf-8

# In[6]:


from sklearn.preprocessing import OneHotEncoder
import pandas as pd

# Sample categorical data
customer_data = [['Male'], ['Female'], ['Female']]

# Create encoder (use sparse_output=False for dense array)
encoder = OneHotEncoder(sparse_output=False)

# Fit and transform the data
encoded_data = encoder.fit_transform(customer_data)

# Optional: convert to DataFrame for readability
encoded_df = pd.DataFrame(encoded_data, columns=encoder.get_feature_names_out(['Gender']))

print(encoded_df)


# In[ ]:




