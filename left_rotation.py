#!/usr/bin/env python
# coding: utf-8

# In[1]:


arr=[1,2,3,6,7]
temp=arr[0]
for i in range (len(arr)-1):
    arr[i]=arr[i+1]
arr[len(arr)-1]=temp 
print(arr)


# In[ ]:





# In[ ]:




