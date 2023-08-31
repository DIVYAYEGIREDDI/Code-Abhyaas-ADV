#!/usr/bin/env python
# coding: utf-8

# In[20]:


#binary search
def bin_search(num,low,high,target):
    if low>high:
        return -1
    mid=(low+high)//2
    if num[mid]==target:
        return mid
    elif target>num[mid]:
        return bin_search(num,mid+1,high,target)
    else:
        return bin_search(num,low,mid-1,target)
a=[1,2,7,3,4,5,6,5,7,6]
n=7
index=bin_search(a,0,len(a)-1,n)
if index==-1:
    print("not found")
else:
    print("Found at index",index)


# In[ ]:




