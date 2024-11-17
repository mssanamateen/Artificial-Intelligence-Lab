#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
df=pd.read_csv("diabetes.csv")


# In[2]:


df.head()


# In[3]:


df.tail()


# In[4]:


df.shape


# In[5]:


df.isnull().sum()


# In[7]:


X=df.iloc[:,:-1].to_numpy()
Y=df.iloc[:,-1].to_numpy()


# In[8]:


X


# In[9]:


Y


# In[11]:


from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=0)


# In[12]:


from sklearn.tree import DecisionTreeClassifier
clf=DecisionTreeClassifier(criterion="entropy",random_state=0)
clf.fit(X_train,Y_train)


# In[15]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
from sklearn.tree import plot_tree
clf.fit(X_train,Y_train)
plt.figure(figsize=(20,10))
plot_tree(clf,feature_names=['Glucose','BMI'],class_names=['No','Yes'])
plt.show()


# In[18]:


clf.set_params(max_depth=3)
clf.fit(X_train,Y_train)
plt.figure(figsize=(20,10))
plot_tree(clf,feature_names=['Glucose','BMI'],class_names=['No','Yes'])
plt.show()


# In[20]:


predictions=clf.predict(X_test)


# In[21]:


clf.predict([[90,20],[200,30]])


# In[22]:


predictions=clf.predict(X_test)


# In[23]:


predictions


# In[ ]:




