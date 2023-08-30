#!/usr/bin/env python
# coding: utf-8

# In[1]:


#right rotation by k positions
def right_rotation(arr,start,end):
    while(start<end):
        temp=arr[start]
        arr[start]=arr[end]
        arr[end]=temp
        start=start+1
        end=end-1
    return arr
arr=[1,2,3,4,5]
n=len(arr)
k=int(input("enter k value:"))
arr=right_rotation(arr,0,n-1)
arr=right_rotation(arr,0,k-1)
arr=right_rotation(arr,k,n-1)
print(arr)
    


# In[ ]:




