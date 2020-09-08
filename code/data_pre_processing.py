#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df=pd.read_csv('AAPL (1).csv')


# In[15]:


df


# In[4]:


df2=pd.read_csv('sensex.csv')


# In[16]:


df2


# In[6]:


df3=pd.read_csv('nasdaq.csv')


# In[17]:


df3


# In[8]:


import matplotlib.pyplot as plt


# In[11]:


X=df3['Open']
Y=df3['Close']


# In[14]:


plt.plot(X)
plt.plot(Y)


# In[19]:


df1=df.append(df2)


# In[20]:


df1


# In[21]:


df4=df1.append(df3)


# In[43]:


df4=df4.drop('Adj Close',axis=1)


# In[25]:


df=pd.read_csv('AAPL.csv')


# In[27]:


df.shape


# In[28]:


df.head()


# In[35]:


l=['symbol','adjClose','adjHigh','adjLow','adjVolume','divCash','splitFactor']


# In[36]:


df5=df.drop(l,axis=1)


# In[38]:


df5.head()


# In[39]:


l=['Unnamed: 0','adjOpen']


# In[40]:


df6=df5.drop(l,axis=1)


# In[41]:


df6.head()


# In[44]:


df4.head()


# In[48]:


df7=df6.rename(columns={'date':'Date','open':'Open','close':'Close','high':'High','volume':'Volume','low':'Low'},inplace=False)


# In[50]:


df7.shape


# In[51]:


df4.shape


# In[61]:


date=df4['Date']


# In[62]:


type(date)


# In[67]:


date.iloc[1]


# In[68]:


y,m,d=date.iloc[1].split("-")


# In[69]:


y,m,d


# In[76]:


import datetime

x = datetime.date(int(y), int(m), int(d))
print(x)


# In[87]:


x=df7['Date'][1]
y,m,d=x.split("-")


# In[92]:


x=datetime.date(int(y),int(m),int(d[:2]))
print(x)


# In[96]:


# converting date into datetime object in python
df7['Date'].iloc[1]
df9=df4
df10=df7
def date_convertion(date):
    y,m,d=date.split("-")
    return datetime.date(int(y),int(m),int(d[:2]))


# In[97]:



for i in range(len(df7['Date'])):
    df7['Date'][i]=date_convertion(df7['Date'][i])


# In[98]:


df7.head()


# In[99]:


def date_convertiondf4(date):
    y,m,d=date.split("-")
    return datetime.date(int(y),int(m),int(d))


# In[101]:


for i in range(len(df4['Date'])):
    df4['Date'].iloc[i]=date_convertiondf4(df4['Date'].iloc[i])


# In[102]:


df4.head()


# In[103]:


df11=df4.append(df7)


# In[104]:


df11.head()


# In[105]:


df11.shape


# In[106]:


df4.shape


# In[107]:


df7.shape


# In[108]:


df11.to_csv('final_stock_data.csv',index=False)


# In[ ]:




