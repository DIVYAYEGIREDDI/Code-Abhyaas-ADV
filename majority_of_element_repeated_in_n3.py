#!/usr/bin/env python
# coding: utf-8

# In[11]:


#majority element (ele>=n/3)
a=[1,1,2,2,3,3,1,1,2,2]
count=0
n=len(a)
ele=None
for i in range(n):
    if count==0:
        ele=a[i]
    if a[i]==ele:
        count+=1
    else:
        count-=1
    i+=1
count = 0
for i in range(n):
    if a[i] == ele:
        count += 1

# Check if the candidate appears more than or equal to n/3 times
if count >= n // 3:
    print(ele)
else:
    print("No majority element found.")


# In[ ]:




