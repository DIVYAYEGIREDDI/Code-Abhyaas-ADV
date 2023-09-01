#!/usr/bin/env python
# coding: utf-8

# In[20]:


#two sum
s=5
a=[0,1,2,5,4,3,7,6]
a.sort()
i=0
n=len(a)
j=n-1
#res=[]
while(i<j):
    s1=a[i]+a[j]
    if s1==s:
        res.append([a[i],a[j]]) 
        #print([i,j]) this is for print indeces of two values
        i+=1
        j-=1
        
    elif s1>s:
        j-=1
      
    else:
        i+=1
for sum in res:
    print(sum)







