#!/usr/bin/env python
# coding: utf-8

# In[50]:


import pandas as pd
import matplotlib.pyplot as plt

# Sample predefined data
data = {
    'Experience': [1, 2, 3, 4, 5],
    'Salary': [30000, 40000, 50000, 60000, 70000]
}

df = pd.DataFrame(data)

# Scatter plot
plt.scatter(df['Experience'], df['Salary'])

# Labels
plt.xlabel('Years of Experience')
plt.ylabel('Salary')

# Title (optional)
plt.title('Experience vs Salary')

# Show plot
plt.show()


# In[ ]:





# In[ ]:




