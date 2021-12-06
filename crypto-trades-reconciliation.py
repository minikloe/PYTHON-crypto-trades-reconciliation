#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
import pandas as pd
import numpy as np


# In[2]:


from pandas.core.frame import DataFrame


# In[3]:


# load csv file

datacsv = pd.read_csv('/Users/kloe/Desktop/Middle Office Analyst Test data file.csv',index_col=False)


# In[4]:


print(datacsv)


# In[5]:


df = pd.DataFrame(datacsv)
print(df)


# In[6]:


# add an empty column for 'Flag any transfer that started before 8am and finished after 8am.'

df['flag'] = [[] for _ in range(len(df))]


# In[7]:


print(df.dtypes)


# In[8]:


print(df)


# In[9]:


# transfer object type to datatime type

df['time'] = pd.to_datetime(df['time'])


# In[10]:


print(df.dtypes)


# In[11]:


# Flag any transfer that started before 8am

df['flag'] = np.where(df['time']>'2/25/20 8:00','started b4 8am','')


# In[12]:


print(df)


# In[13]:


# Flag any transfer that finished after 8am

df['flag'] = np.where(df['time']>'2/25/20 20:00','finished after 8pm','')


# In[14]:


print(df)


# In[15]:


# Match pairs of withdrawals and deposits as ‘transfers',; 

df.groupby('tx_id').agg(lambda x: x.tolist())


# In[ ]:


def twosum(self, n)

