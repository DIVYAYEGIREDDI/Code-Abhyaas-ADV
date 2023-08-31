#!/usr/bin/env python
# coding: utf-8

# In[2]:


#linear search
def linear_search(arr,n,num):
    for i in range(len(arr)):
        if arr[i]==num:
            return i
arr=[1,2,3,4,5]
n=len(arr)
num=int(input())
index=linear_search(arr,n,num)
print("number fount at index:",index)


# In[ ]:




