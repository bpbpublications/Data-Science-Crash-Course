#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd

# Sample data
data = {'CustomerID': [1, 2, 1], 'PurchaseAmount': [100, 200, 50]}
df = pd.DataFrame(data)

# Compute total spent per customer
df['TotalSpent'] = df.groupby('CustomerID')['PurchaseAmount'].transform('sum')

print(df)


# In[ ]:





# In[ ]:




