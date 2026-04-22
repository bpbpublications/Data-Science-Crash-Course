#!/usr/bin/env python
# coding: utf-8

# In[36]:


fs = frozenset([1, 2, 3, 2])
print(fs)  # Output: frozenset({1, 2, 3})

# From a set
s = set([4, 5, 6])
fs2 = frozenset(s)
print(fs2)

# From a string (creates a frozenset of characters)
fs3 = frozenset("data")
print(fs3)  # Output: frozenset({'d', 'a', 't'})


# In[ ]:





# In[ ]:




