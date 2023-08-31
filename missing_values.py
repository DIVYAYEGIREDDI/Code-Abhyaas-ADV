#!/usr/bin/env python
# coding: utf-8

# In[5]:


#find missing number
a=[1,2,3,4,6]
xor=0
for i in range(1,len(a)+2):
    xor=xor^i
for i in range(len(a)):
    xor=xor^a[i]
print(xor)    


# In[ ]:




