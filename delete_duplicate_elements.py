#!/usr/bin/env python
# coding: utf-8

# In[3]:


arr=[1,1,2,2,3,3]
i=0
j=1
while(j<len(arr)):
    if(arr[i]==arr[j]):
        j=j+1
    else:
        i=i+1
        arr[i]=arr[j]
del arr[i+1:]
print(arr)


# In[ ]:




