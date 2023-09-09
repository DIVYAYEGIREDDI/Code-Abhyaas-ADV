#find the majority element repeated in n/3 times
a=[1,1,2,3,4,1,2,2,1,2]
ele1,ele2=None,None
count1,count2=0,0
n=len(a)
for i in range(n):
    if count1==0 and ele2!=a[i]:
        count1=1
        ele1=a[i]
    if count2==0 and ele1!=a[i]:
        count2=1
        ele2=a[i]
    elif a[i]==ele1:
        count1+=1
    elif a[i]==ele2:
        count2+=1
    else:
        count1-=1
        count2-=1
major1,major2=0,0
for i in range(n):
    if a[i]==ele1:
         major1+=1
    if a[i]==ele2:
         major2+=1
ls=[]
if major1>=n//3:
    ls.append(ele1)
if major2>=n//3:
    ls.append(ele2)
print(ls)    
    

    
