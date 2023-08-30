#!/usr/bin/env python
# coding: utf-8

# In[8]:


#print number apper only once
a=[1,1,2,2,3,5,5,6,6]
xor=0
for i in range(len(a)):
    xor=xor^a[i]
print(xor)    


# In[5]:


a=[1,1,2,2,3,5,5]
xor=0
for i in range(len(a)):
    xor=xor^a[i]
print("number appeared once:",xor)

