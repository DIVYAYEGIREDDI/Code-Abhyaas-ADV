#!/usr/bin/env python
# coding: utf-8

# In[10]:


arr=[1,2,3,4]
temp=1
for i in range(len(arr)-1):
    if(arr[i]>arr[i+1]):
        temp=0
        break
if temp:
    print("array is sorted")
else:
    print("array is not sorted")
    


# In[ ]:





# In[ ]:




