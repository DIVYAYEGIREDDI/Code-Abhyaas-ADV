#!/usr/bin/env python
# coding: utf-8

# In[34]:


#write a program to print minimum frequent element
arr=[]
dic={}
minimum=float("inf")
min_element=None
n=int(input("enter number of elements in an array:"))
for i in range (0,n):
    k=int(input("enter elements in array:"))
    arr.append(k)
print("list of elements in an array",arr)
for i in arr:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
for key,val in dic.items():
    if(val<minimum):
            minimum=val
            min_element=key   
print("elements an its frequency in a array:",dic)
print("maximum frequent element and its frequency is",min_element,":",minimum)
        


# In[ ]:





# In[ ]:




