#!/usr/bin/env python
# coding: utf-8

# In[80]:


import pandas as pd
data = {
    'Student': ['Alice', 'Bob', 'Charlie', 'David'],
    'Math': [85, 90, 95, 80],
    'Science': [88, 84, 91, 87]
}

df = pd.DataFrame(data)
df['Average'] = df[['Math', 'Science']].mean(axis=1)
top_students = df.sort_values('Average', ascending=False).head(3)
print(top_students)


# In[ ]:





# In[ ]:




