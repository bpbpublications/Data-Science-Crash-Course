#!/usr/bin/env python
# coding: utf-8

# In[12]:


import plotly.express as px
df = px.data.gapminder().query("year == 2007")
fig = px.choropleth(df, locations="iso_alpha",
                    color="lifeExp",
                    hover_name="country",
                    color_continuous_scale=px.colors.sequential.Plasma)
fig.show()


# In[ ]:




