def fibu(n):    
    a=[0,1]
    x=0
    i=0
    for i in range(n-2):
        x=a[i]+a[i+1]
        a.append(x)
        i+=1
    return a
print(fibu(20))