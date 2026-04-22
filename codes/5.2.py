#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
from feature_engine.encoding import OneHotEncoder

df = pd.DataFrame({'col': [1, 2, 3, 4, 5]})

# Convert to categorical (string)
df['col'] = df['col'].astype(str)

encoder = OneHotEncoder()
transformed_data = encoder.fit_transform(df)

print(transformed_data)


# In[ ]:




