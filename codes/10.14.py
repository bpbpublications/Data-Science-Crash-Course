#!/usr/bin/env python
# coding: utf-8

# In[73]:


from scipy.interpolate import interp1d
x = [0, 1, 2]
y = [0, 1, 4]
f = interp1d(x, y)
print(f(1.5)) 


# In[ ]:





# In[ ]:




