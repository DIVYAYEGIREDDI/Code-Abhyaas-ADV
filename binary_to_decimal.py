#!/usr/bin/env python
# coding: utf-8

# In[14]:


#binary to decimal convertion
a = input()
integer = 0
decimal = 0
fraction = 0
i = 0

while i < len(a):
    if a[i] == ".":
        decimal = 1
        i += 1
        continue
    
    if decimal == 0:
        integer = integer * 2 + int(a[i])
    else:
        fraction = fraction + int(a[i]) / (2 ** decimal)
        decimal += 1
        
    i += 1

result = integer + fraction
print(result)


# In[ ]:





# In[ ]:




