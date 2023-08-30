#!/usr/bin/env python
# coding: utf-8

# In[47]:


#right rotation by 1 position
arr=[1,2,3,4,5]
print(arr)
temp=arr[len(arr)-1]
i=len(arr)-2
while(i>=0):
    arr[i+1]=arr[i]
    i-=1
arr[0]=temp
print(arr)

