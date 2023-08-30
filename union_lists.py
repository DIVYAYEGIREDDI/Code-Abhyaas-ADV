#!/usr/bin/env python
# coding: utf-8

# In[1]:


#union of two lists
def union_lists(list1,list2):
    li=list1
    for i in list2:
        if i not in li:
            li.append(i)
    return li
list1=[1,2,3,4]
list2=[3,2,4,5]
ul=union_lists(list1,list2)
print(ul)

