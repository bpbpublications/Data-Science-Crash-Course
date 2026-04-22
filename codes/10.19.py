#!/usr/bin/env python
# coding: utf-8

# In[81]:


import matplotlib.pyplot as plt
days = list(range(1, 11))
temps = [30, 32, 31, 29, 33, 35, 34, 30, 28, 32]
plt.plot(days, temps, marker='o', color='blue')
plt.title("Daily Temperature Over 10 Days")
plt.xlabel("Day")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.show()


# In[ ]:





# In[ ]:




