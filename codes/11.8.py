#!/usr/bin/env python
# coding: utf-8

# In[14]:


get_ipython().system('pip install folium')
import folium
# Create a map centered at a location
m = folium.Map(location=[28.6139, 77.2090], zoom_start=6)

# Add a marker
folium.Marker([28.6139, 77.2090], popup='New Delhi').add_to(m)

# Display the map
m.save("india_map.html")


# In[15]:


import folium
# Create a map centered at a location
m = folium.Map(location=[28.6139, 77.2090], zoom_start=6)

# Add a marker
folium.Marker([28.6139, 77.2090], popup='New Delhi').add_to(m)

# Display the map
m.save("india_map.html")


# In[ ]:




