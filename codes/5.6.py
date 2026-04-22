#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip uninstall featuretools woodwork -y')


# In[2]:


get_ipython().system('pip install featuretools==1.29.0 woodwork==0.27.0')


# In[ ]:





# In[4]:


import featuretools as ft
import pandas as pd

# Sample data
customers = pd.DataFrame({
    "customer_id":[1,2,3],
    "signup_date":pd.to_datetime(["2022-01-01","2022-02-01","2022-03-01"])
})
orders = pd.DataFrame({
    "order_id":[1,2,3,4],
    "customer_id":[1,2,1,3],
    "order_date":pd.to_datetime(["2022-01-05","2022-02-15","2022-03-01","2022-03-15"]),
    "amount":[100,200,150,300]
})

# Initialize Woodwork with a name!
customers.ww.init(name="customers", index="customer_id", time_index="signup_date")
orders.ww.init(name="orders", index="order_id", time_index="order_date")

# Create EntitySet
es = ft.EntitySet(id="Retail")
es = es.add_dataframe(dataframe_name="customers", dataframe=customers)
es = es.add_dataframe(dataframe_name="orders", dataframe=orders)

# Add relationship
es = es.add_relationship("customers","customer_id","orders","customer_id")

# Generate features
feature_matrix, feature_defs = ft.dfs(entityset=es, target_dataframe_name="customers")
print(feature_matrix)


# In[ ]:




