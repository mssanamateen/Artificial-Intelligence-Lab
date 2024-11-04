#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


arr1=np.array([1,2,3])
arr1


# In[3]:


type(arr1)


# In[6]:


arr2=np.array([[1,2,3.3],[4,5,6.5,]])
arr2


# In[13]:


arr3=np.array([
    [
        [1,2],
        [3,4]
    ],
    [
        [5,6],
        [7,8]
    ]
])
print(arr3)


# In[14]:


arr4=np.array((12,13,15))
arr4


# In[15]:


print(arr1.ndim)


# In[16]:


print(arr2.ndim)


# In[17]:


print(arr3.ndim)


# In[18]:


print(arr4.ndim)


# In[19]:


array5=np.array([1,2,3,5],ndmin=4)
array5


# In[20]:


print(array5.ndim)


# In[22]:


array5.shape


# In[23]:


arr2


# In[25]:


arr2[0][1]


# arr2.shape(2,3)

# In[26]:


arr2.shape


# In[27]:


for x in range(0,2):
    for y in range(0,3):
        print(arr2[x][y])


# In[29]:


arr1.dtype


# In[30]:


arr2.dtype


# In[32]:


arr5=np.array([1,2,3,4,5],dtype='S')
arr5


# In[34]:


array2conv=arr2.astype('i')
array2conv


# 

# In[35]:


array2float=arr2.astype('f')
array2float


# In[41]:


num1=np.zeros((2,2),dtype=int)
num1


# In[47]:


range_array=np.arange(0,10,3)
range_array


# In[61]:


a=np.random.randint(low=4,high=10,size=5)
a


# In[64]:


np.concatenate([arr1,arr4])


# In[65]:


flatarr=arr3.flatten()
flatarr


# In[ ]:




