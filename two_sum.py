#!/usr/bin/env python
# coding: utf-8

# In[20]:


#two sum
s=5
a=[0,1,2,3,4,5]
i=0
n=len(a)
j=n-1
#res=[]
while(i<j):
    s1=a[i]+a[j]
    if s1==s:
        #res.append([i,j]) here we can use this also instead of print 
        print([i,j])
        i+=1
        j-=1
        
    elif s1>s:
        j-=1
      
    else:
        i+=1
#for sum in res:
 #   print(sum)


# In[ ]:





# In[ ]:





# In[ ]:




