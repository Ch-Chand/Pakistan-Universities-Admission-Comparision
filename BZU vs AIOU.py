#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')


# x=np.random.randint(1,20,30)
# y=np.random.randint(20,200,30)

# In[4]:


x=list(range(0,100))
y=np.random.randint(10,300,100)
z=np.random.randint(5,450,100)
y.sort()
z.sort()


# In[5]:


plt.figure(figsize=(16,9))
plt.plot(x,y, label="BZU")
plt.plot(x, z, label="AIOU")
plt.plot(y, z, label="UAEE")
plt.title("Student and their Marks")
plt.xlabel("Marks")
plt.ylabel("Students")
plt.legend()
plt.show()


# In[16]:


x=[15,20,25,30,35,40]
y=np.random.randint(20,400,6)
z=np.random.randint(20,400,6)
b=np.random.randint(20,400,6)


# In[17]:


bins=x
plt.figure(figsize=(16,9))
plt.bar(x,y, label="Bahaudin Zakaria Unversity Multan", width=0.8, color='r', align="center")
a=[15.8,20.8,25.8,30.8,35.8,40.8]
plt.bar(a,z, label="Allama Iqbal University", width=0.8, align="center")
a=[16.6,21.6,26.6,31.6,36.6,41.6]
plt.bar(a,b, label="University of Lahore", width=0.8, align="center")
plt.title("Universities Students in different Years")
plt.xlabel("Year")
plt.ylabel("Students")
plt.legend(loc='upper right', bbox_to_anchor=(1.4, 1),)
plt.show()

