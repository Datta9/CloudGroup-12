#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install --upgrade numexpr')


# In[2]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sklearn


# In[3]:


s3_csv_path = f's3://airlinesatisfaction/data/train.csv'
s3_csv_test_path = f's3://airlinesatisfaction/data/test.csv'
train = pd.read_csv(s3_csv_path)
test = pd.read_csv(s3_csv_test_path)


# In[4]:


train.head()


# In[5]:


train.shape


# In[6]:


test.shape


# In[7]:


train.info()


# In[8]:


train.isnull().sum()


# In[9]:


test.isnull().sum()


# In[10]:


train.dropna(inplace=True)


# In[11]:


test.dropna(inplace=True)


# In[12]:


def dropds(dset):
    dset.drop(["Unnamed: 0","id"],axis=1,inplace=True)
    dset["Gender"] = dset["Gender"].map({"Male":1,"Female":0})
    dset["Customer Type"] = dset["Customer Type"].map({"Loyal Customer":1,"disloyal Customer":0})


# In[13]:


dropds(train)
dropds(test)


# In[14]:


train.shape


# In[15]:


test.shape


# In[16]:


train.head()


# In[17]:


train.info()


# In[18]:


train.info()


# In[19]:


travel_dum = pd.get_dummies(train[["Type of Travel"]],drop_first=True)
class_dum = pd.get_dummies(train[["Class"]],drop_first=True)
train = pd.concat([train,travel_dum,class_dum],axis=1)


# In[20]:


train.head()


# In[21]:


travel_dum = pd.get_dummies(test[["Type of Travel"]],drop_first=True)
class_dum = pd.get_dummies(test[["Class"]],drop_first=True)
test = pd.concat([test,travel_dum,class_dum],axis=1)


# In[22]:


test.head()


# In[23]:


train.drop(["Type of Travel","Class"],axis=1,inplace=True)


# In[24]:


test.drop(["Type of Travel","Class"],axis=1,inplace=True)


# In[25]:


train.head()


# In[26]:


test.head()


# In[27]:


train["satisfaction"] = train["satisfaction"].map({"satisfied":1,"neutral or dissatisfied":0})
test["satisfaction"] = test["satisfaction"].map({"satisfied":1,"neutral or dissatisfied":0})


# In[28]:


train.head()


# In[29]:


train.info()


# In[30]:


import seaborn as sns 
import matplotlib.pyplot as plt 


# In[31]:


plt.figure(figsize=(20,20))
#sns.pairplot(train)


# In[32]:


sns.countplot(x='Online boarding',hue="satisfaction",data=train,palette="dark:green")


# In[33]:


sns.histplot(x='Age',hue="satisfaction",data=train,kde=True,palette="flare")


# In[34]:


sns.countplot(x='Customer Type',hue="satisfaction",data=train)


# In[35]:


sns.histplot(x='Flight Distance',hue="satisfaction",data=train,kde=True,palette="dark")


# In[36]:


sns.countplot(x='Inflight wifi service',hue="satisfaction",data=train,palette="dark:red")


# In[37]:


sns.countplot(x='Food and drink',hue="satisfaction",data=train,palette='dark:orange')


# In[38]:


plt.figure(figsize = (18,18))
sns.heatmap(train.corr(), annot = True, cmap = "RdYlGn")


# In[39]:


from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()


# In[40]:


x_train = train.drop(["satisfaction"],axis=1)
y_train = train['satisfaction']


# In[41]:


x_test = test.drop(["satisfaction"],axis=1)
y_test = test["satisfaction"]


# In[42]:


x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)


# In[43]:


get_ipython().system('pip install xgboost')


# In[44]:


from xgboost import XGBClassifier
xgb = XGBClassifier()


# In[45]:


xgb.fit(x_train,y_train)


# In[46]:


pred = xgb.predict(x_test)


# In[47]:


from sklearn.metrics import accuracy_score, confusion_matrix


# In[48]:


accuracy_score(y_test,pred)


# In[49]:


confusion_matrix(y_test,pred)


# In[50]:


from sklearn.ensemble import RandomForestClassifier
reg_rf = RandomForestClassifier()


# In[51]:


reg_rf.fit(x_train,y_train)
#reg_rf.score(y_test,x_test)


# In[52]:


rf_pred = reg_rf.predict(x_test)


# In[53]:


accuracy_score(y_test,rf_pred)


# In[ ]:





# In[ ]:




