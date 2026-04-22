#!/usr/bin/env python
# coding: utf-8

# In[65]:


import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'London', 'Paris']
}

df = pd.DataFrame(data)
print(df)


data = [
    ['Alice', 25, 'New York'],
    ['Bob', 30, 'London'],
    ['Charlie', 35, 'Paris']
]

df = pd.DataFrame(data, columns=['Name', 'Age', 'City'])
print(df)


# In[ ]:





# In[ ]:




