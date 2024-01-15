a=[0,1]
n=int(input("n: "))
x=0
i=0
for i in range(n-2):
    x=a[i]+a[i+1]
    a.append(x)
    i+=1
print(a)