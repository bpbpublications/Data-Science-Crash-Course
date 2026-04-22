#!/usr/bin/env python
# coding: utf-8

# In[3]:


from sklearn.linear_model import LinearRegression
X = [[1], [2], [3], [4]]
y = [2, 4, 6, 8]

model = LinearRegression()
model.fit(X, y)
print(model.predict([[5]]))  # Output ~ [10]


# In[ ]:




