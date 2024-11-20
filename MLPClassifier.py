#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
data=pd.read_csv('HR_comma_sep.csv')
data.head()


# In[2]:


data.info()


# In[3]:


data['salary'].value_counts()


# In[4]:


data['Department'].value_counts()


# In[5]:


data['last_evaluation'].value_counts()


# In[10]:


data['Department'].unique()


# In[8]:


from sklearn import preprocessing
le=preprocessing.LabelEncoder()


# In[11]:


print(le)
data['salary']=le.fit_transform(data['salary'])
data['Department']=le.fit_transform(data['Department'])


# In[12]:


data[''].unique()


# In[13]:


data['Department'].unique()


# In[19]:


print(pd.__version__)


# In[21]:


X=data[['satisfaction_level','last_evaluation','number_project','average_montly_hours','time_spend_company','Work_accident','promotion_last_5years','Department','salary']]
y=data['left']


# In[23]:


from sklearn.model_selection import train_test_split


# In[24]:


X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=42)
X_train


# In[27]:


from sklearn.neural_network import MLPClassifier
clf=MLPClassifier(hidden_layer_sizes=(6,5),random_state=5,verbose=True,learning_rate_init=0.01)
clf.fit(X_train,y_train)


# In[28]:


ypred=clf.predict(X_test)
from sklearn.metrics import accuracy_score
accuracy_score(y_test,ypred)


# In[29]:


X_test.shape


# In[33]:


n=pd.DataFrame({
    'satisfaction_level':[0.70],'last_evaluation':[0.53],'number_project':[2],'average_montly_hours':[157],'time_spend_company':[3],'Work_accident':[0],'promotion_last_5years':[0],'Department':[1],'salary':[1]
})
new_data=clf.predict(n)
print(new_data)


# In[35]:


from sklearn.metrics import confusion_matrix
y_pred=clf.predict(X_test)
print(confusion_matrix(y_test,ypred))


# In[36]:


print(y_train.value_counts())
print(y_test.value_counts())


# In[37]:


from sklearn.metrics import classification_report
print(classification_report(y_test,ypred))


# In[39]:


from sklearn.metrics import confusion_matrix
y_pred=clf.predict(X_test)
print(confusion_matrix(y_test,ypred))


# In[40]:


print(y_train.value_counts())
print(y_test.value_counts())


# In[ ]:




