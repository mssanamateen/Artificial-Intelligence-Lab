#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


pd.__version__


# In[3]:


cars=pd.Series(["BEmDablu","Toyota","Honda"])
cars


# In[4]:


sindex=pd.Series(["BEmDablu","Honda","Toyota"],index=["Fastest","Yaverage","Slow"])


# In[5]:


sindex


# In[6]:





# In[7]:


colors=pd.Series(["Blue","Silvar","Blyack"])
colors


# In[8]:


car_data=pd.DataFrame({"Car make":cars,"Color":colors})
car_data


# In[10]:


car_sales=pd.read_csv("car-sales.csv")
car_sales


# In[11]:


car_sales.to_csv("export_cars.csv",index=False)


# In[12]:


export_cars.describe()


# In[13]:


export_cars


# In[14]:


export_cars=pd.read_csv("export_cars.csv")


# In[15]:


export_cars


# In[23]:


export_cars.describe


# In[17]:


export_cars.dtypes


# In[19]:


export_cars.shape


# In[20]:


export_cars.info()


# In[21]:


export_cars.columns


# In[22]:


export_cars.index


# In[24]:


car_sales[["Odometer (KM)","Doors"]].mean()


# In[25]:


car_sales.sum()


# In[26]:


car_sales["Doors"].sum()


# In[27]:


len(car_sales)


# In[30]:


car_sales.head(3)


# In[31]:


car_sales.tail(3)


# In[32]:


fruits=pd.Series(["apple","banana","Mango","Berry"],index=[0,3,4,3])


# In[35]:


fruits.iloc[3]


# In[36]:


fruits.loc[3]


# In[37]:


fruits.loc[4]


# In[ ]:




