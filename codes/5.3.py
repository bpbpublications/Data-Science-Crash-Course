#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create a sample pandas DataFrame with some missing values
data = {
    "A": [1, 2, None, 4],
    "B": [None, 2, 3, 4],
    "C": [1, None, None, 4]
}
df = pd.DataFrame(data)

# Plot missing values heatmap
sns.heatmap(df.isnull(), cbar=False, cmap="viridis")
plt.show()


# In[ ]:




