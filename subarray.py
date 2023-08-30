#!/usr/bin/env python
# coding: utf-8

# In[1]:


#print subarray
arr = [1, 2, 3,4]
n = len(arr)
for i in range(n):
    for j in range(i, n):
        subarray = arr[i:j+1]
        print(subarray)

