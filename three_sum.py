#three sum
s = 9
a = [0,2,1,3,5,4,7,6,8]
a.sort()
i=0
n=len(a)
j=n-1
res=[]
for k in range (n):
    if k>0 and a[k]==a[k-1]:
        continue   # Skip duplicates of the first element
    i=k+1
    j=n-1
    while(i<j):
        s1=a[i]+a[j]+a[k]
        if s1==s:
            res.append([a[k],a[i],a[j]]) #print([i,j]) this is for print indeces of two values
            # Move i and j to avoid duplicates
            while(i<j and a[i]==a[i+1]):
                i+=1
            while(i<j and a[j]==a[j-1]):
                j-=1
            i+=1
            j-=1
        
        elif s1>s:
            j-=1
       
        else:
            i+=1
for sum in res:
    print(sum) #this is for values of two number





