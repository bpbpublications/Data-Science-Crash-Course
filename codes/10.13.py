#!/usr/bin/env python
# coding: utf-8

# In[72]:


from scipy.optimize import minimize
f = lambda x: x**2 + 5*np.sin(x)
result = minimize(f, x0=2)
print(f)
print(result)


# In[ ]:





# In[ ]:




