#!/usr/bin/env python
# coding: utf-8

# In[10]:


arr=[12,8,7,15,3,4,10]
largest=sec_largest=float("-inf")
smallest=sec_smallest=float("inf")
for i in range (len(arr)):
    if(arr[i]>largest):
        sec_largest=largest
        largest=arr[i]
    elif(arr[i]>sec_largest and arr[i]<largest):
        sec_largest=arr[i]
    elif(arr[i]<smallest):
        sec_smallest=smallest
        smallest=arr[i]
    elif(arr[i]<sec_smallest and arr[i]>smallest):
        sec_smallest=arr[i]
print("second largest element:",sec_largest)
print("second smallest element:",sec_smallest)
        


# In[ ]:





# In[ ]:





# In[ ]:




