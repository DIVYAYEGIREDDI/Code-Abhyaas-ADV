#!/usr/bin/env python
# coding: utf-8

# In[34]:


#write a program to print maximum frequent element
arr=[]
dic={}
maximum=1
max_element=0
n=int(input("enter number of elements in an array:"))
for i in range (0,n):
    k=int(input("enter elements in array:"))
    arr.append(k)
print("list of elements in an array",arr)
for i in arr:
    if i in dic:
        dic[i]+=1
        if(dic[i]>=maximum):
            maximum=dic[i]
            max_element=i
    else:
        dic[i]=1
print("elements an its frequency in a array:",dic)
print("maximum frequent element and its frequency is",max_element,":",maximum)
        


# In[ ]:




