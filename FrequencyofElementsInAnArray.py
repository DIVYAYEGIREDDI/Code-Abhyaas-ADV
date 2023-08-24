#!/usr/bin/env python
# coding: utf-8

# In[15]:


#Write a program to print element and its frequency in a array of elements
arr=[]
dic={}
n=int(input("enter number of elements in an arr:"))
for i in range (0,n):
    k=int(input("enter element in arr:"))
    arr.append(k)
print("array of elements:",arr)    
for i in arr:
    if i in dic:
        dic[i]+=1
    else:  
        dic[i]=1
print("element and its frequency in a array of elements",dic)

