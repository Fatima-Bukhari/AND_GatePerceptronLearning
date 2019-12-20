#!/usr/bin/env python
# coding: utf-8

# In[255]:


import pandas as pd
import numpy as np
dataset=pd.read_csv("AND_Gate.csv")#,usecols=['titles']


# In[256]:


dataset


# In[257]:


inputs=np.array(dataset[['X1','X2','bias']])
a=inputs.tolist()
a[3]


# In[258]:


output=dataset['output']
output.tolist()

outerlist=
# In[259]:


from random import seed
from random import randrange


# In[260]:


def predict(row,weights):
    activation=weights[0]
    alpha=0.9
    for i in range(len(row)-1):
        activation +=weights[i+1]*row[i]
    return 1.0 if activation >=0.0 else 0.0
       


# In[261]:


dataset=[[2.7833,2.8494,0],
         [1.2231,2.3412,0],
         [7.4421,2.4410,1],
         [2.4530,8.0960,1]]
weights=[-0.1,0.209939,-0.29498]
for row in dataset:
    prediction=predict(row,weights)
    print("Expected=%d,Predicted=%d" % (row[-1],prediction))


# In[262]:


dataset=[[0,0,0],
         [0,1,0],
         [1,0,0],
         [1,1,1]]
weights=[-0.1,0.209939,-0.29498]
for row in dataset:
    prediction=predict(row,weights)
    print("Expected=%d,Predicted=%d" % (row[-1],prediction))


# In[272]:


def predict(row,weights):
    activation=weights[0]
    alpha=0.9
    for i in range(len(row)-1):
        activation +=weights[i+1]*row[i]    
        Expected=row[-1]
        flag=True
        error=Expected-prediction
        if error != 0:
            weights[0]=weights[0] + alpha *(error) * row[0]
            weights[1]=weights[1] + alpha * (error) * row[1]
            weights[2]=weights[2] + alpha * (error) * row[2]
            flag =True
        else:
            flag=False
        print("The new value of weights is", weights[0],"The new valueof weights is", weights[1],"The new valueof weights is", weights[2])
    return 1.0 if activation >=0.0 else 0.0


# In[273]:


dataset=[[0,0,0],
         [0,1,0],
         [1,0,0],
         [1,1,1]]
weights=[-0.1,0.209939,-0.29498]
for row in dataset:
    prediction=predict(row,weights)
    print("The new value of weights is", weights[0],"The new valueof weights is", weights[1],"The new valueof weights is", weights[2])


# In[274]:


dataset=[[2,1,0],
         [0,1,0],
         [1,0,0],
         [1,1,1]]
weights=[-0.1,0.209939,-0.29498]
for row in dataset:
    prediction=predict(row,weights)
    print("The new value of weights is", weights[0],"The new valueof weights is", weights[1],"The new valueof weights is", weights[2])


# In[275]:


dataset=[[2,1,0],
         [3,1,0],
         [4,0,0],
         [3,3,1]]
weights=[-0.1,0.209939,-0.29498]
for row in dataset:
    prediction=predict(row,weights)
    print("The new value of weights is", weights[0],"The new valueof weights is", weights[1],"The new valueof weights is", weights[2])


# In[ ]:





# In[ ]:





# In[ ]:




