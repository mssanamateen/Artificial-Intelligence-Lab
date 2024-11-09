#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd


# In[4]:


pd.__version__


# In[11]:


sindex=pd.Series(["BMW","Toyota","Homnda"],index=["first","second","third"])
sindex


# In[12]:


sindex["second"]


# In[13]:


colors=pd.Series(["red","blue","white"])


# In[14]:


colors


# In[17]:


car_data=pd.DataFrame({"Car make":cars,"color":colors})
car_data


# In[24]:


car_sales=pd.read_csv("car-sales.csv")
car_sales


# In[34]:


car_sales.to_csv("export_cars.csv",index=False)

export_cars=pd.read_csv(")
# In[35]:


export_cars


# In[36]:


export_cars=pd.read_csv("export_cars.csv")


# In[37]:


export_cars


# In[38]:


export_cars.describe()


# In[39]:


export_cars.dtypes


# In[42]:


export_cars.shape


# In[45]:


export_cars.info()


# In[46]:


export_cars.columns


# In[50]:


export_cars.index


# In[51]:


export_cars.describe


# In[54]:


car_sales[["Odometer (KM)","Doors"]].mean()


# 

# In[55]:


car_sales.sum

car_sales.sum()
# In[56]:


car_sales.sum()


# In[57]:


car_sales["Doors"].sum()


# In[58]:


len(car_sales)


# In[59]:


car_sales.head()


# In[60]:


car_sales.tail()


# In[64]:


car_sales.loc[5]


# In[65]:


car_sales.iloc[5]


# In[71]:


fruits=pd.Series(["apple","banana","mango","berry"],index=[0,3,4,3])


# In[72]:


fruits.iloc[3]


# In[73]:


fruits.loc[3]


# In[ ]:




