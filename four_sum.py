#!/usr/bin/env python
# coding: utf-8

# In[21]:


#four sum
s=9
a=[0,1,3,2,4,5,7,6,8]                         
a.sort()
i=0
n=len(a)
j=n-1
res=[]
for l in range(n-3):
    if l>0 and a[l]==a[l-1]:
        continue
   
    for k in range (l+1,n-2):
        if k>l+1 and a[k]==a[k-2]:
            continue
        i=k+1
        j=n-1
        while(i<j):
            s1=a[i]+a[j]+a[k]+a[l]
            if s1==s:
                res.append([a[l],a[k],a[i],a[j]]) 
                #print([i,j]) this is for print indeces of two values
                while i < j and a[i] == a[i + 1]:
                    i += 1
                while i < j and a[j] == a[j - 1]:
                    j -= 1
                i+=1
                j-=1
        
            elif s1>s:
                j-=1
       
            else:
                i+=1
for sum in res:
    print(sum) #this is for values of two number


# In[ ]:




