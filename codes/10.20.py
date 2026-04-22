#!/usr/bin/env python
# coding: utf-8

# In[84]:


from scipy.optimize import minimize
import numpy as np
f = lambda x: x**2 + 10*np.sin(x)
result = minimize(f, x0=0)
print("Minimum at x =", result.x)


# In[ ]:





# In[ ]:




